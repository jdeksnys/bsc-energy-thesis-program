from asyncore import read, write
import os
from matplotlib.pyplot import sca
import requests
from netCDF4 import Dataset
import csv
import numpy as np



class ApiWorkerClass():

    # create net_cdf_downloads directory, change directory to it
    @staticmethod
    def mkDir():
        currDir=os.path.abspath(os.getcwd())
        if not os.path.exists(currDir+"/net_cdf_downloads"):
            os.makedirs(currDir+"/net_cdf_downloads")
        os.chdir(currDir+"/net_cdf_downloads")

    # create request url
    @staticmethod
    def MakeUrl(mesoMicro,latitude,longitude,heightInput,varType):
        varType=varType
        varInput=""
        for i in varType:
            varInput+=f"&variable={i}"
        url=f'https://wps.neweuropeanwindatlas.eu/api/{mesoMicro}-atlas/v1/get-data-point?latitude={latitude}&longitude={longitude}&height={heightInput}{varInput}'
        return url

    # make request, save .nc file to current (net_cdf_downloads) directory
    @staticmethod
    def requestAPI(url):
        r=requests.get(url,allow_redirects=True)
        if r.status_code==200:
            ApiWorkerClass.mkDir()
            if not os.path.exists(os.getcwd()+"/newa_mesoscale_atlas.nc"):
                try:
                    open("newa_mesoscale_atlas.nc","wb").write(r.content)
                except Exception:
                    print("File could not be downloaded")
            else:
                raise Exception("File 'newa_mesoscale_atlas.nc' already downloaded")
        else:
            raise Exception(f"{r.status_code} bad response\nurl: {url}")

    # convert from .nc to .csv
    @staticmethod
    def convertCSV(variables,scale,loc,h):
        variables=variables
        scale=scale
        loc=loc
        h=h
        fileLoc=os.getcwd()+"/newa_mesoscale_atlas.nc"
        data=Dataset(fileLoc)
        # print(data.variables.keys())
        # wind=data.variables['wind_speed_mean'][0]

        filePath=f"{os.getcwd()}/{scale}_data.csv"
        if (not(os.path.exists(filePath))):
            with open(filePath,"w",newline='') as file:
                text=[]
                text.append("scale")
                text.append("location")
                text.append("height")
                for l in variables:
                    text.append(f"'{l}'")
                writer=csv.writer(file)
                writer.writerow(text)
                file.close()
        
        with open(filePath,"a",newline='') as file:
            text=[]
            text.append(scale)
            text.append(loc[0])
            text.append(h)
            for l in variables:
                text.append(data.variables[f"{l}"][0])
            writer=csv.writer(file)
            writer.writerow(text)
            file.close()

        try:
            os.remove(os.getcwd()+"/newa_mesoscale_atlas.nc")
            os.chdir(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
        except Exception:
            print("File (.nc) could not be deleted")
        
        print(scale,loc[0],h)
