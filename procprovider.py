# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Qgis2threejs Processing Provider
        begin                : 2018-11-06
        copyright            : (C) 2018 Minoru Akagi
        email                : akaginch@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/

from PyQt5.QtGui import QIcon
from qgis.core import QgsProcessingProvider

from .qgis2threejstools import pluginDir


class Qgis2threejsProvider(QgsProcessingProvider):

    def __init__(self):
        QgsProcessingProvider.__init__(self)
        self.algs = []

    def unload(self):
        pass

    def loadAlgorithms(self):
        from .procalgorithm import ExportAlgorithm, ExportImageAlgorithm, ExportModelAlgorithm

        self.algs = [ExportAlgorithm(), ExportImageAlgorithm(), ExportModelAlgorithm()]
        for alg in self.algs:
            self.addAlgorithm(alg)

    def id(self):
        return "Qgis2threejs"

    def name(self):
        # tr
        return "Qgis2threejs"

    def longName(self):
        return self.name()

    def icon(self):
        return QIcon(pluginDir("Qgis2threejs.png"))
