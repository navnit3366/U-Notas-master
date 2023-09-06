#!/usr/bin/env python
# -*- coding: utf-8 -*-
# LIB
# Pablo Pizarro, 2014
# Este fichero carga las librerías importantes y las funciones globales
# Importación de librerías

# Importación de liberías de alto nivel
import os
import sys

# Definición de constantes
CONSOLE_WRAP = -25  # define la partición del texto de la consola
CMD_COLORS = {"red":0x40, "lred":0xC0, "gray":0x80, "lgray":0x70, "white":0xF0, "blue":0x10, \
             "green":0x20, "purple":0x50, "yellow":0x60, "lblue":0x90, "lgreen":0xA0, \
             "lpurple":0xD0, "lyellow":0xE0}
PRODUCT_LINK = "http://products.tfsoftware.net16.net/versions"

if os.name != "nt":  # Se comprueba si el SO es windows
    sys.stderr.write("Error :: HOA no puede ejecutarse en GNU-Linux / Mac-OS\n"); exit()

if not (sys.version_info.major == 2 and sys.version_info.minor == 7):  # Se comprueba que Python sea 2.7.x
    version_actual = "(version actual: {0}.{1}.{2})\n".format(sys.version_info.major, sys.version_info.minor, sys.version_info.micro)
    sys.stderr.write("Error :: HOA solo puede ejecutarse en versiones 2.7.x de Python " + version_actual)
    try:
        import time
        import webbrowser
        url = "https://www.python.org/download/releases/"  # pagina de descargas de Python
        sys.stderr.write("Redirigiendo a la pagina de descargas de Python <{0}>\n".format(url))
        time.sleep(2)
        webbrowser.open(url)
    except: pass
    exit()

# Configuración de las librerías de alto nivel
reload(sys)
sys.setdefaultencoding('UTF8')  # defino la codificación UTF-8
sys.dont_write_bytecode = True  # cancelo la compilación .pyc
try: os.remove("lib.pyc")  # elimino el archivo pyc compilado
except: pass

# Agrego librerías al path
_actualpath = str(os.getcwd())
sys.path.append(_actualpath + "\\lib\\")
sys.path.append(_actualpath + "\\lib\\mechanize\\")
sys.path.append(_actualpath + "\\lib\\simplejson\\")
sys.path.append(_actualpath + "\\lib\\wconio\\")

# Importación de librerías de bajo nivel
try:
    from Tkinter import *
    from VerticalScrolledFrame import *
    from functools import partial
    from test import *
    from urllib2 import urlopen, Request
    import WConio
    import analysis
    import ctypes
    import md5
    import random
    import re
    import string
    import time
    import time
    import tkFont
    import tkMessageBox
    import ttk
    import urllib
    import urllib2
    import webbrowser
    import winsound
except:
    print "Error :: Error al cargar librerias"; exit()

def compararVersiones(ver1, ver2):  # Se compara entre dos versiones
    ver1 = ver1.split(".")
    ver2 = ver2.split(".")
    for i in range(2):
        if int(ver1[i]) > int(ver2[i]):
            return 1
        elif int(ver1[i]) < int(ver2[i]):
            return 2

def colorcmd(cmd, color):  # Función que imprime un mensaje con un color
    if color in CMD_COLORS: color = CMD_COLORS[color]
    else: color = 0x0F
    ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), color)
    print cmd,
    ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), 0x07)

def delAcentos(txt):  # Elimina los acentos de un string
    txt = txt.replace("�?", "A").replace("É", "E").replace("�?", "I").replace("Ó", "O").replace("Ú", "U")
    return txt.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

def delMatrix(matrix):  # Borrar una matriz
    a = len(matrix)
    if a > 0:
        for k in range(a): matrix.pop(0)

def getHour():  # Función que retorna la hora de sistema
    return time.ctime(time.time())[11:16]

def getTerminalSize():  # Devuelve el tamaño de la consola
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr: cr = (env.get('LINES', 25), env.get('COLUMNS', 80))
    return int(cr[1]), int(cr[0])

def getVersion(label, headers):  # Obtener la versión del programa de forma local
    http_headers = {"User-Agent":headers}
    request_object = Request(PRODUCT_LINK, None, http_headers)
    response = urllib2.urlopen(request_object)
    html = response.read()
    html = analysis.getBetweenTags(analysis.getBetweenTags(html, "<" + label + ">", "</" + label + ">"), "<version>", "</version>")
    return html.strip()

def isIn(termino, matriz):  # Función que comprueba si un elemento esta en una matriz (no completamente)
    if termino != None:  # Comprueba si el término no es none
        for elem in matriz:
            if elem in termino: return True
    return False

def loadFromArchive(archive, lang="Cargando archivo '{0}' ...", showState=True):  # Carga un archivo y retorna una matriz
    if showState != False: print lang.format("(...)" + archive[CONSOLE_WRAP:].replace("//", "/")).replace("\"", ""),
    try:  # Se carga el archivo
        l = list()
        archive = open(archive, "r")
        for i in archive:
            l.append(i.decode('utf-8').strip())
        archive.close()
        if showState != False: print "ok"
    except:
        if showState != False: print "error"
        l = []
    return l

def obtenerFecha():  # Obtiene la fecha del dia actual
    from datetime import date
    fecha = date.today()
    return str(fecha.day) + "/" + str(fecha.month) + "/" + str(fecha.year)

def openWeb(url, event):  # Abre una dirección web
    webbrowser.open(url)

def printAsciiArt():  # Imprime el arte ascii de la introducción
    WConio.clrscr()  # limpio la pantalla previa
    try:
        (width, height) = getTerminalSize()  # se obtiene el largo de la consola para dejarlo centrado
        asciiart = open("data/documents/ascii.txt", "r")
        for i in asciiart: print " "*(int((width - 26) / 2) - 10), i.rstrip()
        asciiart.close()
    except: pass
