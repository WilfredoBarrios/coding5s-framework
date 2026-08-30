import os
import win32com.client

# ==========================================
# ⚙️ VARIABLES DE CONFIGURACIÓN PRINCIPALES
# ==========================================
ARCHIVO_BASE_NOMBRE = "creator_kit_Base_File_for_CKs.xlsx"
PESTANA_BASE_ORIGEN = "BaseData"           # Pestaña en el archivo base
RANGO_A_COPIAR = "A1:B10"                  # Rango a copiar desde el archivo base

PESTANA_DESTINO_CK = "FGen_S1"     # Pestaña destino en los Creator Kits
CELDA_INICIAL_DESTINO = "C95"               # Celda inicial donde se posiciona el pegado
# ==========================================

def actualizar_creator_kits_masivamente():
    directorio_raiz = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo_base = os.path.join(directorio_raiz, ARCHIVO_BASE_NOMBRE)
    
    print(f"Iniciando proceso de actualización masiva...")
    print(f"Directorio raíz: {directorio_raiz}")
    print(f"Archivo base: {ruta_archivo_base}\n")
    
    # Detener el script inmediatamente si el archivo base no está en la carpeta raíz
    if not os.path.exists(ruta_archivo_base):
        print(f"[ERROR CRÍTICO] No se encontró el archivo base '{ARCHIVO_BASE_NOMBRE}' en la raíz. Deteniendo proceso.")
        return

    # 1. Búsqueda recursiva de archivos que contengan "Creator Kit"
    archivos_excel = []
    for raiz, directorios, archivos in os.walk(directorio_raiz):
        for archivo in archivos:
            if archivo.endswith(".xlsx") and not archivo.startswith("~$"):
                if archivo != ARCHIVO_BASE_NOMBRE:
                    archivos_excel.append(os.path.join(raiz, archivo))
    
    creator_kits = [ruta for ruta in archivos_excel if "Creator Kit" in os.path.basename(ruta)]
    
    if not creator_kits:
        print("No se encontraron archivos que contengan 'Creator Kit' en el nombre.")
        return

    print(f"Se encontraron {len(creator_kits)} Creator Kits para actualizar.")

    # 2. Inicializar Excel mediante COM Automation
    excel = None
    wb_base = None

    try:
        excel = win32com.client.Dispatch("Excel.Application")
        excel.Visible = False
        excel.DisplayAlerts = False
        excel.ScreenUpdating = False  # Evita renderizado en pantalla (acelera el proceso)
        excel.EnableEvents = False    # Evita la ejecución de eventos automáticos

        # 3. Leer la matriz de valores desde el archivo base
        print(f"Cargando valores desde '{PESTANA_BASE_ORIGEN}' (Rango: {RANGO_A_COPIAR})...")
        wb_base = excel.Workbooks.Open(os.path.abspath(ruta_archivo_base))
        ws_base = wb_base.Sheets(PESTANA_BASE_ORIGEN)
        
        # Ingestión de valores estáticos en memoria
        matriz_valores = ws_base.Range(RANGO_A_COPIAR).Value
        
        # Cierre seguro del archivo base inmediatamente después de leer
        wb_base.Close(False)
        wb_base = None

        print("Matriz cargada con éxito. Aplicando actualizaciones en lote...\n")

        # 4. Iterar sobre cada Creator Kit encontrado
        for ruta_creator in creator_kits:
            nombre_creator = os.path.basename(ruta_creator)
            print(f"Procesando: {nombre_creator}")

            wb_ck = None
            try:
                wb_ck = excel.Workbooks.Open(os.path.abspath(ruta_creator))
                ws_ck = wb_ck.Sheets(PESTANA_DESTINO_CK)

                # Calcular las celdas exactas según las dimensiones de la matriz copiada
                filas = len(matriz_valores)
                columnas = len(matriz_valores[0])

                celda_inicio = ws_ck.Range(CELDA_INICIAL_DESTINO)
                col_inicio = celda_inicio.Column
                row_inicio = celda_inicio.Row

                celda_fin = ws_ck.Cells(row_inicio + filas - 1, col_inicio + columnas - 1)
                rango_destino = ws_ck.Range(celda_inicio, celda_fin)

                # PEGAR SOLO VALORES ESTÁTICOS:
                rango_destino.Value = matriz_valores

                # Forzar recálculo completo de las fórmulas del Creator Kit
                excel.Calculate()

                # Guardar cambios y cerrar
                wb_ck.Close(True)  # True guarda los cambios automáticamente
                wb_ck = None
                print(f"  [Éxito] Datos pegados y fórmulas recalculadas.\n")

            except Exception as e:
                print(f"  [Error] Falló el procesamiento de {nombre_creator}: {e}\n")
                if wb_ck:
                    wb_ck.Close(False)  # Forzar cierre si falló a mitad de proceso

    except Exception as e_global:
        print(f"[ERROR GLOBAL] Ocurrió un error en el proceso principal: {e_global}")

    finally:
        # Limpieza absoluta de la instancia de Excel
        if wb_base:
            try:
                wb_base.Close(False)
            except:
                pass

        if excel:
            try:
                excel.ScreenUpdating = True
                excel.EnableEvents = True
                excel.Quit()
            except:
                pass

        print("Proceso de actualización masiva finalizado. Instancia de Excel liberada.")

if __name__ == "__main__":
    actualizar_creator_kits_masivamente()