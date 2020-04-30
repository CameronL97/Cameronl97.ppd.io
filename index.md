# Climate model

A simple model that gathers data from the internet and plots it using python

## Description 
The model created gathers a .nc from the USA government page for rainfall. The program creates a base map and plots the data on. It takes the most recent weather data off the website to display. The aim of this was to test myself to make a program that could then be adapted to the UK. 

## Required modules 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the modules

* [matplotlib](https://matplotlib.org/users/installing.html) 

```bash
pip install matplotlib
``` 
* [datetime](https://pypi.org/project/DateTime/) 

```bash
pip install datetime 
``` 
* [urllib.request](https://docs.python.org/3/library/urllib.request.html)

```bash
pip install urllib.request
```
* [cartopy](https://pypi.org/project/Cartopy/)

```bash
pip install Cartopy
```
* [MetPy](https://pypi.org/project/MetPy/)

```bash
pip install MetPy
```
* [netCDF4](https://pypi.org/project/netCDF4/)

```bash
pip install netCDF4
```
## Sample Code 
This section of code shows how the program gathers data from the website and turns it into a readable file by python

```bash
#get the code from the website for 1 day 
dt = datetime.utcnow() - timedelta(days=1)  
#takes the url and gets the most recent data can be changed to a specific day 
url = 'http://water.weather.gov/precip/downloads/{dt:%Y/%m/%d}/nws_precip_1day_'\
      '{dt:%Y%m%d}_conus.nc'.format(dt=dt)
#reads the data from the website 
data = urlopen(url).read()
#creates a new array to store the data in 
nc = Dataset('data', memory=data)
```
## Output 
The data is plotted onto a map of the USA, the colour map is a colour map from matplot lib that generated 21 colours for each boundary. 

![Weathermap](https://imgur.com/6i8TVh0.png)


## Contributing

This model does not require any contribution at this time however if you wish to work on the model it is free to work on.

## Authors and acknowledgement

Code modified by Cameron Leighton.

[Original code can be found here](https://unidata.github.io/python-training/gallery/precipitation_map/)

## License 

[MIT](https://choosealicense.com/licenses/mit/)
