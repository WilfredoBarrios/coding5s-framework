import os
import shutil
import win32com.client
import time
import tempfile
from utils import is_file_locked


def ejecutar_inyeccion_formulas(lista_kits, directorio_raiz, callback_log=print, callback_progress=None,
                                cancel_event=None):
    limite_caracteres = 8100
    pestana_destino = "PromptGenerator"
    fila_fin = 200

    mapa_formulas = [
        {"sheet": "FGen_S1", "origen": "E3:E50", "col_destino": "K"},
        {"sheet": "FGen_S1", "origen": "E54:E79", "col_destino": "Z"},
        {"sheet": "FGen_S1", "origen": "E83:E104", "col_destino": "L"},
        {"sheet": "FGen_S2", "origen": "E3:E42", "col_destino": "N"},
        {"sheet": "FGen_S2", "origen": "E46:E73", "col_destino": "AA"},
        {"sheet": "FGen_S2", "origen": "E80:E97", "col_destino": "O"},
        {"sheet": "FGen_S3", "origen": "E3:E38", "col_destino": "Q"},
        {"sheet": "FGen_S3", "origen": "E46:E71", "col_destino": "AB"},
        {"sheet": "FGen_S3", "origen": "E80:E96", "col_destino": "R"},
        {"sheet": "FGen_S4", "origen": "E3:E40", "col_destino": "T"},
        {"sheet": "FGen_S4", "origen": "E45:E74", "col_destino": "AC"},
        {"sheet": "FGen_S4", "origen": "E80:E97", "col_destino": "U"},
        {"sheet": "FGen_S5", "origen": "E3:E35", "col_destino": "W"},
        {"sheet": "FGen_S5", "origen": "E46:E72", "col_destino": "AD"},
        {"sheet": "FGen_S5", "origen": "E80:E96", "col_destino": "X"},
    ]

    if not lista_kits:
        callback_log("❌ [Warning] No Creator Kits selected for formula injection.\n")
        return False

    excel = None
    exitosos = 0
    fallidos = 0
    total = len(lista_kits)

    try:
        excel = win32com.client.DispatchEx("Excel.Application")
        excel.Visible = False
        excel.DisplayAlerts = False
        excel.ScreenUpdating = False
        excel.EnableEvents = False
        excel.Interactive = False

        for idx, kit in enumerate(lista_kits):
            # 🔥 NUEVO: Comprobar si el usuario presionó cancelar
            if cancel_event and cancel_event.is_set():
                callback_log("\n⚠️ [CANCELLED] Process interrupted by user.\n")
                break

            nombre_kit = kit["nombre"]
            ruta_kit = kit["ruta"]

            if callback_progress:
                callback_progress(idx + 1, total, nombre_kit)

            callback_log(f"\n📂 Processing Kit ({idx + 1}/{total}): {nombre_kit}\n")

            if is_file_locked(ruta_kit):
                callback_log(f"  ❌ [LOCKED] File is open in Excel or locked by OS. Skipping.\n")
                fallidos += 1
                continue

            temp_dir = tempfile.gettempdir()
            backup_path = os.path.join(temp_dir, f"backup_{int(time.time())}_{nombre_kit}")
            shutil.copy2(ruta_kit, backup_path)

            wb = None
            exito_kit = True

            try:
                wb = excel.Workbooks.Open(ruta_kit)
                ws_destino = wb.Sheets(pestana_destino)

                for tarea in mapa_formulas:
                    sheet_origen = tarea["sheet"]
                    rango_origen = tarea["origen"]
                    col_destino = tarea["col_destino"]
                    rango_pegar_full = f"{col_destino}9:{col_destino}{fila_fin}"

                    try:
                        ws_origen = wb.Sheets(sheet_origen)
                        valores_verdes = ws_origen.Range(rango_origen).Value

                        fragmentos = [str(fila[0]) for fila in valores_verdes if fila[0] is not None]
                        formula_texto = "\n".join(fragmentos)
                        largo_formula = len(formula_texto)

                        if largo_formula > limite_caracteres:
                            callback_log(
                                f"  ❌ [LIMIT ERROR] {sheet_origen} has {largo_formula} chars (Exceeds {limite_caracteres}).\n")
                            exito_kit = False
                            break

                        exito_escritura = False
                        intentos_maximos = 5

                        for intento in range(intentos_maximos):
                            try:
                                time.sleep(0.2)
                                ws_destino.Range(rango_pegar_full).Formula = formula_texto
                                exito_escritura = True
                                break
                            except Exception as err_com:
                                if "busy" in str(err_com) and intento < intentos_maximos - 1:
                                    time.sleep(1.0 * (intento + 1))
                                    try:
                                        excel.Calculate()
                                    except:
                                        pass
                                else:
                                    raise err_com

                        if not exito_escritura:
                            raise Exception("Excel remained busy after multiple retries.")

                        time.sleep(0.1)
                        callback_log(
                            f"  ✅ {sheet_origen} -> {col_destino}9:{col_destino}{fila_fin} [{largo_formula} chars]\n")

                    except Exception as e:
                        callback_log(f"  ❌ Error in task {sheet_origen}: {e}\n")
                        exito_kit = False
                        break

                if exito_kit:
                    wb.Close(True)
                    os.remove(backup_path)
                    exitosos += 1
                    callback_log(f"  🎉 Kit updated and saved successfully!\n")
                else:
                    wb.Close(False)
                    shutil.copy2(backup_path, ruta_kit)
                    os.remove(backup_path)
                    fallidos += 1
                    callback_log(f"  ⚠️ Changes ROLLED BACK for {nombre_kit} due to errors.\n")

            except Exception as e:
                if wb: wb.Close(False)
                shutil.copy2(backup_path, ruta_kit)
                os.remove(backup_path)
                fallidos += 1
                callback_log(f"  ❌ [CRITICAL ERROR] Failed processing {nombre_kit}. Rolled back. Details: {e}\n")

        callback_log(f"\n✅ PROCESS FINISHED: {exitosos} Successful, {fallidos} Failed.\n")
        return True

    except Exception as e:
        callback_log(f"❌ [GLOBAL ERROR INJECTION]: {e}\n")
        return False
    finally:
        if excel:
            try:
                excel.Interactive = True
                excel.ScreenUpdating = True
                excel.EnableEvents = True
                excel.Quit()
            except:
                pass


def ejecutar_actualizacion_base(
        lista_kits,
        directorio_raiz,
        lista_rangos,
        archivo_base="creator_kit_Base_File_for_CKs.xlsx",
        callback_log=print,
        callback_progress=None,
        cancel_event=None
):
    ruta_base = os.path.join(directorio_raiz, archivo_base)
    if not os.path.exists(ruta_base):
        callback_log(f"❌ [CRITICAL ERROR] Base file not found: '{archivo_base}'\n")
        return False

    if not lista_kits or not lista_rangos:
        return False

    excel = None
    exitosos = 0
    fallidos = 0
    total = len(lista_kits)

    try:
        excel = win32com.client.DispatchEx("Excel.Application")
        excel.Visible = False
        excel.DisplayAlerts = False
        excel.ScreenUpdating = False
        excel.EnableEvents = False
        excel.Interactive = False

        callback_log(f"📥 Reading base matrices from '{archivo_base}'...\n")
        wb_base = excel.Workbooks.Open(ruta_base)
        nombres_pestanas_base = [sheet.Name for sheet in wb_base.Sheets]

        # Guardar en memoria los valores extraidos de los rangos habilitados
        matrices = []
        for i, rango in enumerate(lista_rangos):
            p_base = rango["pestana_base"]
            r_copiar = rango["rango_copiar"]
            if p_base not in nombres_pestanas_base:
                callback_log(f"❌ [ERROR] Sheet '{p_base}' does not exist in Base File.\n")
                wb_base.Close(False)
                return False
            try:
                matriz = wb_base.Sheets(p_base).Range(r_copiar).Value
                matrices.append(matriz)
                callback_log(f"  -> Extracted Range {i + 1} from '{p_base}' [{r_copiar}]\n")
            except Exception as e:
                callback_log(f"❌ [ERROR] Failed to extract Range {i + 1} from '{p_base}': {e}\n")
                wb_base.Close(False)
                return False

        wb_base.Close(False)

        for idx, kit in enumerate(lista_kits):
            # 🔥 NUEVO: Comprobar si el usuario presionó cancelar
            if cancel_event and cancel_event.is_set():
                callback_log("\n⚠️ [CANCELLED] Process interrupted by user.\n")
                break

            nombre_kit = kit["nombre"]
            ruta_kit = kit["ruta"]

            if callback_progress:
                callback_progress(idx + 1, total, nombre_kit)

            callback_log(f"\n🔄 Updating BaseData ({idx + 1}/{total}): {nombre_kit}\n")

            if is_file_locked(ruta_kit):
                callback_log(f"  ❌ [LOCKED] File is open or locked. Skipping.\n")
                fallidos += 1
                continue

            temp_dir = tempfile.gettempdir()
            backup_path = os.path.join(temp_dir, f"backup_{int(time.time())}_{nombre_kit}")
            shutil.copy2(ruta_kit, backup_path)

            wb_ck = None
            try:
                wb_ck = excel.Workbooks.Open(ruta_kit)
                nombres_pestanas_ck = [sheet.Name for sheet in wb_ck.Sheets]

                for i, rango in enumerate(lista_rangos):
                    p_dest = rango["pestana_destino_ck"]
                    c_dest = rango["celda_destino"]
                    matriz = matrices[i]

                    if p_dest not in nombres_pestanas_ck:
                        raise Exception(f"Sheet '{p_dest}' does not exist in target kit.")

                    ws_ck = wb_ck.Sheets(p_dest)
                    filas = len(matriz)
                    columnas = len(matriz[0]) if isinstance(matriz[0], (list, tuple)) else 1

                    celda_inicio = ws_ck.Range(c_dest)
                    celda_fin = ws_ck.Cells(celda_inicio.Row + filas - 1, celda_inicio.Column + columnas - 1)

                    ws_ck.Range(celda_inicio, celda_fin).Value = matriz
                    callback_log(f"  -> Applied Range {i + 1} to '{p_dest}' @ {c_dest}\n")

                time.sleep(0.1)
                excel.Calculate()
                time.sleep(0.1)

                wb_ck.Close(True)
                os.remove(backup_path)
                exitosos += 1
                callback_log(f"  ✅ All configured BaseData ranges updated successfully.\n")
            except Exception as e:
                if wb_ck: wb_ck.Close(False)
                shutil.copy2(backup_path, ruta_kit)
                os.remove(backup_path)
                fallidos += 1
                callback_log(f"  ❌ Error processing {nombre_kit}. Rolled back. Details: {e}\n")

        callback_log(f"\n✅ PROCESS FINISHED: {exitosos} Successful, {fallidos} Failed.\n")
        return True

    except Exception as e:
        callback_log(f"❌ [GLOBAL ERROR BASE UPDATE]: {e}\n")
        return False
    finally:
        if excel:
            try:
                excel.Interactive = True
                excel.ScreenUpdating = True
                excel.EnableEvents = True
                excel.Quit()
            except:
                pass


def ejecutar_generacion_student_kits(lista_kits, directorio_raiz, idioma_objetivo, callback_progress, callback_log,
                                     cancel_event=None):
    exito_global = True
    total = len(lista_kits)
    template_path = os.path.join(directorio_raiz, "Student_Kit_Template.xlsx")

    if not os.path.exists(template_path):
        callback_log("❌ Error: 'Student_Kit_Template.xlsx' not found in root directory.\n")
        return False

    excel = None
    try:
        excel = win32com.client.DispatchEx("Excel.Application")
        excel.Visible = False
        excel.DisplayAlerts = False
        excel.ScreenUpdating = False
        excel.EnableEvents = False
        excel.Interactive = False

        for i, kit in enumerate(lista_kits, start=1):
            # 🔥 NUEVO: Comprobar si el usuario presionó cancelar
            if cancel_event and cancel_event.is_set():
                callback_log("\n⚠️ [CANCELLED] Process interrupted by user.\n")
                exito_global = False
                break

            creator_path = kit["ruta"]
            nombre_creator = kit.get("nombre", kit.get("nombre_real", "Unknown Kit"))
            callback_progress(i, total, nombre_creator)
            callback_log(f"\n[{i}/{total}] Processing: {nombre_creator}\n")

            if is_file_locked(creator_path):
                callback_log(f"  ❌ [LOCKED] File is open or locked. Skipping.\n")
                exito_global = False
                continue

            try:
                # 1. Determinar el nombre
                if "Creator Kit" in nombre_creator:
                    nuevo_nombre = nombre_creator.replace("Creator Kit", f"Student Kit ({idioma_objetivo})")
                else:
                    nombre_base = os.path.splitext(nombre_creator)[0]
                    nuevo_nombre = f"{nombre_base} Student Kit ({idioma_objetivo}).xlsx"

                student_path = os.path.join(os.path.dirname(creator_path), nuevo_nombre)

                # 2. Copiar Template
                callback_log(f"  -> Creating copy: {nuevo_nombre}\n")
                shutil.copy2(template_path, student_path)

                # 3. Extraer valores del Creator Kit con COM
                callback_log("  -> Opening Creator Kit to update language and trigger prompt formulas...\n")
                wb_creator = excel.Workbooks.Open(creator_path)

                nombres_pestanas_ck = [sheet.Name for sheet in wb_creator.Sheets]
                if "PromptGenerator" not in nombres_pestanas_ck:
                    callback_log("  ❌ Error: 'PromptGenerator' sheet not found in Creator Kit.\n")
                    wb_creator.Close(False)
                    exito_global = False
                    continue

                ws_creator = wb_creator.Sheets("PromptGenerator")

                # 🔥 NUEVO: Inyectar el idioma objetivo en B6 para forzar recálculo de fórmulas de prompts
                ws_creator.Range("B6").Value = idioma_objetivo
                excel.Calculate()  # Le decimos a Excel que procese todas las fórmulas nuevas
                time.sleep(0.5)  # Breve pausa de seguridad para garantizar que el motor de Excel termine

                callback_log("  -> Extracting updated values from Creator Kit (E9:Y200 y I2:I3)...\n")
                valores_crudos = ws_creator.Range("E9:Y200").Value

                # Extraer los valores adicionales de I2:I3
                valores_i2_i3 = ws_creator.Range("I2:I3").Value

                # Cerramos el Creator Kit SIN guardar (False) para mantener intacto tu archivo original
                wb_creator.Close(False)

                # --- FILTRO LIMPIADOR DE ERRORES Y MATRIZ ---
                valores_limpios = []
                for fila in valores_crudos:
                    fila_limpia = []
                    for celda in fila:
                        # Filtrar errores nativos de Excel transmitidos por COM (ints negativos)
                        if isinstance(celda, int) and celda <= -2146826200:
                            fila_limpia.append("")
                        # Filtrar cadenas de texto que representan errores
                        elif isinstance(celda, str) and celda.strip().upper() in ["#N/A", "#REF!", "#VALUE!", "#NAME?",
                                                                                  "#DIV/0!", "#NUM!"]:
                            fila_limpia.append("")
                        else:
                            fila_limpia.append(celda)
                    valores_limpios.append(tuple(fila_limpia))

                # 4. Inyección directa respetando tus columnas Track intactas
                callback_log("  -> Injecting values, language, and applying workbook protection...\n")
                wb_student = excel.Workbooks.Open(student_path)

                nombres_pestanas_stu = [sheet.Name for sheet in wb_student.Sheets]
                sheet_name = "Coding5sStudentKit" if "Coding5sStudentKit" in nombres_pestanas_stu else \
                    nombres_pestanas_stu[0]
                ws_student = wb_student.Sheets(sheet_name)

                # Inyectar idioma en B3
                ws_student.Range("B3").Value = idioma_objetivo

                # 🔥 NUEVO: Inyectar el rango adicional I2:I3 en G2:G3 (solo valores)
                ws_student.Range("G2:G3").Value = valores_i2_i3

                # Calcular las dimensiones exactas para evitar que Excel rellene columnas extra con #N/A
                filas = len(valores_limpios)
                columnas = len(valores_limpios[0]) if filas > 0 else 0

                # B9 equivale a Fila 9, Columna 2
                celda_inicio = ws_student.Cells(9, 2)
                # LÍNEA CORREGIDA: Ahora calcula dinámicamente desde la columna 2 hasta la 22 (V)
                celda_fin = ws_student.Cells(8 + filas, celda_inicio.Column + columnas - 1)
                rango_destino = ws_student.Range(celda_inicio, celda_fin)

                # Volcar los datos puros y desactivar el WrapText
                rango_destino.Value = valores_limpios
                rango_destino.WrapText = False

                # Proteger la estructura del libro
                wb_student.Protect(Password="wil", Structure=True, Windows=False)

                wb_student.Save()
                wb_student.Close(True)

                callback_log("  ✅ Student Kit successfully created, populated, formatted, and protected.\n")

            except Exception as e:
                callback_log(f"  ❌ Exception: {str(e)}\n")
                if 'wb_creator' in locals() and wb_creator:
                    try:
                        wb_creator.Close(False)
                    except:
                        pass
                if 'wb_student' in locals() and wb_student:
                    try:
                        wb_student.Close(False)
                    except:
                        pass
                exito_global = False

        return exito_global
    finally:
        if excel:
            try:
                excel.Interactive = True
                excel.ScreenUpdating = True
                excel.EnableEvents = True
                excel.Quit()
            except:
                pass