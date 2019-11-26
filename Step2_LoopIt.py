#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height') 

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
#trialClock = core.Clock()


#%% your loop here
# start by copying your one trial here, then identify what needs to be
# changed on every trial.  Likely your stimuli, but you might want to change a few things


# make a list or a pd.DataFrame that contains trial-specific info (stimulus, etc)
# e.g. stim = ['1.jpg','2.jpg','3.jpg']
text_blue = visual.TextStim(win, text="blue", color="brown")
col_blue = visual.TextStim(win, text="orange", color="blue")
text_red = visual.TextStim(win, text="red", color="green")
col_red = visual.TextStim(win, text="brown", color="red")
text_yellow = visual.TextStim(win, text="yellow", color="orange")
col_yellow = visual.TextStim(win, text="green", color="yellow")

stim = [text_blue, col_blue, text_red, col_red, text_yellow, col_yellow]
stim = pd.Dataframe(stim)
stim = stim.sample(frac=1)

response = []

instructionText = visual.TextStim(win, text = "If the colour of the word \
                                  that appears is a primary colour of the \
                                  artist's colour wheel (Red-Yellow-Blue), \
                                  press ‘y'. Otherwise, press 'n'",
                                  color='black')
instructionText.draw()
win.flip()
event.waitKeys()
# make your loop
for text in stim:
    text.draw()
    win.flip()
    keys = event.waitKeys(maxWait = 2, keyList = ['y', 'n'])
    response.append(keys)
    
    
    # include your trial code in your loop but replace anything that should 
    # change on each trial with a variable that uses your iterater
    # e.g. thisStimName = stim[t]
    #      thisStim = visual.ImageStim(win, image=thisStimName ...)
    
    # if you're recording responses, be sure to store your responses in a list
    # or DataFrame which also uses your iterater!


#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

core.wait(2)
win.close()
