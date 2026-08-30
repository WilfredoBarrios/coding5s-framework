import os
import win32com.client

# ==========================================
# ⚙️ CONFIGURACIÓN PRINCIPAL
# ==========================================
# 1. Coloca aquí el nombre exacto del Creator Kit que estás editando
ARCHIVO_CREATOR_KIT = "Coding5s Python OOP Lib CustomTkinter Creator Kit v0.4.xlsx" 

# 2. Límite de seguridad
LIMITE_CARACTERES = 8100
PESTANA_DESTINO = "PromptGenerator"
FILA_FIN = 200

# ==========================================
# 🗺️ EL MAPA DE COORDENADAS
# ==========================================
MAPA_FORMULAS = [
    # ---- STAGE 1 ----
    {"sheet": "FGen_S1", "origen": "E3:E50",   "col_destino": "K"}, # Topics
    {"sheet": "FGen_S1", "origen": "E54:E79",  "col_destino": "Z"}, # Projects
    {"sheet": "FGen_S1", "origen": "E83:E104", "col_destino": "L"}, # Mentors
    
    # ---- STAGE 2 ----
    {"sheet": "FGen_S2", "origen": "E3:E42",   "col_destino": "N"}, # Topics
    {"sheet": "FGen_S2", "origen": "E46:E73",  "col_destino": "AA"},# Projects
    {"sheet": "FGen_S2", "origen": "E80:E97",  "col_destino": "O"}, # Mentors

    # ---- STAGE 3 ----
    {"sheet": "FGen_S3", "origen": "E3:E38",   "col_destino": "Q"}, # Topics
    {"sheet": "FGen_S3", "origen": "E46:E71",  "col_destino": "AB"},# Projects
    {"sheet": "FGen_S3", "origen": "E80:E96",  "col_destino": "R"}, # Mentors

    # ---- STAGE 4 ----
    {"sheet": "FGen_S4", "origen": "E3:E40",   "col_destino": "T"}, # Topics
    {"sheet": "FGen_S4", "origen": "E45:E74",  "col_destino": "AC"},# Projects
    {"sheet": "FGen_S4", "origen": "E80:E97",  "col_destino": "U"}, # Mentors

    # ---- STAGE 5 ----
    {"sheet": "FGen_S5", "origen": "E3:E35",   "col_destino": "W"}, # Topics
    {"sheet": "FGen_S5", "origen": "E46:E72",  "col_destino": "AD"},# Projects
    {"sheet": "FGen_S5", "origen": "E80:E96",  "col_destino": "X"}, # Mentors
]

def inyectar_formulas_masivamente():
    directorio_raiz = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(directorio_raiz, ARCHIVO_CREATOR_KIT)
    
    print("==================================================")
    print("🚀 INICIANDO AUTO-INJECTOR DE FÓRMULAS CODING5S")
    print("==================================================\n")
    print(f"Archivo objetivo: {ARCHIVO_CREATOR_KIT}")
    
    if not os.path.exists(ruta_archivo):
        print(f"❌ [ERROR CRÍTICO] No se encontró el archivo '{ARCHIVO_CREATOR_KIT}' en la misma carpeta del script.")
        return

    excel = None
    wb = None
    
    try:
        # Abrimos un proceso fantasma, independiente y aislado
        excel = win32com.client.DispatchEx("Excel.Application")
        excel.Visible = False
        excel.DisplayAlerts = False
        excel.ScreenUpdating = False
        excel.EnableEvents = False
        excel.Interactive = False

        print("Abriendo archivo en memoria...\n")
        wb = excel.Workbooks.Open(ruta_archivo)
        ws_destino = wb.Sheets(PESTANA_DESTINO)

        for tarea in MAPA_FORMULAS:
            sheet_origen = tarea["sheet"]
            rango_origen = tarea["origen"]
            col_destino = tarea["col_destino"]
            
            rango_pegar_full = f"{col_destino}9:{col_destino}{FILA_FIN}"
            print(f"Procesando {sheet_origen} ({rango_origen})  =>  {PESTANA_DESTINO}!{rango_pegar_full} ...")
            
            try:
                ws_origen = wb.Sheets(sheet_origen)
                
                # Extraemos la matriz de celdas verdes. Retorna una tupla de tuplas, ej: (("=",), ("A1 &",), ...)
                valores_verdes = ws_origen.Range(rango_origen).Value
                
                # Replicamos lo que hace el Bloc de Notas: unimos todo el texto descartando celdas vacías (None)
                fragmentos = []
                for fila in valores_verdes:
                    if fila[0] is not None:
                        fragmentos.append(str(fila[0]))
                
                # Unimos con salto de línea para replicar con exactitud microscópica el pegado desde Notepad
                formula_texto = "\n".join(fragmentos)
                
                # =========================================================
                # 🛑 SEGURO DE VIDA: LÍMITE DE EXCEL (8192 Caracteres)
                # =========================================================
                largo_formula = len(formula_texto)
                if largo_formula > LIMITE_CARACTERES:
                    print(f"\n❌ [ERROR CRÍTICO: LÍMITE SUPERADO]")
                    print(f"🚨 La fórmula originada en {sheet_origen} (Rango: {rango_origen}) tiene {largo_formula} caracteres.")
                    print(f"🚨 El límite seguro es {LIMITE_CARACTERES}. ¡DETENIENDO EL PROCESO PARA SALVAR EL ARCHIVO!")
                    print("Por favor, acorta la fórmula en Excel e inténtalo de nuevo.\n")
                    
                    # Salida de emergencia: Cerramos y descartamos todo para proteger tu archivo
                    wb.Close(False)
                    wb = None
                    return
                # =========================================================

                # Inyección de la fórmula en el rango completo (Hace el "drag" automáticamente)
                ws_destino.Range(rango_pegar_full).Formula = formula_texto
                print(f"  ✅ Inyección exitosa. Largo de la fórmula: {largo_formula} caracteres.")
                
            except Exception as e_tarea:
                print(f"  ❌ Error al procesar {sheet_origen}: {e_tarea}")
                print("Abortando para proteger el archivo.")
                if wb:
                    wb.Close(False)
                    wb = None
                return

        # Si el for termina sin activar el límite ni lanzar errores, guardamos los cambios.
        print("\n💾 Guardando archivo...")
        wb.Close(True)  # True = Guardar cambios
        wb = None
        print("🎉 ¡TODAS LAS FÓRMULAS FUERON ACTUALIZADAS CON ÉXITO!")

    except Exception as e_global:
        print(f"\n❌ [ERROR GLOBAL] Ocurrió un fallo en el proceso: {e_global}")
        if wb:
            try:
                wb.Close(False)
            except:
                pass

    finally:
        if excel:
            try:
                excel.Interactive = True
                excel.ScreenUpdating = True
                excel.EnableEvents = True
                excel.Quit()
            except:
                pass
        print("Proceso finalizado. Memoria limpia.")

if __name__ == "__main__":
    inyectar_formulas_masivamente()