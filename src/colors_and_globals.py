###########################################################################
# This is the master color mode controlling variable. The architecture
# currently supports only "Dark" or "Light". I may branch this to colorize
# the interface, but that would require creating a type of HEX calculating
# algorithm for each plot trace, etc
###########################################################################
colorMode = "Dark"

###########################################################################
# Version of the application
###########################################################################
progversion = "2.0.4"
progbuild = "8"
progdate = "20150329"

###########################################################################
# Application Globals
###########################################################################
font = {'size' : 7}
init_posx = 150
init_posy = 0
init_app_width = 1000
init_app_height = 850
plotTitleSize = 8
plotLabelSize = 6
legendSize = 6
if(colorMode == "Dark"):
  ColorModeDef = "background-color: #494949;"
  ColorWidgetDef = "#494949"
  canvas_alpha = 0.2
  graph_bgcolor = "#696969"
  grid_color = '#555555'
else:
  ColorModeDef = "background-color: #d9d9d9;"
  ColorWidgetDef = "#d9d9d9"
  canvas_alpha = 0.2
  graph_bgcolor = "#e9e9e9"
  grid_color = '#aaaaaa'

###########################################################################
# Graphing Widget Values
###########################################################################
plot_angle = "-45"

DiscreteParticleFluxLabelThinner = 5
DualXrayFluxLabelThinner = 7
SolarParticleFluxLabelThinner = 1
ACEDiffElectronProtonFluxLabelThinner = 1
ACEIntegralProtonFluxLabelThinner = 2
ACEInterplanetaryMagFieldLabelThinner = 1
ACESolarWindPlasmaLabelThinner = 7

if(colorMode == "Light"):
  DifferentialEnergeticProtonFluxColors = {
    'P1' :'#9f0000',
    'P2' :'#7f3f00',
    'P3' :'#5f5f00',
    'P4' :'#3f7f00',
    'P5' :'#009f00',
    'P6' :'#007f3f',
    'P7' :'#005f5f',
    'P8' :'#003f7f',
    'P9' :'#00009f',
    'P10':'#3f009f',
    'P11':'#6f009f'
  }
elif(colorMode == "Dark"):
  DifferentialEnergeticProtonFluxColors = {
    'P1' :'#ff0000',
    'P2' :'#bf4f00',
    'P3' :'#8f8f00',
    'P4' :'#4fbf00',
    'P5' :'#00ff00',
    'P6' :'#00bf4f',
    'P7' :'#008f8f',
    'P8' :'#00bf4f',
    'P9' :'#0000ff',
    'P10':'#5f00ff',
    'P11':'#af00ff'
  }

if(colorMode == "Light"):
  GOESGeomagFieldFluxColors = {
    'Hp'    : '#9f0000',
    'He'    : '#009f00',
    'Hn'    : '#00009f',
    'Total' : '#5f005f'
  }
elif(colorMode == "Dark"):
  GOESGeomagFieldFluxColors = {
    'Hp'    : '#ff0000',
    'He'    : '#00ff00',
    'Hn'    : '#0000ff',
    'Total' : '#7f007f'
  }

if(colorMode == "Light"):
  GOESDiscreteParticleFluxColors = {
    'P1': '#9f0000',
    'P2': '#7f3f00',
    'P3': '#5f5f00',
    'P4': '#3f7f00',
    'P5': '#009f00',
    'E1': '#007f3f',
    'E2': '#005f5f',
    'E3': '#003f7f',
    'E4': '#00009f',
    'E5': '#3f009f'
  }
elif(colorMode == "Dark"):
  GOESDiscreteParticleFluxColors = {
    'P1': '#ff0000',
    'P2': '#bf4f00',
    'P3': '#8f8f00',
    'P4': '#4fbf00',
    'P5': '#00ff00',
    'E1': '#00bf4f',
    'E2': '#008f8f',
    'E3': '#00bf4f',
    'E4': '#0000ff',
    'E5': '#5f00ff'
  }

if(colorMode == "Light"):
  GOESIntegralParticleFluxColors = {
    'P>1'   : '#9f0000',
    'P>5'   : '#6f3f00',
    'P>10'  : '#3f6f00',
    'P>30'  : '#009f00',
    'P>50'  : '#006f3f',
    'P>100' : '#003f6f',
    'E>0.8' : '#00009f',
    'E>2.0' : '#3f006f',
    'E>4.0' : '#6f003f'
  }
elif(colorMode == "Dark"):
  GOESIntegralParticleFluxColors = {
    'P>1'   : '#ff0000',
    'P>5'   : '#af5f00',
    'P>10'  : '#5faf00',
    'P>30'  : '#00ff00',
    'P>50'  : '#00af5f',
    'P>100' : '#005faf',
    'E>0.8' : '#0000ff',
    'E>2.0' : '#5f00af',
    'E>4.0' : '#af005f'
  }

if(colorMode == "Light"):
  GOESXrayFluxColors = {
    'Short' : '#9f0000',
    'Long'  : '#00009f'
  }
elif(colorMode == "Dark"):
  GOESXrayFluxColors = {
    'Short' : '#ff0000',
    'Long'  : '#0000ff'
  }

if(colorMode == "Light"):
  ACEDiffElecProtFluxColors = {
    '38-53'     : '#9f0000',
    '175-315'   : '#5f5f00',
    '47-68'     : '#009f00',
    '115-195'   : '#005f5f',
    '310-580'   : '#00009f',
    '795-1193'  : '#3f007f',
    '1060-1900' : '#7f003f'
  }
elif(colorMode == "Dark"):
  ACEDiffElecProtFluxColors = {
    '38-53'     : '#ff0000',
    '175-315'   : '#7f7f00',
    '47-68'     : '#00ff00',
    '115-195'   : '#007f7f',
    '310-580'   : '#0000ff',
    '795-1193'  : '#4f00bf',
    '1060-1900' : '#bf004f'
  }

ACEIntegralProtonFluxColors = {
  "Light": [
    '#7f7f00',
    '#007f7f'
  ],
  "Dark": [
    '#bf3f00',
    '#003fbf'
  ]
}

ACESolarWindPlasmaColors = {
  "Light": [
    '#9f0000',
    '#009f00',
    '#00009f'
  ],
  "Dark": [
    '#ff0000',
    '#00ff00',
    '#0000ff'
  ]
}
