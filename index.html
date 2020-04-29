"""
Created on Wed Apr 29 14:48:22 2020

@author: CameronL97

Python code to create a daily weathermap of the USA for PPD module 
"""

#Import the modules 
import matplotlib #imports matplotlib for graph creation 
matplotlib.use('TkAgg') #forces matplotlib to to use TkAgg which renders to a Tk Canvas

import tkinter #Imports tkinter to ensure that the model can have a simple gui and TkCanvas can be used 

from datetime import datetime, timedelta #Imports the date and time module that allows for the most up to date data to be downloaded 

from urllib.request import urlopen # Imports urllib library that allows for web scraping to occur in the program

import cartopy.crs as ccrs #
import cartopy.feature as cfeature

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

from metpy.units import masked_array, units

from netCDF4 import Dataset



dt = datetime.utcnow() - timedelta(days=1)  # This should always be available
url = 'http://water.weather.gov/precip/downloads/{dt:%Y/%m/%d}/nws_precip_1day_'\
      '{dt:%Y%m%d}_conus.nc'.format(dt=dt)
data = urlopen(url).read()
nc = Dataset('data', memory=data)



prcpvar = nc.variables['observation']
data = masked_array(prcpvar[:], units(prcpvar.units.lower())).to('mm')
x = nc.variables['x'][:]
y = nc.variables['y'][:]
proj_var = nc.variables[prcpvar.grid_mapping]

globe = ccrs.Globe(semimajor_axis=proj_var.earth_radius)
proj = ccrs.Stereographic(central_latitude=90.0,
                          central_longitude=proj_var.straight_vertical_longitude_from_pole,
                          true_scale_latitude=proj_var.standard_parallel, globe=globe)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, projection=proj)

# draw coastlines, state and country boundaries, edge of map.
ax.coastlines()
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.STATES)

# draw filled contours.
clevs = [0, 1, 2.5, 5, 7.5, 10, 15, 20, 30, 40,
         50, 70, 100, 150, 200, 250, 300, 400, 500, 600, 750]
# In future MetPy
# norm, cmap = ctables.registry.get_with_boundaries('precipitation', clevs)
cmap_data = [(1.0, 1.0, 1.0),
             (0.3137255012989044, 0.8156862854957581, 0.8156862854957581),
             (0.0, 1.0, 1.0),
             (0.0, 0.8784313797950745, 0.501960813999176),
             (0.0, 0.7529411911964417, 0.0),
             (0.501960813999176, 0.8784313797950745, 0.0),
             (1.0, 1.0, 0.0),
             (1.0, 0.6274510025978088, 0.0),
             (1.0, 0.0, 0.0),
             (1.0, 0.125490203499794, 0.501960813999176),
             (0.9411764740943909, 0.250980406999588, 1.0),
             (0.501960813999176, 0.125490203499794, 1.0),
             (0.250980406999588, 0.250980406999588, 1.0),
             (0.125490203499794, 0.125490203499794, 0.501960813999176),
             (0.125490203499794, 0.125490203499794, 0.125490203499794),
             (0.501960813999176, 0.501960813999176, 0.501960813999176),
             (0.8784313797950745, 0.8784313797950745, 0.8784313797950745),
             (0.9333333373069763, 0.8313725590705872, 0.7372549176216125),
             (0.8549019694328308, 0.6509804129600525, 0.47058823704719543),
             (0.6274510025978088, 0.42352941632270813, 0.23529411852359772),
             (0.4000000059604645, 0.20000000298023224, 0.0)]
cmap = mcolors.ListedColormap(cmap_data, 'precipitation')
norm = mcolors.BoundaryNorm(clevs, cmap.N)

cs = ax.contourf(x, y, data, clevs, cmap=cmap, norm=norm)

# add colorbar.
cbar = plt.colorbar(cs, orientation='horizontal')
cbar.set_label(data.units)

ax.set_title(prcpvar.long_name + ' for period ending ' + nc.creation_time)


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