import ctypes
import sys
from gui_app import Coding5sHubApp

def main():
    # Crear un Mutex (candado) en Windows para garantizar una sola instancia
    mutex_name = "Global\\Coding5s_Automation_Hub_Mutex"
    mutex = ctypes.windll.kernel32.CreateMutexW(None, False, mutex_name)
    last_error = ctypes.windll.kernel32.GetLastError()

    ERROR_ALREADY_EXISTS = 183

    if last_error == ERROR_ALREADY_EXISTS:
        # Mostrar alerta nativa de Windows si el programa ya está abierto
        ctypes.windll.user32.MessageBoxW(
            0,
            "Coding5s Hub is already running.\nPlease check your taskbar or open windows.",
            "Instance Already Open",
            0x30 | 0x0  # Icono de Advertencia y botón OK
        )
        sys.exit(0)

    app = Coding5sHubApp()
    app.mainloop()

if __name__ == "__main__":
    main()