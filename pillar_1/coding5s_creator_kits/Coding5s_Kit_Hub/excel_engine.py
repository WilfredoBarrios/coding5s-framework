import os
import shutil
import win32com.client
import time
import tempfile
from utils import is_file_locked


def ejecutar_inyeccion_formulas(lista_kits, directorio_raiz, callback_log=print, callback_progress=None):
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
            nombre_kit = kit["nombre"]
            ruta_kit = kit["ruta"]

            if callback_progress:
                callback_progress(idx + 1, total, nombre_kit)

            callback_log(f"\n📂 Processing Kit ({idx + 1}/{total}): {nombre_kit}\n")

            if is_file_locked(ruta_kit):
                callback_log(f"  ❌ [LOCKED] File is open in Excel or locked by OS. Skipping.\n")
                fallidos += 1
                continue

            # --- EPHEMERAL BACKUP ---
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

                        # --- SISTEMA DE REINTENTO ANTI-SATURACIÓN COM ---
                        exito_escritura = False
                        intentos_maximos = 5

                        for intento in range(intentos_maximos):
                          try:
                            # Forzar a Excel a respirar antes de recibir el bloque masivo
                            time.sleep(0.2)
                            ws_destino.Range(rango_pegar_full).Formula = formula_texto
                            exito_escritura = True
                            break
                          except Exception as err_com:
                            if "busy" in str(err_com) and intento < intentos_maximos - 1:
                              time.sleep(1.0 * (intento + 1))  # Pausa exponencial más larga (1s, 2s, 3s...)
                              try:
                                excel.Calculate()
                              except:
                                pass
                            else:
                              raise err_com

                        if not exito_escritura:
                          raise Exception("Excel remained busy after multiple retries.")
                        # -----------------------------------------------

                        time.sleep(0.1)  # Respiro final para la tarea
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
        archivo_base="creator_kit_Base_File_for_CKs.xlsx",
        pestana_base="BaseData",
        rango_copiar="A1:B10",
        pestana_destino_ck="FGen_S1",
        celda_destino="C95",
        callback_log=print,
        callback_progress=None
):
    ruta_base = os.path.join(directorio_raiz, archivo_base)
    if not os.path.exists(ruta_base):
        callback_log(f"❌ [CRITICAL ERROR] Base file not found: '{archivo_base}'\n")
        return False

    if not lista_kits:
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

        callback_log(f"📥 Reading base matrix from '{archivo_base}' -> Sheet: '{pestana_base}' [{rango_copiar}]...\n")
        wb_base = excel.Workbooks.Open(ruta_base)

        # Validar existencia de la pestaña base
        nombres_pestanas_base = [sheet.Name for sheet in wb_base.Sheets]
        if pestana_base not in nombres_pestanas_base:
            callback_log(
                f"❌ [ERROR] Sheet '{pestana_base}' does not exist in Base File. Available: {nombres_pestanas_base}\n")
            wb_base.Close(False)
            return False

        matriz_valores = wb_base.Sheets(pestana_base).Range(rango_copiar).Value
        wb_base.Close(False)

        for idx, kit in enumerate(lista_kits):
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

                # Validar existencia de la pestaña destino en el Creator Kit
                nombres_pestanas_ck = [sheet.Name for sheet in wb_ck.Sheets]
                if pestana_destino_ck not in nombres_pestanas_ck:
                    raise Exception(
                        f"Sheet '{pestana_destino_ck}' does not exist in target kit. Available: {nombres_pestanas_ck}")

                ws_ck = wb_ck.Sheets(pestana_destino_ck)

                filas = len(matriz_valores)
                columnas = len(matriz_valores[0]) if isinstance(matriz_valores[0], (list, tuple)) else 1

                celda_inicio = ws_ck.Range(celda_destino)
                celda_fin = ws_ck.Cells(celda_inicio.Row + filas - 1, celda_inicio.Column + columnas - 1)

                ws_ck.Range(celda_inicio, celda_fin).Value = matriz_valores
                time.sleep(0.1)
                excel.Calculate()
                time.sleep(0.1)

                wb_ck.Close(True)
                os.remove(backup_path)
                exitosos += 1
                callback_log(f"  ✅ BaseData updated successfully in '{pestana_destino_ck}' @ {celda_destino}.\n")
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


def ejecutar_generacion_student_kits(lista_kits, directorio_raiz, idioma_objetivo, callback_log=print,
                                     callback_progress=None):
    template_global = os.path.join(directorio_raiz, "Student Kit Template.xlsx")
    password_gracias = "wil"

    if not os.path.exists(template_global):
        callback_log(f"❌ [CRITICAL ERROR] 'Student Kit Template.xlsx' not found.\n")
        return False
    if not lista_kits:
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
            nombre_creator = kit["nombre"]
            ruta_creator = kit["ruta"]
            carp_actual = os.path.dirname(ruta_creator)

            if callback_progress:
                callback_progress(idx + 1, total, nombre_creator)

            callback_log(f"\n🎓 Generating Student Kit ({idx + 1}/{total}): {nombre_creator}\n")

            if is_file_locked(ruta_creator):
                callback_log(f"  ❌ [LOCKED] Creator Kit is open or locked. Skipping.\n")
                fallidos += 1
                continue

            base_nombre = nombre_creator.replace("Creator Kit", f"Student Kit ({idioma_objetivo})")
            nombre_student_esperado = " ".join(base_nombre.split())
            ruta_student = os.path.join(carp_actual, nombre_student_esperado)

            if is_file_locked(ruta_student):
                callback_log(f"  ❌ [LOCKED] Target Student Kit is currently open. Skipping.\n")
                fallidos += 1
                continue

            if not os.path.exists(ruta_student):
                shutil.copy(template_global, ruta_student)
                callback_log(f"  📁 Created new template copy: {nombre_student_esperado}\n")

            wb_creator, wb_est = None, None
            try:
                wb_creator = excel.Workbooks.Open(ruta_creator)
                ws_creator = wb_creator.Sheets("PromptGenerator")
                ws_creator.Range("B6").Value = idioma_objetivo
                excel.Calculate()
                time.sleep(0.1)

                matriz_valores = ws_creator.Range("E9:Y200").Value
                valores_i2_i3 = ws_creator.Range("I2:I3").Value
                wb_creator.Close(False)

                wb_est = excel.Workbooks.Open(ruta_student)
                try:
                    wb_est.Unprotect(password_gracias)
                except:
                    pass

                ws_est = wb_est.Sheets("Coding5sStudentKit")
                filas, columnas = len(matriz_valores), len(matriz_valores[0])

                ws_est.Range(ws_est.Cells(9, 2), ws_est.Cells(9 + filas - 1, 2 + columnas - 1)).Value = matriz_valores
                ws_est.Range("G2:G3").Value = valores_i2_i3
                time.sleep(0.1)

                ws_est.Range("B9:Y200").WrapText = False
                ws_est.Range("G2:G3").WrapText = False
                if ws_est.AutoFilterMode: ws_est.AutoFilterMode = False

                wb_est.Protect(Password=password_gracias, Structure=True, Windows=False)
                wb_est.Close(True)
                exitosos += 1
                callback_log(f"  ✅ Student Kit synced successfully.\n")

            except Exception as e:
                if wb_creator: wb_creator.Close(False)
                if wb_est: wb_est.Close(False)
                fallidos += 1
                callback_log(f"  ❌ Error generating {nombre_student_esperado}. Details: {e}\n")

        callback_log(f"\n✅ PROCESS FINISHED: {exitosos} Successful, {fallidos} Failed.\n")
        return True

    except Exception as e:
        callback_log(f"❌ [GLOBAL ERROR STUDENT KITS]: {e}\n")
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