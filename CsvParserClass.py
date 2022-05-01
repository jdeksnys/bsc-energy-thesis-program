import os
import csv
import tkinter as tk
from tkinter import filedialog
from sqlalchemy import null
import pandas as pd
import string



class CsvParserClass:

    def ParseCsv():
        root = tk.Tk()
        root.withdraw()
        fileDir = filedialog.askopenfilename()

        if(fileDir!=null):
            alphabet=list(string.ascii_uppercase)
            a=0
            locationArray=[]

            with open(fileDir,'r') as _file:
                df=pd.DataFrame(csv.reader(_file))

                # check if even no. of elements in row (long+lat)
                if df.shape[1]%2==0:
                    
                    for row in range(0,df.shape[0]):
                        iter=0

                        for element in range(0,(int)(df.shape[1]/2)):
                            nameTag=f"{alphabet[a]}{element+1}"
                            lon=df.iat[row,iter]
                            lat=df.iat[row,iter+1]

                            locationArray.append([nameTag,lon,lat])
                            iter+=2

                        a+=1
        
        return locationArray
