"""
Created on Wed Apr 27 14:48:22 2020

@author: CameronL97

Python code to create a daily weathermap of the USA for PPD module 
"""

#Import the modules 
import matplotlib #imports matplotlib for graph creation 
matplotlib.use('TkAgg') #forces matplotlib to to use TkAgg which renders to a Tk Canvas

import tkinter #Imports tkinter to ensure that the model can have a simple gui and TkCanvas can be used 

from datetime import datetime, timedelta #Imports the date and time module that allows for the most up to date data to be downloaded 

from urllib.request import urlopen # Imports urllib library that allows for web scraping to occur in the program

import cartopy.crs as ccrs #imports the map builder
import cartopy.feature as cfeature #imports features such as borders and state lines

import matplotlib.colors as mcolors #imports colour system for the output
import matplotlib.pyplot as plt #imports necessary chart data

from metpy.units import masked_array, units #imports module that allows for the creation of masks and assigns units to values

from netCDF4 import Dataset #imports the module to read .nc files 


#get the code from the website for 1 day 
dt = datetime.utcnow() - timedelta(days=1)  
#take the url and gets the most recent data can be changed to a specific day 
url = 'http://water.weather.gov/precip/downloads/{dt:%Y/%m/%d}/nws_precip_1day_'\
      '{dt:%Y%m%d}_conus.nc'.format(dt=dt)
#read the data from the website 
data = urlopen(url).read()
#create a new array to store the data in 
nc = Dataset('data', memory=data)

#set the name of the variables in the data set 
prcpvar = nc.variables['observation']
#Set the space markrs to : and set units to mm  
data = masked_array(prcpvar[:], units(prcpvar.units.lower())).to('mm')
#set the x and y variables
x = nc.variables['x'][:]
y = nc.variables['y'][:]
#convert the x and y coordinates to a grid for mapping 
proj_var = nc.variables[prcpvar.grid_mapping]
#create a globe and places the x and y coordinates on the 
globe = ccrs.Globe(semimajor_axis=proj_var.earth_radius)
proj = ccrs.Stereographic(central_latitude=90.0,
                          central_longitude=proj_var.straight_vertical_longitude_from_pole,
                          true_scale_latitude=proj_var.standard_parallel, globe=globe)
#create the figure 
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, projection=proj)

# draw coastlines, state and country boundaries, edge of map.
ax.coastlines()
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.STATES)

# draw filled contours boundaries for rainfall, data boundaries are in mm 
clevs = [0, 1, 2.5, 5, 7.5, 10, 25, 50, 75, 100,
         150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]

#assign a colour for each boundary in the data from matplotlib.colours 
cmap_data = [(5.00000000e-01, 0.00000000e+00, 1.00000000e+00, 1.00000000e+00),
             (4.00000000e-01, 1.56434465e-01, 9.96917334e-01, 1.00000000e+00),
             (3.00000000e-01, 3.09016994e-01, 9.87688341e-01, 1.00000000e+00),
             (2.00000000e-01, 4.53990500e-01, 9.72369920e-01, 1.00000000e+00),
             (1.00000000e-01, 5.87785252e-01, 9.51056516e-01, 1.00000000e+00),
             (0.00000000e+00, 7.07106781e-01, 9.23879533e-01, 1.00000000e+00),
             (1.00000000e-01, 8.09016994e-01, 8.91006524e-01, 1.00000000e+00),
             (2.00000000e-01, 8.91006524e-01, 8.52640164e-01, 1.00000000e+00),
             (3.00000000e-01, 9.51056516e-01, 8.09016994e-01, 1.00000000e+00),
             (4.00000000e-01, 9.87688341e-01, 7.60405966e-01, 1.00000000e+00),
             (5.00000000e-01, 1.00000000e+00, 7.07106781e-01, 1.00000000e+00),
             (6.00000000e-01, 9.87688341e-01, 6.49448048e-01, 1.00000000e+00),
             (7.00000000e-01, 9.51056516e-01, 5.87785252e-01, 1.00000000e+00),
             (8.00000000e-01, 8.91006524e-01, 5.22498565e-01, 1.00000000e+00),
             (9.00000000e-01, 8.09016994e-01, 4.53990500e-01, 1.00000000e+00),
             (1.00000000e+00, 7.07106781e-01, 3.82683432e-01, 1.00000000e+00),
             (1.00000000e+00, 5.87785252e-01, 3.09016994e-01, 1.00000000e+00),
             (1.00000000e+00, 4.53990500e-01, 2.33445364e-01, 1.00000000e+00),
             (1.00000000e+00, 3.09016994e-01, 1.56434465e-01, 1.00000000e+00),
             (1.00000000e+00, 1.56434465e-01, 7.84590957e-02, 1.00000000e+00),
             (1.00000000e+00, 1.22464680e-16, 6.12323400e-17, 1.00000000e+00)]
cmap = mcolors.ListedColormap(cmap_data, 'precipitation')
norm = mcolors.BoundaryNorm(clevs, cmap.N)

cs = ax.contourf(x, y, data, clevs, cmap=cmap, norm=norm)

# add colourbar to the figure 
cbar = plt.colorbar(cs, orientation='horizontal')
cbar.set_label(data.units)

ax.set_title(prcpvar.long_name + ' for period ending ' + nc.creation_time)

#run the program and have it run using tkinter and tkagg
def run():
    canvas.draw()

root = tkinter.Tk()
root.wm_title(prcpvar.long_name + ' for period ending ' + nc.creation_time)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


tkinter.mainloop()