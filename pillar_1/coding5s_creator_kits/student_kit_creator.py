import os
import shutil
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

    excel = None
    try:
        # Usar DispatchEx crea una instancia 100% nueva y aislada en memoria
        excel = win32com.client.DispatchEx("Excel.Application")
        
        # Configuraciones estrictas para modo fantasma
        excel.Visible = False
        excel.DisplayAlerts = False
        excel.ScreenUpdating = False
        excel.EnableEvents = False
        excel.Interactive = False  # Bloquea intentos de la UI de tomar el foco

        for ruta_creator in creator_kits:
            nombre_creator = os.path.basename(ruta_creator)
            nombre_student_esperado = nombre_creator.replace("Creator Kit", "Student Kit")
            carp_actual = os.path.dirname(ruta_creator)

            ruta_student = os.path.join(carp_actual, nombre_student_esperado)

            if not os.path.exists(ruta_student):
                print(f"[Creando desde Plantilla Global] {nombre_student_esperado}")
                shutil.copy(ruta_template_global, ruta_student)

            print(f"Procesando par:\n [Origen]  {nombre_creator}\n [Destino] {nombre_student_esperado}")
            
            wb_creator = None
            wb_est = None
            
            try:
                # 1. Abrir Creator Kit y actualizar idioma SOLO en memoria
                wb_creator = excel.Workbooks.Open(os.path.abspath(ruta_creator))
                ws_creator = wb_creator.Sheets("PromptGenerator")
                ws_creator.Range("B6").Value = RESULTS_IN_LANGUAGE
                
                # Forzar recálculo
                excel.Calculate()
                
                # 2. Extraer valores recalculados directamente mediante COM
                matriz_valores = ws_creator.Range("E9:Y200").Value
                valores_i2_i3 = ws_creator.Range("I2:I3").Value
                
                # 3. Cerrar el Creator Kit SIN GUARDAR CAMBIOS (Mantiene el original intacto)
                wb_creator.Close(False)
                wb_creator = None

                # 4. Abrir el Student Kit
                wb_est = excel.Workbooks.Open(os.path.abspath(ruta_student))

                try:
                    wb_est.Unprotect(GRACIAS)
                except Exception:
                    pass

                ws_est = wb_est.Sheets("Coding5sStudentKit")

                # 5. Calcular dimensiones dinámicamente y pegar E9:Y200 a partir de B9
                filas = len(matriz_valores)
                columnas = len(matriz_valores[0])
                
                celda_inicio = ws_est.Cells(9, 2)
                celda_fin = ws_est.Cells(9 + filas - 1, 2 + columnas - 1)
                
                rango_destino = ws_est.Range(celda_inicio, celda_fin)
                rango_destino.Value = matriz_valores

                # 6. Pegar el rango I2:I3 en G2:G3
                rango_g2_g3 = ws_est.Range("G2:G3")
                rango_g2_g3.Value = valores_i2_i3

                # 7. Formateo y limpieza
                rango_destino.WrapText = False
                rango_g2_g3.WrapText = False

                if ws_est.AutoFilterMode:
                    ws_est.AutoFilterMode = False

                # 8. Proteger y guardar el Student Kit
                wb_est.Protect(Password=GRACIAS, Structure=True, Windows=False)
                wb_est.Close(True)  # True = Guardar cambios
                wb_est = None
                
                print(f"  [Éxito] Sincronizada correctamente con idioma '{RESULTS_IN_LANGUAGE}'.\n")
                
            except Exception as e:
                print(f"  [Error] Problema al procesar con Excel: {e}\n")
                if wb_creator:
                    try:
                        wb_creator.Close(False)
                    except:
                        pass
                if wb_est:
                    try:
                        wb_est.Close(False)
                    except:
                        pass

    finally:
        # Limpieza absoluta de la instancia de Excel
        if excel:
            try:
                excel.Interactive = True
                excel.ScreenUpdating = True
                excel.EnableEvents = True
                excel.Quit()
            except:
                pass
        print("Proceso finalizado.")

if __name__ == "__main__":
    generar_student_kits()