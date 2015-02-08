#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

import urllib.request
import urllib.error

"""
  Locations of data that I want to capture and eventually graph. This data
  is provided from the GOES and ACE satellites.

  = GOES =
  Energetic Proton Flux
    http://services.swpc.noaa.gov/text/goes-energetic-proton-flux-primary.txt
    http://services.swpc.noaa.gov/text/goes-energetic-proton-flux-secondary.txt
  Geomagnetic Components and Total Field
    http://services.swpc.noaa.gov/text/goes-magnetometer-primary.txt
    http://services.swpc.noaa.gov/text/goes-magnetometer-secondary.txt
  Energetic Particle Flux
    http://services.swpc.noaa.gov/text/goes-magnetospheric-particle-flux-ts1-primary.txt
    http://services.swpc.noaa.gov/text/goes-magnetospheric-particle-flux-ts1-secondary.txt
  Solar Particle and Electron Flux
    http://services.swpc.noaa.gov/text/goes-particle-flux-primary.txt
    http://services.swpc.noaa.gov/text/goes-particle-flux-secondary.txt
  xRay Flux
    http://services.swpc.noaa.gov/text/goes-xray-flux-primary.txt
    http://services.swpc.noaa.gov/text/goes-xray-flux-secondary.txt

  = ACE =
  Differential Electron / Proton Flux
    http://services.swpc.noaa.gov/text/ace-epam.txt
  Solar Isotope Spectrometer
    http://services.swpc.noaa.gov/text/ace-sis.txt
  Interplanetary Magnetic Field
    http://services.swpc.noaa.gov/text/ace-magnetometer.txt
  Solar Wind Plasma
    http://services.swpc.noaa.gov/text/ace-swepam.txt

  xRay Imager:
    http://sxi.ngdc.noaa.gov
  Coronograph Imager:
    http://lasco-www.nrl.navy.mil/index.php?p=content/realtime

  Exhaustive list of text files is located here:
    http://services.swpc.noaa.gov/text/

  Loads more data to look at here:
    http://www.swpc.noaa.gov/Data/index.html#measurements
"""

#################################################
#               GOES Data                       #
#################################################
def getGOESRangeProtonFlux():
  """
    Apparently the NOAA Data Site was restructured which could explain
    why I was having issues accessing data when I first started writing
    this script/application.

    This particular URL happens to be from GOES-13, the primary source of
    Proton Flux, however GOES-15 also provides Proton Flux measurements as
    a secondary source.
  """
  URL = 'http://services.swpc.noaa.gov/text/goes-energetic-proton-flux-primary.txt'
  try:
    fh = urllib.request.urlopen(URL)
  except:
    print("NoaaApi.getGOESRangeProtonFlux > Error opening File Handle, retrying...")
    fh = ""
    fh = urllib.request.urlopen(URL)
  # Create the empty data structure
  data_ret = {
    "source":"",
    "data":{
      "Protons 0.7 - 4 MeV"   :[],
      "Protons 4 - 9 MeV"     :[],
      "Protons 9 - 15 MeV"    :[],
      "Protons 15 - 40 MeV"   :[],
      "Protons 38 - 82 MeV"   :[],
      "Protons 84 - 200 MeV"  :[],
      "Protons 110 - 900 MeV" :[],
      "Protons 350 - 420 MeV" :[],
      "Protons 420 - 510 MeV" :[],
      "Protons 510 - 700 MeV" :[],
      "Protons >700 MeV"      :[]
    },
    "units":"p/cm2 * s * sr * MeV",
    "datestamp":[],
    "rawlines":[]
  }
  # Loop through the remote data file
  for read_line in fh.readlines():
    read_line = read_line.decode('utf-8').split()
    if(len(read_line) > 1):
      # Get the data samples
      if((read_line[0][0] != '#') and (read_line[0][0] != ':')):
        data_ret["rawlines"   ].append(read_line)
        data_ret["datestamp"  ].append("%s/%s/%s:%s"%(read_line[0],read_line[1],
          read_line[2],read_line[3]))
        data_ret["data"]["Protons 0.7 - 4 MeV"  ].append(read_line[6])
        data_ret["data"]["Protons 4 - 9 MeV"    ].append(read_line[7])
        data_ret["data"]["Protons 9 - 15 MeV"   ].append(read_line[8])
        data_ret["data"]["Protons 15 - 40 MeV"  ].append(read_line[9])
        data_ret["data"]["Protons 38 - 82 MeV"  ].append(read_line[10])
        data_ret["data"]["Protons 84 - 200 MeV" ].append(read_line[11])
        data_ret["data"]["Protons 110 - 900 MeV"].append(read_line[12])
        data_ret["data"]["Protons 350 - 420 MeV"].append(read_line[13])
        data_ret["data"]["Protons 420 - 510 MeV"].append(read_line[14])
        data_ret["data"]["Protons 510 - 700 MeV"].append(read_line[15])
        data_ret["data"]["Protons >700 MeV"     ].append(read_line[16])
      # Get some header info
      elif(read_line[1] == 'Source:'):
        data_ret["source"] = str(read_line[2])
  # Convert the data points from strings to numbers
  for key in data_ret["data"].keys():
    data_ret["data"][key] = [float(i) for i in data_ret["data"][key]]
  return data_ret

def getGOESGoemagFieldFlux():
  """
    This function call will return the three dimensions of geomagnetic Flux
    density around the earth. The three dimensions and the total field have
    units of nanotesla.
  """
  URL = 'http://services.swpc.noaa.gov/text/goes-magnetometer-primary.txt'
  try:
    fh = urllib.request.urlopen(URL)
  except:
    print("NoaaApi.getGOESGoemagFieldFlux > Error opening File Handle, retrying...")
    fh = urllib.request.urlopen(URL)
  # Create the empty data structure
  data_ret = {
    "source":"",
    "data":{
      "Hp"    :[],
      "He"    :[],
      "Hn"    :[],
      "Total" :[]
    },
    "units":"nT",
    "datestamp":[],
    "rawlines":[]
  }
  # Loop through the remote data file
  for read_line in fh.readlines():
    read_line = read_line.decode('utf-8').split()
    if(len(read_line) > 1):
      # Get the data samples
      if((read_line[0][0] != '#') and (read_line[0][0] != ':')):
        data_ret["rawlines"].append(read_line)
        data_ret["datestamp"].append("%s/%s/%s:%s"%(read_line[0],read_line[1],
          read_line[2],read_line[3]))
        data_ret["data"]["Hp"].append(read_line[6])
        data_ret["data"]["He"].append(read_line[7])
        data_ret["data"]["Hn"].append(read_line[8])
        data_ret["data"]["Total"].append(read_line[9])
      # Get some header info
      elif(read_line[1] == 'Source:'):
        data_ret["source"] = str(read_line[2])
  # Convert the data points from strings to numbers
  for key in data_ret["data"].keys():
    data_ret["data"][key] = [float(i) for i in data_ret["data"][key]]
  return data_ret

def getGOESDiscreteParticleFlux():
  """
    This call will collect the data from the energetic Proton/Electron Flux. This
    API returns a list of 10 data lists of as many distinct proton and electron
    energies.
  """
  URL = 'http://services.swpc.noaa.gov/text/goes-magnetospheric-particle-flux-ts1-primary.txt'
  try:
    fh = urllib.request.urlopen(URL)
  except:
    print("NoaaApi.getGOESDiscreteParticleFlux > Error opening File Handle, retrying...")
    fh = urllib.request.urlopen(URL)
  # Create the empty data structure
  data_ret = {
    "source":"",
    "data":{
      "P1"    :[],
      "P2"    :[],
      "P3"    :[],
      "P4"    :[],
      "P5"    :[],
      "E1"    :[],
      "E2"    :[],
      "E3"    :[],
      "E4"    :[],
      "E5"    :[]
    },
    "units":{
      "P1"    : "95 keV Protons",
      "P2"    : "140 keV Protons",
      "P3"    : "210 keV Protons",
      "P4"    : "300 keV Protons",
      "P5"    : "475 keV Protons",
      "E1"    : "40 keV Electrons",
      "E2"    : "75 keV Electrons",
      "E3"    : "150 keV Electrons",
      "E4"    : "275 keV Electrons",
      "E5"    : "475 keV Electrons"
    },
    "datestamp":[],
    "rawlines":[]
  }
  # Loop through the remote data file
  for read_line in fh.readlines():
    read_line = read_line.decode('utf-8').split()
    if(len(read_line) > 1):
      # Get the data samples
      if((read_line[0][0] != '#') and (read_line[0][0] != ':')):
        data_ret["rawlines"].append(read_line)
        data_ret["datestamp"].append("%s/%s/%s:%s"%(read_line[0],read_line[1],
          read_line[2],read_line[3]))
        data_ret["data"]["P1"].append(read_line[6])
        data_ret["data"]["P2"].append(read_line[7])
        data_ret["data"]["P3"].append(read_line[8])
        data_ret["data"]["P4"].append(read_line[9])
        data_ret["data"]["P5"].append(read_line[10])
        data_ret["data"]["E1"].append(read_line[11])
        data_ret["data"]["E2"].append(read_line[12])
        data_ret["data"]["E3"].append(read_line[13])
        data_ret["data"]["E4"].append(read_line[14])
        data_ret["data"]["E5"].append(read_line[15])
      # Get some header info
      elif(read_line[1] == 'Source:'):
        data_ret["source"] = str(read_line[2])
  # Convert the data points from strings to numbers
  for key in data_ret["data"].keys():
    data_ret["data"][key] = [float(i) for i in data_ret["data"][key]]
  return data_ret

def getGOESRangeParticleFlux():
  """
    Similar to the getGOESDiscreteParticleFlux function, however this dataset returns
    particle counts for only 6 proton ranges and 3 electron ranges. The ranges of
    particle energies are low-barrier energies and greater.
    For instance the first set of data is of protons >1MeV, while the second is
    of protons >5MeV.
  """
  URL = 'http://services.swpc.noaa.gov/text/goes-particle-flux-primary.txt'
  try:
    fh = urllib.request.urlopen(URL)
  except:
    print("NoaaApi.getGOESRangeParticleFlux > Error opening File Handle, retrying...")
    fh = urllib.request.urlopen(URL)
  # Create the empty data structure
  data_ret = {
    "source":"",
    "data":{
      "P1"    :[],
      "P5"    :[],
      "P10"   :[],
      "P30"   :[],
      "P50"   :[],
      "P100"  :[],
      "E0.8"  :[],
      "E2.0"  :[],
      "E4.0"  :[]
    },
    "units":{
      "P1"    : ">1 Mev",
      "P5"    : ">5 Mev",
      "P10"   : ">10 Mev",
      "P30"   : ">30 Mev",
      "P50"   : ">50 Mev",
      "P100"  : ">100 Mev",
      "E0.8"  : ">0.8 Mev",
      "E2.0"  : ">2.0 Mev",
      "E4.0"  : ">4.0 Mev"
    },
    "datestamp":[],
    "rawlines":[]
  }
  # Loop through the remote data file
  for read_line in fh.readlines():
    read_line = read_line.decode('utf-8').split()
    if(len(read_line) > 1):
      # Get the data samples
      if((read_line[0][0] != '#') and (read_line[0][0] != ':')):
        data_ret["rawlines"].append(read_line)
        data_ret["datestamp"].append("%s/%s/%s:%s"%(read_line[0],read_line[1],
          read_line[2],read_line[3]))
        data_ret["data"]["P1"].append(read_line[6])
        data_ret["data"]["P5"].append(read_line[7])
        data_ret["data"]["P10"].append(read_line[8])
        data_ret["data"]["P30"].append(read_line[9])
        data_ret["data"]["P50"].append(read_line[10])
        data_ret["data"]["P100"].append(read_line[11])
        data_ret["data"]["E0.8"].append(read_line[12])
        data_ret["data"]["E2.0"].append(read_line[13])
        data_ret["data"]["E4.0"].append(read_line[14])
      # Get some header info
      elif(read_line[1] == 'Source:'):
        data_ret["source"] = str(read_line[2])
  # Convert the data points from strings to numbers
  for key in data_ret["data"].keys():
    data_ret["data"][key] = [float(i) for i in data_ret["data"][key]]
  return data_ret

def getGOESXrayFlux():
  """
    Apparently the NOAA Data Site was restructured which could explain
    why I was having issues accessing data when I first started writing
    this script/application.
  """
  URL = 'http://services.swpc.noaa.gov/text/goes-xray-flux-primary.txt'
  try:
    fh = urllib.request.urlopen(URL)
  except:
    print("NoaaApi.getGOESXrayFlux > Error opening File Handle, retrying...")
    fh = urllib.request.urlopen(URL)
  # Create the empty data structure
  data_ret = {
    "source":"",
    "data":{
      "long" :[],
      "short":[],
    },
    "units":"W/m2",
    "datestamp":[],
    "rawlines":[]
  }
  # Loop through the remote data file
  for read_line in fh.readlines():
    read_line = read_line.decode('utf-8').split()
    if(len(read_line) > 1):
      # Get the data samples
      if((read_line[0][0] != '#') and (read_line[0][0] != ':')):
        data_ret["rawlines"].append(read_line)
        data_ret["datestamp"].append("%s/%s/%s:%s"%(read_line[0],read_line[1],read_line[2],read_line[3]))
        data_ret["data"]["long"].append(read_line[7])
        data_ret["data"]["short"].append(read_line[6])
      # Get some header info
      elif(read_line[1] == 'Source:'):
        data_ret["source"] = str(read_line[2])
  # Convert the data points from strings to numbers
  for key in data_ret["data"].keys():
    data_ret["data"][key] = [float(i) for i in data_ret["data"][key]]
  return data_ret

#################################################
#                  ACE Data                     #
#################################################
def getDiffElecProtFlux():
  """
  """
  pass

def getSolarIsotopeSpectrometer():
  """
  """
  pass

def getInterplanetMagField():
  """
  """
  pass

def getSolarPlasma():
  """
  """
  pass

if __name__ == '__main__':
  # Get Proton Flux Data
  print("")
  print("------------------------------------")
  print("           Range Proton Flux")
  print("------------------------------------")
  alldata = getGOESRangeProtonFlux()
  print("data source is:")
  print(alldata["source"])
  for key,value in alldata["data"].items():
    print("%s data is:" % (key))
    print(value)
  print("data units are:")
  print(alldata["units"])
  print("timestamps are:")
  print(alldata["datestamp"])

  # Get Geomagnetic Flux Data
  print("")
  print("------------------------------------")
  print("          Geomagnetic Flux")
  print("------------------------------------")
  alldata = getGOESGoemagFieldFlux()
  print("data source is:")
  print(alldata["source"])
  for key,value in alldata["data"].items():
    print("%s data is:" % (key))
    print(value)
  print("data units are:")
  print(alldata["units"])
  print("timestamps are:")
  print(alldata["datestamp"])

  # Get Discrete Energetic Particle Flux Data
  print("")
  print("------------------------------------")
  print("  Discrete Energetic Particle Flux")
  print("------------------------------------")
  alldata = getGOESDiscreteParticleFlux()
  print("data source is:")
  print(alldata["source"])
  for key,value in alldata["data"].items():
    print("%s data is:" % (key))
    print(value)
  for key,value in alldata["units"].items():
    print("%s unit is:" % (key))
    print(value)
  print("timestamps are:")
  print(alldata["datestamp"])

  # Get Range Energetic Particle Flux Data
  print("")
  print("------------------------------------")
  print("   Range Energetic Particle Flux")
  print("------------------------------------")
  alldata = getGOESRangeParticleFlux()
  print("data source is:")
  print(alldata["source"])
  for key,value in alldata["data"].items():
    print("%s data is:" % (key))
    print(value)
  for key,value in alldata["units"].items():
    print("%s unit is:" % (key))
    print(value)
  print("timestamps are:")
  print(alldata["datestamp"])

  # Get XRay Flux Data
  print("")
  print("------------------------------------")
  print("           XRay Flux")
  print("------------------------------------")
  alldata = getGOESXrayFlux()
  print("data source is:")
  print(alldata["source"])
  print("data_short data is:")
  print(alldata["data"]["short"])
  print("data_long data is:")
  print(alldata["data"]["long"])
  print("data units are:")
  print(alldata["units"])
  print("timestamps are:")
  print(alldata["datestamp"])
