environment="development"


if(environment=="development"):
    scales=["mesoscale","microscale"]
    # locations=[["A1",56.066587, 21.085157],["A2",56.041954, 21.107528]]    
    heights_mesoscale=[75.0]
    heights_microscale=[50.0]
    vars_mesoscale=['wind_speed_mean']
    vars_microscale=['wind_speed']


elif (environment=="production"):            
    scales=["mesoscale","microscale"]
    # locations=[["A1",56.066587, 21.085157],["A2",56.041954, 21.107528],["A3",56.065884, 21.151737],
                # ["B1",56.066029, 21.243481],["B2",56.054663, 21.286504],["B3",56.001495, 21.274706],
                # ["C1",56.241500, 23.514382],["C2",56.272789, 23.465436],["C3",56.286535, 23.219001]]            
    heights_mesoscale=[75.0]#,100.0,150.0] # specify with one decimal figure
    heights_microscale=[50.0,100.0,200.0]
    vars_mesoscale=['wind_speed_mean','power_dens_mean','wind_speed_min','wind_speed_max']
    vars_microscale=['wind_speed', 'power_dens']