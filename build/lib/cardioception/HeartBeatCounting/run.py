# Author: Nicolas Legrand <nicolas.legrand@cfin.au.dk>

from cardioception.HeartBeatCounting.task import sequence, tutorial, rest
from cardioception.HeartBeatCounting.parameters import getParameters
from psychopy import gui

# Create a GUI and store subject ID
g = gui.Dlg()
g.addField("Subject ID:")
g.addField("Subject Number:")
g.addField("Serial Port:")
g.show()

# Get parameters
parameters = getParameters(g.data[0], g.data[1], g.data[2])

# Run tutorial
tutorial(parameters)

if parameters['restPeriod'] is True:
    rest(parameters)

# Run the entire sequence
sequence(parameters)