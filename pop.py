#!/usr/bin/env python
# -*- coding: utf-8 -*-
# POP - U-Files
# Pablo Pizarro, 2014

# Importación de librerias
from lib import *

# Constantes del programa
DEFAULT_FONT_TITLE = "Arial", 10
COMMENT_COLOR = "#666666"
LANGS = {"AR":"العربي", \
         "DE":"Deutsch", \
         "EN":"English", \
         "ES":"Español", \
         "FR":"Français", \
         "HI":"हिंदी", \
         "IT":"Italiano", \
         "JA":"日本", \
         "PR-PT":"Português", \
         "RU":"Русский", \
         "TH":"ภาษาไทย", \
         "ZH-CN":"中国的"}

class Pop:  # Ventanas emergentes

    def __init__(self, properties):  # Función constructora
        self.lang = properties[0]
        if "list" in str(type(self.lang)): title = self.lang[0]
        else: title = properties[0]
        icon = properties[1]
        typeObject = properties[2]
        size = properties[4], properties[3]
        if title == "Error" or title == "Buscar" or title == "Licencia": self.w = Toplevel()
        else: self.w = Tk()
        self.w.protocol("WM_DELETE_WINDOW", self.kill)
        self.values = []
        if size[0] != 0 and size[1] != 0:
            self.w.minsize(width=size[0], height=size[1])
            self.w.geometry('%dx%d+%d+%d' % (size[0], size[1], (self.w.winfo_screenwidth() - size[0]) / 2, (self.w.winfo_screenheight() - size[1]) / 2))
        self.w.resizable(width=False, height=False)
        self.w.focus_force()
        self.w.title(title)
        try: self.w.iconbitmap(icon)
        except: self.w.iconbitmap("data/icons/ucursos.ico")
        self.sent = False

        if typeObject == "about":  # Acerca de
            Label(self.w, text=self.lang[1] + properties[5], font=DEFAULT_FONT_TITLE, border=5).pack()
            Label(self.w, text=self.lang[2] + properties[6], font=DEFAULT_FONT_TITLE, border=5).pack()
            Label(self.w, text=self.lang[3] + str(properties[7]), font=DEFAULT_FONT_TITLE, border=5).pack()
            Button(self.w, text=self.lang[4], command=self.w.destroy, relief=GROOVE).pack()
            self.w.bind("<Return>", self.destruir)
            self.w.bind("<Escape>", self.destruir)
        elif typeObject == "actualizacion":  # Actualización del programa
            def resp(res, typ="normal"):  # Función que envia una respuesta
                delMatrix(self.values)
                self.values.append(res)
                if typ == "act": self.values.append(self.buscaractualizacion.get())
                self.sent = True
                self.destruir()
            Label(self.w, text=self.lang[4], font=DEFAULT_FONT_TITLE, border=10).pack()
            Label(self.w, text=self.lang[1].format(properties[5]), font=DEFAULT_FONT_TITLE, border=1).pack()
            Label(self.w, text=self.lang[2].format(properties[6]), font=DEFAULT_FONT_TITLE, border=1).pack()
            F = Frame(self.w)
            F.pack(pady=6)
            Button(F, text=self.lang[5], command=lambda:resp("si", "act"), width=8, relief=GROOVE).pack(side=LEFT)  # si
            Label(F, text=" ").pack(side=LEFT)
            Button(F, text=self.lang[6], command=lambda:resp("no", "act"), width=8, relief=GROOVE).pack(side=LEFT)  # no
            Label(F, text=" ").pack()
            self.buscaractualizacion = IntVar(self.w)
            self.buscaractualizacion.set(0)
            c = Checkbutton(self.w, text=self.lang[3], variable=self.buscaractualizacion, onvalue=1, offvalue=0)
            c.pack()
        elif typeObject == "config":  # Ventana de configuraciones
            Label(self.w, text=self.lang[1] + " - U-Notas", font=DEFAULT_FONT_TITLE, border=10).pack()
            self.configtitle = properties[13]
            self.configon = self.lang[10]
            # Se cargan todos los idiomas disponibles
            f = Frame(self.w, border=1)
            f.pack(fill=X)
            langlist = loadFromArchive(properties[7] + "/config/langs.txt", self.lang[7], False)
            if len(langlist) != 0:
                for k in range(len(langlist)):  # Reemplazo el final de cada lang en langlist por ""
                    try:
                        if langlist[k] != "":
                            langlist[k] = langlist[k].replace(properties[8], "") + " - " + LANGS[langlist[k].replace(properties[8], "")]
                        else: langlist.pop(k)
                    except: pass
            else:
                tkMessageBox.showerror(self.lang[6], self.lang[5])
                try: self.destruir(None)
                except: print ""
            self.conflang = StringVar(self.w)
            self.conflang.set(properties[5] + " - " + LANGS[properties[5]])  # valor por defecto
            Label(f, text=self.lang[2], anchor=E, width=16).pack(side=LEFT)
            w = apply(OptionMenu, (f, self.conflang) + tuple(langlist))  # menu de opciones para el idioma
            w["width"] = 12
            w["relief"] = GROOVE
            w["anchor"] = W
            w.pack(side=LEFT)
            # Modo de título
            f = Frame(self.w, border=1)
            f.pack(fill=X)
            self.conftitulo = StringVar(self.w)
            self.conftitulo.set(properties[12].format(properties[13], self.lang[4]))  # valor por defecto
            rules = loadFromArchive(properties[14] + "rules_1.ini", self.lang[7], False)
            if len(rules) != 0:
                for k in range(len(rules)):
                    try:
                        if rules[k] != "":
                            rules[k] = rules[k].format(properties[13], self.lang[4])
                        else: rules.pop(k)
                    except: pass
            else:
                tkMessageBox.showerror(self.lang[6], self.lang[8])
                try: self.destruir(None)
                except: print ""
            Label(f, text=self.lang[3], anchor=E, width=16).pack(side=LEFT)
            w = apply(OptionMenu, (f, self.conftitulo) + tuple(rules))
            w["width"] = 24
            w["relief"] = GROOVE
            w["anchor"] = W
            w.pack(side=LEFT)
            # Modo de nombre del curso
            f = Frame(self.w, border=1)
            f.pack(fill=X)
            self.confnombrecurso = StringVar(self.w)
            self.confnombrecurso.set(properties[11].format(self.lang[4], self.lang[9]))  # valor por defecto
            rules_1 = loadFromArchive(properties[14] + "rules_2.ini", self.lang[7], False)
            if len(rules) != 0:
                for k in range(len(rules_1)):
                    try:
                        if rules_1[k] != "":
                            rules_1[k] = rules_1[k].format(self.lang[4], self.lang[9])
                        else: rules.pop(k)
                    except: pass
            else:
                tkMessageBox.showerror(self.lang[6], self.lang[4])
                try: self.destruir(None)
                except: print ""
            Label(f, text=self.lang[8], anchor=E, width=16).pack(side=LEFT)
            w = apply(OptionMenu, (f, self.confnombrecurso) + tuple(rules_1))
            w["width"] = 21
            w["relief"] = GROOVE
            w["anchor"] = W
            w.pack(side=LEFT)
            # Activar color rojo
            f = Frame(self.w, border=1)
            f.pack(fill=X)
            self.confrojo = StringVar(self.w)
            if properties[9] == 1: s = self.lang[10]  # se define el sonido que llega por el comando
            else: s = self.lang[11]
            self.confrojo.set(s)  # valor por defecto
            Label(f, text=self.lang[12], anchor=E, width=16).pack(side=LEFT)
            w = apply(OptionMenu, (f, self.confrojo) + tuple([self.lang[10], self.lang[11]]))  # menu de opciones para sonido
            w["width"] = 12
            w["relief"] = GROOVE
            w["anchor"] = W
            w.pack(side=LEFT)
            # Separador decimal
            f = Frame(self.w, border=1)
            f.pack(fill=X)
            self.confdecimal = StringVar(self.w)
            if properties[10] == "punto": s = self.lang[15]  # se define el sonido que llega por el comando
            else: s = self.lang[16]
            self.confdecimal.set(s)  # valor por defecto
            Label(f, text=self.lang[14], anchor=E, width=16).pack(side=LEFT)
            w = apply(OptionMenu, (f, self.confdecimal) + tuple([self.lang[15], self.lang[16]]))  # menu de opciones para sonido
            w["width"] = 12
            w["relief"] = GROOVE
            w["anchor"] = W
            w.pack(side=LEFT)
            # Escala de notas
            f = Frame(self.w, border=1)
            f.pack(fill=X)
            self.confescala = StringVar(self.w)
            self.confescala.set(properties[16])  # valor por defecto
            Label(f, text=self.lang[17], anchor=E, width=16).pack(side=LEFT)
            w = apply(OptionMenu, (f, self.confescala) + tuple([properties[15][0], properties[15][1]]))  # menu de opciones para sonido
            w["width"] = 12
            w["relief"] = GROOVE
            w["anchor"] = W
            w.pack(side=LEFT)
            self.w.bind("<Escape>", self.destruir)
            Button(self.w, text=self.lang[13], command=self.sendconfig, relief=GROOVE, width=7).pack(pady=7)
        elif typeObject == "error" or typeObject == "aviso":  # Alerta
            try:
                if typeObject == "error": winsound.MessageBeep(16)  # Sonido de error
                elif typeObject == "aviso": winsound.MessageBeep(1)  # Sonido de error
            except: pass
            Label(self.w, text=properties[5], wraplength=250, anchor=N, border=10).pack()
            Button(self.w, text=self.lang[1], command=self.w.destroy, relief=GROOVE).pack()
            self.w.bind("<Return>", self.destruir)
            self.w.bind("<Escape>", self.destruir)
            self.w.focus_force()
        elif typeObject == "preguntarSNC":  # Preguntar si/no/cancelar
            if properties[5]: winsound.MessageBeep(-1)
            self.w.focus_force()
            Label(self.w, text=self.lang[1], font=DEFAULT_FONT_TITLE, border=10).pack()  # desea guardar
            F = Frame(self.w)
            F.pack()
            Button(F, text=self.lang[2], command=lambda:self.response("si"), width=5, relief=GROOVE).pack(side=LEFT)  # si
            Label(F, text=" ").pack(side=LEFT)
            Button(F, text=self.lang[4], command=lambda:self.response("cancel"), width=8, relief=GROOVE).pack(side=LEFT)  # cancelar
            Label(F, text=" ").pack(side=LEFT)
            Button(F, text=self.lang[3], command=lambda:self.response("no"), width=5, relief=GROOVE).pack()  # no
        elif typeObject in ["licence", "changelog", "ayuda", "longtext"]:  # Licencia o gnu
            try: name = properties[6]
            except: name = ""
            archivo = open(properties[5], "r")
            Yscroll = Scrollbar(self.w)
            Yscroll.pack(side=RIGHT, fill=Y)
            texto = Text(self.w, wrap=NONE,
            yscrollcommand=Yscroll.set, xscrollcommand=None)
            texto.focus_force()
            for i in archivo: texto.insert(INSERT, i)
            texto.pack(fill=BOTH)
            texto.configure(state="disabled")
            Yscroll.config(command=texto.yview)
            archivo.close()
            self.w.bind("<Return>", self.destruir)
            self.w.bind("<Escape>", self.destruir)

    def destruir(self, e=None):  # Función para destruir la ventana
        self.w.destroy()

    def kill(self):  # Función que destruye la ventana
        self.sent = False
        self.w.destroy()

    def sendconfig(self, e=None):  # Función que envia la informacion de la configuración
        delMatrix(self.values)
        a = self.conflang.get().strip().upper().split("-")[0].strip()
        b = self.conftitulo.get().strip().replace(self.configtitle, "{0}").replace(self.lang[4], "{1}")
        c = self.confnombrecurso.get().strip().replace(self.lang[4], "{0}").replace(self.lang[9], "{1}")
        d = self.confrojo.get().strip()
        e = self.confdecimal.get().strip().lower()
        f = self.confescala.get().strip()
        if d == self.configon: d = True
        else: d = False
        self.values.append(a)
        self.values.append(b)
        self.values.append(c)
        self.values.append(d)
        self.values.append(e)
        self.values.append(f)
        self.sent = True
        self.destruir()

    def response(self, res):  # Función que envia una respuesta
        delMatrix(self.values)
        self.values.append(res)
        self.sent = True
        self.destruir()
