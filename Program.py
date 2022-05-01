from asyncore import read, write
from hashlib import new
import os
import requests
from netCDF4 import Dataset
import csv
import numpy as np
# from ApiWorkerClass import ApiWorkerClass
# from ApiCallerClass import ApiCallerClassClass
import ApiCallerClass
import ProgramSettings
import CsvParserClass
os.system('Clear')




class program:

    def main():
        locations=CsvParserClass.CsvParserClass.ParseCsv()

        scales=ProgramSettings.scales
        heights_mesoscale=ProgramSettings.heights_mesoscale
        heights_microscale=ProgramSettings.heights_microscale
        vars_mesoscale=ProgramSettings.vars_mesoscale
        vars_microscale=ProgramSettings.vars_microscale

        ApiCallerClass.ApiWorkerClassClass.CallApi(scales,locations,heights_mesoscale,heights_microscale,vars_mesoscale,vars_microscale)

program.main()

