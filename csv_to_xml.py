# -*- coding: utf-8 -*-

import csv
from xml_creator import xmlCreator
from pretty_xml import p


with open('file.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        xmlCreator(row['CIRCUNSCRIPCION'], row['TOMO'], row['ANO'], row['NROLIBRO'], row['ACTANRO'], row['PRIMERNOMBRE'], row['PRIMERAPELLIDO'], row['TIPODOCUMENTO'], row['NRODOCUMENTO'], row['GENERO'], row['FECHADEF'])
