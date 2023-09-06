#!/usr/bin/env python
# -*- coding: utf-8 -*-
# U-notas - archivo principal del programa
# Pablo Pizarro, 2014

# Importación de librerías de alto nivel
from lib import *

# Información del programa
AUTOR_NAME = "Pablo Pizarro"
AUTOR_NAME_EMAIL = "pablopizarro@ing.uchile.cl"
PROGRAM_VERSION = "0.8"
PROGRAM_TITLE = "U-Notas"

# Introducción
printAsciiArt()
colorcmd("\nU-Notas - version: " + PROGRAM_VERSION, "purple")
print "\nAutor: " + AUTOR_NAME

# Importación de librerías de bajo nivel
print "\nImportando librerias ...",
try:
    from analysis import *
    from browser import *
    from eval import *
    from pop import *
    from textures import *
    from test import *
    import gc
    print "ok"
except: print "abortado"; exit("Error al cargar las librerias")

# Configuración de las librerias
gc.enable()

# Constantes del programa
AVAIABLE_LANGS_TOPRINT = ["es", "en", "de", "it", "fr", "pr-pt"]  # idiomas disponibles para imprimir en consola
CONFIGURATION_DATA = ["ES", "background1", "notas/alumno", True, "punto", "{0}", "{0}", ESCALAS[1]]  # configuraciones del programa
COLORED_ARGUMENT = False  # define si se colorean las entradas en la consola
DEFAULT_LANG_CONTENT = "ES"  # idioma del contenido
FOLDER_CONFIG = ACTUAL_FOLDER + "config/"  # carpeta de configuraciones
FOLDER_DOCUMENTS = DATA_FOLDER + "documents/"  # carpeta de documentos
FOLDER_LANGS = ACTUAL_FOLDER + "langs/"  # carpeta de idiomas
HREF_HEADERS = "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1"  # headers para el browser
HREF_UPASAPORTE = "https://www.u-cursos.cl/upasaporte/login?servicio=ucursos&UCURSOS_SERVER=web38-int"  # página de inicio de upasaporte
LOGIN_FORM = ["username", "password"]  # formulario de inicio de sesión (por defecto)
PROGRAM_SIZE = [750, 450]  # tamaño en pixeles del programa
WEB_BASIC_HEADER = "Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)"  # header básico para consultas http sin una ventana browser

# Archivos del programa
FILE_ACTL_CONFIG = FOLDER_CONFIG + "actl.ini"  # actualización del programa
FILE_CONFIG = FOLDER_CONFIG + "config.ini"  # configuración del programa

# Se cargan las configuraciones
try:  # Se cargan la lista de idiomas disponibles
    LANG_LIST = loadFromArchive(FOLDER_LANGS + "/config/langs.txt", "Cargando archivo '{0}' ...", False)
    LANG_CONST = loadFromArchive(FOLDER_LANGS + "/config/const.ini", "Cargando archivo '{0}' ...", False)
    LANG_END = LANG_CONST[0]
    LANG_SEP = LANG_CONST[1].replace("*", " ")
except:  # Si ocurre un error al cargar el archivo de idiomas se termina la ejecución del programa
    print "Error :: Error fatal"
    Pop([["Error fatal", "Cerrar"], FOLDER_ICONS + "cross.ico", "error", 85, 300, "No se encuentra el archivo de idiomas, " + \
             PROGRAM_TITLE + " no puede iniciarse."]).w.mainloop(0)
    exit("No se encuentra el archivo de idiomas")
def loadConfig():  # Se cargan las configuraciones del juego
    try:  # Se consulta el archivo de configuraciones
        print "Consultando configuraciones ...", ; conf_file = open(FILE_CONFIG, "r")
        for i in conf_file:
            i = i.strip()
            c_command = i.split("=")
            if c_command[0].strip() == "SEPARADOR_DECIMAL":
                c_after_command = str(c_command[1]).split(",")
                CONFIGURATION_DATA[4] = c_after_command[0].strip().lower()
            if c_command[0].strip() == "ESCALA":
                c_after_command = str(c_command[1]).split(",")
                escala = c_after_command[0].strip().lower()
                if escala not in ESCALAS: print "{ESCALA} incorrecta ...",
                else: CONFIGURATION_DATA[7] = c_after_command[0].strip().lower()
            if c_command[0].strip() == "RULE_TITLE":
                c_after_command = str(c_command[1]).split(",")
                CONFIGURATION_DATA[6] = c_after_command[0].strip().upper()
            if c_command[0].strip() == "RULE_TITLE_CURSO":
                c_after_command = str(c_command[1]).split(",")
                CONFIGURATION_DATA[5] = c_after_command[0].strip().upper()
            if c_command[0].strip() == "ROJO":
                c_after_command = str(c_command[1]).split(",")
                if c_after_command[0].strip().upper() == "ON": CONFIGURATION_DATA[3] = True
                else: CONFIGURATION_DATA[3] = False
            if c_command[0].strip() == "LANGUAJE":  # idioma
                c_after_command = str(c_command[1]).split(",")
                # Si existe un elemento y esta en la lista de idiomas disponibles
                if len(c_after_command[0].strip()) != 0 and (c_after_command[0].strip().upper() + LANG_END in LANG_LIST):
                    CONFIGURATION_DATA[0] = c_after_command[0].strip().upper()
        conf_file.close(); print "ok"
    except:  # Se genera un nuevo archivo de configuraciones si este no existe
        print "generando configuraciones ...", ; archivo = open(CONFIGURATION_FILE, "w")
        archivo = open(FILE_CONFIG, "w")
        archivo.write("#Archivo de Configuraciones\n")
        archivo.write("#No haga cambios indebidos, ellos pueden afectar al comportamiento del programa\n\n")
        archivo.write("#Idioma\n")
        archivo.write("LANGUAJE = " + CONFIGURATION_DATA[0] + "\n\n")
        archivo.write("#Regla de título\n")
        archivo.write("RULE_TITLE = " + CONFIGURATION_DATA[6] + "\n\n")
        archivo.write("#Regla de título de curso\n")
        archivo.write("RULE_TITLE_CURSO = " + CONFIGURATION_DATA[5] + "\n\n")
        archivo.write("#Activar color rojo en notas\n")
        if CONFIGURATION_DATA[3]: archivo.write("ROJO = ON\n\n")
        else: archivo.write("ROJO = OFF\n\n")
        archivo.write("#Separador decimal\n")
        archivo.write("SEPARADOR_DECIMAL = " + CONFIGURATION_DATA[4] + "\n\n")
        archivo.write("#Escala\n")
        archivo.write("ESCALA = " + CONFIGURATION_DATA[7] + "\n\n")
        archivo.close(); print "ok"

# Idiomas
LANG = {}  # lista de strings para el idioma
def loadLang(first=True):  # Carga el idioma
    try:  # Se carga el idioma
        # Cargo el idioma definido por el archivo de configuraciones
        if COLORED_ARGUMENT:  # argumento colorido
            if first: print "Cargando idioma", ; colorcmd(CONFIGURATION_DATA[0].lower(), "lgray"); print "...",
            else: print lang(746), ; colorcmd(CONFIGURATION_DATA[0].lower(), "lgray"); print "...",
        else:
            if first: print "Cargando idioma", CONFIGURATION_DATA[0].lower(), "...",
            else: print lang(746), CONFIGURATION_DATA[0].lower(), "...",
        archivo = open(FOLDER_LANGS + CONFIGURATION_DATA[0] + LANG_END, "r")
        for i in archivo:
            item = i.strip().replace("\ufeff", "").split(LANG_SEP)
            if "\xef\xbb\xbf" in item[0]: item[0] = item[0][3:]  # elimino caracteres que no sean utf-8
            if item[0] == "": item[0] = "10"
            LANG[int(item[0].replace("\ufeff", ""))] = item[1].replace("|", " ")  # asigno los espacios
        archivo.close()
        print "ok"
    except:  # Error al cargar idioma, muestra mensaje y termina el programa
        print "Error fatal"; Pop([["Error fatal", "Cerrar"], FOLDER_ICONS + "cross.ico", "error", 85, 300, "Error al cargar el archivo de idioma '" + \
                                  CONFIGURATION_DATA[0] + "', " + PROGRAM_TITLE + " no puede iniciarse"]).w.mainloop(0)
        os._exit("Error al cargar el idioma")
def lang(i, a="", b="", c=""):  # Función que recibe un id y retorna el string correspondiente a dicho id
    try:  # Si existe el lang en la matriz de datos
        if len(a + b + c) != 0: return LANG[i].replace("%", a).replace("&", b).replace("$", c)
        else: return LANG[i]
    except:
        print "Error: ID[{0}] no existe en el archivo de idiomas '".format(i) + CONFIGURATION_DATA[0] + "'"
        return "%LANG ID[{0}]".format(i)

class UNotas:  # U-notas, entorno gráfico e interacción de objetos

    def __init__(self):  # Función constructora

        # Se definen variables locales para la acumulación de errores
        totalerrors = 0; totalwarnings = 0;

        # Métodos del constructor
        def _about(event=None):
            e = Pop([[lang(19), lang(31), lang(32), lang(33), lang(26)], self.images.image("ucursos"), "about", 115, 220, \
                 AUTOR_NAME, AUTOR_NAME_EMAIL, PROGRAM_VERSION])
            e.w.mainloop(1); del e
        def _ayuda(a=None, b=None):
            e = Pop([lang(18), self.images.image("help"), "ayuda", 400, 600, FOLDER_DOCUMENTS + "ayuda.txt"])
            e.w.mainloop(1); del e
        def _changelog(event=None):
            e = Pop([lang(21), self.images.image("page_gear"), "changelog", 400, 600, FOLDER_DOCUMENTS + "changelog.txt"])
            e.w.mainloop(1); del e
        def _configuracion(a=None):
            conf = Pop([[lang(16), lang(65), lang(69), lang(70), lang(75), lang(72), lang(25), lang(66), lang(71), lang(74), lang(67), lang(68), \
                         lang(76), lang(77), lang(78), lang(79), lang(80), lang(83)], \
                        self.images.image("configuration"), "config", 275, 316, CONFIGURATION_DATA[0], \
                        CONFIGURATION_DATA[2], FOLDER_LANGS, LANG_END, CONFIGURATION_DATA[3], CONFIGURATION_DATA[4], CONFIGURATION_DATA[5], \
                        CONFIGURATION_DATA[6], PROGRAM_TITLE, FOLDER_CONFIG, ESCALAS, CONFIGURATION_DATA[7]])
            conf.w.mainloop(1)
            if conf.sent:  # Se genera un nuevo archivo de configuraciones
                if (CONFIGURATION_DATA[3] != conf.values[3] or CONFIGURATION_DATA[4] != str(conf.values[4]) or CONFIGURATION_DATA[5] != str(conf.values[2]) \
                or CONFIGURATION_DATA[6] != str(conf.values[1]) or CONFIGURATION_DATA[7] != str(conf.values[5])):
                    print lang(81),
                    archivo = open(FILE_CONFIG, "w")
                    archivo.write("#Archivo de Configuraciones\n")
                    archivo.write("#No haga cambios indebidos, ellos pueden afectar al comportamiento del programa\n\n")
                    archivo.write("#Idioma\n")
                    archivo.write("LANGUAJE = " + str(conf.values[0]) + "\n\n")
                    archivo.write("#Regla de título\n")
                    archivo.write("RULE_TITLE = " + str(conf.values[1]) + "\n\n")
                    archivo.write("#Regla de título de curso\n")
                    archivo.write("RULE_TITLE_CURSO = " + str(conf.values[2]) + "\n\n")
                    archivo.write("#Activar color rojo en notas\n")
                    if conf.values[3]: archivo.write("ROJO = ON\n\n")
                    else: archivo.write("ROJO = OFF\n\n")
                    archivo.write("#Separador decimal\n")
                    archivo.write("SEPARADOR_DECIMAL = " + str(conf.values[4]) + "\n\n")
                    archivo.write("#Escala\n")
                    archivo.write("ESCALA = " + str(conf.values[5]) + "\n\n")
                    archivo.close(); print lang(12)
                    # Se aplican los cambios
                    print lang(82),
                    CONFIGURATION_DATA[3] = conf.values[3]
                    CONFIGURATION_DATA[4] = str(conf.values[4])
                    CONFIGURATION_DATA[5] = str(conf.values[2])
                    CONFIGURATION_DATA[6] = str(conf.values[1])
                    CONFIGURATION_DATA[7] = str(conf.values[5])
                    if CONFIGURATION_DATA[0] != conf.values[0]:  # Si cambió el idioma
                        CONFIGURATION_DATA[0] = conf.values[0]
                        LANG = {}
                        loadLang(False)
                        self.menubar.delete(0, 2)
                        self.archivomenu = Menu(self.menubar, tearoff=0)
                        self.archivomenu.add_command(label=lang(10), command=self.iniciar_sesion, accelerator="Ctrl+I")
                        self.archivomenu.add_command(label=lang(15), command=self.cerrar_sesion, accelerator="Ctrl+L")
                        self.archivomenu.add_separator()
                        self.archivomenu.add_command(label=lang(16), command=_configuracion, accelerator="Ctrl+C")
                        self.archivomenu.add_command(label=lang(17), command=self.salir, accelerator="Ctrl+S")
                        self.archivomenu.entryconfig(1, state=DISABLED)
                        self.menubar.add_cascade(label=lang(14), menu=self.archivomenu)
                        self.vermenu = Menu(self.menubar, tearoff=0)
                        self.ayudamenu = Menu(self.menubar, tearoff=0)
                        self.ayudamenu.add_command(label=lang(19), command=_about)
                        self.ayudamenu.add_command(label=lang(18), command=_ayuda, accelerator="Ctrl+A")
                        self.ayudamenu.add_command(label=lang(21), command=_changelog)
                        self.ayudamenu.add_command(label=lang(20), command=_licence)
                        self.menubar.add_cascade(label=lang(18), menu=self.ayudamenu)
                        if CONFIGURATION_DATA[0].lower() not in AVAIABLE_LANGS_TOPRINT:
                            sys.stdout, sys.stderr, sys.stdin, sys.__stdout__, sys.__stderr__, sys.__stdin__ = noStdOut(), noStdOut(), noStdOut(), \
                            noStdOut(), noStdOut(), noStdOut()
                    if self.loaded:
                        self.box_main()
                        if self.cursoloaded: self.cargar_curso(self.cursoloaded[0], self.cursoloaded[1], self.cursoloaded[2], None)
                    else: self.box_login()
                    print lang(12)
            del conf
        def _licence(event=None):
            e = Pop([lang(34), self.images.image("licence"), "licence", 400, 600, FOLDER_DOCUMENTS + "/licence/GNU.txt"])
            e.w.mainloop(1); del e
        def _update(event=None):
            if self.loaded and self.cursoloaded:
                self.cargar_curso(self.cursoloaded[0], self.cursoloaded[1], self.cursoloaded[2], None)

        # Creación de la ventana
        self.root = Tk()
        self.root.title(PROGRAM_TITLE)
        self.root.minsize(width=PROGRAM_SIZE[0], height=PROGRAM_SIZE[1])
        self.root.resizable(width=False, height=False)
        self.root.geometry('%dx%d+%d+%d' % (PROGRAM_SIZE[0], PROGRAM_SIZE[1], (self.root.winfo_screenwidth() - PROGRAM_SIZE[0]) / 2, \
                                          (self.root.winfo_screenheight() - PROGRAM_SIZE[1] - 50) / 2))
        self.root.focus_force()
        self.root.focus()

        # Creación de variables
        self.activecurso = False  # define si se ha cargado ya un curso
        self.browser = Browser()  # instancio el objeto browser
        self.browser.addHeaders(HREF_HEADERS)  # se agregan los headers al browser
        self.cursoloaded = []
        self.fonts = [tkFont.Font(family="Helvetica", size=9, weight=tkFont.BOLD), tkFont.Font(family="Helvetica", size=8), \
                      tkFont.Font(family="Helvetica", size=8, weight=tkFont.BOLD), tkFont.Font(family="Arial", size=12), \
                      tkFont.Font(family="Arial", size=13), tkFont.Font(family="Arial", size=11), \
                      tkFont.Font(family="Helvetica", size=10, slant="italic"), tkFont.Font(family="Arial", size=9), \
                      tkFont.Font(family="Arial", size=12), tkFont.Font(family="Times", size=12)]
        self.evaluaciones = {}  # diccionario que contiene las notas del usuario de una cierta asignatura
        self.loaded = False  # define si se ha iniciado la sesión
        print lang(11), ; self.images = UfilesTextures([lang(13), lang(12)]); print lang(12)  # cargo las texturas

        # Genero la interfaz gráfica
        try:
            print lang(46), ;self.root.iconbitmap(self.images.image("ucursos"))  # icono del programa
            self.menubar = Menu(self.root)  # creación de menús
            self.root.config(menu=self.menubar, cursor="arrow")
            self.archivomenu = Menu(self.menubar, tearoff=0)
            self.archivomenu.add_command(label=lang(10), command=self.iniciar_sesion, accelerator="Ctrl+I")
            self.archivomenu.add_command(label=lang(15), command=self.cerrar_sesion, accelerator="Ctrl+L")
            self.archivomenu.add_separator()
            self.archivomenu.add_command(label=lang(16), command=_configuracion, accelerator="Ctrl+C")
            self.archivomenu.add_command(label=lang(17), command=self.salir, accelerator="Ctrl+S")
            self.archivomenu.entryconfig(1, state=DISABLED)
            self.menubar.add_cascade(label=lang(14), menu=self.archivomenu)
            self.vermenu = Menu(self.menubar, tearoff=0)
            self.ayudamenu = Menu(self.menubar, tearoff=0)
            self.ayudamenu.add_command(label=lang(19), command=_about)
            self.ayudamenu.add_command(label=lang(18), command=_ayuda, accelerator="Ctrl+A")
            self.ayudamenu.add_command(label=lang(21), command=_changelog)
            self.ayudamenu.add_command(label=lang(20), command=_licence)
            self.menubar.add_cascade(label=lang(18), menu=self.ayudamenu)
            self.root.config(border=0, padx=0)
            self.background = Canvas(self.root, width=PROGRAM_SIZE[0], height=PROGRAM_SIZE[1], bd=-10, state=DISABLED, highlightthickness=0)
            self.background.pack(padx=0, pady=0, fill=BOTH, anchor=NW)
            self.background.create_image(PROGRAM_SIZE[0] / 2, PROGRAM_SIZE[1] / 2, image=self.images.image(CONFIGURATION_DATA[1])); self.background.update()
            self.box_login(); print lang(12)
        except: print lang(64); totalerrors += 1

        # Establezco los eventos del programa
        try:
            def _callback(event): self.root.focus()
            print lang(47), ;
            self.root.bind("<Control-A>", _ayuda); self.root.bind("<Control-a>", _ayuda)
            self.root.bind("<Control-C>", _configuracion); self.root.bind("<Control-c>", _configuracion)
            self.root.bind("<Control-I>", self.iniciar_sesion); self.root.bind("<Control-i>", self.iniciar_sesion)
            self.root.bind("<Control-L>", self.cerrar_sesion); self.root.bind("<Control-l>", self.cerrar_sesion)
            self.root.bind("<Control-S>", self.salir); self.root.bind("<Control-s>", self.salir)
            self.root.bind("<F1>", _ayuda)
            self.root.bind("<F5>", _update)
            self.root.protocol("WM_DELETE_WINDOW", self.salir)
            self.background.bind("<Button-1>", partial(_callback)); print lang(12);
        except: print lang(63); totalerrors += 1

        # Obtengo las actualizaciones del programa
        try:
            try:
                consultar = True
                archivo = open(FILE_ACTL_CONFIG, "r")
                for i in archivo:
                    if i == "-actl=1": consultar = False
            except: pass
            if consultar:  # Si esta activado la consulta
                print lang(35), ;
                version = getVersion("unotas", WEB_BASIC_HEADER)
                comparacion = compararVersiones(version, PROGRAM_VERSION)
                if comparacion == 2: print lang(36, version)
                elif comparacion == 0: print lang(37)
                else:
                    print lang(38)
                    e = Pop([[lang(39), lang(40), lang(41), lang(42), lang(43), lang(44), lang(29)], self.images.image("actualizacion"), "actualizacion", \
                             145, 280, PROGRAM_VERSION, version])
                    e.w.mainloop(1)
                    if e.sent:
                        if e.values[0] == "si": webbrowser.open(PRODUCT_LINK)
                        if e.values[1] == 1:
                            print lang(53), ;archivo = open(FILE_ACTL_CONFIG, "w"); archivo.write("-actl=1"); archivo.close(); print lang(12)
                    del e
        except: print lang(45); totalwarnings += 1

        # Mensaje que indica la finalización del constructor
        print lang(59),
        if totalwarnings == 0 and totalerrors == 0: print lang(12)
        else:
            if totalwarnings != 0 and totalerrors == 0: print lang(60).format(str(totalwarnings)).strip()
            elif totalerrors != 0 and totalwarnings == 0: print lang(61).format(str(totalerrors)).strip()
            elif totalwarnings != 0 and totalerrors != 0: print lang(62).format(str(totalerrors), str(totalwarnings)).strip()
        del totalwarnings; del totalerrors; print ""

        # Solo para probar
        self.loaded = True; self.box_main(); HREF_UPASAPORTE = "x"; self.test = True

    def box_error(self, code, string=""):  # Crea un diálogo de error
        self.root.config(menu=self.menubar, cursor="arrow")
        if string == "": box = Pop([[lang(25), lang(26)], self.images.image("exclamation"), "aviso", 70, 300, getError(code)])
        else: box = Pop([[lang(25), lang(26)], self.images.image("exclamation"), "aviso", 70, 300, getError(code).format(string)])
        box.w.mainloop(1)
        del box

    def box_main(self):  # Carga la página principal
        if self.loaded:
            self.background.delete(ALL)
            self.loginPassword.pack_forget()
            self.loginPassword.pack_forget()
            self.background.create_image(PROGRAM_SIZE[0] / 2, PROGRAM_SIZE[1] / 2, image=self.images.image("background2"))
            self.background.config(bd=-10)
            self.background.create_text(40, 120, text=lang(54), font=self.fonts[0], anchor=W, fill="#cb9a2d")
            self.background.update()
            self.box_menu_cursos()
            self.root.title(PROGRAM_TITLE)

    def box_menu_cursos(self):  # Dibujar los cursos del usuario
        def color_config(widget, color, event):
            widget.configure(foreground=color)
        if self.loaded:
            print lang(48), ;
            cursos = getCursos(self.browser.getHtml())
            font = tkFont.Font(family="Helvetica", size=9)
            height = 148
            cursos.sort()
            for curso in cursos:
                cursosFrame = Frame(self.background)
                txt = CONFIGURATION_DATA[5].format(curso[0], curso[2])
                curso_label = Label(cursosFrame, text=txt, font=self.fonts[1], \
                      anchor=W, fg="#858585", background="#FBFBFB", activeforeground="#CCCCCC", takefocus=True, width=24, cursor="hand2")
                curso_label.pack(fill=X, anchor=W)
                curso_label.bind("<Button-1>", partial(self.cargar_curso, curso[0], curso[2], curso[1]))
                curso_label.bind("<Button-3>", partial(openWeb, curso[1]))
                curso_label.bind("<Enter>", partial(color_config, curso_label, "#666666"))
                curso_label.bind("<Leave>", partial(color_config, curso_label, "#858585"))
                self.background.create_image(92, height, image=self.images.image("menu_cursos_box"))
                self.background.create_window(100, height, window=cursosFrame)
                self.background.create_image(13, height, image=self.images.image("cursos"))
                height += 27
            self.background.update(); print lang(12)

    def box_login(self):  # Dibuja el box de login
        def _clearLogin():
            self.loginPassword.delete(0, END)
            self.loginUsername.delete(0, END)
            self.loginUsername.focus()
        def _send(event):
            self.iniciar_sesion("box")
        def _toPassword(event):
            self.loginPassword.focus()
        self.background.delete(ALL)
        self.root.title(PROGRAM_TITLE)
        self.background.create_image(PROGRAM_SIZE[0] / 2, PROGRAM_SIZE[1] / 2, image=self.images.image(CONFIGURATION_DATA[1]))
        loginFrame = Frame(self.background)
        self.loginUsername = Entry(loginFrame, font=self.fonts[4], relief=GROOVE, fg="#333333")
        self.loginUsername.pack(pady=1)
        self.loginPassword = Entry(loginFrame, font=self.fonts[4], relief=GROOVE, fg="#333333"); self.loginPassword.pack(pady=1)
        self.loginPassword.config(show="*")
        self.loginPassword.bind("<Return>", _send)
        self.loginUsername.bind("<Return>", _toPassword)
        self.loginUsername.focus()
        self.background.create_text(PROGRAM_SIZE[0] / 2 - 155, PROGRAM_SIZE[1] / 2 - 36, text=lang(22), font=self.fonts[3], anchor=W)
        self.background.create_text(PROGRAM_SIZE[0] / 2 - 155, PROGRAM_SIZE[1] / 2 - 12, text=lang(23), font=self.fonts[3], anchor=W)
        button1Frame = Frame(self.background)
        bt_iniciarSesion = Button(button1Frame, text=lang(10), font=self.fonts[9], relief=GROOVE, command=lambda:self.iniciar_sesion("box"), \
                                  bg="#F6F7F8").pack(padx=0, pady=0)
        self.background.create_window(PROGRAM_SIZE[0] / 2 + 75 - 125, PROGRAM_SIZE[1] / 2 + 45, window=button1Frame)
        button2Frame = Frame(self.background)
        bt_iniciarReset = Button(button2Frame, text=lang(24), font=self.fonts[9], relief=GROOVE, command=_clearLogin, bg="#F6F7F8").pack(padx=0, pady=0)
        self.background.create_window(PROGRAM_SIZE[0] / 2 + 50, PROGRAM_SIZE[1] / 2 + 45, window=button2Frame)
        self.background.create_window(PROGRAM_SIZE[0] / 2 + 55, PROGRAM_SIZE[1] / 2 - 25, window=loginFrame)
        self.background.update(); self.root.title(PROGRAM_TITLE);

    def buscar(self, term):  # Función de buscar
        if self.loaded:  # Si se ha iniciado la sesión
            if self.activecurso:  # Si se ha cargado un curso
                if term != "" and term != lang(55):  # Si el término a buscar no está vacío
                    term = term.lower()
                    query = []
                    id_pack = 0
                    for k in self.files:  # Recorro los archivos
                        id_elem = 0
                        for j in k:  # Recorro los packs
                            for t in range(0, 8):  # Recorro las propiedades del archivo
                                if term in str(j[t]).lower():  # Si se encuentra el término
                                    query.append([id_pack, id_elem]); break
                            id_elem += 1
                        id_pack += 1
                    if len(query) != 0:  # Si se han encontrado archivos
                        self.filtrar("ver:busqueda", query)
                    else:  # Si no se encontró nada
                        box = Pop([[lang(49), lang(26)], self.images.image("folder_explore"), "aviso", 70, 300, lang(74)])
                        box.w.mainloop(1)
                        del box

    def cargar_curso(self, nombre, codigo, link, event):  # Carga un curso
        def _abortar():
            _delete_curso_frame()
            _delete_loading_widget()
            self.root.title(PROGRAM_TITLE)
            self.box_error(CURSOSxERROR_CANT_LOAD_CURSO, codigo); print lang(50)
            self.activecurso = False; delMatrix(self.cursoloaded);
            self.cursoloaded = []; self.evaluaciones = {}; return
        def _curso_toolbar():  # Dibuja el frame de los archivos
            def _buscar(form, event):  # Buscar un string
                self.buscar(form.get())
                form.delete(0, END)
                form.insert(0, lang(64))
                self.root.focus_force()
            def _del_search_form(form, event):  # Borra el contenido del campo de texto si este no ha sido escrito
                if form.get() == lang(64):
                    form.delete(0, END)
                    form.insert(0, "")
            def _herramienta(opc, event):  # Herramientas del curso
                if len(self.evaluaciones) == 0 and not opc == "configurar":
                    Pop([[lang(86), lang(26)], self.images.image("application_error"), "aviso", 83, 300, lang(85)])
                else:
                    print opc
            def _quit_focus(form, event):  # Quita el foco al buscador
                self.background.focus_force()
                if form.get() == "":
                    form.delete(0, END)
                    form.insert(0, lang(64))
            self.background.create_image(490, 230, image=self.images.image("box_curso"), tag='curso_background')
            frame_buscar = Frame(self.background)
            buscar_input = Entry(frame_buscar, width=30, font=self.fonts[6], fg="#6A7180", relief=GROOVE, bd=0, highlightbackground="#CCCCCC", \
                                 highlightcolor="#969CEB", highlightthickness=1, bg="#F6F7F8")
            buscar_input.pack()
            buscar_input.insert(0, lang(55))
            buscar_button_Frame = Frame(self.background, bg="#CCCCCC", cursor="hand2")
            canvas_buscarf = Canvas(buscar_button_Frame, width=20, height=20, bd=-2, bg="#F6F7F8", highlightthickness=0)
            canvas_buscarf.pack(anchor=NW, padx=0, pady=0)
            canvas_buscarf.create_image(9, 9, image=self.images.image("lupa"))
            button1 = Frame(self.background, cursor="hand2", bg="#E0E0E0")
            button1_canvas = Canvas(button1, width=42, height=38, bd=-3, bg="#E0E0E0", highlightthickness=0)
            button1_canvas.pack()
            button1_canvas.create_image(20, 17, image=self.images.image("notas"))
            button2 = Frame(self.background, cursor="hand2", bg="#E0E0E0")
            button2_canvas = Canvas(button2, width=42, height=38, bd=-3, bg="#E0E0E0", highlightthickness=0)
            button2_canvas.pack()
            button2_canvas.create_image(20, 17, image=self.images.image("datos_curso"))
            button3 = Frame(self.background, cursor="hand2", bg="#E0E0E0")
            button3_canvas = Canvas(button3, width=42, height=38, bd=-3, bg="#E0E0E0", highlightthickness=0)
            button3_canvas.pack()
            button3_canvas.create_image(20, 17, image=self.images.image("cursos_departamento"))
            canvas_buscarf.bind("<Button-1>", partial(_buscar, buscar_input))
            buscar_input.bind("<Escape>", partial(_quit_focus, buscar_input))
            buscar_input.bind("<FocusIn>", partial(_del_search_form, buscar_input))
            buscar_input.bind("<FocusOut>", partial(_quit_focus, buscar_input))
            buscar_input.bind("<Return>", partial(_buscar, buscar_input))
            button1_canvas.bind("<Button-1>", partial(_herramienta, "simular"))
            button2_canvas.bind("<Button-1>", partial(_herramienta, "exportar"))
            button3_canvas.bind("<Button-1>", partial(_herramienta, "configurar"))
            self.background.create_window(PROGRAM_SIZE[0] - 112, 15, window=frame_buscar, tag='buscar_form')
            self.background.create_window(PROGRAM_SIZE[0] - 16, 14, window=buscar_button_Frame, tag='buscar_lupa')
            self.background.create_window(PROGRAM_SIZE[0] - 518, 42, window=button1, tag='button1')
            self.background.create_text(PROGRAM_SIZE[0] - 556, 62, text=lang(56), font=self.fonts[7], fill="#666666", width=80, anchor=NW, tag="button1:txt")
            self.background.create_window(PROGRAM_SIZE[0] - 430, 42, window=button2, tag='button2')
            self.background.create_text(PROGRAM_SIZE[0] - 473, 62, text=lang(57), font=self.fonts[7], fill="#666666", width=90, anchor=NW, tag="button2:txt")
            self.background.create_window(PROGRAM_SIZE[0] - 340, 42, window=button3, tag='button3')
            self.background.create_text(PROGRAM_SIZE[0] - 378, 62, text=lang(58), font=self.fonts[7], fill="#666666", width=80, anchor=NW, tag="button3:txt")
        def _delete_curso_frame():  # Elimina el frame del curso anterior
            self.background.delete('buscar_form'); self.background.delete('buscar_lupa')
            self.background.delete('button1'); self.background.delete('button1:txt')
            self.background.delete('button2'); self.background.delete('button2:txt')
            self.background.delete('button3'); self.background.delete('button3:txt')
            self.background.delete('curso_background'); self.background.delete('no_notas'); self.background.update()
        def _delete_loading_widget():  # Elimina el frame "cargando..."
            self.background.delete('loading_text')
            self.background.delete('loading_widget')
            self.background.delete('loading_background')
            self.background.config(cursor="arrow")
        def _loading_frame():  # Dibuja el frame "cargando"
            self.background.config(cursor="wait")
            self.background.create_image(490, -150, image=self.images.image("box_curso"), tag='loading_background')
            frame_loading = Frame(self.background)
            ttk.Progressbar(frame_loading, mode='indeterminate', name='bp', phase=0, length=200).pack()
            bp = frame_loading.nametowidget('bp')
            bp.start(20)
            self.background.create_window(PROGRAM_SIZE[0] / 2 + 130, 49, window=frame_loading, tag='loading_text')
            self.background.create_text(PROGRAM_SIZE[0] / 2 - 57, 50, text=lang(52), font=self.fonts[5], anchor=W, tag='loading_widget')
            self.background.focus_force()
            self.background.update()
        if self.loaded:  # si se ha iniciado sesión
            print lang(51).format(codigo),
            if self.activecurso: _delete_curso_frame()
            if True:  # Se carga el curso
                _loading_frame()
                link += CONFIGURATION_DATA[2]
                self.root.title(CONFIGURATION_DATA[6].format(PROGRAM_TITLE, nombre))
                self.cursoloaded = [nombre, codigo, link]

                # Se obtiene la información html
                #if self.browser.abrirLink(link) == BR_ERRORxNO_ACCESS_WEB:  # Si no se pudo cargar la web
                #   _abortar()
                #html = self.browser.getHtml()
                html = CURSO3
                if buscarNotas(html):  # si existen notas por obtener
                    self.evaluaciones = {}
                    obtenerEvaluaciones(html, CONFIGURATION_DATA[4], CONFIGURATION_DATA[7], self.evaluaciones)
                    _delete_loading_widget(); _curso_toolbar()
                    print self.evaluaciones.keys()
                else:
                    _delete_loading_widget(); _curso_toolbar()
                    self.background.create_text(PROGRAM_SIZE[0] / 2, PROGRAM_SIZE[1] / 2, text=lang(84), font=self.fonts[8], anchor=W, tag='no_notas')
                self.activecurso = True  # se define el curso como cargado
                print lang(12)
            else: _abortar()

    def cerrar_sesion(self, event=None):  # Cerrar la sesion
        if self.loaded:  # Si hay una sesión activa
            e = Pop([[lang(15), lang(27), lang(28), lang(29), lang(30)], self.images.image("help"), "preguntarSNC", \
                         75, 250, True])  # Se pregunta si quiere guardar o no
            e.w.mainloop(1)
            if e.sent:  # Se procede en función de la respuesta
                if e.values[0] == "si":  # Se cierra la sesión
                    self.archivomenu.entryconfig(1, state=DISABLED);
                    self.browser.clearCookies()
                    self.box_login()
                    self.activecurso = False; self.loaded = False;
                    delMatrix(self.cursoloaded); del(self.evaluaciones);
                    self.root.title(PROGRAM_TITLE)
                    return True
                else: return False
            del e
        else: return True

    def iniciar_sesion(self, event=None):  # Iniciar sesión
        if event == "box": pass  # si se inició sesión desde el box
        else:  # Si se inició sesión desde un atajo de teclado o desde el menú
            self.cerrar_sesion(); return
        print lang(49), ; login = [self.loginUsername.get(), self.loginPassword.get()]
        if self.browser.abrirLink(HREF_UPASAPORTE) == BR_ERRORxNO_ACCESS_WEB:  # Si no se pudo cargar la web
            self.box_error(BR_ERRORxNO_ACCESS_WEB); print lang(50); return
        self.browser.selectFormById(0)
        self.browser.submitForm(LOGIN_FORM, login)  # se envian los datos
        estado = comprobarLogin(self.browser.getHtml())
        if estado is not True: self.box_error(estado); print lang(50); return  # si no se inició la sesión
        else:  # si la sesión se inició
            print lang(12)
            self.archivomenu.entryconfig(1, state=NORMAL)
            self.loaded = True  # indica que se ha iniciado la sesión
            self.loginPassword.destroy()
            self.loginUsername.destroy()
            self.box_main()
            self.root.config(cursor="arrow")

    def salir(self):  # Salir del programa
        self.browser.clearCookies()
        os.system("taskkill /PID " + str(os.getpid()) + " /F")

# Inicio del programa
if __name__ == '__main__':
    loadConfig()
    loadLang(True)  # se carga el idioma por defecto
    window = UNotas()
    window.root.mainloop(0)
