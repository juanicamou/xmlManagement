# -*- coding: utf-8 -*-
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree, tostring
from pretty_xml import p
def xmlCreator(circup_, tomo_, ano_, nroLibro_, actaNro_, primerNombre_, primerApellido_, tipoDoc_, nroDoc_, genero_, fechaDef_):

# Creación de XML Frame
#-------------------------------------------------------------------------------
    top = Element('xml') # XML root
    Acta = SubElement(top, 'Acta')
    tipoacta = SubElement(Acta, 'circunscripcion')
    tipoacta.text= 'DEFUNCIONES'
    circunscripcion = SubElement(Acta, 'circunscripcion')
    circunscripcion.text= circup_
    tomo = SubElement(Acta, 'tomo')
    tomo.text= tomo_
    ano = SubElement(Acta, 'ano')
    ano.text= ano_
    nrolibro = SubElement(Acta, 'nrolibro')
    nrolibro.text= nroLibro_
    actanro = SubElement(Acta, 'actanro')
    actanro.text= actaNro_
    primernombre = SubElement(Acta, 'primernombre')
    primernombre.text= primerNombre_
    segundonombre = SubElement(Acta, 'segundonombre')
    tercernombre = SubElement(Acta, 'tercernombre')
    primerapellido = SubElement(Acta, 'primerapellido')
    primerapellido.text= primerApellido_
    segundoapellido = SubElement(Acta, 'segundoapellido')
    tercerapellido = SubElement(Acta, 'tercerapellido')
    tipodocumento = SubElement(Acta, 'tipodocumento')
    tipodocumento.text= tipoDoc_
    nrodocumento = SubElement(Acta, 'nrodocumento')
    nrodocumento.text= nroDoc_
    genero = SubElement(Acta, 'genero')
    genero.text= genero_
    fechadefuncion = SubElement(Acta, 'fechadefuncion')
    fechadefuncion.text= fechaDef_
    imagefilename = SubElement(Acta, 'imagefilename')
    imagefilename.text= 'imagePath_'
    obs  = SubElement(Acta, 'obs ')
    DetalleFallaProcesamiento = SubElement(top, 'DetalleFallaProcesamiento')
    fechaProceso = SubElement(DetalleFallaProcesamiento, 'fechaProceso')
    fechaProceso.text= '???????'
    observacionRCE = SubElement(DetalleFallaProcesamiento, 'observacionRCE')
    observacionRCE.text= '????????'
#-------------------------------------------------------------------------------

# XML output
#-------------------------------------------------------------------------------

    file_ = 'prueba.xml'
    outfile = open(file_, 'w')
    outfile.write(p(top))
    outfile.close()
#-------------------------------------------------------------------------------
