import json
import os
import sys


def is_file_locked(filepath):
    """Verifica si un archivo está bloqueado por el OS o abierto en Excel."""
    if not os.path.exists(filepath):
        return False
    if "~$" in os.path.basename(filepath):
        return True
    try:
        # Intento de renombrar el archivo a sí mismo (falla si está en uso)
        os.rename(filepath, filepath)
        return False
    except OSError:
        return True


def get_config_path():
    """Obtiene la ruta segura para guardar config.json en AppData."""
    appdata = os.getenv('APPDATA')
    if appdata:
        config_dir = os.path.join(appdata, "Coding5s_Hub")
        os.makedirs(config_dir, exist_ok=True)
        return os.path.join(config_dir, "config.json")
    return "config.json"


def cargar_configuracion():
    """Carga la última ruta y preferencias del usuario."""
    ruta = get_config_path()
    if os.path.exists(ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"last_directory": "", "last_language": "English"}


def guardar_configuracion(directorio, idioma):
    """Guarda la ruta y preferencias del usuario."""
    ruta = get_config_path()
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump({"last_directory": directorio, "last_language": idioma}, f)
    except Exception:
        pass


def cargar_contenido_texto(filename, directorio_raiz):
    """Carga archivos .md o .txt, soportando el entorno portable de PyInstaller de forma prioritaria."""
    # Buscar primero en el empaquetado interno de PyInstaller
    if hasattr(sys, "_MEIPASS"):
        ruta = os.path.join(sys._MEIPASS, filename)
    else:
        ruta = os.path.join(directorio_raiz, filename)

    if os.path.exists(ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            pass

    # Fallback por si acaso busca en la raíz local
    ruta_local = os.path.join(directorio_raiz, filename)
    if os.path.exists(ruta_local):
        try:
            with open(ruta_local, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            pass

    return f"⚠️ No se pudo cargar el archivo: {filename}"


def buscar_creator_kits(directorio_raiz):
    """Escanea recursivamente en busca de archivos 'Creator Kit'."""
    archivos_creator = []
    for raiz, directorios, archivos in os.walk(directorio_raiz):
        for archivo in archivos:
            if archivo.endswith(".xlsx") and not archivo.startswith("~$") and "Creator Kit" in archivo:
                ruta_completa = os.path.join(raiz, archivo)
                rel_path = os.path.relpath(raiz, directorio_raiz)
                subcarpeta = "/" if rel_path == "." else f"/{rel_path.replace(os.sep, '/')}"
                archivos_creator.append({"nombre": archivo, "ruta": ruta_completa, "subcarpeta": subcarpeta})
    return archivos_creator


def buscar_todos_los_excels(directorio_raiz):
    """Escanea recursivamente TODOS los archivos .xlsx."""
    archivos_excel = []
    for raiz, directorios, archivos in os.walk(directorio_raiz):
        for archivo in archivos:
            if archivo.endswith(".xlsx") and not archivo.startswith("~$"):
                ruta_completa = os.path.join(raiz, archivo)
                rel_path = os.path.relpath(raiz, directorio_raiz)
                subcarpeta = "/" if rel_path == "." else f"/{rel_path.replace(os.sep, '/')}"
                nombre_formateado = f"[{subcarpeta}] {archivo}" if subcarpeta != "/" else f"[/] {archivo}"
                archivos_excel.append(
                    {"nombre_formateado": nombre_formateado, "nombre_real": archivo, "ruta": ruta_completa,
                     "subcarpeta": subcarpeta})
    return archivos_excel


def verificar_archivos_base(directorio_raiz):
    """Verifica si existen los archivos base necesarios."""
    base_file_path = os.path.join(directorio_raiz, "creator_kit_Base_File_for_CKs.xlsx")
    template_path = os.path.join(directorio_raiz, "Student Kit Template.xlsx")
    return os.path.exists(base_file_path), os.path.exists(template_path)


def cargar_metadatos_idiomas(directorio_raiz):
    """Carga languages.json priorizando el entorno empaquetado de PyInstaller."""
    rutas_a_probar = []

    # Si está empaquetado, la ruta principal es _MEIPASS
    if hasattr(sys, "_MEIPASS"):
        rutas_a_probar.append(os.path.join(sys._MEIPASS, "languages.json"))

    # Ruta local basada en el directorio proporcionado
    if directorio_raiz:
        rutas_a_probar.append(os.path.join(directorio_raiz, "languages.json"))

    # Ruta local basada en el directorio del script actual (desarrollo)
    rutas_a_probar.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "languages.json"))

    for ruta_json in rutas_a_probar:
        if os.path.exists(ruta_json):
            try:
                with open(ruta_json, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass

    return {"English": {"category": "High-Resource Language", "spoken_in": "United States"}}


def abrir_archivo_en_sistema(ruta_archivo):
    """Abre un archivo en Windows."""
    if os.path.exists(ruta_archivo):
        os.startfile(ruta_archivo)