# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 11:40:04 2024

@author: David
"""
import math
def solar_PV_function(building_width,building_length,roof_angle,pv_width,pv_height,pv_power):
    roof_length = building_width/math.cos(roof_angle*math.pi/180)
    roof_area = roof_length*building_length
    solarpv_area = pv_width/1000*pv_height/1000
    Num_panels = math.floor(roof_area/solarpv_area)
    Total_kWp = pv_power*Num_panels/1000
    #print("For a building length {:.1f} m and width {:.1f} m, \ with a roof with inclined with an angle {}, you can fit {} Solar PV panels \of {:.2f} kWp. You can install a total of {} kWp".format(building_length,building_width,)
        
    print(Num_panels)
    print(Total_kWp)
    print(roof_length)
    print(roof_area)
    
    
solar_PV_function(8,28,22,1690,1046,400)