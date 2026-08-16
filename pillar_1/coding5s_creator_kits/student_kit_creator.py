import os
import shutil
import openpyxl
import win32com.client

GRACIAS = "wil"
RESULTS_IN_LANGUAGE = "English"
def generar_student_kits():
    directorio_raiz = os.path.dirname(os.path.abspath(__file__))
    ruta_template_global = os.path.join(directorio_raiz, "Student Kit Template.xlsx")
    
    print(f"Iniciando escaneo recursivo en: {directorio_raiz}")
    print(f"Plantilla base global: {ruta_template_global}\n")
    
    if not os.path.exists(ruta_template_global):
        print(f"[ERROR CRÍTICO] No se encontró 'Student Kit Template.xlsx' en la raíz: {directorio_raiz}")
        return

    archivos_excel = []
    for raiz, directorios, archivos in os.walk(directorio_raiz):
        for archivo in archivos:
            if archivo.endswith(".xlsx") and not archivo.startswith("~$"):
                archivos_excel.append(os.path.join(raiz, archivo))
    
    creator_kits = [ruta for ruta in archivos_excel if "Creator Kit" in os.path.basename(ruta)]
    
    if not creator_kits:
        print("No se encontraron archivos 'Creator Kit'.")
        return

    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False
    excel.DisplayAlerts = False

    try:
        for ruta_creator in creator_kits:
            nombre_creator = os.path.basename(ruta_creator)
            nombre_student_esperado = nombre_creator.replace("Creator Kit", "Student Kit")
            carp_actual = os.path.dirname(ruta_creator)

            ruta_student = os.path.join(carp_actual, nombre_student_esperado)

            if not os.path.exists(ruta_student):
                print(f"[Creando desde Plantilla Global] {nombre_student_esperado}")
                shutil.copy(ruta_template_global, ruta_student)

            print(f"Procesando par:\n [Origen]  {nombre_creator}\n [Destino] {nombre_student_esperado}")
            try:
                # 1. Abrir Creator Kit con Excel real para actualizar B6 y recalcular fórmulas
                wb_creator_com = excel.Workbooks.Open(os.path.abspath(ruta_creator))
                ws_creator_com = wb_creator_com.Sheets("PromptGenerator")
                ws_creator_com.Range("B6").Value = RESULTS_IN_LANGUAGE
                
                # Forzar recálculo completo de la hoja de cálculo
                excel.Calculate()
                
                # Guardar cambios en el Creator Kit
                wb_creator_com.Save()
                wb_creator_com.Close()

                # 2. Leer la matriz recalculada y los metadatos I2:I3 con openpyxl
                wb_creator = openpyxl.load_workbook(ruta_creator, data_only=True)
                sheet_creator = wb_creator["PromptGenerator"]
                
                # Extracción completa de celdas E9:Y200
                matriz_valores = []
                for fila in range(9, 201):
                    fila_vals = []
                    for col in range(5, 26): # Columna 5 (E) a 25 (Y)
                        fila_vals.append(sheet_creator.cell(row=fila, column=col).value)
                    matriz_valores.append(fila_vals)
                
                valores_i2_i3 = [
                    [sheet_creator.cell(row=2, column=9).value], # I2
                    [sheet_creator.cell(row=3, column=9).value]  # I3
                ]
                
                wb_creator.close()

                # 3. Abrir el Student Kit con Excel real para pegar los datos
                wb_est = excel.Workbooks.Open(os.path.abspath(ruta_student))

                try:
                    wb_est.Unprotect(GRACIAS)
                except Exception:
                    pass

                ws_est = wb_est.Sheets("Coding5sStudentKit")

                # 4. Pegar la matriz E9:Y200 a partir de B9
                celda_inicio = ws_est.Cells(9, 2)
                celda_fin = ws_est.Cells(9 + len(matriz_valores) - 1, 2 + len(matriz_valores[0]) - 1)
                
                rango_destino = ws_est.Range(celda_inicio, celda_fin)
                rango_destino.Value = matriz_valores

                # 5. Pegar el rango adicional I2:I3 en G2:G3
                rango_g2_g3 = ws_est.Range("G2:G3")
                rango_g2_g3.Value = valores_i2_i3

                # 6. Correcciones de formato (Wrap Text y Filtros)
                rango_destino.WrapText = False
                rango_g2_g3.WrapText = False

                if ws_est.AutoFilterMode:
                    ws_est.AutoFilterMode = False

                # 7. Aplicar protección de estructura y guardar
                wb_est.Protect(Password=GRACIAS, Structure=True, Windows=False)

                wb_est.Save()
                wb_est.Close()
                print(f"  [Éxito] Sincronizada correctamente con idioma '{RESULTS_IN_LANGUAGE}'.\n")
                
            except Exception as e:
                print(f"  [Error] Problema al procesar con Excel: {e}\n")
    finally:
        excel.Quit()
        print("Proceso finalizado.")

if __name__ == "__main__":
    generar_student_kits()