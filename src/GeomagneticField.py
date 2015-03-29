from MyMplCanvas import MyMplCanvas
import NoaaApi
import numpy
import colors_and_globals
"""
  As of MatPlotLib 1.5 qt4_compat will be deprecated for the more general
  qt_compat. Pulling that in instead.
"""
from matplotlib.backends import qt_compat
"""
  Branch using PyQt or PySide based on MatPlotLib values.
"""
if(qt_compat.QT_API == qt_compat.QT_API_PYSIDE):
  from PySide import QtGui, QtCore
else:
  from PyQt4 import QtGui, QtCore

###########################################################################
# Specific Plot Canvas Objects
###########################################################################
class MyGOESGoemagFieldFluxCanvas(MyMplCanvas):
  datas = {}
  units = {}
  label_list = []
  stamp = []
  def __init__(self, *args, **kwargs):
    """
      Initialize the updating object.
    """
    MyMplCanvas.__init__(self, left_edge=0.15, right_edge=0.82, top_edge=0.9,
      bottom_edge=0.22, *args, **kwargs)
    timer = QtCore.QTimer(self)
    # Tie the "update_figure" function to the timer
    timer.timeout.connect(self.update_figure)
    # Millisecond Timer, Assign the update time based on the value returned by
    # the API call, store the API call data in an object-global data variable
    # to reduce the number of API calls required to initialize the plot
    timer.start(60000)

  def compute_initial_figure(self):
    """
      Initial data plot.
    """
    # Get the new data
    (self.label_list,self.datas,self.stamp,self.units) = \
      NoaaApi.getGOESGeomagFieldFlux()
    # Get number of data points
    data_points = numpy.linspace(0,1,len(self.stamp))
    # Next plot overwrites all previous plots
    self.axes.hold(False)
    self.axes.plot(0)
    self.axes.hold(True)
    # Plot all data sets
    plot1 = [self.axes.plot(data_points, self.datas[key],
      colors_and_globals.GOESGeomagFieldFluxColors[key],
      label=key
      ) for key in self.label_list]
    # Format the Graph
    self.format_graph()

  def format_graph(self):
    # Set the graph background color
    self.axes.set_axis_bgcolor(colors_and_globals.graph_bgcolor)
    # Change Plot to logarithmic
    self.axes.set_yscale("log")
    # Show all plot grids
    self.axes.grid(True, which="both", color=colors_and_globals.grid_color)
    # Thin the number of x-axis labels and ticks, this works with the list of
    # tuples that are the date/time stamps
    self.stamp = [x \
      for x in self.stamp[0::7]
    ]
    # Get number of data points
    data_points = numpy.linspace(0,1,len(self.stamp))
    # Set number of X-Axis ticks
    self.axes.set_xticks(data_points)
    # Separate dates and times
    (dates,times) = zip(*self.stamp)
    # Change the plot tick labels
    if(colors_and_globals.plot_angle.find("-") != -1):
      self.axes.set_xticklabels(times,
        rotation=colors_and_globals.plot_angle, rotation_mode='anchor',
        horizontalalignment='left', fontsize=colors_and_globals.plotLabelSize)
    else:
      self.axes.set_xticklabels(times,
        rotation=colors_and_globals.plot_angle, rotation_mode='anchor',
        horizontalalignment='right', fontsize=colors_and_globals.plotLabelSize)
    # Show Units of y-axis
    self.axes.set_ylabel("nano Tesla [nT]", rotation='vertical',
      fontsize=colors_and_globals.plotLabelSize)
    # Show Units of x-axis
    if(dates[0] != dates[-1]):
      self.axes.set_xlabel(("UTC Time (%s - %s)"%(dates[0],dates[-1])),
        fontsize=colors_and_globals.plotLabelSize)
    else:
      self.axes.set_xlabel(("UTC Time (%s)"%(dates[-1])),
        fontsize=colors_and_globals.plotLabelSize)
    # Set the Plot Title
    self.axes.set_title("Geomagnetic Field", fontsize=colors_and_globals.plotTitleSize)
