# -*- coding: utf-8 -*-

# Crayfish - A collection of tools for TUFLOW and other hydraulic modelling packages
# Copyright (C) 2012 Peter Wells for Lutra Consulting

# peter dot wells at lutraconsulting dot co dot uk
# Lutra Consulting
# 23 Chestnut Close
# Burgess Hill
# West Sussex
# RH15 8HN

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import QgsCoordinateReferenceSystem
from qgis.gui import QgsGenericProjectionSelector

from crayfish_viewer_plugin_layer_props_dialog_ui import Ui_CrayfishViewerPluginLayerPropsDialog


class CrayfishViewerPluginPropsDialog(QDialog, Ui_CrayfishViewerPluginLayerPropsDialog):
    def __init__(self, layer):
        QDialog.__init__(self)
        self.layer = layer

        self.setupUi(self)
        self.window().setWindowTitle('Layer Properties - %s' % (self.layer.name()))

        self.crs = self.layer.crs()

        p = self.layer.provider
        ec, ec4, ec3 = p.elementCount(), p.elementCount_E4Q(), p.elementCount_E3T()
        ecx = ec - ec4 - ec3  # unknown elements
        html = '''<table>
          <tr><td width="50%%">Nodes</td><td align="right"><b>%d</b></td>
          </tr><tr><td>&nbsp;</td></tr>
          <tr><td>Elements</td><td align="right"><b>%d</b></td></tr>
          <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;E4Q</td><td align="right">%d</td></tr>
          <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;E3T</td><td align="right">%d</td></tr>
          <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;Unknown</td><td align="right">%d</td></tr>
          </table>''' % (p.nodeCount(), ec, ec4, ec3, ecx)
        self.editMetadata.setReadOnly(True)
        self.editMetadata.setHtml(html)

        self.updateEditCRS()
        self.connect(self.buttonBox, SIGNAL("accepted()"), self.onOK)
        self.connect(self.btnSpecifyCRS, SIGNAL("clicked()"), self.onSpecifyCRS)

    def updateEditCRS(self):
        self.editCRS.setText(self.crs.authid() + " - " + self.crs.description())
        self.editCRS.setCursorPosition(0)

    def onSpecifyCRS(self):

        selector = QgsGenericProjectionSelector(self)
        selector.setMessage("Specify CRS of the mesh file")
        selector.setSelectedCrsId(self.layer.crs().srsid())
        if selector.exec_():
          self.crs = QgsCoordinateReferenceSystem(selector.selectedCrsId(), QgsCoordinateReferenceSystem.InternalCrsId)
          self.updateEditCRS()

    def onOK(self):

        self.layer.setCrs(self.crs)
        self.accept()
