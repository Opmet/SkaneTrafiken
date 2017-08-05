# -*- coding: UTF-8 -*-
'''
Created on 29 maj 2017

@author: Joakim Andersson
'''
import urllib
import urllib2
from xml.dom import minidom
from qgis.core import *
from qgis.utils import iface

# Lägg till röd start punkt.  
def startPoint(x,y):
    # Skapa lager
    startLayer = QgsVectorLayer("Point?crs=epsg:3021", "Start", "memory")
    if not startLayer.isValid():
        print "Layer failed to load!"
    # Lägg start punkt i lager
    pr = startLayer.dataProvider()
    fet = QgsFeature()
    fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(y,x)))
    pr.addFeatures([fet])
    # Lägg svg bild i lager
    svgStyle = {}
    svgStyle['name'] = '/crosses/Cross4.svg'
    svgStyle['fill'] = '#ff0000'
    svgStyle['size'] = '5'
    symLyr = QgsSvgMarkerSymbolLayerV2.create(svgStyle)
    startLayer.rendererV2().symbols()[0].changeSymbolLayer(0, symLyr)
    # Lägg till lager
    QgsMapLayerRegistry.instance().addMapLayer(startLayer)
    return startLayer

# Lägg till busshålplatser.  
def skaneTrafiken(points):
    # Skapa lager
    busLayer = QgsVectorLayer("Point?crs=epsg:3021", "Skanetrafiken", "memory")
    if not busLayer.isValid():
        print "Layer failed to load!"
    # Lägg tre närmaste busshållplatserna i lagret om inte null.
    pr = busLayer.dataProvider()
    fet = QgsFeature()
    for i in range(3):
        if not 0:
            coordinates = points[i].split(":")
            x = int(coordinates[0])
            y = int(coordinates[1])
            fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(y,x)))
            pr.addFeatures([fet])
    # Lägg svg bild i lager
    svgStyle = {}
    svgStyle['name'] = '/transport/transport_bus_stop2.svg'
    svgStyle['size'] = '9'
    symLyr1 = QgsSvgMarkerSymbolLayerV2.create(svgStyle)
    busLayer.rendererV2().symbols()[0].changeSymbolLayer(0, symLyr1)
    # Lägg till lager
    QgsMapLayerRegistry.instance().addMapLayer(busLayer)
    return busLayer

# Plockar ut koordinater till närmaste busshållplatser
def xmlHandler(xml):
    xmlString = minidom.parseString(xml)
    xmlDoc = xmlString.getElementsByTagName("NearestStopArea")
    points = []
    for node in xmlDoc:
        x = node.getElementsByTagName("X")[0].childNodes[0].nodeValue
        y = node.getElementsByTagName("Y")[0].childNodes[0].nodeValue
        points.append( x + ":" + y )
    return points

# Hämtar xml från skånetrafiken.
# Koordinatsystemet är RT90
def openAPI(x,y,m):
    url = 'http://www.labs.skanetrafiken.se/v2.2/neareststation.asp'
    values = {'x' : x,'y' : y,'Radius' : m }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    xml = response.read()
    return xml

# Zoom
def zoomToLayer(startLayer):
    canvas = iface.mapCanvas()
    extent = startLayer.extent()
    canvas.setExtent(extent)
    return

# Startpunkt
def main(x,y,m):
    xml = openAPI(x,y,m)
    points = xmlHandler(xml)
    startLayer = startPoint(x,y)
    skaneTrafiken(points) # Skapa lager
    zoomToLayer(startLayer)
    return