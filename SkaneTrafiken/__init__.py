# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SkaneTrafiken
                                 A QGIS plugin
 Visar tre närmaste busshållplatserna i Skåne
                             -------------------
        begin                : 2017-06-29
        copyright            : (C) 2017 by Joakim Andersson
        email                : joakim@ktv-sjobo.se
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SkaneTrafiken class from file SkaneTrafiken.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .skane_trafiken import SkaneTrafiken
    return SkaneTrafiken(iface)
