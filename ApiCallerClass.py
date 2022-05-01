import os
from ApiWorkerClass import ApiWorkerClass
# os.system('Clear')



class ApiWorkerClassClass:

    #main function
    def CallApi(scales,locations,heights_mesoscale,heights_microscale,vars_mesoscale,vars_microscale):
        
        # declare variables
        scales=scales
        locations=locations
        heights_mesoscale=heights_mesoscale
        heights_microscale=heights_microscale
        vars_mesoscale=vars_mesoscale
        vars_microscale=vars_microscale

        # loop through meso, locations, heights, create csv file
        for scale in scales:
            filePath=f"{os.getcwd()}/net_cdf_downloads/{scale}_data.csv"

            if (not(os.path.exists(filePath))):
                for loc in locations:
                    latitude=loc[1]
                    longitude=loc[2]
                    if scale=="mesoscale":
                        heights=heights_mesoscale
                    elif scale=="microscale":
                        heights=heights_microscale

                    for h in heights:
                        # call steps
                        if scale=="mesoscale":
                            variables=vars_mesoscale
                        elif scale=="microscale":
                            variables=vars_microscale
                        url=ApiWorkerClass.MakeUrl(scale,latitude,longitude,h,variables)
                        ApiWorkerClass.requestAPI(url)
                        ApiWorkerClass.convertCSV(variables,scale,loc,h)
            else:
                print(f"Error!  {scale} data already downloaded")