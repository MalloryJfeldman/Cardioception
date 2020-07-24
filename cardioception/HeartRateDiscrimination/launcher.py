# Author: Nicolas Legrand <nicolas.legrand@cfin.au.dk>

from parameters import getParameters
from task import run
from psychopy import gui

# Create a GUI and ask for high-evel experiment parameters
g = gui.Dlg()
g.addField("participant", initial='Participant')
g.addField("session", initial='001')
g.addField("Serial Port:", initial=None)
g.addField("Setup:", initial='behavioral')
g.addField("stairType:", initial='psi')
g.show()

# Set global task parameters here
parameters = getParameters(
    participant=g.data[0], session=g.data[1], serialPort=g.data[2],
    setup=g.data[3], stairType=g.data[4], nTrials=80, screenNb=0)
    #BrainVisionIP='10.60.88.162')

# Limit the number of trials to run
# parameters['Conditions'] = parameters['Conditions'][:4]
parameters['nFeedback'] = 2
parameters['nConfidence'] = 2
parameters['nBreaking'] = 20

# Run task
run(parameters, confidenceRating=True, runTutorial=False)

parameters['win'].close()
