#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Evaluaciones
# Pablo Pizarro, 2014
# Provee de las herramientas lógicas y matemáticas necesarias para almacenar notas

# Importación de librerías
import math

# Definición de constantes
DECIMALES = 1
ESCALAS = ["10 - 70", "1 - 7"]
LETTERS = "ABCDEFGHIJKMN�LOPQRSTUVWXYZ"

class evaluacion:  # Clase evaluación

    def __init__(self, nombre, notas, notas_p, notas_ponderacion, notas_fecha, escala):  # Método constructor

        # Se definen las variables de la clase
        self.escala = ""
        self.nombre = ""
        self.notas = []
        self.notas_preguntas = []
        self.notas_ponderacion = []
        self.notas_fecha = []
        self.tag = ""
        self.total_notas = 0

        #Se agrega la información al objeto
        self.nombre = nombre.strip()
        self.tag = self.crearTag(self.nombre)
        if type(notas) is not list: print "Error :: Error en TDA notas"; exit("TDA incorrecto")
        else: self.notas = notas
        if type(notas_p) is not list: print "Error :: Error en TDA notas"; exit("TDA incorrecto")
        else: self.notas_preguntas = notas_p
        if type(notas_ponderacion) is not list: print "Error :: Error en TDA notas"; exit("TDA incorrecto")
        else: self.notas_ponderacion = notas_ponderacion
        if type(notas_fecha) is not list: print "Error :: Error en TDA notas"; exit("TDA incorrecto")
        else: self.notas_fecha = notas_fecha
        if escala not in ESCALAS: print "Error :: Escala incorrecta"; exit("Escala incorrecta")
        else: self.escala = escala
        self.total_notas = len(self.notas)
        if len(self.notas_fecha) != self.total_notas or len(self.notas_ponderacion) != self.total_notas or len(self.notas_preguntas) != self.total_notas:
            print "Error :: Falta informacion en notas"; exit("Informacion erronea")
        for i in notas:
            if i==0: self.total_notas-=1

        print self.obtenerNotas()
        print self.obtenerPreguntasControles()
        print self.obtenerPonderaciones()
        print self.obtenerFechas()
        print self.promedioAritmetico()
        print self.promedioGeometrico()
        print self.desviacionEstandar()
        print self.kEsimoMayor(1)
        print self.kEsimoMenor(1)

    def convertirAPorcentaje(self, lista):
        porcentajes = []
        for i in lista:
            i = float(i)
            if i < 1.0: porcentajes.append(int(i * 100))
            else: porcentajes.append(i)
        return porcentajes

    def crearTag(self, nombre):  # Función que crea el tag de la evaluación
        tag = ""
        for l in nombre:
            if l in LETTERS: tag += l
        return tag

    def clonarNotas(self):  # Función que retorna la lista de notas clonada
        notas = []
        for i in self.notas:
            if i!=0: notas.append(i)
        return notas

    def desviacionEstandar(self):
        if self.total_notas>1:
            prom = self.promedioAritmetico()
            suma = 0.0
            for i in self.notas:
                if i!=0: suma += (i - prom) * (i - prom)
            std = math.sqrt((1.0 / (self.total_notas - 1)) * suma)
            if self.escala == ESCALAS[0]: return int(round(std, 0))
            else: return round(std, DECIMALES)
        else:
            if self.escala == ESCALAS[0]: return 0
            else: return 0.0

    def kEsimoMayor(self, k):  # Retorna el número k-ésimo
        if 1 <= k <= self.total_notas:  # Si el k es v�lido
            for i in range(0, self.total_notas):
                if (i + 1) == k:
                    nota = self.ordenarLista(self.clonarNotas())
                    nota.reverse()
                    return nota[i]
        else: print "Error :: k no valido"; return -1

    def kEsimoMenor(self, k):  # Retorna el número k-ésimo menor de las notas
        if 1 <= k <= self.total_notas:  # Si el k es v�lido
            for i in range(0, self.total_notas):
                if (i + 1) == k: return self.ordenarLista(self.clonarNotas())[i]
        else: print "Error :: k no valido"; return -1

    def max(self):  # Retorna la nota máxima
        return self.kEsimoMayor(1)

    def mediana(self):  # Retorna la mediana de las notas
        notas = self.ordenarLista(self.clonarNotas())
        i = (self.total_notas - 1) // 2
        if (self.total_notas % 2): mediana = notas[i]
        else: mediana = (notas[i] + notas[i + 1]) / 2.0
        if self.escala == ESCALAS[0]: return int(mediana)
        else: return round(mediana, DECIMALES)

    def min(self):  # Retorna la menor nota
        return self.kEsimoMenor(1)

    def obtenerFechas(self):  # Retorna las fechas de las evaluaciones
        return self.notas_fecha

    def obtenerNombre(self):  # Retorna el nombre de la evaluación
        return self.nombre

    def obtenerNumeroNotas(self):  # Retorna el número de notas
        return self.total_notas

    def obtenerNotas(self):  # Retorna las notas de la evaluación
        return self.notas

    def obtenerPonderaciones(self):  # Retornas las ponderaciones de las evaluaciones
        return self.notas_ponderacion

    def obtenerPreguntasControles(self):  # Retorna todas las preguntas de las evaluaciones
        return self.notas_preguntas

    def obtenerTag(self):  # Retorna el tag de la evaluación
        return self.tag

    def ordenarLista(self, lista):  # Función que ordena una lista usando quicksort
        if lista == []: return []
        else:
            pivote = lista[0]
            min = self.ordenarLista([x for x in lista[1:] if x < pivote])
            max = self.ordenarLista([x for x in lista[1:] if x >= pivote])
            return min + [pivote] + max

    def promedioAritmetico(self):  # Obtiene el promedio de la evaluación
        total = 0.0
        for i in self.notas: total += i
        prom = total / self.total_notas
        if self.escala == ESCALAS[0]: return int(prom)
        else: return round(prom, DECIMALES)

    def promedioGeometrico(self):  # Obtiene el promedio geométrico
        total = 1.0
        for nota in self.notas:
            if nota!=0: total *= nota
        total = math.pow(total, (1.0 / self.total_notas))
        if self.escala == ESCALAS[0]: return int(total)
        else: return round(total, DECIMALES)

    def resumenNota(self, index):  # Obtiene el resumen de la nota en el index i
        return [self.notas[index], self.convertirAPorcentaje(self.notas_ponderacion[index]), self.notas_preguntas[index], self.notas_fecha[index]]
