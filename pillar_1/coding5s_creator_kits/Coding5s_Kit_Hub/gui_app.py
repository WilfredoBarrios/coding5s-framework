import os
import shutil
import threading
from tkinter import filedialog
import webbrowser
import customtkinter as ctk
import sys

from excel_engine import (
    ejecutar_actualizacion_base,
    ejecutar_generacion_student_kits,
    ejecutar_inyeccion_formulas,
)
from utils import (
    abrir_archivo_en_sistema,
    buscar_creator_kits,
    buscar_todos_los_excels,
    cargar_metadatos_idiomas,
    verificar_archivos_base,
    cargar_configuracion,
    guardar_configuracion,
    cargar_contenido_texto
)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class CustomModal(ctk.CTkToplevel):
    """Modal 100% CustomTkinter para reemplazar los diálogos nativos de Windows."""

    def __init__(self, master, title, message, tipo="info"):
        super().__init__(master)
        self.title(title)

        # Centrar relativo a la ventana principal
        x = master.winfo_x() + (master.winfo_width() // 2) - 200
        y = master.winfo_y() + (master.winfo_height() // 2) - 100
        self.geometry(f"400x200+{x}+{y}")

        self.transient(master)
        self.resizable(False, False)
        self.result = False

        color = "#3498db"
        if tipo == "error":
            color = "#e74c3c"
        elif tipo == "warning":
            color = "#f39c12"
        elif tipo == "confirm":
            color = "#2ecc71"

        lbl_title = ctk.CTkLabel(self, text=title, font=ctk.CTkFont("Arial", 16, "bold"), text_color=color)
        lbl_title.pack(pady=(20, 5))

        lbl_msg = ctk.CTkLabel(self, text=message, font=ctk.CTkFont("Arial", 13), wraplength=350)
        lbl_msg.pack(pady=(0, 20), padx=20, expand=True)

        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(fill="x", pady=15, side="bottom")

        if tipo == "confirm":
            btn_yes = ctk.CTkButton(btn_frame, text="Yes", command=self.on_yes, fg_color="#2ecc71",
                                    hover_color="#27ae60", width=100)
            btn_yes.pack(side="left", expand=True, padx=10)
            btn_no = ctk.CTkButton(btn_frame, text="No", command=self.on_no, fg_color="#e74c3c", hover_color="#c0392b",
                                   width=100)
            btn_no.pack(side="right", expand=True, padx=10)
        else:
            btn_ok = ctk.CTkButton(btn_frame, text="OK", command=self.on_yes, width=100)
            btn_ok.pack(expand=True)

        self.grab_set()
        self.wait_window()

    def on_yes(self):
        self.result = True
        self.destroy()

    def on_no(self):
        self.result = False
        self.destroy()


class TextRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.configure(state="normal")
        self.text_widget.insert("end", string)
        self.text_widget.see("end")
        self.text_widget.configure(state="disabled")

    def flush(self):
        pass


class Coding5sHubApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("⚙️ Coding5s — Creator & Student Kit Automation Hub v1.1")
        self.geometry("1180x850")
        self.minsize(1050, 750)

        # Detectar el directorio real del programa (o del ejecutable)
        if getattr(sys, "frozen", False):
            self.app_dir = os.path.dirname(os.path.abspath(sys.executable))
        else:
            self.app_dir = os.path.dirname(os.path.abspath(__file__))

        # 🚀 CORRECCIÓN: El directorio de trabajo SIEMPRE será la carpeta del ejecutable.
        self.directorio_raiz = self.app_dir

        # Cargamos la configuración (idioma guardado) pero NO sobreescribimos la ruta.
        self.config = cargar_configuracion()

        self.creator_kits_encontrados = []
        self.todos_excels_encontrados = []
        self.checkboxes_kits = []
        self.checkboxes_opn = []
        self.dict_idiomas = {}

        self.ui_elements = {"inj": [], "upd": [], "stu": [], "opn": []}

        self.archivo_seleccionado_open_tab = ctk.StringVar(value="")
        self.archivo_seleccionado_inj = ctk.StringVar(value="")

        self.search_var_inj = ctk.StringVar()
        self.search_var_upd = ctk.StringVar()
        self.search_var_stu = ctk.StringVar()
        self.search_var_opn = ctk.StringVar()

        self.search_var_inj.trace_add("write", lambda *args: self.aplicar_filtro("inj", self.search_var_inj.get()))
        self.search_var_upd.trace_add("write", lambda *args: self.aplicar_filtro("upd", self.search_var_upd.get()))
        self.search_var_stu.trace_add("write", lambda *args: self.aplicar_filtro("stu", self.search_var_stu.get()))
        self.search_var_opn.trace_add("write", lambda *args: self.aplicar_filtros_opn())

        self._build_top_bar()

        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True, padx=15, pady=(5, 15))

        self.tab_injector = self.tabview.add("💉 1. Formula Injector")
        self.tab_updater = self.tabview.add("🔄 2. BaseData Updater")
        self.tab_student = self.tabview.add("🎓 3. Student Kit Generator")
        self.tab_open = self.tabview.add("📂 4. Open Files")
        self.tab_help = self.tabview.add("❓ 5. Help")

        self._build_tab_injector()
        self._build_tab_updater()
        self._build_tab_student()
        self._build_tab_open()
        self._build_tab_help()

        self.refrescar_lista_kits()

    def _build_top_bar(self):
        top_frame = ctk.CTkFrame(self)
        top_frame.pack(fill="x", padx=15, pady=(15, 5))

        lbl_dir = ctk.CTkLabel(top_frame, text="Working Directory:", font=ctk.CTkFont("Arial", 12, "bold"))
        lbl_dir.pack(side="left", padx=(10, 5), pady=10)

        self.entry_dir = ctk.CTkEntry(top_frame, width=500)
        self.entry_dir.insert(0, self.directorio_raiz)
        self.entry_dir.configure(state="readonly")
        self.entry_dir.pack(side="left", padx=5, pady=10)

        btn_browse = ctk.CTkButton(top_frame, text="📂 Browse", width=80, command=self.seleccionar_directorio)
        btn_browse.pack(side="left", padx=5, pady=10)

        btn_refresh = ctk.CTkButton(top_frame, text="🔄 Refresh", width=80, fg_color="#d35400", hover_color="#a84300",
                                    command=self.refrescar_lista_kits)
        btn_refresh.pack(side="left", padx=5, pady=10)

        btn_about = ctk.CTkButton(top_frame, text="ℹ️ About", width=80, fg_color="#34495e", hover_color="#2c3e50",
                                  command=self.mostrar_about)
        btn_about.pack(side="right", padx=10, pady=10)

    def mostrar_about(self):
        about_text = cargar_contenido_texto("about_content.md", self.app_dir)
        modal = ctk.CTkToplevel(self)
        modal.title("About Coding5s Hub")
        x = self.winfo_x() + (self.winfo_width() // 2) - 250
        y = self.winfo_y() + (self.winfo_height() // 2) - 190
        modal.geometry(f"500x380+{x}+{y}")
        modal.transient(self)
        modal.grab_set()

        tb = ctk.CTkTextbox(modal, wrap="word", font=ctk.CTkFont("Arial", 13))
        tb.pack(fill="both", expand=True, padx=20, pady=(20, 10))
        tb.insert("1.0", about_text)
        tb.configure(state="disabled")

        frame_links = ctk.CTkFrame(modal, fg_color="transparent")
        frame_links.pack(fill="x", padx=20, pady=(0, 15))

        ctk.CTkButton(frame_links, text="🌐 Website", width=100, fg_color="#3498db",
                      command=lambda: webbrowser.open("https://coding5s.com/")).pack(side="left", padx=5)
        ctk.CTkButton(frame_links, text="🐙 GitHub", width=100, fg_color="#2c3e50",
                      command=lambda: webbrowser.open("https://github.com/WilfredoBarrios/coding5s-framework")).pack(
            side="left", padx=5)
        ctk.CTkButton(frame_links, text="📺 YouTube", width=100, fg_color="#e74c3c", hover_color="#c0392b",
                      command=lambda: webbrowser.open("https://www.youtube.com/@Coding5s")).pack(side="left", padx=5)

        btn_close = ctk.CTkButton(modal, text="Close", command=modal.destroy)
        btn_close.pack(pady=(0, 20))

    def seleccionar_directorio(self):
        folder = filedialog.askdirectory(initialdir=self.directorio_raiz)
        if folder:
            self.directorio_raiz = folder
            self.entry_dir.configure(state="normal")
            self.entry_dir.delete(0, "end")
            self.entry_dir.insert(0, self.directorio_raiz)
            self.entry_dir.configure(state="readonly")

            idioma_actual = self.option_lang.get() if hasattr(self, 'option_lang') else "English"
            guardar_configuracion(self.directorio_raiz, idioma_actual)
            self.refrescar_lista_kits()

    def aplicar_filtro(self, tipo, query):
        query = query.lower()
        for item in self.ui_elements[tipo]:
            if query in item["nombre"]:
                item["w"].grid(row=item["row"], column=0, sticky="w", padx=5, pady=4)
                item["lbl"].grid(row=item["row"], column=1, sticky="w", padx=10, pady=4)
            else:
                item["w"].grid_remove()
                item["lbl"].grid_remove()
        self.actualizar_contadores()

    def actualizar_contadores(self, *args):
        q_upd = self.search_var_upd.get().lower()
        sel_upd = sum(
            1 for item in self.checkboxes_kits if item["var_upd"].get() and q_upd in item["kit"]["nombre"].lower())
        vis_upd = sum(1 for item in self.checkboxes_kits if q_upd in item["kit"]["nombre"].lower())

        if sel_upd > 0:
            self.lbl_counter_upd.configure(text=f"✅ {sel_upd} of {vis_upd} visible files selected",
                                           text_color="#2ecc71", font=ctk.CTkFont("Arial", 12, "bold"))
        else:
            self.lbl_counter_upd.configure(text=f"0 of {vis_upd} visible files selected", text_color="#A0A0A0",
                                           font=ctk.CTkFont("Arial", 11, slant="italic"))

        q_stu = self.search_var_stu.get().lower()
        sel_stu = sum(
            1 for item in self.checkboxes_kits if item["var_stu"].get() and q_stu in item["kit"]["nombre"].lower())
        vis_stu = sum(1 for item in self.checkboxes_kits if q_stu in item["kit"]["nombre"].lower())

        if sel_stu > 0:
            self.lbl_counter_stu.configure(text=f"✅ {sel_stu} of {vis_stu} visible files selected",
                                           text_color="#2ecc71", font=ctk.CTkFont("Arial", 12, "bold"))
        else:
            self.lbl_counter_stu.configure(text=f"0 of {vis_stu} visible files selected", text_color="#A0A0A0",
                                           font=ctk.CTkFont("Arial", 11, slant="italic"))

    def _build_tab_injector(self):
        tab = self.tab_injector
        ctk.CTkLabel(tab, text="Massive Formula Injector (FGen -> PromptGenerator)",
                     font=ctk.CTkFont("Arial", 15, "bold")).pack(anchor="w", padx=10, pady=(5, 0))
        ctk.CTkLabel(tab, text="📖 Select ONLY ONE Creator Kit. Formulas will be injected safely.",
                     text_color="#A0A0A0").pack(anchor="w", padx=10, pady=(0, 10))

        frame_files = ctk.CTkFrame(tab)
        frame_files.pack(fill="both", expand=True, padx=10, pady=5)

        frame_sub_header = ctk.CTkFrame(frame_files, fg_color="transparent")
        frame_sub_header.pack(fill="x", padx=10, pady=(5, 0))

        ctk.CTkLabel(frame_sub_header, text="Select a SINGLE Creator Kit to Process:",
                     font=ctk.CTkFont("Arial", 12, "bold")).pack(side="left")

        # BÚSQUEDA Y '✖'
        search_frame_inj = ctk.CTkFrame(frame_sub_header, fg_color="transparent")
        search_frame_inj.pack(side="right", padx=10)

        ctk.CTkEntry(search_frame_inj, textvariable=self.search_var_inj, placeholder_text="🔍 Search...", height=24,
                     width=130).pack(side="left")
        ctk.CTkButton(search_frame_inj, text="✖", width=24, height=24, fg_color="transparent", hover_color="#555555",
                      text_color="#f1c40f", command=lambda: self.search_var_inj.set("")).pack(side="left", padx=(2, 0))

        self.scroll_injector_kits = ctk.CTkScrollableFrame(frame_files, height=140)
        self.scroll_injector_kits.pack(fill="both", expand=True, padx=10, pady=5)
        self.scroll_injector_kits.grid_columnconfigure(0, weight=3)
        self.scroll_injector_kits.grid_columnconfigure(1, weight=2)

        bot_frame = ctk.CTkFrame(frame_files, fg_color="transparent")
        bot_frame.pack(fill="x", padx=10, pady=8)

        self.lbl_status_inj = ctk.CTkLabel(bot_frame, text="🟢 Ready to process", font=ctk.CTkFont("Arial", 12, "bold"),
                                           text_color="#2ecc71")
        self.lbl_status_inj.pack(side="left", padx=5)

        ctk.CTkButton(bot_frame, text="💉 Inject Formulas", fg_color="#1f538d", hover_color="#14375e",
                      font=ctk.CTkFont("Arial", 13, "bold"), command=self.hilo_inyectar_formulas).pack(side="right",
                                                                                                       padx=5)

        ctk.CTkLabel(tab, text="Execution Logs:", font=ctk.CTkFont("Arial", 12, "bold")).pack(anchor="w", padx=10,
                                                                                              pady=(2, 0))
        self.log_injector = ctk.CTkTextbox(tab, height=140, font=ctk.CTkFont("Consolas", 11))
        self.log_injector.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.log_injector.configure(state="disabled")

    def _build_tab_updater(self):
        tab = self.tab_updater

        for widget in tab.winfo_children():
            widget.destroy()

        ctk.CTkLabel(tab, text="BaseData Mass Updater (Creator Kits Sync)", font=ctk.CTkFont("Arial", 15, "bold")).pack(
            anchor="w", padx=10, pady=(5, 0))
        ctk.CTkLabel(tab, text="📖 Configure your injection parameters below and select the kits to sync.",
                     text_color="#A0A0A0").pack(anchor="w", padx=10, pady=(0, 5))

        frame_config = ctk.CTkFrame(tab)
        frame_config.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(frame_config, text="Base File:", font=ctk.CTkFont("Arial", 11, "bold")).grid(row=0, column=0,
                                                                                                  padx=10, pady=5,
                                                                                                  sticky="e")
        self.upd_base_file = ctk.CTkEntry(frame_config, width=230)
        self.upd_base_file.insert(0, "creator_kit_Base_File_for_CKs.xlsx")
        self.upd_base_file.configure(state="readonly")
        self.upd_base_file.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(frame_config, text="Base Sheet:", font=ctk.CTkFont("Arial", 11, "bold")).grid(row=0, column=2,
                                                                                                   padx=10, pady=5,
                                                                                                   sticky="e")
        self.upd_base_sheet = ctk.CTkEntry(frame_config, width=120)
        self.upd_base_sheet.insert(0, "BaseData")
        self.upd_base_sheet.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(frame_config, text="Copy Range:", font=ctk.CTkFont("Arial", 11, "bold")).grid(row=1, column=0,
                                                                                                   padx=10, pady=5,
                                                                                                   sticky="e")
        self.upd_copy_range = ctk.CTkEntry(frame_config, width=230)
        self.upd_copy_range.insert(0, "A1:B10")
        self.upd_copy_range.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(frame_config, text="Target Sheet:", font=ctk.CTkFont("Arial", 11, "bold")).grid(row=1, column=2,
                                                                                                     padx=10, pady=5,
                                                                                                     sticky="e")
        self.upd_dest_sheet = ctk.CTkEntry(frame_config, width=120)
        self.upd_dest_sheet.insert(0, "FGen_S1")
        self.upd_dest_sheet.grid(row=1, column=3, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(frame_config, text="Target Cell:", font=ctk.CTkFont("Arial", 11, "bold")).grid(row=2, column=0,
                                                                                                    padx=10, pady=5,
                                                                                                    sticky="e")
        self.upd_dest_cell = ctk.CTkEntry(frame_config, width=230)
        self.upd_dest_cell.insert(0, "C95")
        self.upd_dest_cell.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        frame_status = ctk.CTkFrame(tab, fg_color="transparent")
        frame_status.pack(fill="x", padx=10, pady=(0, 5))
        self.lbl_status_upd_file = ctk.CTkLabel(frame_status, text="📄 Checking...",
                                                font=ctk.CTkFont("Arial", 12, "bold"))
        self.lbl_status_upd_file.pack(side="left")

        self.btn_find_base = ctk.CTkButton(frame_status, text="🔍 Find Base File", width=110, height=24,
                                           fg_color="#8e44ad", command=self.buscar_archivo_base_manual)
        self.btn_find_base.pack(side="right", padx=(5, 0))
        self.btn_open_base = ctk.CTkButton(frame_status, text="📂 Open Base File", width=110, height=24,
                                           fg_color="#146c43", command=lambda: abrir_archivo_en_sistema(
                os.path.join(self.directorio_raiz, self.upd_base_file.get())))
        self.btn_open_base.pack(side="right")

        frame_files = ctk.CTkFrame(tab)
        frame_files.pack(fill="both", expand=True, padx=10, pady=5)

        frame_sub_header = ctk.CTkFrame(frame_files, fg_color="transparent")
        frame_sub_header.pack(fill="x", padx=10, pady=(5, 0))
        ctk.CTkLabel(frame_sub_header, text="Select Creator Kits:", font=ctk.CTkFont("Arial", 12, "bold")).pack(
            side="left")

        self.lbl_counter_upd = ctk.CTkLabel(frame_sub_header, text="0 of 0 visible files selected",
                                            font=ctk.CTkFont("Arial", 11, slant="italic"), text_color="#A0A0A0")
        self.lbl_counter_upd.pack(side="left", padx=15)

        ctk.CTkButton(frame_sub_header, text="Deselect All", width=80, height=24, fg_color="#555555",
                      command=lambda: self.marcar_desmarcar_todos("upd", False)).pack(side="right")
        ctk.CTkButton(frame_sub_header, text="Select All", width=80, height=24,
                      command=lambda: self.marcar_desmarcar_todos("upd", True)).pack(side="right", padx=(5, 5))

        # BÚSQUEDA Y '✖'
        search_frame_upd = ctk.CTkFrame(frame_sub_header, fg_color="transparent")
        search_frame_upd.pack(side="right", padx=10)

        self.search_entry_upd = ctk.CTkEntry(search_frame_upd, textvariable=self.search_var_upd,
                                             placeholder_text="🔍 Search...", height=24, width=130)
        self.search_entry_upd.pack(side="left")

        ctk.CTkButton(
            search_frame_upd, text="✖", width=24, height=24, fg_color="transparent", hover_color="#555555",
            text_color="#f1c40f", command=lambda: self.search_var_upd.set("")
        ).pack(side="left", padx=(2, 0))

        self.scroll_updater_kits = ctk.CTkScrollableFrame(frame_files, height=140)
        self.scroll_updater_kits.pack(fill="both", expand=True, padx=10, pady=5)
        self.scroll_updater_kits.grid_columnconfigure(0, weight=3)
        self.scroll_updater_kits.grid_columnconfigure(1, weight=2)

        bot_frame = ctk.CTkFrame(frame_files, fg_color="transparent")
        bot_frame.pack(fill="x", padx=10, pady=8)

        self.lbl_status_upd = ctk.CTkLabel(bot_frame, text="🟢 Ready to process", font=ctk.CTkFont("Arial", 12, "bold"),
                                           text_color="#2ecc71")
        self.lbl_status_upd.pack(side="left", padx=5)

        ctk.CTkButton(bot_frame, text="🔄 Update Selected Kits", fg_color="#2fa572", hover_color="#237d55",
                      font=ctk.CTkFont("Arial", 13, "bold"), command=self.hilo_actualizar_base).pack(side="right",
                                                                                                     padx=5)

        ctk.CTkLabel(tab, text="Execution Logs:", font=ctk.CTkFont("Arial", 12, "bold")).pack(anchor="w", padx=10,
                                                                                              pady=(2, 0))
        self.log_updater = ctk.CTkTextbox(tab, height=140, font=ctk.CTkFont("Consolas", 11))
        self.log_updater.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.log_updater.configure(state="disabled")

    def _build_tab_student(self):
        tab = self.tab_student
        ctk.CTkLabel(tab, text="Student Kit Generator & Language Sync", font=ctk.CTkFont("Arial", 15, "bold")).pack(
            anchor="w", padx=10, pady=(5, 0))

        frame_status = ctk.CTkFrame(tab, fg_color="transparent")
        frame_status.pack(fill="x", padx=10, pady=(0, 5))
        self.lbl_status_stu_file = ctk.CTkLabel(frame_status, text="📄 Checking...",
                                                font=ctk.CTkFont("Arial", 12, "bold"))
        self.lbl_status_stu_file.pack(side="left")

        self.btn_find_template = ctk.CTkButton(frame_status, text="🔍 Find Template", width=110, height=24,
                                               fg_color="#8e44ad", command=self.buscar_template_manual)
        self.btn_open_template = ctk.CTkButton(frame_status, text="📂 Open Template", width=110, height=24,
                                               fg_color="#146c43", command=lambda: abrir_archivo_en_sistema(
                os.path.join(self.directorio_raiz, "Student Kit Template.xlsx")))

        frame_config = ctk.CTkFrame(tab)
        frame_config.pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(frame_config, text="Target Language (B6):", font=ctk.CTkFont("Arial", 12, "bold")).pack(
            side="left", padx=(10, 5), pady=10)

        self.option_lang = ctk.CTkOptionMenu(frame_config, values=["English"], width=180,
                                             command=self.al_cambiar_idioma)
        self.option_lang.pack(side="left", padx=5, pady=10)
        self.option_lang.set(self.config.get("last_language", "English"))

        self.lbl_lang_category = ctk.CTkLabel(frame_config, text="", font=ctk.CTkFont("Arial", 13, "bold"),
                                              text_color="#F1C40F")
        self.lbl_lang_category.pack(side="left", padx=(25, 10), pady=10)
        self.lbl_lang_spoken = ctk.CTkLabel(frame_config, text="", font=ctk.CTkFont("Arial", 13, "bold"),
                                            text_color="#F1C40F")
        self.lbl_lang_spoken.pack(side="left", padx=10, pady=10)

        frame_files = ctk.CTkFrame(tab)
        frame_files.pack(fill="both", expand=True, padx=10, pady=5)

        frame_sub_header = ctk.CTkFrame(frame_files, fg_color="transparent")
        frame_sub_header.pack(fill="x", padx=10, pady=(5, 0))
        ctk.CTkLabel(frame_sub_header, text="Select Kits to Generate:", font=ctk.CTkFont("Arial", 12, "bold")).pack(
            side="left")

        self.lbl_counter_stu = ctk.CTkLabel(frame_sub_header, text="0 of 0 visible files selected",
                                            font=ctk.CTkFont("Arial", 11, slant="italic"), text_color="#A0A0A0")
        self.lbl_counter_stu.pack(side="left", padx=15)

        ctk.CTkButton(frame_sub_header, text="Deselect All", width=80, height=24, fg_color="#555555",
                      command=lambda: self.marcar_desmarcar_todos("stu", False)).pack(side="right")
        ctk.CTkButton(frame_sub_header, text="Select All", width=80, height=24,
                      command=lambda: self.marcar_desmarcar_todos("stu", True)).pack(side="right", padx=(5, 5))

        # BÚSQUEDA Y '✖'
        search_frame_stu = ctk.CTkFrame(frame_sub_header, fg_color="transparent")
        search_frame_stu.pack(side="right", padx=10)

        self.search_entry_stu = ctk.CTkEntry(search_frame_stu, textvariable=self.search_var_stu,
                                             placeholder_text="🔍 Search...", height=24, width=130)
        self.search_entry_stu.pack(side="left")
        ctk.CTkButton(
            search_frame_stu, text="✖", width=24, height=24, fg_color="transparent", hover_color="#555555",
            text_color="#f1c40f", command=lambda: self.search_var_stu.set("")
        ).pack(side="left", padx=(2, 0))

        self.scroll_student_kits = ctk.CTkScrollableFrame(frame_files, height=120)
        self.scroll_student_kits.pack(fill="both", expand=True, padx=10, pady=5)
        self.scroll_student_kits.grid_columnconfigure(0, weight=3)
        self.scroll_student_kits.grid_columnconfigure(1, weight=2)

        bot_frame = ctk.CTkFrame(frame_files, fg_color="transparent")
        bot_frame.pack(fill="x", padx=10, pady=8)

        self.lbl_status_stu = ctk.CTkLabel(bot_frame, text="🟢 Ready to process", font=ctk.CTkFont("Arial", 12, "bold"),
                                           text_color="#2ecc71")
        self.lbl_status_stu.pack(side="left", padx=5)

        ctk.CTkButton(bot_frame, text="🎓 Generate Student Kits", fg_color="#b25e1a", hover_color="#894711",
                      font=ctk.CTkFont("Arial", 13, "bold"), command=self.hilo_generar_students).pack(side="right",
                                                                                                      padx=5)

        ctk.CTkLabel(tab, text="Execution Logs:", font=ctk.CTkFont("Arial", 12, "bold")).pack(anchor="w", padx=10,
                                                                                              pady=(2, 0))
        self.log_student = ctk.CTkTextbox(tab, height=140, font=ctk.CTkFont("Consolas", 11))
        self.log_student.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.log_student.configure(state="disabled")

    def _build_tab_open(self):
        tab = self.tab_open
        ctk.CTkLabel(tab, text="Excel File Explorer (Smart Filter & Multi-Copy)",
                     font=ctk.CTkFont("Arial", 15, "bold")).pack(anchor="w", padx=10, pady=(5, 5))
        frame_files = ctk.CTkFrame(tab)
        frame_files.pack(fill="both", expand=True, padx=10, pady=5)

        frame_sub_header = ctk.CTkFrame(frame_files, fg_color="transparent")
        frame_sub_header.pack(fill="x", padx=10, pady=(5, 0))

        self.filtro_tipo_opn = ctk.StringVar(value="All Kits")
        seg_btn = ctk.CTkSegmentedButton(frame_sub_header, values=["All Kits", "Creator Kits", "Student Kits"],
                                         variable=self.filtro_tipo_opn, command=lambda x: self.aplicar_filtros_opn())
        seg_btn.pack(side="left")

        self.modo_multi_opn = ctk.BooleanVar(value=False)
        switch_multi = ctk.CTkSwitch(frame_sub_header, text="Multi-Select Mode", variable=self.modo_multi_opn,
                                     command=self.dibujar_lista_opn)
        switch_multi.pack(side="left", padx=20)

        # --- BOTONES SELECT/DESELECT Y BÚSQUEDA ORDENADOS ---
        self.btn_opn_deselect = ctk.CTkButton(frame_sub_header, text="Deselect All", width=80, height=24,
                                              fg_color="#555555",
                                              command=lambda: self.marcar_desmarcar_todos_opn(False), state="disabled")
        self.btn_opn_deselect.pack(side="right")

        self.btn_opn_select = ctk.CTkButton(frame_sub_header, text="Select All", width=80, height=24,
                                            command=lambda: self.marcar_desmarcar_todos_opn(True), state="disabled")
        self.btn_opn_select.pack(side="right", padx=(5, 5))

        search_frame_opn = ctk.CTkFrame(frame_sub_header, fg_color="transparent")
        search_frame_opn.pack(side="right", padx=10)

        self.search_entry_opn = ctk.CTkEntry(search_frame_opn, textvariable=self.search_var_opn,
                                             placeholder_text="🔍 Search...", height=24, width=130)
        self.search_entry_opn.pack(side="left")

        ctk.CTkButton(search_frame_opn, text="✖", width=24, height=24, fg_color="transparent", hover_color="#555555",
                      text_color="#f1c40f", command=lambda: self.search_var_opn.set("")).pack(side="left", padx=(2, 0))
        # ----------------------------------------------------

        self.scroll_open_excels = ctk.CTkScrollableFrame(frame_files, height=350)
        self.scroll_open_excels.pack(fill="both", expand=True, padx=10, pady=5)
        self.scroll_open_excels.grid_columnconfigure(0, weight=3)
        self.scroll_open_excels.grid_columnconfigure(1, weight=2)

        bot_frame = ctk.CTkFrame(frame_files, fg_color="transparent")
        bot_frame.pack(fill="x", padx=10, pady=12)

        self.btn_save_copy = ctk.CTkButton(bot_frame, text="💾 Save Copy of Selected", fg_color="#8e44ad",
                                           hover_color="#732d91", font=ctk.CTkFont("Arial", 13, "bold"),
                                           state="disabled", command=self.guardar_copia_archivo)
        self.btn_save_copy.pack(side="left", padx=5)

        self.btn_open_file = ctk.CTkButton(bot_frame, text="🚀 Open Selected in Excel", fg_color="#146c43",
                                           hover_color="#0f5132", font=ctk.CTkFont("Arial", 13, "bold"),
                                           state="disabled", command=self.abrir_excel_seleccionado)
        self.btn_open_file.pack(side="right", padx=5)

    def _build_tab_help(self):
        tab = self.tab_help
        ctk.CTkLabel(tab, text="📖 Automation Hub Documentation", font=ctk.CTkFont("Arial", 15, "bold")).pack(anchor="w",
                                                                                                             padx=10,
                                                                                                             pady=(5,
                                                                                                                   5))

        help_text = cargar_contenido_texto("help_content.md", self.app_dir)
        tb = ctk.CTkTextbox(tab, wrap="word", font=ctk.CTkFont("Arial", 13))
        tb.pack(fill="both", expand=True, padx=10, pady=(5, 10))
        tb.insert("1.0", help_text)
        tb.configure(state="disabled")

        frame_links = ctk.CTkFrame(tab, fg_color="transparent")
        frame_links.pack(fill="x", padx=10, pady=10)

        ctk.CTkButton(frame_links, text="🌐 Official Website", fg_color="#3498db",
                      command=lambda: webbrowser.open("https://coding5s.com/")).pack(side="left", padx=5)
        ctk.CTkButton(frame_links, text="🐙 GitHub Framework", fg_color="#2c3e50",
                      command=lambda: webbrowser.open("https://github.com/WilfredoBarrios/coding5s-framework")).pack(
            side="left", padx=5)
        ctk.CTkButton(frame_links, text="📺 YouTube Tutorials", fg_color="#e74c3c", hover_color="#c0392b",
                      command=lambda: webbrowser.open("https://www.youtube.com/@Coding5s")).pack(side="left", padx=5)

    def aplicar_filtros_opn(self):
        query = self.search_var_opn.get().lower()
        tipo_filtro = self.filtro_tipo_opn.get()

        for item in self.ui_elements["opn"]:
            coincide_busqueda = query in item["nombre"]
            coincide_tipo = True

            if tipo_filtro == "Creator Kits" and item["tipo_kit"] != "creator kit":
                coincide_tipo = False
            elif tipo_filtro == "Student Kits" and item["tipo_kit"] != "student kit":
                coincide_tipo = False

            if coincide_busqueda and coincide_tipo:
                item["w"].grid(row=item["row"], column=0, sticky="w", padx=5, pady=4)
                item["lbl"].grid(row=item["row"], column=1, sticky="w", padx=10, pady=4)
            else:
                item["w"].grid_remove()
                item["lbl"].grid_remove()

    def dibujar_lista_opn(self):
        for w in self.scroll_open_excels.winfo_children(): w.destroy()
        self.ui_elements["opn"] = []
        self.checkboxes_opn = []
        self.archivo_seleccionado_open_tab.set("")

        # --- HABILITAR/DESHABILITAR BOTONES MULTI-SELECT ---
        es_multi = self.modo_multi_opn.get()
        if hasattr(self, 'btn_opn_select'):
            estado = "normal" if es_multi else "disabled"
            self.btn_opn_select.configure(state=estado)
            self.btn_opn_deselect.configure(state=estado)
        # ---------------------------------------------------

        ctk.CTkLabel(self.scroll_open_excels, text="File Name", font=ctk.CTkFont("Arial", 12, "bold"),
                     text_color="#3498db").grid(row=0, column=0, sticky="w", padx=5, pady=(0, 5))
        ctk.CTkLabel(self.scroll_open_excels, text="Subfolder Path", font=ctk.CTkFont("Arial", 12, "bold"),
                     text_color="#3498db").grid(row=0, column=1, sticky="w", padx=10, pady=(0, 5))

        archivos_validos = [f for f in self.todos_excels_encontrados if
                            "Creator Kit" in f["nombre_real"] or "Student Kit" in f["nombre_real"]]

        if not archivos_validos:
            ctk.CTkLabel(self.scroll_open_excels, text="⚠️ No Kits found in directory.", text_color="orange").grid(
                row=1, column=0, padx=5, pady=5, sticky="w")
            self.btn_open_file.configure(state="disabled")
            self.btn_save_copy.configure(state="disabled")
            return

        for i, item in enumerate(archivos_validos, start=1):
            nombre = item["nombre_real"]
            lbl = ctk.CTkLabel(self.scroll_open_excels, text=item["subcarpeta"], text_color="#A0A0A0")

            if es_multi:
                var_chk = ctk.BooleanVar(value=False)
                w = ctk.CTkCheckBox(self.scroll_open_excels, text=nombre, variable=var_chk,
                                    command=self.al_seleccionar_opn)
                self.checkboxes_opn.append({"kit": item, "var": var_chk})
            else:
                w = ctk.CTkRadioButton(self.scroll_open_excels, text=nombre,
                                       variable=self.archivo_seleccionado_open_tab, value=item["ruta"],
                                       command=self.al_seleccionar_opn)

            tipo_kit = "creator kit" if "Creator Kit" in nombre else "student kit"
            self.ui_elements["opn"].append(
                {"w": w, "lbl": lbl, "nombre": nombre.lower(), "row": i, "tipo_kit": tipo_kit})

            w.grid(row=i, column=0, sticky="w", padx=5, pady=4)
            lbl.grid(row=i, column=1, sticky="w", padx=10, pady=4)

        self.aplicar_filtros_opn()
        self.al_seleccionar_opn()

    def guardar_copia_archivo(self):
        es_multi = self.modo_multi_opn.get()
        if es_multi:
            seleccionados = [c["kit"] for c in self.checkboxes_opn if c["var"].get()]
            if not seleccionados: return

            ruta_destino = filedialog.askdirectory(title="Select Destination Folder")
            if ruta_destino:
                exitos = 0
                errores = 0
                for kit in seleccionados:
                    try:
                        shutil.copy2(kit["ruta"], os.path.join(ruta_destino, kit["nombre_real"]))
                        exitos += 1
                    except Exception:
                        errores += 1
                CustomModal(self, "Copy Summary", f"✅ Copied {exitos} files.\n❌ Errors: {errores}", tipo="info")
        else:
            ruta_origen = self.archivo_seleccionado_open_tab.get()
            if not ruta_origen: return

            nombre_sugerido = os.path.basename(ruta_origen)
            ruta_destino = filedialog.asksaveasfilename(
                title="Save Copy As...",
                initialfile=nombre_sugerido,
                defaultextension=".xlsx",
                filetypes=[("Excel Files", "*.xlsx")]
            )
            if ruta_destino:
                try:
                    shutil.copy2(ruta_origen, ruta_destino)
                    CustomModal(self, "Success", "File successfully copied.", tipo="info")
                except Exception as e:
                    CustomModal(self, "Error", f"Failed to save copy:\n{e}", tipo="error")

    def buscar_archivo_base_manual(self):
        ruta = filedialog.askopenfilename(title="Select BaseData File", filetypes=[("Excel Files", "*.xlsx")])
        if ruta:
            nombre_archivo = os.path.basename(ruta)
            shutil.copy(ruta, os.path.join(self.directorio_raiz, nombre_archivo))

            # Actualiza el entry readonly
            self.upd_base_file.configure(state="normal")
            self.upd_base_file.delete(0, "end")
            self.upd_base_file.insert(0, nombre_archivo)
            self.upd_base_file.configure(state="readonly")

            self.refrescar_lista_kits()

    def buscar_template_manual(self):
        ruta = filedialog.askopenfilename(title="Select Student Template", filetypes=[("Excel Files", "*.xlsx")])
        if ruta and os.path.basename(ruta) == "Student Kit Template.xlsx":
            shutil.copy(ruta, os.path.join(self.directorio_raiz, "Student Kit Template.xlsx"))
            self.refrescar_lista_kits()
        elif ruta:
            CustomModal(self, "Invalid File", "Select exactly:\n'Student Kit Template.xlsx'", tipo="error")

    def al_cambiar_idioma(self, idioma_seleccionado):
        if idioma_seleccionado in self.dict_idiomas:
            info = self.dict_idiomas[idioma_seleccionado]
            self.lbl_lang_category.configure(text=info.get('category', ''))
            self.lbl_lang_spoken.configure(text=f"Spoken In: {info.get('spoken_in', '')}")
            guardar_configuracion(self.directorio_raiz, idioma_seleccionado)
        else:
            self.lbl_lang_category.configure(text="")
            self.lbl_lang_spoken.configure(text="")

    def al_seleccionar_opn(self, *args):
        es_multi = self.modo_multi_opn.get()

        if es_multi:
            cant_seleccionados = sum(1 for c in self.checkboxes_opn if c["var"].get())

            # Guardar copias no tiene límite
            estado_save = "normal" if cant_seleccionados > 0 else "disabled"
            self.btn_save_copy.configure(state=estado_save)

            # Límite de seguridad para abrir en Excel (Máximo 3)
            if 1 <= cant_seleccionados <= 3:
                self.btn_open_file.configure(state="normal", text="🚀 Open Selected in Excel")
            elif cant_seleccionados > 3:
                self.btn_open_file.configure(state="disabled", text="⚠️ Max 3 Files to Open")
            else:
                self.btn_open_file.configure(state="disabled", text="🚀 Open Selected in Excel")
        else:
            hay_seleccion = bool(self.archivo_seleccionado_open_tab.get())
            estado = "normal" if hay_seleccion else "disabled"
            self.btn_open_file.configure(state=estado, text="🚀 Open Selected in Excel")
            self.btn_save_copy.configure(state=estado)

    def marcar_desmarcar_todos_opn(self, estado):
        """Marca o desmarca todos los kits en la pestaña Open Files (Solo los visibles)."""
        if not self.modo_multi_opn.get():
            return

        query = self.search_var_opn.get().lower()
        tipo_filtro = self.filtro_tipo_opn.get()

        for item in self.checkboxes_opn:
            nombre = item["kit"]["nombre_real"].lower()

            # FIX: Evaluamos contra 'creator kit' en minúsculas para que coincida con 'nombre'
            tipo_kit = "creator kit" if "creator kit" in nombre else "student kit"

            coincide_busqueda = query in nombre
            coincide_tipo = True

            if tipo_filtro == "Creator Kits" and tipo_kit != "creator kit":
                coincide_tipo = False
            elif tipo_filtro == "Student Kits" and tipo_kit != "student kit":
                coincide_tipo = False

            if coincide_busqueda and coincide_tipo:
                item["var"].set(estado)

        self.al_seleccionar_opn()

    def abrir_excel_seleccionado(self):
        es_multi = self.modo_multi_opn.get()
        if es_multi:
            rutas = [c["kit"]["ruta"] for c in self.checkboxes_opn if c["var"].get()]
            for ruta in rutas:
                abrir_archivo_en_sistema(ruta)
        else:
            if self.archivo_seleccionado_open_tab.get():
                abrir_archivo_en_sistema(self.archivo_seleccionado_open_tab.get())

    def refrescar_lista_kits(self):
        self.creator_kits_encontrados = buscar_creator_kits(self.directorio_raiz)
        self.todos_excels_encontrados = buscar_todos_los_excels(self.directorio_raiz)
        has_base, has_template = verificar_archivos_base(self.directorio_raiz)

        if has_base:
            self.lbl_status_upd_file.configure(text="📄 creator_kit_Base_File_for_CKs.xlsx | Status: ✅ Present",
                                               text_color="#2ecc71")
            self.btn_find_base.pack_forget()
            self.btn_open_base.pack(side="left", padx=15)
        else:
            self.lbl_status_upd_file.configure(text="📄 creator_kit_Base_File_for_CKs.xlsx | Status: ❌ Missing",
                                               text_color="#e74c3c")
            self.btn_open_base.pack_forget()
            self.btn_find_base.pack(side="left", padx=15)

        if has_template:
            self.lbl_status_stu_file.configure(text="📄 Student Kit Template.xlsx | Status: ✅ Present",
                                               text_color="#2ecc71")
            self.btn_find_template.pack_forget()
            self.btn_open_template.pack(side="left", padx=15)
        else:
            self.lbl_status_stu_file.configure(text="📄 Student Kit Template.xlsx | Status: ❌ Missing",
                                               text_color="#e74c3c")
            self.btn_open_template.pack_forget()
            self.btn_find_template.pack(side="left", padx=15)

        self.dict_idiomas = cargar_metadatos_idiomas(self.app_dir)
        if self.dict_idiomas:
            self.option_lang.configure(values=list(self.dict_idiomas.keys()))
            current_lang = self.option_lang.get()
            if current_lang not in self.dict_idiomas:
                current_lang = list(self.dict_idiomas.keys())[0]
                self.option_lang.set(current_lang)
            self.al_cambiar_idioma(current_lang)

        for scroll in [self.scroll_injector_kits, self.scroll_updater_kits, self.scroll_student_kits]:
            for w in scroll.winfo_children(): w.destroy()

        self.checkboxes_kits = []
        self.ui_elements["inj"] = []
        self.ui_elements["upd"] = []
        self.ui_elements["stu"] = []
        self.archivo_seleccionado_inj.set("")

        for scroll in [self.scroll_injector_kits, self.scroll_updater_kits, self.scroll_student_kits]:
            if not self.creator_kits_encontrados:
                ctk.CTkLabel(scroll, text="⚠️ No 'Creator Kit' files found.", text_color="orange").grid(row=0, column=0,
                                                                                                        padx=5, pady=5,
                                                                                                        sticky="w")
                continue

            ctk.CTkLabel(scroll, text="File Name", font=ctk.CTkFont("Arial", 12, "bold"), text_color="#3498db").grid(
                row=0, column=0, sticky="w", padx=5, pady=(0, 5))
            ctk.CTkLabel(scroll, text="Subfolder Path", font=ctk.CTkFont("Arial", 12, "bold"),
                         text_color="#3498db").grid(row=0, column=1, sticky="w", padx=10, pady=(0, 5))

            for i, item in enumerate(self.creator_kits_encontrados, start=1):
                nombre = item["nombre"]

                if scroll == self.scroll_injector_kits:
                    w = ctk.CTkRadioButton(scroll, text=nombre, variable=self.archivo_seleccionado_inj,
                                           value=item["ruta"])
                    lbl = ctk.CTkLabel(scroll, text=item["subcarpeta"], text_color="#A0A0A0")
                    self.ui_elements["inj"].append({"w": w, "lbl": lbl, "nombre": nombre.lower(), "row": i})
                else:
                    var_chk = ctk.BooleanVar(value=False)
                    w = ctk.CTkCheckBox(scroll, text=nombre, variable=var_chk, command=self.actualizar_contadores)
                    lbl = ctk.CTkLabel(scroll, text=item["subcarpeta"], text_color="#A0A0A0")
                    if scroll == self.scroll_updater_kits:
                        self.checkboxes_kits.append(
                            {"kit": item, "var_upd": var_chk, "var_stu": ctk.BooleanVar(value=False)})
                        self.ui_elements["upd"].append({"w": w, "lbl": lbl, "nombre": nombre.lower(), "row": i})
                    else:
                        for c in self.checkboxes_kits:
                            if c["kit"]["ruta"] == item["ruta"]: c["var_stu"] = var_chk
                        self.ui_elements["stu"].append({"w": w, "lbl": lbl, "nombre": nombre.lower(), "row": i})

                w.grid(row=i, column=0, sticky="w", padx=5, pady=4)
                lbl.grid(row=i, column=1, sticky="w", padx=10, pady=4)

        self.aplicar_filtro("inj", self.search_var_inj.get())
        self.aplicar_filtro("upd", self.search_var_upd.get())
        self.aplicar_filtro("stu", self.search_var_stu.get())

        # Redibuja y filtra completamente la pestaña Open
        self.dibujar_lista_opn()

    def marcar_desmarcar_todos(self, tipo, estado):
        query = self.search_var_upd.get().lower() if tipo == "upd" else self.search_var_stu.get().lower()
        for item in self.checkboxes_kits:
            if query in item["kit"]["nombre"].lower():
                if tipo == "upd":
                    item["var_upd"].set(estado)
                elif tipo == "stu":
                    item["var_stu"].set(estado)
        self.actualizar_contadores()

    def obtener_kits_seleccionados(self, tipo):
        if tipo == "inj":
            return [k for k in self.creator_kits_encontrados if k["ruta"] == self.archivo_seleccionado_inj.get()]
        return [c["kit"] for c in self.checkboxes_kits if c[f"var_{tipo}"].get()]

    def actualizar_progreso(self, actual, total, texto, lbl_status):
        def _update():
            lbl_status.configure(text=f"⏳ Processing [{actual}/{total}]: {texto}", text_color="#3498db")

        self.after(0, _update)

    def preparar_hilo(self, log_widget, tipo, msg_confirm, func_engine, kwargs_engine, lbl_status, auto_refresh=False):
        kits = self.obtener_kits_seleccionados(tipo)
        if not kits:
            CustomModal(self, "No Selection", "Please select at least one Kit.", tipo="warning")
            return

        confirm = CustomModal(self, "Confirm Action", f"Are you sure you want to process {len(kits)} selected kit(s)?",
                              tipo="confirm")
        if not confirm.result:
            return

        lbl_status.configure(text="⏳ Initializing process...", text_color="#f1c40f")

        log_widget.configure(state="normal")
        log_widget.delete("1.0", "end")
        log_widget.configure(state="disabled")

        redirector = TextRedirector(log_widget)
        kwargs_engine["lista_kits"] = kits
        kwargs_engine["callback_log"] = redirector.write

        def run_wrapper():
            exito = func_engine(**kwargs_engine)

            def _finish():
                if exito:
                    lbl_status.configure(text="✅ Successfully Updated!", text_color="#2ecc71")
                    if auto_refresh:
                        self.refrescar_lista_kits()
                else:
                    lbl_status.configure(text="❌ Finished with errors (check logs)", text_color="#e74c3c")

            self.after(0, _finish)

        threading.Thread(target=run_wrapper, daemon=True).start()

    def hilo_inyectar_formulas(self):
        self.preparar_hilo(
            self.log_injector, "inj", "Inject Formulas", ejecutar_inyeccion_formulas,
            {"directorio_raiz": self.directorio_raiz,
             "callback_progress": lambda a, t, n: self.actualizar_progreso(a, t, n, self.lbl_status_inj)},
            self.lbl_status_inj
        )

    def hilo_actualizar_base(self):
        self.preparar_hilo(
            self.log_updater, "upd", "Update BaseData", ejecutar_actualizacion_base,
            {
                "directorio_raiz": self.directorio_raiz,
                "archivo_base": self.upd_base_file.get(),
                "pestana_base": self.upd_base_sheet.get(),
                "rango_copiar": self.upd_copy_range.get(),
                "pestana_destino_ck": self.upd_dest_sheet.get(),
                "celda_destino": self.upd_dest_cell.get(),
                "callback_progress": lambda a, t, n: self.actualizar_progreso(a, t, n, self.lbl_status_upd)
            },
            self.lbl_status_upd
        )

    def hilo_generar_students(self):
        self.preparar_hilo(
            self.log_student, "stu", "Generate Student Kits", ejecutar_generacion_student_kits,
            {"directorio_raiz": self.directorio_raiz, "idioma_objetivo": self.option_lang.get(),
             "callback_progress": lambda a, t, n: self.actualizar_progreso(a, t, n, self.lbl_status_stu)},
            self.lbl_status_stu,
            auto_refresh=True
        )


if __name__ == "__main__":
    app = Coding5sHubApp()
    app.mainloop()