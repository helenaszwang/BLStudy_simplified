#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on October 23, 2022, at 11:25
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'CombinedMST'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\wangs\\OneDrive - The University of Western Ontario\\Desktop\\ProjectBL\\BLStudy\\Session1\\Session1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1504, 1003], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "HeadphonePlay"
HeadphonePlayClock = core.Clock()
CheckSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='CheckSound')
CheckSound.setVolume(1)
counter = 0
checkcount = str(counter) + "/6"
QuestionTxt = visual.TextStim(win=win, name='QuestionTxt',
    text='Which tone was the quietest?\n(Press the corresponding number on your keyboard)\n\n1 = First  2 = Second  3 = Third',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
CheckTrial = visual.TextStim(win=win, name='CheckTrial',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
CrossHeadphone = visual.TextStim(win=win, name='CrossHeadphone',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
CheckResp = keyboard.Keyboard()

# Initialize components for Routine "HeadphoneFeedback"
HeadphoneFeedbackClock = core.Clock()
FeedbackTxt = visual.TextStim(win=win, name='FeedbackTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Welcome1"
Welcome1Clock = core.Clock()
WelcomeTxt1 = visual.TextStim(win=win, name='WelcomeTxt1',
    text='In this part, you will be presented with sound files for different made up \'words\'. Some of these files have been accidentally duplicated and we need your help looking for the duplicated files.\n\nThere are 100 sound files in total but almost half of them are duplicates. Your task is to listen to each sound and label it as either "OLD" (duplicate) or "NEW".',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ContinueKey1 = visual.TextStim(win=win, name='ContinueKey1',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ContinueResp = keyboard.Keyboard()
Task1Slide = visual.ImageStim(
    win=win,
    name='Task1Slide', 
    image='Task 1.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.7, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "PracticeBegin"
PracticeBeginClock = core.Clock()
WelcomeContinueKey2 = keyboard.Keyboard()
PracticeText2 = visual.TextStim(win=win, name='PracticeText2',
    text="Let's start with some practice",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Practice1"
Practice1Clock = core.Clock()
WTcount = 0
TrialNumber = visual.TextStim(win=win, name='TrialNumber',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
PracticeSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='PracticeSound')
PracticeSound.setVolume(1)
PracticeCross = visual.TextStim(win=win, name='PracticeCross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
PracticeRespKey2 = keyboard.Keyboard()

# Initialize components for Routine "PracticeFeedback"
PracticeFeedbackClock = core.Clock()
Practice_resp = keyboard.Keyboard()
PracticeMssg = visual.TextStim(win=win, name='PracticeMssg',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
FeedbackCross = visual.TextStim(win=win, name='FeedbackCross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Start"
StartClock = core.Clock()
StartTxt = visual.TextStim(win=win, name='StartTxt',
    text='Great job! This is the end of the practice.\n\n\nWe will now begin the actual task. There are 100 sound files in total. The words from the practice are not part of the actual task. ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
StartTast = keyboard.Keyboard()

# Initialize components for Routine "Countdown"
CountdownClock = core.Clock()
No3 = visual.TextStim(win=win, name='No3',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
No2 = visual.TextStim(win=win, name='No2',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
No1 = visual.TextStim(win=win, name='No1',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Count1"
Count1Clock = core.Clock()
no_3 = visual.TextStim(win=win, name='no_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "MSTWord"
MSTWordClock = core.Clock()
TargetSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='TargetSound')
TargetSound.setVolume(1)
ItemNumber = visual.TextStim(win=win, name='ItemNumber',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
MST_resp = keyboard.Keyboard()
Option2 = visual.TextStim(win=win, name='Option2',
    text='Old or New?',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "End1"
End1Clock = core.Clock()
EndMssg = visual.TextStim(win=win, name='EndMssg',
    text='Great job! This is the end of this component. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
End1Cont = keyboard.Keyboard()

# Initialize components for Routine "WelcomeSound"
WelcomeSoundClock = core.Clock()
Pt2WelcomeMssg = visual.TextStim(win=win, name='Pt2WelcomeMssg',
    text='In this part, you will be presented with sound files for different environmental sounds. Some of these files have been accidentally duplicated and we need your help looking for the duplicated files.\n\nThere are 128 sound files in total but almost one third of them are duplicates. Your task is to listen to each sound and label it as "OLD" (duplicate) or "NEW".',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='Press SPACE to begin the practice',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()
Task2Slide = visual.ImageStim(
    win=win,
    name='Task2Slide', 
    image='Task 2.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.7, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "PracticeBegin"
PracticeBeginClock = core.Clock()
WelcomeContinueKey2 = keyboard.Keyboard()
PracticeText2 = visual.TextStim(win=win, name='PracticeText2',
    text="Let's start with some practice",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "SoundPractice"
SoundPracticeClock = core.Clock()
Tcount = 0
PracticeSound2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='PracticeSound2')
PracticeSound2.setVolume(1)
PracticeCrossW = visual.TextStim(win=win, name='PracticeCrossW',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
PracticeTrialNo = visual.TextStim(win=win, name='PracticeTrialNo',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
PracticeRespKey2II = keyboard.Keyboard()

# Initialize components for Routine "SoundPracticeFeedback"
SoundPracticeFeedbackClock = core.Clock()
Message = visual.TextStim(win=win, name='Message',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
PracticeCrossW2 = visual.TextStim(win=win, name='PracticeCrossW2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
PracticeSoundKey = keyboard.Keyboard()

# Initialize components for Routine "MSTSoundStart"
MSTSoundStartClock = core.Clock()
MSTSoundStrtMssg = visual.TextStim(win=win, name='MSTSoundStrtMssg',
    text='Great job! This is the end of the practice.\n\n\nWe will now begin the actual task. There are 128 sound files in total. The sounds from the practice are not part of the actual task. ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
MSTSoundStrtKey = keyboard.Keyboard()

# Initialize components for Routine "Countdown"
CountdownClock = core.Clock()
No3 = visual.TextStim(win=win, name='No3',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
No2 = visual.TextStim(win=win, name='No2',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
No1 = visual.TextStim(win=win, name='No1',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Count2"
Count2Clock = core.Clock()
no2 = visual.TextStim(win=win, name='no2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "MSTSound"
MSTSoundClock = core.Clock()
MSTSoundCount = visual.TextStim(win=win, name='MSTSoundCount',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
MSTSoundPlay = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='MSTSoundPlay')
MSTSoundPlay.setVolume(1)
MSTSoundCross = visual.TextStim(win=win, name='MSTSoundCross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "MSTSoundResponse"
MSTSoundResponseClock = core.Clock()
MSTSoundKey = keyboard.Keyboard()
Options2II = visual.TextStim(win=win, name='Options2II',
    text='Old or New?',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "End1"
End1Clock = core.Clock()
EndMssg = visual.TextStim(win=win, name='EndMssg',
    text='Great job! This is the end of this component. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
End1Cont = keyboard.Keyboard()

# Initialize components for Routine "Welcome3"
Welcome3Clock = core.Clock()
Task3Slide = visual.ImageStim(
    win=win,
    name='Task3Slide', 
    image='Task 3.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.7, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
SimContKey = keyboard.Keyboard()

# Initialize components for Routine "Countdown"
CountdownClock = core.Clock()
No3 = visual.TextStim(win=win, name='No3',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
No2 = visual.TextStim(win=win, name='No2',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
No1 = visual.TextStim(win=win, name='No1',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Count3"
Count3Clock = core.Clock()
Cross1Sec = visual.TextStim(win=win, name='Cross1Sec',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "SimilarityPresentation"
SimilarityPresentationClock = core.Clock()
simcount = 0
FirstSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='FirstSound')
FirstSound.setVolume(1)
SecondSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='SecondSound')
SecondSound.setVolume(1)
Cross = visual.TextStim(win=win, name='Cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
NumberOne = visual.TextStim(win=win, name='NumberOne',
    text='Sound 1',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
NumberTwo = visual.TextStim(win=win, name='NumberTwo',
    text='Sound 2',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
SimTrialNumber = visual.TextStim(win=win, name='SimTrialNumber',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "SimlarityResponse"
SimlarityResponseClock = core.Clock()
SimilarityRatingScale = visual.TextStim(win=win, name='SimilarityRatingScale',
    text='1 ----------------- 2 ----------------- 3 ----------------- 4 \nDifferent                                                   Same ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
SimilarityRatingKey = keyboard.Keyboard()

# Initialize components for Routine "End1"
End1Clock = core.Clock()
EndMssg = visual.TextStim(win=win, name='EndMssg',
    text='Great job! This is the end of this component. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
End1Cont = keyboard.Keyboard()

# Initialize components for Routine "Welcome4"
Welcome4Clock = core.Clock()
Task4Slide = visual.ImageStim(
    win=win,
    name='Task4Slide', 
    image='Task 4.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.7, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Welcome4End = keyboard.Keyboard()

# Initialize components for Routine "Count3"
Count3Clock = core.Clock()
Cross1Sec = visual.TextStim(win=win, name='Cross1Sec',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "SoundLabeling"
SoundLabelingClock = core.Clock()
SoundLabelQuestion = visual.TextStim(win=win, name='SoundLabelQuestion',
    text='What is this sound?',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Sound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='Sound')
Sound.setVolume(1)
LabelingKey = keyboard.Keyboard()

# Initialize components for Routine "End1"
End1Clock = core.Clock()
EndMssg = visual.TextStim(win=win, name='EndMssg',
    text='Great job! This is the end of this component. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
End1Cont = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Headphone_check.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "HeadphonePlay"-------
    continueRoutine = True
    # update component parameters for each repeat
    CheckSound.setSound(File, hamming=True)
    CheckSound.setVolume(1, log=False)
    counter += 1
    checkcount = str(counter) + "/6"
    CheckTrial.setText(checkcount)
    CheckResp.keys = []
    CheckResp.rt = []
    _CheckResp_allKeys = []
    # keep track of which components have finished
    HeadphonePlayComponents = [CheckSound, QuestionTxt, CheckTrial, CrossHeadphone, CheckResp]
    for thisComponent in HeadphonePlayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    HeadphonePlayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "HeadphonePlay"-------
    while continueRoutine:
        # get current time
        t = HeadphonePlayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=HeadphonePlayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop CheckSound
        if CheckSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CheckSound.frameNStart = frameN  # exact frame index
            CheckSound.tStart = t  # local t and not account for scr refresh
            CheckSound.tStartRefresh = tThisFlipGlobal  # on global time
            CheckSound.play(when=win)  # sync with win flip
        
        # *QuestionTxt* updates
        if QuestionTxt.status == NOT_STARTED and tThisFlip >= CheckSound.getDuration() + 0.5-frameTolerance:
            # keep track of start time/frame for later
            QuestionTxt.frameNStart = frameN  # exact frame index
            QuestionTxt.tStart = t  # local t and not account for scr refresh
            QuestionTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(QuestionTxt, 'tStartRefresh')  # time at next scr refresh
            QuestionTxt.setAutoDraw(True)
        
        # *CheckTrial* updates
        if CheckTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CheckTrial.frameNStart = frameN  # exact frame index
            CheckTrial.tStart = t  # local t and not account for scr refresh
            CheckTrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CheckTrial, 'tStartRefresh')  # time at next scr refresh
            CheckTrial.setAutoDraw(True)
        if CheckTrial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CheckTrial.tStartRefresh + CheckSound.getDuration() + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                CheckTrial.tStop = t  # not accounting for scr refresh
                CheckTrial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(CheckTrial, 'tStopRefresh')  # time at next scr refresh
                CheckTrial.setAutoDraw(False)
        
        # *CrossHeadphone* updates
        if CrossHeadphone.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CrossHeadphone.frameNStart = frameN  # exact frame index
            CrossHeadphone.tStart = t  # local t and not account for scr refresh
            CrossHeadphone.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CrossHeadphone, 'tStartRefresh')  # time at next scr refresh
            CrossHeadphone.setAutoDraw(True)
        if CrossHeadphone.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CrossHeadphone.tStartRefresh + CheckSound.getDuration() + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                CrossHeadphone.tStop = t  # not accounting for scr refresh
                CrossHeadphone.frameNStop = frameN  # exact frame index
                win.timeOnFlip(CrossHeadphone, 'tStopRefresh')  # time at next scr refresh
                CrossHeadphone.setAutoDraw(False)
        
        # *CheckResp* updates
        waitOnFlip = False
        if CheckResp.status == NOT_STARTED and tThisFlip >= CheckSound.getDuration() + 0.5-frameTolerance:
            # keep track of start time/frame for later
            CheckResp.frameNStart = frameN  # exact frame index
            CheckResp.tStart = t  # local t and not account for scr refresh
            CheckResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CheckResp, 'tStartRefresh')  # time at next scr refresh
            CheckResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(CheckResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(CheckResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if CheckResp.status == STARTED and not waitOnFlip:
            theseKeys = CheckResp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _CheckResp_allKeys.extend(theseKeys)
            if len(_CheckResp_allKeys):
                CheckResp.keys = _CheckResp_allKeys[-1].name  # just the last key pressed
                CheckResp.rt = _CheckResp_allKeys[-1].rt
                # was this correct?
                if (CheckResp.keys == str(Correct)) or (CheckResp.keys == Correct):
                    CheckResp.corr = 1
                else:
                    CheckResp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in HeadphonePlayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "HeadphonePlay"-------
    for thisComponent in HeadphonePlayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    CheckSound.stop()  # ensure sound has stopped at end of routine
    trials_2.addData('CheckSound.started', CheckSound.tStartRefresh)
    trials_2.addData('CheckSound.stopped', CheckSound.tStopRefresh)
    if CheckResp.corr == 1:
        message = "CORRECT"
    else:
        message = "INCORRECT"
    trials_2.addData('QuestionTxt.started', QuestionTxt.tStartRefresh)
    trials_2.addData('QuestionTxt.stopped', QuestionTxt.tStopRefresh)
    trials_2.addData('CheckTrial.started', CheckTrial.tStartRefresh)
    trials_2.addData('CheckTrial.stopped', CheckTrial.tStopRefresh)
    trials_2.addData('CrossHeadphone.started', CrossHeadphone.tStartRefresh)
    trials_2.addData('CrossHeadphone.stopped', CrossHeadphone.tStopRefresh)
    # check responses
    if CheckResp.keys in ['', [], None]:  # No response was made
        CheckResp.keys = None
        # was no response the correct answer?!
        if str(Correct).lower() == 'none':
           CheckResp.corr = 1;  # correct non-response
        else:
           CheckResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('CheckResp.keys',CheckResp.keys)
    trials_2.addData('CheckResp.corr', CheckResp.corr)
    if CheckResp.keys != None:  # we had a response
        trials_2.addData('CheckResp.rt', CheckResp.rt)
    trials_2.addData('CheckResp.started', CheckResp.tStartRefresh)
    trials_2.addData('CheckResp.stopped', CheckResp.tStopRefresh)
    # the Routine "HeadphonePlay" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "HeadphoneFeedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    FeedbackTxt.setText(message)
    # keep track of which components have finished
    HeadphoneFeedbackComponents = [FeedbackTxt]
    for thisComponent in HeadphoneFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    HeadphoneFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "HeadphoneFeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = HeadphoneFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=HeadphoneFeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FeedbackTxt* updates
        if FeedbackTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FeedbackTxt.frameNStart = frameN  # exact frame index
            FeedbackTxt.tStart = t  # local t and not account for scr refresh
            FeedbackTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FeedbackTxt, 'tStartRefresh')  # time at next scr refresh
            FeedbackTxt.setAutoDraw(True)
        if FeedbackTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FeedbackTxt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                FeedbackTxt.tStop = t  # not accounting for scr refresh
                FeedbackTxt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FeedbackTxt, 'tStopRefresh')  # time at next scr refresh
                FeedbackTxt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in HeadphoneFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "HeadphoneFeedback"-------
    for thisComponent in HeadphoneFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('FeedbackTxt.started', FeedbackTxt.tStartRefresh)
    trials_2.addData('FeedbackTxt.stopped', FeedbackTxt.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
WordTask = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='WordTask')
thisExp.addLoop(WordTask)  # add the loop to the experiment
thisWordTask = WordTask.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisWordTask.rgb)
if thisWordTask != None:
    for paramName in thisWordTask:
        exec('{} = thisWordTask[paramName]'.format(paramName))

for thisWordTask in WordTask:
    currentLoop = WordTask
    # abbreviate parameter names if possible (e.g. rgb = thisWordTask.rgb)
    if thisWordTask != None:
        for paramName in thisWordTask:
            exec('{} = thisWordTask[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Welcome1"-------
    continueRoutine = True
    # update component parameters for each repeat
    ContinueResp.keys = []
    ContinueResp.rt = []
    _ContinueResp_allKeys = []
    # keep track of which components have finished
    Welcome1Components = [WelcomeTxt1, ContinueKey1, ContinueResp, Task1Slide]
    for thisComponent in Welcome1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Welcome1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Welcome1"-------
    while continueRoutine:
        # get current time
        t = Welcome1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Welcome1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *WelcomeTxt1* updates
        if WelcomeTxt1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            WelcomeTxt1.frameNStart = frameN  # exact frame index
            WelcomeTxt1.tStart = t  # local t and not account for scr refresh
            WelcomeTxt1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(WelcomeTxt1, 'tStartRefresh')  # time at next scr refresh
            WelcomeTxt1.setAutoDraw(True)
        
        # *ContinueKey1* updates
        if ContinueKey1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ContinueKey1.frameNStart = frameN  # exact frame index
            ContinueKey1.tStart = t  # local t and not account for scr refresh
            ContinueKey1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ContinueKey1, 'tStartRefresh')  # time at next scr refresh
            ContinueKey1.setAutoDraw(True)
        
        # *ContinueResp* updates
        waitOnFlip = False
        if ContinueResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ContinueResp.frameNStart = frameN  # exact frame index
            ContinueResp.tStart = t  # local t and not account for scr refresh
            ContinueResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ContinueResp, 'tStartRefresh')  # time at next scr refresh
            ContinueResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ContinueResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ContinueResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ContinueResp.status == STARTED and not waitOnFlip:
            theseKeys = ContinueResp.getKeys(keyList=['space'], waitRelease=False)
            _ContinueResp_allKeys.extend(theseKeys)
            if len(_ContinueResp_allKeys):
                ContinueResp.keys = _ContinueResp_allKeys[-1].name  # just the last key pressed
                ContinueResp.rt = _ContinueResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Task1Slide* updates
        if Task1Slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Task1Slide.frameNStart = frameN  # exact frame index
            Task1Slide.tStart = t  # local t and not account for scr refresh
            Task1Slide.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task1Slide, 'tStartRefresh')  # time at next scr refresh
            Task1Slide.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Welcome1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Welcome1"-------
    for thisComponent in Welcome1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    WordTask.addData('WelcomeTxt1.started', WelcomeTxt1.tStartRefresh)
    WordTask.addData('WelcomeTxt1.stopped', WelcomeTxt1.tStopRefresh)
    WordTask.addData('ContinueKey1.started', ContinueKey1.tStartRefresh)
    WordTask.addData('ContinueKey1.stopped', ContinueKey1.tStopRefresh)
    # check responses
    if ContinueResp.keys in ['', [], None]:  # No response was made
        ContinueResp.keys = None
    WordTask.addData('ContinueResp.keys',ContinueResp.keys)
    if ContinueResp.keys != None:  # we had a response
        WordTask.addData('ContinueResp.rt', ContinueResp.rt)
    WordTask.addData('ContinueResp.started', ContinueResp.tStartRefresh)
    WordTask.addData('ContinueResp.stopped', ContinueResp.tStopRefresh)
    WordTask.addData('Task1Slide.started', Task1Slide.tStartRefresh)
    WordTask.addData('Task1Slide.stopped', Task1Slide.tStopRefresh)
    # the Routine "Welcome1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "PracticeBegin"-------
    continueRoutine = True
    # update component parameters for each repeat
    WelcomeContinueKey2.keys = []
    WelcomeContinueKey2.rt = []
    _WelcomeContinueKey2_allKeys = []
    # keep track of which components have finished
    PracticeBeginComponents = [WelcomeContinueKey2, PracticeText2]
    for thisComponent in PracticeBeginComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeBeginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "PracticeBegin"-------
    while continueRoutine:
        # get current time
        t = PracticeBeginClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeBeginClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *WelcomeContinueKey2* updates
        waitOnFlip = False
        if WelcomeContinueKey2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            WelcomeContinueKey2.frameNStart = frameN  # exact frame index
            WelcomeContinueKey2.tStart = t  # local t and not account for scr refresh
            WelcomeContinueKey2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(WelcomeContinueKey2, 'tStartRefresh')  # time at next scr refresh
            WelcomeContinueKey2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(WelcomeContinueKey2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(WelcomeContinueKey2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if WelcomeContinueKey2.status == STARTED and not waitOnFlip:
            theseKeys = WelcomeContinueKey2.getKeys(keyList=['space'], waitRelease=False)
            _WelcomeContinueKey2_allKeys.extend(theseKeys)
            if len(_WelcomeContinueKey2_allKeys):
                WelcomeContinueKey2.keys = _WelcomeContinueKey2_allKeys[-1].name  # just the last key pressed
                WelcomeContinueKey2.rt = _WelcomeContinueKey2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *PracticeText2* updates
        if PracticeText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PracticeText2.frameNStart = frameN  # exact frame index
            PracticeText2.tStart = t  # local t and not account for scr refresh
            PracticeText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PracticeText2, 'tStartRefresh')  # time at next scr refresh
            PracticeText2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeBeginComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracticeBegin"-------
    for thisComponent in PracticeBeginComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if WelcomeContinueKey2.keys in ['', [], None]:  # No response was made
        WelcomeContinueKey2.keys = None
    WordTask.addData('WelcomeContinueKey2.keys',WelcomeContinueKey2.keys)
    if WelcomeContinueKey2.keys != None:  # we had a response
        WordTask.addData('WelcomeContinueKey2.rt', WelcomeContinueKey2.rt)
    WordTask.addData('WelcomeContinueKey2.started', WelcomeContinueKey2.tStartRefresh)
    WordTask.addData('WelcomeContinueKey2.stopped', WelcomeContinueKey2.tStopRefresh)
    WordTask.addData('PracticeText2.started', PracticeText2.tStartRefresh)
    WordTask.addData('PracticeText2.stopped', PracticeText2.tStopRefresh)
    # the Routine "PracticeBegin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    PracticeTrials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('WordMST_practicetrials.xlsx'),
        seed=None, name='PracticeTrials')
    thisExp.addLoop(PracticeTrials)  # add the loop to the experiment
    thisPracticeTrial = PracticeTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial:
            exec('{} = thisPracticeTrial[paramName]'.format(paramName))
    
    for thisPracticeTrial in PracticeTrials:
        currentLoop = PracticeTrials
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
        if thisPracticeTrial != None:
            for paramName in thisPracticeTrial:
                exec('{} = thisPracticeTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Practice1"-------
        continueRoutine = True
        # update component parameters for each repeat
        WTcount += 1
        WTrialCount = 'Trial ' + str(WTcount)
        TrialNumber.setText(WTrialCount)
        PracticeSound.setSound(SoundFile, hamming=True)
        PracticeSound.setVolume(1, log=False)
        PracticeRespKey2.keys = []
        PracticeRespKey2.rt = []
        _PracticeRespKey2_allKeys = []
        # keep track of which components have finished
        Practice1Components = [TrialNumber, PracticeSound, PracticeCross, PracticeRespKey2]
        for thisComponent in Practice1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Practice1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Practice1"-------
        while continueRoutine:
            # get current time
            t = Practice1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Practice1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TrialNumber* updates
            if TrialNumber.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialNumber.frameNStart = frameN  # exact frame index
                TrialNumber.tStart = t  # local t and not account for scr refresh
                TrialNumber.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialNumber, 'tStartRefresh')  # time at next scr refresh
                TrialNumber.setAutoDraw(True)
            # start/stop PracticeSound
            if PracticeSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeSound.frameNStart = frameN  # exact frame index
                PracticeSound.tStart = t  # local t and not account for scr refresh
                PracticeSound.tStartRefresh = tThisFlipGlobal  # on global time
                PracticeSound.play(when=win)  # sync with win flip
            
            # *PracticeCross* updates
            if PracticeCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeCross.frameNStart = frameN  # exact frame index
                PracticeCross.tStart = t  # local t and not account for scr refresh
                PracticeCross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeCross, 'tStartRefresh')  # time at next scr refresh
                PracticeCross.setAutoDraw(True)
            
            # *PracticeRespKey2* updates
            waitOnFlip = False
            if PracticeRespKey2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeRespKey2.frameNStart = frameN  # exact frame index
                PracticeRespKey2.tStart = t  # local t and not account for scr refresh
                PracticeRespKey2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeRespKey2, 'tStartRefresh')  # time at next scr refresh
                PracticeRespKey2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(PracticeRespKey2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(PracticeRespKey2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if PracticeRespKey2.status == STARTED and not waitOnFlip:
                theseKeys = PracticeRespKey2.getKeys(keyList=['space'], waitRelease=False)
                _PracticeRespKey2_allKeys.extend(theseKeys)
                if len(_PracticeRespKey2_allKeys):
                    PracticeRespKey2.keys = _PracticeRespKey2_allKeys[-1].name  # just the last key pressed
                    PracticeRespKey2.rt = _PracticeRespKey2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Practice1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Practice1"-------
        for thisComponent in Practice1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        PracticeTrials.addData('TrialNumber.started', TrialNumber.tStartRefresh)
        PracticeTrials.addData('TrialNumber.stopped', TrialNumber.tStopRefresh)
        PracticeSound.stop()  # ensure sound has stopped at end of routine
        PracticeTrials.addData('PracticeSound.started', PracticeSound.tStartRefresh)
        PracticeTrials.addData('PracticeSound.stopped', PracticeSound.tStopRefresh)
        PracticeTrials.addData('PracticeCross.started', PracticeCross.tStartRefresh)
        PracticeTrials.addData('PracticeCross.stopped', PracticeCross.tStopRefresh)
        # check responses
        if PracticeRespKey2.keys in ['', [], None]:  # No response was made
            PracticeRespKey2.keys = None
        PracticeTrials.addData('PracticeRespKey2.keys',PracticeRespKey2.keys)
        if PracticeRespKey2.keys != None:  # we had a response
            PracticeTrials.addData('PracticeRespKey2.rt', PracticeRespKey2.rt)
        PracticeTrials.addData('PracticeRespKey2.started', PracticeRespKey2.tStartRefresh)
        PracticeTrials.addData('PracticeRespKey2.stopped', PracticeRespKey2.tStopRefresh)
        # the Routine "Practice1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "PracticeFeedback"-------
        continueRoutine = True
        # update component parameters for each repeat
        #Tcount += 1
        #TrialCount = 'Trial ' + str(Tcount)
        if Type == 'NEW':
            message = "This is a NEW word. \nThis is your first time hearing this word."
        elif Type == 'SIMILAR':
            message = "This is a NEW word. \nNote that this one sounds similar to the previous word but is not exactly the same."
        elif Type == 'OLD':
            message = "This is an OLD word. \nThis word is exactly the same as the first word."
        Practice_resp.keys = []
        Practice_resp.rt = []
        _Practice_resp_allKeys = []
        PracticeMssg.setText(message)
        # keep track of which components have finished
        PracticeFeedbackComponents = [Practice_resp, PracticeMssg, FeedbackCross]
        for thisComponent in PracticeFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "PracticeFeedback"-------
        while continueRoutine:
            # get current time
            t = PracticeFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Practice_resp* updates
            waitOnFlip = False
            if Practice_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Practice_resp.frameNStart = frameN  # exact frame index
                Practice_resp.tStart = t  # local t and not account for scr refresh
                Practice_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Practice_resp, 'tStartRefresh')  # time at next scr refresh
                Practice_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Practice_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Practice_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Practice_resp.status == STARTED and not waitOnFlip:
                theseKeys = Practice_resp.getKeys(keyList=['space'], waitRelease=False)
                _Practice_resp_allKeys.extend(theseKeys)
                if len(_Practice_resp_allKeys):
                    Practice_resp.keys = _Practice_resp_allKeys[-1].name  # just the last key pressed
                    Practice_resp.rt = _Practice_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *PracticeMssg* updates
            if PracticeMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeMssg.frameNStart = frameN  # exact frame index
                PracticeMssg.tStart = t  # local t and not account for scr refresh
                PracticeMssg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeMssg, 'tStartRefresh')  # time at next scr refresh
                PracticeMssg.setAutoDraw(True)
            
            # *FeedbackCross* updates
            if FeedbackCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FeedbackCross.frameNStart = frameN  # exact frame index
                FeedbackCross.tStart = t  # local t and not account for scr refresh
                FeedbackCross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FeedbackCross, 'tStartRefresh')  # time at next scr refresh
                FeedbackCross.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PracticeFeedback"-------
        for thisComponent in PracticeFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if Practice_resp.corr == 1:
            feedback = 'CORRECT'
        else:
            feedback = 'INCORRECT'
        # check responses
        if Practice_resp.keys in ['', [], None]:  # No response was made
            Practice_resp.keys = None
        PracticeTrials.addData('Practice_resp.keys',Practice_resp.keys)
        if Practice_resp.keys != None:  # we had a response
            PracticeTrials.addData('Practice_resp.rt', Practice_resp.rt)
        PracticeTrials.addData('Practice_resp.started', Practice_resp.tStartRefresh)
        PracticeTrials.addData('Practice_resp.stopped', Practice_resp.tStopRefresh)
        PracticeTrials.addData('PracticeMssg.started', PracticeMssg.tStartRefresh)
        PracticeTrials.addData('PracticeMssg.stopped', PracticeMssg.tStopRefresh)
        PracticeTrials.addData('FeedbackCross.started', FeedbackCross.tStartRefresh)
        PracticeTrials.addData('FeedbackCross.stopped', FeedbackCross.tStopRefresh)
        # the Routine "PracticeFeedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'PracticeTrials'
    
    
    # ------Prepare to start Routine "Start"-------
    continueRoutine = True
    # update component parameters for each repeat
    StartTast.keys = []
    StartTast.rt = []
    _StartTast_allKeys = []
    # keep track of which components have finished
    StartComponents = [StartTxt, StartTast]
    for thisComponent in StartComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    StartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Start"-------
    while continueRoutine:
        # get current time
        t = StartClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=StartClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StartTxt* updates
        if StartTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StartTxt.frameNStart = frameN  # exact frame index
            StartTxt.tStart = t  # local t and not account for scr refresh
            StartTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StartTxt, 'tStartRefresh')  # time at next scr refresh
            StartTxt.setAutoDraw(True)
        
        # *StartTast* updates
        waitOnFlip = False
        if StartTast.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StartTast.frameNStart = frameN  # exact frame index
            StartTast.tStart = t  # local t and not account for scr refresh
            StartTast.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StartTast, 'tStartRefresh')  # time at next scr refresh
            StartTast.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(StartTast.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(StartTast.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if StartTast.status == STARTED and not waitOnFlip:
            theseKeys = StartTast.getKeys(keyList=['space'], waitRelease=False)
            _StartTast_allKeys.extend(theseKeys)
            if len(_StartTast_allKeys):
                StartTast.keys = _StartTast_allKeys[-1].name  # just the last key pressed
                StartTast.rt = _StartTast_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StartComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Start"-------
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    WordTask.addData('StartTxt.started', StartTxt.tStartRefresh)
    WordTask.addData('StartTxt.stopped', StartTxt.tStopRefresh)
    # check responses
    if StartTast.keys in ['', [], None]:  # No response was made
        StartTast.keys = None
    WordTask.addData('StartTast.keys',StartTast.keys)
    if StartTast.keys != None:  # we had a response
        WordTask.addData('StartTast.rt', StartTast.rt)
    WordTask.addData('StartTast.started', StartTast.tStartRefresh)
    WordTask.addData('StartTast.stopped', StartTast.tStopRefresh)
    count = 0
    condition = "0:100"
    import random
    c = random.randint(0, 6)
    if c == 0:
        condition = "0:100"
    elif c == 1:
        condition = "100:200"
    elif c == 2:
        condition = "200:300"
    elif c == 3:
        condition = "300:400"
    elif c == 4:
        condition = "400:500"
    elif c == 5:
        condition = "500:600"
    # the Routine "Start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Countdown"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    CountdownComponents = [No3, No2, No1]
    for thisComponent in CountdownComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CountdownClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Countdown"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CountdownClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CountdownClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *No3* updates
        if No3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            No3.frameNStart = frameN  # exact frame index
            No3.tStart = t  # local t and not account for scr refresh
            No3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(No3, 'tStartRefresh')  # time at next scr refresh
            No3.setAutoDraw(True)
        if No3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > No3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                No3.tStop = t  # not accounting for scr refresh
                No3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(No3, 'tStopRefresh')  # time at next scr refresh
                No3.setAutoDraw(False)
        
        # *No2* updates
        if No2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            No2.frameNStart = frameN  # exact frame index
            No2.tStart = t  # local t and not account for scr refresh
            No2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(No2, 'tStartRefresh')  # time at next scr refresh
            No2.setAutoDraw(True)
        if No2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > No2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                No2.tStop = t  # not accounting for scr refresh
                No2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(No2, 'tStopRefresh')  # time at next scr refresh
                No2.setAutoDraw(False)
        
        # *No1* updates
        if No1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            No1.frameNStart = frameN  # exact frame index
            No1.tStart = t  # local t and not account for scr refresh
            No1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(No1, 'tStartRefresh')  # time at next scr refresh
            No1.setAutoDraw(True)
        if No1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > No1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                No1.tStop = t  # not accounting for scr refresh
                No1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(No1, 'tStopRefresh')  # time at next scr refresh
                No1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CountdownComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Countdown"-------
    for thisComponent in CountdownComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    WordTask.addData('No3.started', No3.tStartRefresh)
    WordTask.addData('No3.stopped', No3.tStopRefresh)
    WordTask.addData('No2.started', No2.tStartRefresh)
    WordTask.addData('No2.stopped', No2.tStopRefresh)
    WordTask.addData('No1.started', No1.tStartRefresh)
    WordTask.addData('No1.stopped', No1.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('WordMST_trials.xlsx', selection='0:100'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Count1"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        count += 1
        number = str(count) + "/100"
        
        
        # keep track of which components have finished
        Count1Components = [no_3]
        for thisComponent in Count1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Count1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Count1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Count1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Count1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *no_3* updates
            if no_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                no_3.frameNStart = frameN  # exact frame index
                no_3.tStart = t  # local t and not account for scr refresh
                no_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(no_3, 'tStartRefresh')  # time at next scr refresh
                no_3.setAutoDraw(True)
            if no_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > no_3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    no_3.tStop = t  # not accounting for scr refresh
                    no_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(no_3, 'tStopRefresh')  # time at next scr refresh
                    no_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Count1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Count1"-------
        for thisComponent in Count1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('no_3.started', no_3.tStartRefresh)
        trials.addData('no_3.stopped', no_3.tStopRefresh)
        
        # ------Prepare to start Routine "MSTWord"-------
        continueRoutine = True
        # update component parameters for each repeat
        TargetSound.setSound(File, hamming=True)
        TargetSound.setVolume(1, log=False)
        ItemNumber.setText(number)
        MST_resp.keys = []
        MST_resp.rt = []
        _MST_resp_allKeys = []
        # keep track of which components have finished
        MSTWordComponents = [TargetSound, ItemNumber, MST_resp, Option2]
        for thisComponent in MSTWordComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MSTWordClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "MSTWord"-------
        while continueRoutine:
            # get current time
            t = MSTWordClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MSTWordClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop TargetSound
            if TargetSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TargetSound.frameNStart = frameN  # exact frame index
                TargetSound.tStart = t  # local t and not account for scr refresh
                TargetSound.tStartRefresh = tThisFlipGlobal  # on global time
                TargetSound.play(when=win)  # sync with win flip
            
            # *ItemNumber* updates
            if ItemNumber.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ItemNumber.frameNStart = frameN  # exact frame index
                ItemNumber.tStart = t  # local t and not account for scr refresh
                ItemNumber.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ItemNumber, 'tStartRefresh')  # time at next scr refresh
                ItemNumber.setAutoDraw(True)
            
            # *MST_resp* updates
            waitOnFlip = False
            if MST_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                MST_resp.frameNStart = frameN  # exact frame index
                MST_resp.tStart = t  # local t and not account for scr refresh
                MST_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MST_resp, 'tStartRefresh')  # time at next scr refresh
                MST_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(MST_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(MST_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if MST_resp.status == STARTED and not waitOnFlip:
                theseKeys = MST_resp.getKeys(keyList=['1', '2'], waitRelease=False)
                _MST_resp_allKeys.extend(theseKeys)
                if len(_MST_resp_allKeys):
                    MST_resp.keys = _MST_resp_allKeys[-1].name  # just the last key pressed
                    MST_resp.rt = _MST_resp_allKeys[-1].rt
                    # was this correct?
                    if (MST_resp.keys == str(WordCorrect)) or (MST_resp.keys == WordCorrect):
                        MST_resp.corr = 1
                    else:
                        MST_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *Option2* updates
            if Option2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Option2.frameNStart = frameN  # exact frame index
                Option2.tStart = t  # local t and not account for scr refresh
                Option2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Option2, 'tStartRefresh')  # time at next scr refresh
                Option2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MSTWordComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MSTWord"-------
        for thisComponent in MSTWordComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TargetSound.stop()  # ensure sound has stopped at end of routine
        trials.addData('TargetSound.started', TargetSound.tStartRefresh)
        trials.addData('TargetSound.stopped', TargetSound.tStopRefresh)
        trials.addData('ItemNumber.started', ItemNumber.tStartRefresh)
        trials.addData('ItemNumber.stopped', ItemNumber.tStopRefresh)
        # check responses
        if MST_resp.keys in ['', [], None]:  # No response was made
            MST_resp.keys = None
            # was no response the correct answer?!
            if str(WordCorrect).lower() == 'none':
               MST_resp.corr = 1;  # correct non-response
            else:
               MST_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('MST_resp.keys',MST_resp.keys)
        trials.addData('MST_resp.corr', MST_resp.corr)
        if MST_resp.keys != None:  # we had a response
            trials.addData('MST_resp.rt', MST_resp.rt)
        trials.addData('MST_resp.started', MST_resp.tStartRefresh)
        trials.addData('MST_resp.stopped', MST_resp.tStopRefresh)
        trials.addData('Option2.started', Option2.tStartRefresh)
        trials.addData('Option2.stopped', Option2.tStopRefresh)
        # the Routine "MSTWord" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'WordTask'


# ------Prepare to start Routine "End1"-------
continueRoutine = True
# update component parameters for each repeat
End1Cont.keys = []
End1Cont.rt = []
_End1Cont_allKeys = []
# keep track of which components have finished
End1Components = [EndMssg, End1Cont]
for thisComponent in End1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
End1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End1"-------
while continueRoutine:
    # get current time
    t = End1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=End1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndMssg* updates
    if EndMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndMssg.frameNStart = frameN  # exact frame index
        EndMssg.tStart = t  # local t and not account for scr refresh
        EndMssg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndMssg, 'tStartRefresh')  # time at next scr refresh
        EndMssg.setAutoDraw(True)
    
    # *End1Cont* updates
    waitOnFlip = False
    if End1Cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        End1Cont.frameNStart = frameN  # exact frame index
        End1Cont.tStart = t  # local t and not account for scr refresh
        End1Cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End1Cont, 'tStartRefresh')  # time at next scr refresh
        End1Cont.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(End1Cont.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(End1Cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if End1Cont.status == STARTED and not waitOnFlip:
        theseKeys = End1Cont.getKeys(keyList=['space'], waitRelease=False)
        _End1Cont_allKeys.extend(theseKeys)
        if len(_End1Cont_allKeys):
            End1Cont.keys = _End1Cont_allKeys[-1].name  # just the last key pressed
            End1Cont.rt = _End1Cont_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End1"-------
for thisComponent in End1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndMssg.started', EndMssg.tStartRefresh)
thisExp.addData('EndMssg.stopped', EndMssg.tStopRefresh)
# check responses
if End1Cont.keys in ['', [], None]:  # No response was made
    End1Cont.keys = None
thisExp.addData('End1Cont.keys',End1Cont.keys)
if End1Cont.keys != None:  # we had a response
    thisExp.addData('End1Cont.rt', End1Cont.rt)
thisExp.addData('End1Cont.started', End1Cont.tStartRefresh)
thisExp.addData('End1Cont.stopped', End1Cont.tStopRefresh)
thisExp.nextEntry()
# the Routine "End1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
SoundTask = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='SoundTask')
thisExp.addLoop(SoundTask)  # add the loop to the experiment
thisSoundTask = SoundTask.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSoundTask.rgb)
if thisSoundTask != None:
    for paramName in thisSoundTask:
        exec('{} = thisSoundTask[paramName]'.format(paramName))

for thisSoundTask in SoundTask:
    currentLoop = SoundTask
    # abbreviate parameter names if possible (e.g. rgb = thisSoundTask.rgb)
    if thisSoundTask != None:
        for paramName in thisSoundTask:
            exec('{} = thisSoundTask[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "WelcomeSound"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    WelcomeSoundComponents = [Pt2WelcomeMssg, text_3, key_resp, Task2Slide]
    for thisComponent in WelcomeSoundComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    WelcomeSoundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "WelcomeSound"-------
    while continueRoutine:
        # get current time
        t = WelcomeSoundClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=WelcomeSoundClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Pt2WelcomeMssg* updates
        if Pt2WelcomeMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pt2WelcomeMssg.frameNStart = frameN  # exact frame index
            Pt2WelcomeMssg.tStart = t  # local t and not account for scr refresh
            Pt2WelcomeMssg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pt2WelcomeMssg, 'tStartRefresh')  # time at next scr refresh
            Pt2WelcomeMssg.setAutoDraw(True)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Task2Slide* updates
        if Task2Slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Task2Slide.frameNStart = frameN  # exact frame index
            Task2Slide.tStart = t  # local t and not account for scr refresh
            Task2Slide.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Task2Slide, 'tStartRefresh')  # time at next scr refresh
            Task2Slide.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WelcomeSoundComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "WelcomeSound"-------
    for thisComponent in WelcomeSoundComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SoundTask.addData('Pt2WelcomeMssg.started', Pt2WelcomeMssg.tStartRefresh)
    SoundTask.addData('Pt2WelcomeMssg.stopped', Pt2WelcomeMssg.tStopRefresh)
    SoundTask.addData('text_3.started', text_3.tStartRefresh)
    SoundTask.addData('text_3.stopped', text_3.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    SoundTask.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        SoundTask.addData('key_resp.rt', key_resp.rt)
    SoundTask.addData('key_resp.started', key_resp.tStartRefresh)
    SoundTask.addData('key_resp.stopped', key_resp.tStopRefresh)
    SoundTask.addData('Task2Slide.started', Task2Slide.tStartRefresh)
    SoundTask.addData('Task2Slide.stopped', Task2Slide.tStopRefresh)
    # the Routine "WelcomeSound" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "PracticeBegin"-------
    continueRoutine = True
    # update component parameters for each repeat
    WelcomeContinueKey2.keys = []
    WelcomeContinueKey2.rt = []
    _WelcomeContinueKey2_allKeys = []
    # keep track of which components have finished
    PracticeBeginComponents = [WelcomeContinueKey2, PracticeText2]
    for thisComponent in PracticeBeginComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeBeginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "PracticeBegin"-------
    while continueRoutine:
        # get current time
        t = PracticeBeginClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeBeginClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *WelcomeContinueKey2* updates
        waitOnFlip = False
        if WelcomeContinueKey2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            WelcomeContinueKey2.frameNStart = frameN  # exact frame index
            WelcomeContinueKey2.tStart = t  # local t and not account for scr refresh
            WelcomeContinueKey2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(WelcomeContinueKey2, 'tStartRefresh')  # time at next scr refresh
            WelcomeContinueKey2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(WelcomeContinueKey2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(WelcomeContinueKey2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if WelcomeContinueKey2.status == STARTED and not waitOnFlip:
            theseKeys = WelcomeContinueKey2.getKeys(keyList=['space'], waitRelease=False)
            _WelcomeContinueKey2_allKeys.extend(theseKeys)
            if len(_WelcomeContinueKey2_allKeys):
                WelcomeContinueKey2.keys = _WelcomeContinueKey2_allKeys[-1].name  # just the last key pressed
                WelcomeContinueKey2.rt = _WelcomeContinueKey2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *PracticeText2* updates
        if PracticeText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PracticeText2.frameNStart = frameN  # exact frame index
            PracticeText2.tStart = t  # local t and not account for scr refresh
            PracticeText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PracticeText2, 'tStartRefresh')  # time at next scr refresh
            PracticeText2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeBeginComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracticeBegin"-------
    for thisComponent in PracticeBeginComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if WelcomeContinueKey2.keys in ['', [], None]:  # No response was made
        WelcomeContinueKey2.keys = None
    SoundTask.addData('WelcomeContinueKey2.keys',WelcomeContinueKey2.keys)
    if WelcomeContinueKey2.keys != None:  # we had a response
        SoundTask.addData('WelcomeContinueKey2.rt', WelcomeContinueKey2.rt)
    SoundTask.addData('WelcomeContinueKey2.started', WelcomeContinueKey2.tStartRefresh)
    SoundTask.addData('WelcomeContinueKey2.stopped', WelcomeContinueKey2.tStopRefresh)
    SoundTask.addData('PracticeText2.started', PracticeText2.tStartRefresh)
    SoundTask.addData('PracticeText2.stopped', PracticeText2.tStopRefresh)
    # the Routine "PracticeBegin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    SoundPracticeLoop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('SoundMST_trials.xlsx', selection='0:5'),
        seed=None, name='SoundPracticeLoop')
    thisExp.addLoop(SoundPracticeLoop)  # add the loop to the experiment
    thisSoundPracticeLoop = SoundPracticeLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSoundPracticeLoop.rgb)
    if thisSoundPracticeLoop != None:
        for paramName in thisSoundPracticeLoop:
            exec('{} = thisSoundPracticeLoop[paramName]'.format(paramName))
    
    for thisSoundPracticeLoop in SoundPracticeLoop:
        currentLoop = SoundPracticeLoop
        # abbreviate parameter names if possible (e.g. rgb = thisSoundPracticeLoop.rgb)
        if thisSoundPracticeLoop != None:
            for paramName in thisSoundPracticeLoop:
                exec('{} = thisSoundPracticeLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "SoundPractice"-------
        continueRoutine = True
        # update component parameters for each repeat
        Tcount += 1
        TrialCount = 'Trial ' + str(Tcount)
        PracticeSound2.setSound(SoundMST_File, hamming=True)
        PracticeSound2.setVolume(1, log=False)
        PracticeTrialNo.setText(TrialCount)
        PracticeRespKey2II.keys = []
        PracticeRespKey2II.rt = []
        _PracticeRespKey2II_allKeys = []
        # keep track of which components have finished
        SoundPracticeComponents = [PracticeSound2, PracticeCrossW, PracticeTrialNo, PracticeRespKey2II]
        for thisComponent in SoundPracticeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        SoundPracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "SoundPractice"-------
        while continueRoutine:
            # get current time
            t = SoundPracticeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=SoundPracticeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop PracticeSound2
            if PracticeSound2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeSound2.frameNStart = frameN  # exact frame index
                PracticeSound2.tStart = t  # local t and not account for scr refresh
                PracticeSound2.tStartRefresh = tThisFlipGlobal  # on global time
                PracticeSound2.play(when=win)  # sync with win flip
            
            # *PracticeCrossW* updates
            if PracticeCrossW.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeCrossW.frameNStart = frameN  # exact frame index
                PracticeCrossW.tStart = t  # local t and not account for scr refresh
                PracticeCrossW.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeCrossW, 'tStartRefresh')  # time at next scr refresh
                PracticeCrossW.setAutoDraw(True)
            
            # *PracticeTrialNo* updates
            if PracticeTrialNo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeTrialNo.frameNStart = frameN  # exact frame index
                PracticeTrialNo.tStart = t  # local t and not account for scr refresh
                PracticeTrialNo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeTrialNo, 'tStartRefresh')  # time at next scr refresh
                PracticeTrialNo.setAutoDraw(True)
            
            # *PracticeRespKey2II* updates
            waitOnFlip = False
            if PracticeRespKey2II.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeRespKey2II.frameNStart = frameN  # exact frame index
                PracticeRespKey2II.tStart = t  # local t and not account for scr refresh
                PracticeRespKey2II.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeRespKey2II, 'tStartRefresh')  # time at next scr refresh
                PracticeRespKey2II.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(PracticeRespKey2II.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(PracticeRespKey2II.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if PracticeRespKey2II.status == STARTED and not waitOnFlip:
                theseKeys = PracticeRespKey2II.getKeys(keyList=['space'], waitRelease=False)
                _PracticeRespKey2II_allKeys.extend(theseKeys)
                if len(_PracticeRespKey2II_allKeys):
                    PracticeRespKey2II.keys = _PracticeRespKey2II_allKeys[-1].name  # just the last key pressed
                    PracticeRespKey2II.rt = _PracticeRespKey2II_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SoundPracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "SoundPractice"-------
        for thisComponent in SoundPracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        PracticeSound2.stop()  # ensure sound has stopped at end of routine
        SoundPracticeLoop.addData('PracticeSound2.started', PracticeSound2.tStartRefresh)
        SoundPracticeLoop.addData('PracticeSound2.stopped', PracticeSound2.tStopRefresh)
        SoundPracticeLoop.addData('PracticeCrossW.started', PracticeCrossW.tStartRefresh)
        SoundPracticeLoop.addData('PracticeCrossW.stopped', PracticeCrossW.tStopRefresh)
        SoundPracticeLoop.addData('PracticeTrialNo.started', PracticeTrialNo.tStartRefresh)
        SoundPracticeLoop.addData('PracticeTrialNo.stopped', PracticeTrialNo.tStopRefresh)
        # check responses
        if PracticeRespKey2II.keys in ['', [], None]:  # No response was made
            PracticeRespKey2II.keys = None
        SoundPracticeLoop.addData('PracticeRespKey2II.keys',PracticeRespKey2II.keys)
        if PracticeRespKey2II.keys != None:  # we had a response
            SoundPracticeLoop.addData('PracticeRespKey2II.rt', PracticeRespKey2II.rt)
        SoundPracticeLoop.addData('PracticeRespKey2II.started', PracticeRespKey2II.tStartRefresh)
        SoundPracticeLoop.addData('PracticeRespKey2II.stopped', PracticeRespKey2II.tStopRefresh)
        # the Routine "SoundPractice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "SoundPracticeFeedback"-------
        continueRoutine = True
        # update component parameters for each repeat
        if SoundType == 'NEW':
            message = "This is a NEW sound. \nThis is your first time hearing this sound."
        elif SoundType == 'SIMILAR':
            message = "This is a NEW sound. \nNote that this one sounds similar to the previous sound but is not exactly the same."
        elif SoundType == 'OLD':
            message = "This is an OLD sound. \nThis sound is exactly the same as the first sound."
        Message.setText(message)
        PracticeSoundKey.keys = []
        PracticeSoundKey.rt = []
        _PracticeSoundKey_allKeys = []
        # keep track of which components have finished
        SoundPracticeFeedbackComponents = [Message, PracticeCrossW2, PracticeSoundKey]
        for thisComponent in SoundPracticeFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        SoundPracticeFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "SoundPracticeFeedback"-------
        while continueRoutine:
            # get current time
            t = SoundPracticeFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=SoundPracticeFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Message* updates
            if Message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Message.frameNStart = frameN  # exact frame index
                Message.tStart = t  # local t and not account for scr refresh
                Message.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Message, 'tStartRefresh')  # time at next scr refresh
                Message.setAutoDraw(True)
            
            # *PracticeCrossW2* updates
            if PracticeCrossW2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeCrossW2.frameNStart = frameN  # exact frame index
                PracticeCrossW2.tStart = t  # local t and not account for scr refresh
                PracticeCrossW2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeCrossW2, 'tStartRefresh')  # time at next scr refresh
                PracticeCrossW2.setAutoDraw(True)
            
            # *PracticeSoundKey* updates
            waitOnFlip = False
            if PracticeSoundKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeSoundKey.frameNStart = frameN  # exact frame index
                PracticeSoundKey.tStart = t  # local t and not account for scr refresh
                PracticeSoundKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeSoundKey, 'tStartRefresh')  # time at next scr refresh
                PracticeSoundKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(PracticeSoundKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(PracticeSoundKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if PracticeSoundKey.status == STARTED and not waitOnFlip:
                theseKeys = PracticeSoundKey.getKeys(keyList=['space'], waitRelease=False)
                _PracticeSoundKey_allKeys.extend(theseKeys)
                if len(_PracticeSoundKey_allKeys):
                    PracticeSoundKey.keys = _PracticeSoundKey_allKeys[-1].name  # just the last key pressed
                    PracticeSoundKey.rt = _PracticeSoundKey_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SoundPracticeFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "SoundPracticeFeedback"-------
        for thisComponent in SoundPracticeFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if PracticeSoundKey.corr == 1:
            feedback = 'CORRECT'
        else:
            feedback = 'INCORRECT'
        SoundPracticeLoop.addData('Message.started', Message.tStartRefresh)
        SoundPracticeLoop.addData('Message.stopped', Message.tStopRefresh)
        SoundPracticeLoop.addData('PracticeCrossW2.started', PracticeCrossW2.tStartRefresh)
        SoundPracticeLoop.addData('PracticeCrossW2.stopped', PracticeCrossW2.tStopRefresh)
        # check responses
        if PracticeSoundKey.keys in ['', [], None]:  # No response was made
            PracticeSoundKey.keys = None
        SoundPracticeLoop.addData('PracticeSoundKey.keys',PracticeSoundKey.keys)
        if PracticeSoundKey.keys != None:  # we had a response
            SoundPracticeLoop.addData('PracticeSoundKey.rt', PracticeSoundKey.rt)
        SoundPracticeLoop.addData('PracticeSoundKey.started', PracticeSoundKey.tStartRefresh)
        SoundPracticeLoop.addData('PracticeSoundKey.stopped', PracticeSoundKey.tStopRefresh)
        # the Routine "SoundPracticeFeedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'SoundPracticeLoop'
    
    
    # ------Prepare to start Routine "MSTSoundStart"-------
    continueRoutine = True
    # update component parameters for each repeat
    MSTSoundStrtKey.keys = []
    MSTSoundStrtKey.rt = []
    _MSTSoundStrtKey_allKeys = []
    # keep track of which components have finished
    MSTSoundStartComponents = [MSTSoundStrtMssg, MSTSoundStrtKey]
    for thisComponent in MSTSoundStartComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    MSTSoundStartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "MSTSoundStart"-------
    while continueRoutine:
        # get current time
        t = MSTSoundStartClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=MSTSoundStartClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *MSTSoundStrtMssg* updates
        if MSTSoundStrtMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MSTSoundStrtMssg.frameNStart = frameN  # exact frame index
            MSTSoundStrtMssg.tStart = t  # local t and not account for scr refresh
            MSTSoundStrtMssg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MSTSoundStrtMssg, 'tStartRefresh')  # time at next scr refresh
            MSTSoundStrtMssg.setAutoDraw(True)
        
        # *MSTSoundStrtKey* updates
        waitOnFlip = False
        if MSTSoundStrtKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MSTSoundStrtKey.frameNStart = frameN  # exact frame index
            MSTSoundStrtKey.tStart = t  # local t and not account for scr refresh
            MSTSoundStrtKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MSTSoundStrtKey, 'tStartRefresh')  # time at next scr refresh
            MSTSoundStrtKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(MSTSoundStrtKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(MSTSoundStrtKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if MSTSoundStrtKey.status == STARTED and not waitOnFlip:
            theseKeys = MSTSoundStrtKey.getKeys(keyList=['space'], waitRelease=False)
            _MSTSoundStrtKey_allKeys.extend(theseKeys)
            if len(_MSTSoundStrtKey_allKeys):
                MSTSoundStrtKey.keys = _MSTSoundStrtKey_allKeys[-1].name  # just the last key pressed
                MSTSoundStrtKey.rt = _MSTSoundStrtKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MSTSoundStartComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "MSTSoundStart"-------
    for thisComponent in MSTSoundStartComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    count = 0
    rows = "5:133"
    import random
    s = random.randint(0, 1)
    if s == 0:
        rows = "5:133"
    elif s == 1:
        rows = "133:261"
    elif s == 2:
        rows = "261:389"
    elif s == 3:
        rows = "389:517"
    elif s == 4:
        rows = "517:645"
    elif s == 5:
        rows = "645:773"
    
    SoundTask.addData('MSTSoundStrtMssg.started', MSTSoundStrtMssg.tStartRefresh)
    SoundTask.addData('MSTSoundStrtMssg.stopped', MSTSoundStrtMssg.tStopRefresh)
    # check responses
    if MSTSoundStrtKey.keys in ['', [], None]:  # No response was made
        MSTSoundStrtKey.keys = None
    SoundTask.addData('MSTSoundStrtKey.keys',MSTSoundStrtKey.keys)
    if MSTSoundStrtKey.keys != None:  # we had a response
        SoundTask.addData('MSTSoundStrtKey.rt', MSTSoundStrtKey.rt)
    SoundTask.addData('MSTSoundStrtKey.started', MSTSoundStrtKey.tStartRefresh)
    SoundTask.addData('MSTSoundStrtKey.stopped', MSTSoundStrtKey.tStopRefresh)
    # the Routine "MSTSoundStart" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Countdown"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    CountdownComponents = [No3, No2, No1]
    for thisComponent in CountdownComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CountdownClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Countdown"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CountdownClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CountdownClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *No3* updates
        if No3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            No3.frameNStart = frameN  # exact frame index
            No3.tStart = t  # local t and not account for scr refresh
            No3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(No3, 'tStartRefresh')  # time at next scr refresh
            No3.setAutoDraw(True)
        if No3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > No3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                No3.tStop = t  # not accounting for scr refresh
                No3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(No3, 'tStopRefresh')  # time at next scr refresh
                No3.setAutoDraw(False)
        
        # *No2* updates
        if No2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            No2.frameNStart = frameN  # exact frame index
            No2.tStart = t  # local t and not account for scr refresh
            No2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(No2, 'tStartRefresh')  # time at next scr refresh
            No2.setAutoDraw(True)
        if No2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > No2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                No2.tStop = t  # not accounting for scr refresh
                No2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(No2, 'tStopRefresh')  # time at next scr refresh
                No2.setAutoDraw(False)
        
        # *No1* updates
        if No1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            No1.frameNStart = frameN  # exact frame index
            No1.tStart = t  # local t and not account for scr refresh
            No1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(No1, 'tStartRefresh')  # time at next scr refresh
            No1.setAutoDraw(True)
        if No1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > No1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                No1.tStop = t  # not accounting for scr refresh
                No1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(No1, 'tStopRefresh')  # time at next scr refresh
                No1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CountdownComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Countdown"-------
    for thisComponent in CountdownComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SoundTask.addData('No3.started', No3.tStartRefresh)
    SoundTask.addData('No3.stopped', No3.tStopRefresh)
    SoundTask.addData('No2.started', No2.tStartRefresh)
    SoundTask.addData('No2.stopped', No2.tStopRefresh)
    SoundTask.addData('No1.started', No1.tStartRefresh)
    SoundTask.addData('No1.stopped', No1.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    MSTSoundLoop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('SoundMST_trials.xlsx', selection='5:133'),
        seed=None, name='MSTSoundLoop')
    thisExp.addLoop(MSTSoundLoop)  # add the loop to the experiment
    thisMSTSoundLoop = MSTSoundLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMSTSoundLoop.rgb)
    if thisMSTSoundLoop != None:
        for paramName in thisMSTSoundLoop:
            exec('{} = thisMSTSoundLoop[paramName]'.format(paramName))
    
    for thisMSTSoundLoop in MSTSoundLoop:
        currentLoop = MSTSoundLoop
        # abbreviate parameter names if possible (e.g. rgb = thisMSTSoundLoop.rgb)
        if thisMSTSoundLoop != None:
            for paramName in thisMSTSoundLoop:
                exec('{} = thisMSTSoundLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Count2"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        count += 1
        number = str(count) + "/128"
        NoSoundOn = 0
        if count == 45 or count == 82:
            NoSoundOn = 1
        else:
            NoSoundOn = 0
        # keep track of which components have finished
        Count2Components = [no2]
        for thisComponent in Count2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Count2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Count2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Count2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Count2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *no2* updates
            if no2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                no2.frameNStart = frameN  # exact frame index
                no2.tStart = t  # local t and not account for scr refresh
                no2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(no2, 'tStartRefresh')  # time at next scr refresh
                no2.setAutoDraw(True)
            if no2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > no2.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    no2.tStop = t  # not accounting for scr refresh
                    no2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(no2, 'tStopRefresh')  # time at next scr refresh
                    no2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Count2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Count2"-------
        for thisComponent in Count2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        MSTSoundLoop.addData('no2.started', no2.tStartRefresh)
        MSTSoundLoop.addData('no2.stopped', no2.tStopRefresh)
        
        # ------Prepare to start Routine "MSTSound"-------
        continueRoutine = True
        # update component parameters for each repeat
        MSTSoundCount.setText(number)
        MSTSoundPlay.setSound(SoundMST_File, hamming=True)
        MSTSoundPlay.setVolume(1, log=False)
        # keep track of which components have finished
        MSTSoundComponents = [MSTSoundCount, MSTSoundPlay, MSTSoundCross]
        for thisComponent in MSTSoundComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MSTSoundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "MSTSound"-------
        while continueRoutine:
            # get current time
            t = MSTSoundClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MSTSoundClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *MSTSoundCount* updates
            if MSTSoundCount.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MSTSoundCount.frameNStart = frameN  # exact frame index
                MSTSoundCount.tStart = t  # local t and not account for scr refresh
                MSTSoundCount.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MSTSoundCount, 'tStartRefresh')  # time at next scr refresh
                MSTSoundCount.setAutoDraw(True)
            if MSTSoundCount.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > MSTSoundCount.tStartRefresh + MSTSoundPlay.getDuration()+0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    MSTSoundCount.tStop = t  # not accounting for scr refresh
                    MSTSoundCount.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(MSTSoundCount, 'tStopRefresh')  # time at next scr refresh
                    MSTSoundCount.setAutoDraw(False)
            # start/stop MSTSoundPlay
            if MSTSoundPlay.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MSTSoundPlay.frameNStart = frameN  # exact frame index
                MSTSoundPlay.tStart = t  # local t and not account for scr refresh
                MSTSoundPlay.tStartRefresh = tThisFlipGlobal  # on global time
                MSTSoundPlay.play(when=win)  # sync with win flip
            
            # *MSTSoundCross* updates
            if MSTSoundCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MSTSoundCross.frameNStart = frameN  # exact frame index
                MSTSoundCross.tStart = t  # local t and not account for scr refresh
                MSTSoundCross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MSTSoundCross, 'tStartRefresh')  # time at next scr refresh
                MSTSoundCross.setAutoDraw(True)
            if MSTSoundCross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > MSTSoundCross.tStartRefresh + MSTSoundPlay.getDuration()+0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    MSTSoundCross.tStop = t  # not accounting for scr refresh
                    MSTSoundCross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(MSTSoundCross, 'tStopRefresh')  # time at next scr refresh
                    MSTSoundCross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MSTSoundComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MSTSound"-------
        for thisComponent in MSTSoundComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        MSTSoundLoop.addData('MSTSoundCount.started', MSTSoundCount.tStartRefresh)
        MSTSoundLoop.addData('MSTSoundCount.stopped', MSTSoundCount.tStopRefresh)
        MSTSoundPlay.stop()  # ensure sound has stopped at end of routine
        MSTSoundLoop.addData('MSTSoundPlay.started', MSTSoundPlay.tStartRefresh)
        MSTSoundLoop.addData('MSTSoundPlay.stopped', MSTSoundPlay.tStopRefresh)
        MSTSoundLoop.addData('MSTSoundCross.started', MSTSoundCross.tStartRefresh)
        MSTSoundLoop.addData('MSTSoundCross.stopped', MSTSoundCross.tStopRefresh)
        # the Routine "MSTSound" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "MSTSoundResponse"-------
        continueRoutine = True
        # update component parameters for each repeat
        MSTSoundKey.keys = []
        MSTSoundKey.rt = []
        _MSTSoundKey_allKeys = []
        #MSTSoundOptions.alignText='left'
        #MSTSoundNote.alignText='left'
        # keep track of which components have finished
        MSTSoundResponseComponents = [MSTSoundKey, Options2II]
        for thisComponent in MSTSoundResponseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MSTSoundResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "MSTSoundResponse"-------
        while continueRoutine:
            # get current time
            t = MSTSoundResponseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MSTSoundResponseClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *MSTSoundKey* updates
            waitOnFlip = False
            if MSTSoundKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MSTSoundKey.frameNStart = frameN  # exact frame index
                MSTSoundKey.tStart = t  # local t and not account for scr refresh
                MSTSoundKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MSTSoundKey, 'tStartRefresh')  # time at next scr refresh
                MSTSoundKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(MSTSoundKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(MSTSoundKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if MSTSoundKey.status == STARTED and not waitOnFlip:
                theseKeys = MSTSoundKey.getKeys(keyList=['1', '2'], waitRelease=False)
                _MSTSoundKey_allKeys.extend(theseKeys)
                if len(_MSTSoundKey_allKeys):
                    MSTSoundKey.keys = _MSTSoundKey_allKeys[-1].name  # just the last key pressed
                    MSTSoundKey.rt = _MSTSoundKey_allKeys[-1].rt
                    # was this correct?
                    if (MSTSoundKey.keys == str(SoundCorrect)) or (MSTSoundKey.keys == SoundCorrect):
                        MSTSoundKey.corr = 1
                    else:
                        MSTSoundKey.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *Options2II* updates
            if Options2II.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Options2II.frameNStart = frameN  # exact frame index
                Options2II.tStart = t  # local t and not account for scr refresh
                Options2II.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Options2II, 'tStartRefresh')  # time at next scr refresh
                Options2II.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MSTSoundResponseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MSTSoundResponse"-------
        for thisComponent in MSTSoundResponseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if MSTSoundKey.keys in ['', [], None]:  # No response was made
            MSTSoundKey.keys = None
            # was no response the correct answer?!
            if str(SoundCorrect).lower() == 'none':
               MSTSoundKey.corr = 1;  # correct non-response
            else:
               MSTSoundKey.corr = 0;  # failed to respond (incorrectly)
        # store data for MSTSoundLoop (TrialHandler)
        MSTSoundLoop.addData('MSTSoundKey.keys',MSTSoundKey.keys)
        MSTSoundLoop.addData('MSTSoundKey.corr', MSTSoundKey.corr)
        if MSTSoundKey.keys != None:  # we had a response
            MSTSoundLoop.addData('MSTSoundKey.rt', MSTSoundKey.rt)
        MSTSoundLoop.addData('MSTSoundKey.started', MSTSoundKey.tStartRefresh)
        MSTSoundLoop.addData('MSTSoundKey.stopped', MSTSoundKey.tStopRefresh)
        MSTSoundLoop.addData('Options2II.started', Options2II.tStartRefresh)
        MSTSoundLoop.addData('Options2II.stopped', Options2II.tStopRefresh)
        # the Routine "MSTSoundResponse" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'MSTSoundLoop'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'SoundTask'


# ------Prepare to start Routine "End1"-------
continueRoutine = True
# update component parameters for each repeat
End1Cont.keys = []
End1Cont.rt = []
_End1Cont_allKeys = []
# keep track of which components have finished
End1Components = [EndMssg, End1Cont]
for thisComponent in End1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
End1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End1"-------
while continueRoutine:
    # get current time
    t = End1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=End1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndMssg* updates
    if EndMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndMssg.frameNStart = frameN  # exact frame index
        EndMssg.tStart = t  # local t and not account for scr refresh
        EndMssg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndMssg, 'tStartRefresh')  # time at next scr refresh
        EndMssg.setAutoDraw(True)
    
    # *End1Cont* updates
    waitOnFlip = False
    if End1Cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        End1Cont.frameNStart = frameN  # exact frame index
        End1Cont.tStart = t  # local t and not account for scr refresh
        End1Cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End1Cont, 'tStartRefresh')  # time at next scr refresh
        End1Cont.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(End1Cont.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(End1Cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if End1Cont.status == STARTED and not waitOnFlip:
        theseKeys = End1Cont.getKeys(keyList=['space'], waitRelease=False)
        _End1Cont_allKeys.extend(theseKeys)
        if len(_End1Cont_allKeys):
            End1Cont.keys = _End1Cont_allKeys[-1].name  # just the last key pressed
            End1Cont.rt = _End1Cont_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End1"-------
for thisComponent in End1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndMssg.started', EndMssg.tStartRefresh)
thisExp.addData('EndMssg.stopped', EndMssg.tStopRefresh)
# check responses
if End1Cont.keys in ['', [], None]:  # No response was made
    End1Cont.keys = None
thisExp.addData('End1Cont.keys',End1Cont.keys)
if End1Cont.keys != None:  # we had a response
    thisExp.addData('End1Cont.rt', End1Cont.rt)
thisExp.addData('End1Cont.started', End1Cont.tStartRefresh)
thisExp.addData('End1Cont.stopped', End1Cont.tStopRefresh)
thisExp.nextEntry()
# the Routine "End1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Welcome3"-------
continueRoutine = True
# update component parameters for each repeat
SimContKey.keys = []
SimContKey.rt = []
_SimContKey_allKeys = []
# keep track of which components have finished
Welcome3Components = [Task3Slide, SimContKey]
for thisComponent in Welcome3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Welcome3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome3"-------
while continueRoutine:
    # get current time
    t = Welcome3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Welcome3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Task3Slide* updates
    if Task3Slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Task3Slide.frameNStart = frameN  # exact frame index
        Task3Slide.tStart = t  # local t and not account for scr refresh
        Task3Slide.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Task3Slide, 'tStartRefresh')  # time at next scr refresh
        Task3Slide.setAutoDraw(True)
    
    # *SimContKey* updates
    waitOnFlip = False
    if SimContKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SimContKey.frameNStart = frameN  # exact frame index
        SimContKey.tStart = t  # local t and not account for scr refresh
        SimContKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SimContKey, 'tStartRefresh')  # time at next scr refresh
        SimContKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(SimContKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(SimContKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if SimContKey.status == STARTED and not waitOnFlip:
        theseKeys = SimContKey.getKeys(keyList=['space'], waitRelease=False)
        _SimContKey_allKeys.extend(theseKeys)
        if len(_SimContKey_allKeys):
            SimContKey.keys = _SimContKey_allKeys[-1].name  # just the last key pressed
            SimContKey.rt = _SimContKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome3"-------
for thisComponent in Welcome3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Task3Slide.started', Task3Slide.tStartRefresh)
thisExp.addData('Task3Slide.stopped', Task3Slide.tStopRefresh)
# check responses
if SimContKey.keys in ['', [], None]:  # No response was made
    SimContKey.keys = None
thisExp.addData('SimContKey.keys',SimContKey.keys)
if SimContKey.keys != None:  # we had a response
    thisExp.addData('SimContKey.rt', SimContKey.rt)
thisExp.addData('SimContKey.started', SimContKey.tStartRefresh)
thisExp.addData('SimContKey.stopped', SimContKey.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Countdown"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
CountdownComponents = [No3, No2, No1]
for thisComponent in CountdownComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
CountdownClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Countdown"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = CountdownClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=CountdownClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *No3* updates
    if No3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        No3.frameNStart = frameN  # exact frame index
        No3.tStart = t  # local t and not account for scr refresh
        No3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(No3, 'tStartRefresh')  # time at next scr refresh
        No3.setAutoDraw(True)
    if No3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > No3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            No3.tStop = t  # not accounting for scr refresh
            No3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(No3, 'tStopRefresh')  # time at next scr refresh
            No3.setAutoDraw(False)
    
    # *No2* updates
    if No2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        No2.frameNStart = frameN  # exact frame index
        No2.tStart = t  # local t and not account for scr refresh
        No2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(No2, 'tStartRefresh')  # time at next scr refresh
        No2.setAutoDraw(True)
    if No2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > No2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            No2.tStop = t  # not accounting for scr refresh
            No2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(No2, 'tStopRefresh')  # time at next scr refresh
            No2.setAutoDraw(False)
    
    # *No1* updates
    if No1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        No1.frameNStart = frameN  # exact frame index
        No1.tStart = t  # local t and not account for scr refresh
        No1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(No1, 'tStartRefresh')  # time at next scr refresh
        No1.setAutoDraw(True)
    if No1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > No1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            No1.tStop = t  # not accounting for scr refresh
            No1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(No1, 'tStopRefresh')  # time at next scr refresh
            No1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CountdownComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Countdown"-------
for thisComponent in CountdownComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('No3.started', No3.tStartRefresh)
thisExp.addData('No3.stopped', No3.tStopRefresh)
thisExp.addData('No2.started', No2.tStartRefresh)
thisExp.addData('No2.stopped', No2.tStopRefresh)
thisExp.addData('No1.started', No1.tStartRefresh)
thisExp.addData('No1.stopped', No1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
SimilarityRating = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Similarity_trials.xlsx', selection='0:83'),
    seed=None, name='SimilarityRating')
thisExp.addLoop(SimilarityRating)  # add the loop to the experiment
thisSimilarityRating = SimilarityRating.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSimilarityRating.rgb)
if thisSimilarityRating != None:
    for paramName in thisSimilarityRating:
        exec('{} = thisSimilarityRating[paramName]'.format(paramName))

for thisSimilarityRating in SimilarityRating:
    currentLoop = SimilarityRating
    # abbreviate parameter names if possible (e.g. rgb = thisSimilarityRating.rgb)
    if thisSimilarityRating != None:
        for paramName in thisSimilarityRating:
            exec('{} = thisSimilarityRating[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Count3"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Count3Components = [Cross1Sec]
    for thisComponent in Count3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Count3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Count3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Count3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Count3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Cross1Sec* updates
        if Cross1Sec.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Cross1Sec.frameNStart = frameN  # exact frame index
            Cross1Sec.tStart = t  # local t and not account for scr refresh
            Cross1Sec.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cross1Sec, 'tStartRefresh')  # time at next scr refresh
            Cross1Sec.setAutoDraw(True)
        if Cross1Sec.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cross1Sec.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Cross1Sec.tStop = t  # not accounting for scr refresh
                Cross1Sec.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Cross1Sec, 'tStopRefresh')  # time at next scr refresh
                Cross1Sec.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Count3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Count3"-------
    for thisComponent in Count3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SimilarityRating.addData('Cross1Sec.started', Cross1Sec.tStartRefresh)
    SimilarityRating.addData('Cross1Sec.stopped', Cross1Sec.tStopRefresh)
    
    # ------Prepare to start Routine "SimilarityPresentation"-------
    continueRoutine = True
    # update component parameters for each repeat
    simcount += 1
    simcounter = str(simcount) + "/83"
    FirstSound.setSound(Sound1, hamming=True)
    FirstSound.setVolume(1, log=False)
    SecondSound.setSound(Sound2, hamming=True)
    SecondSound.setVolume(1, log=False)
    SimTrialNumber.setText(simcounter)
    # keep track of which components have finished
    SimilarityPresentationComponents = [FirstSound, SecondSound, Cross, NumberOne, NumberTwo, SimTrialNumber]
    for thisComponent in SimilarityPresentationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SimilarityPresentationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SimilarityPresentation"-------
    while continueRoutine:
        # get current time
        t = SimilarityPresentationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SimilarityPresentationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop FirstSound
        if FirstSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FirstSound.frameNStart = frameN  # exact frame index
            FirstSound.tStart = t  # local t and not account for scr refresh
            FirstSound.tStartRefresh = tThisFlipGlobal  # on global time
            FirstSound.play(when=win)  # sync with win flip
        # start/stop SecondSound
        if SecondSound.status == NOT_STARTED and tThisFlip >= FirstSound.getDuration() + 1.0-frameTolerance:
            # keep track of start time/frame for later
            SecondSound.frameNStart = frameN  # exact frame index
            SecondSound.tStart = t  # local t and not account for scr refresh
            SecondSound.tStartRefresh = tThisFlipGlobal  # on global time
            SecondSound.play(when=win)  # sync with win flip
        
        # *Cross* updates
        if Cross.status == NOT_STARTED and tThisFlip >= FirstSound.getDuration()-frameTolerance:
            # keep track of start time/frame for later
            Cross.frameNStart = frameN  # exact frame index
            Cross.tStart = t  # local t and not account for scr refresh
            Cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cross, 'tStartRefresh')  # time at next scr refresh
            Cross.setAutoDraw(True)
        if Cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cross.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Cross.tStop = t  # not accounting for scr refresh
                Cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Cross, 'tStopRefresh')  # time at next scr refresh
                Cross.setAutoDraw(False)
        
        # *NumberOne* updates
        if NumberOne.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NumberOne.frameNStart = frameN  # exact frame index
            NumberOne.tStart = t  # local t and not account for scr refresh
            NumberOne.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NumberOne, 'tStartRefresh')  # time at next scr refresh
            NumberOne.setAutoDraw(True)
        if NumberOne.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NumberOne.tStartRefresh + FirstSound.getDuration()-frameTolerance:
                # keep track of stop time/frame for later
                NumberOne.tStop = t  # not accounting for scr refresh
                NumberOne.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NumberOne, 'tStopRefresh')  # time at next scr refresh
                NumberOne.setAutoDraw(False)
        
        # *NumberTwo* updates
        if NumberTwo.status == NOT_STARTED and tThisFlip >= FirstSound.getDuration() + 1.0-frameTolerance:
            # keep track of start time/frame for later
            NumberTwo.frameNStart = frameN  # exact frame index
            NumberTwo.tStart = t  # local t and not account for scr refresh
            NumberTwo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NumberTwo, 'tStartRefresh')  # time at next scr refresh
            NumberTwo.setAutoDraw(True)
        if NumberTwo.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NumberTwo.tStartRefresh + SecondSound.getDuration()-frameTolerance:
                # keep track of stop time/frame for later
                NumberTwo.tStop = t  # not accounting for scr refresh
                NumberTwo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NumberTwo, 'tStopRefresh')  # time at next scr refresh
                NumberTwo.setAutoDraw(False)
        
        # *SimTrialNumber* updates
        if SimTrialNumber.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SimTrialNumber.frameNStart = frameN  # exact frame index
            SimTrialNumber.tStart = t  # local t and not account for scr refresh
            SimTrialNumber.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SimTrialNumber, 'tStartRefresh')  # time at next scr refresh
            SimTrialNumber.setAutoDraw(True)
        if SimTrialNumber.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > SimTrialNumber.tStartRefresh + FirstSound.getDuration() + 1 + SecondSound.getDuration()-frameTolerance:
                # keep track of stop time/frame for later
                SimTrialNumber.tStop = t  # not accounting for scr refresh
                SimTrialNumber.frameNStop = frameN  # exact frame index
                win.timeOnFlip(SimTrialNumber, 'tStopRefresh')  # time at next scr refresh
                SimTrialNumber.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SimilarityPresentationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SimilarityPresentation"-------
    for thisComponent in SimilarityPresentationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    FirstSound.stop()  # ensure sound has stopped at end of routine
    SimilarityRating.addData('FirstSound.started', FirstSound.tStartRefresh)
    SimilarityRating.addData('FirstSound.stopped', FirstSound.tStopRefresh)
    SecondSound.stop()  # ensure sound has stopped at end of routine
    SimilarityRating.addData('SecondSound.started', SecondSound.tStartRefresh)
    SimilarityRating.addData('SecondSound.stopped', SecondSound.tStopRefresh)
    SimilarityRating.addData('Cross.started', Cross.tStartRefresh)
    SimilarityRating.addData('Cross.stopped', Cross.tStopRefresh)
    SimilarityRating.addData('NumberOne.started', NumberOne.tStartRefresh)
    SimilarityRating.addData('NumberOne.stopped', NumberOne.tStopRefresh)
    SimilarityRating.addData('NumberTwo.started', NumberTwo.tStartRefresh)
    SimilarityRating.addData('NumberTwo.stopped', NumberTwo.tStopRefresh)
    SimilarityRating.addData('SimTrialNumber.started', SimTrialNumber.tStartRefresh)
    SimilarityRating.addData('SimTrialNumber.stopped', SimTrialNumber.tStopRefresh)
    # the Routine "SimilarityPresentation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "SimlarityResponse"-------
    continueRoutine = True
    # update component parameters for each repeat
    SimilarityRatingKey.keys = []
    SimilarityRatingKey.rt = []
    _SimilarityRatingKey_allKeys = []
    # keep track of which components have finished
    SimlarityResponseComponents = [SimilarityRatingScale, SimilarityRatingKey]
    for thisComponent in SimlarityResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SimlarityResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SimlarityResponse"-------
    while continueRoutine:
        # get current time
        t = SimlarityResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SimlarityResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *SimilarityRatingScale* updates
        if SimilarityRatingScale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SimilarityRatingScale.frameNStart = frameN  # exact frame index
            SimilarityRatingScale.tStart = t  # local t and not account for scr refresh
            SimilarityRatingScale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SimilarityRatingScale, 'tStartRefresh')  # time at next scr refresh
            SimilarityRatingScale.setAutoDraw(True)
        
        # *SimilarityRatingKey* updates
        waitOnFlip = False
        if SimilarityRatingKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SimilarityRatingKey.frameNStart = frameN  # exact frame index
            SimilarityRatingKey.tStart = t  # local t and not account for scr refresh
            SimilarityRatingKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SimilarityRatingKey, 'tStartRefresh')  # time at next scr refresh
            SimilarityRatingKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(SimilarityRatingKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(SimilarityRatingKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if SimilarityRatingKey.status == STARTED and not waitOnFlip:
            theseKeys = SimilarityRatingKey.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _SimilarityRatingKey_allKeys.extend(theseKeys)
            if len(_SimilarityRatingKey_allKeys):
                SimilarityRatingKey.keys = _SimilarityRatingKey_allKeys[-1].name  # just the last key pressed
                SimilarityRatingKey.rt = _SimilarityRatingKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SimlarityResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SimlarityResponse"-------
    for thisComponent in SimlarityResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SimilarityRating.addData('SimilarityRatingScale.started', SimilarityRatingScale.tStartRefresh)
    SimilarityRating.addData('SimilarityRatingScale.stopped', SimilarityRatingScale.tStopRefresh)
    # check responses
    if SimilarityRatingKey.keys in ['', [], None]:  # No response was made
        SimilarityRatingKey.keys = None
    SimilarityRating.addData('SimilarityRatingKey.keys',SimilarityRatingKey.keys)
    if SimilarityRatingKey.keys != None:  # we had a response
        SimilarityRating.addData('SimilarityRatingKey.rt', SimilarityRatingKey.rt)
    SimilarityRating.addData('SimilarityRatingKey.started', SimilarityRatingKey.tStartRefresh)
    SimilarityRating.addData('SimilarityRatingKey.stopped', SimilarityRatingKey.tStopRefresh)
    # the Routine "SimlarityResponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'SimilarityRating'


# ------Prepare to start Routine "End1"-------
continueRoutine = True
# update component parameters for each repeat
End1Cont.keys = []
End1Cont.rt = []
_End1Cont_allKeys = []
# keep track of which components have finished
End1Components = [EndMssg, End1Cont]
for thisComponent in End1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
End1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End1"-------
while continueRoutine:
    # get current time
    t = End1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=End1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndMssg* updates
    if EndMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndMssg.frameNStart = frameN  # exact frame index
        EndMssg.tStart = t  # local t and not account for scr refresh
        EndMssg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndMssg, 'tStartRefresh')  # time at next scr refresh
        EndMssg.setAutoDraw(True)
    
    # *End1Cont* updates
    waitOnFlip = False
    if End1Cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        End1Cont.frameNStart = frameN  # exact frame index
        End1Cont.tStart = t  # local t and not account for scr refresh
        End1Cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End1Cont, 'tStartRefresh')  # time at next scr refresh
        End1Cont.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(End1Cont.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(End1Cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if End1Cont.status == STARTED and not waitOnFlip:
        theseKeys = End1Cont.getKeys(keyList=['space'], waitRelease=False)
        _End1Cont_allKeys.extend(theseKeys)
        if len(_End1Cont_allKeys):
            End1Cont.keys = _End1Cont_allKeys[-1].name  # just the last key pressed
            End1Cont.rt = _End1Cont_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End1"-------
for thisComponent in End1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndMssg.started', EndMssg.tStartRefresh)
thisExp.addData('EndMssg.stopped', EndMssg.tStopRefresh)
# check responses
if End1Cont.keys in ['', [], None]:  # No response was made
    End1Cont.keys = None
thisExp.addData('End1Cont.keys',End1Cont.keys)
if End1Cont.keys != None:  # we had a response
    thisExp.addData('End1Cont.rt', End1Cont.rt)
thisExp.addData('End1Cont.started', End1Cont.tStartRefresh)
thisExp.addData('End1Cont.stopped', End1Cont.tStopRefresh)
thisExp.nextEntry()
# the Routine "End1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Welcome4"-------
continueRoutine = True
# update component parameters for each repeat
Welcome4End.keys = []
Welcome4End.rt = []
_Welcome4End_allKeys = []
# keep track of which components have finished
Welcome4Components = [Task4Slide, Welcome4End]
for thisComponent in Welcome4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Welcome4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome4"-------
while continueRoutine:
    # get current time
    t = Welcome4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Welcome4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Task4Slide* updates
    if Task4Slide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Task4Slide.frameNStart = frameN  # exact frame index
        Task4Slide.tStart = t  # local t and not account for scr refresh
        Task4Slide.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Task4Slide, 'tStartRefresh')  # time at next scr refresh
        Task4Slide.setAutoDraw(True)
    
    # *Welcome4End* updates
    waitOnFlip = False
    if Welcome4End.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome4End.frameNStart = frameN  # exact frame index
        Welcome4End.tStart = t  # local t and not account for scr refresh
        Welcome4End.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome4End, 'tStartRefresh')  # time at next scr refresh
        Welcome4End.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Welcome4End.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Welcome4End.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Welcome4End.status == STARTED and not waitOnFlip:
        theseKeys = Welcome4End.getKeys(keyList=['space'], waitRelease=False)
        _Welcome4End_allKeys.extend(theseKeys)
        if len(_Welcome4End_allKeys):
            Welcome4End.keys = _Welcome4End_allKeys[-1].name  # just the last key pressed
            Welcome4End.rt = _Welcome4End_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome4"-------
for thisComponent in Welcome4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Task4Slide.started', Task4Slide.tStartRefresh)
thisExp.addData('Task4Slide.stopped', Task4Slide.tStopRefresh)
# check responses
if Welcome4End.keys in ['', [], None]:  # No response was made
    Welcome4End.keys = None
thisExp.addData('Welcome4End.keys',Welcome4End.keys)
if Welcome4End.keys != None:  # we had a response
    thisExp.addData('Welcome4End.rt', Welcome4End.rt)
thisExp.addData('Welcome4End.started', Welcome4End.tStartRefresh)
thisExp.addData('Welcome4End.stopped', Welcome4End.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
SoundLabelLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Similarity_trials.xlsx', selection='83:171'),
    seed=None, name='SoundLabelLoop')
thisExp.addLoop(SoundLabelLoop)  # add the loop to the experiment
thisSoundLabelLoop = SoundLabelLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSoundLabelLoop.rgb)
if thisSoundLabelLoop != None:
    for paramName in thisSoundLabelLoop:
        exec('{} = thisSoundLabelLoop[paramName]'.format(paramName))

for thisSoundLabelLoop in SoundLabelLoop:
    currentLoop = SoundLabelLoop
    # abbreviate parameter names if possible (e.g. rgb = thisSoundLabelLoop.rgb)
    if thisSoundLabelLoop != None:
        for paramName in thisSoundLabelLoop:
            exec('{} = thisSoundLabelLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Count3"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Count3Components = [Cross1Sec]
    for thisComponent in Count3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Count3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Count3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Count3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Count3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Cross1Sec* updates
        if Cross1Sec.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Cross1Sec.frameNStart = frameN  # exact frame index
            Cross1Sec.tStart = t  # local t and not account for scr refresh
            Cross1Sec.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cross1Sec, 'tStartRefresh')  # time at next scr refresh
            Cross1Sec.setAutoDraw(True)
        if Cross1Sec.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cross1Sec.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Cross1Sec.tStop = t  # not accounting for scr refresh
                Cross1Sec.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Cross1Sec, 'tStopRefresh')  # time at next scr refresh
                Cross1Sec.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Count3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Count3"-------
    for thisComponent in Count3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SoundLabelLoop.addData('Cross1Sec.started', Cross1Sec.tStartRefresh)
    SoundLabelLoop.addData('Cross1Sec.stopped', Cross1Sec.tStopRefresh)
    
    # ------Prepare to start Routine "SoundLabeling"-------
    continueRoutine = True
    # update component parameters for each repeat
    Sound.setSound(Sound1, hamming=True)
    Sound.setVolume(1, log=False)
    LabelingKey.keys = []
    LabelingKey.rt = []
    _LabelingKey_allKeys = []
    # keep track of which components have finished
    SoundLabelingComponents = [SoundLabelQuestion, Sound, LabelingKey]
    for thisComponent in SoundLabelingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SoundLabelingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SoundLabeling"-------
    while continueRoutine:
        # get current time
        t = SoundLabelingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SoundLabelingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *SoundLabelQuestion* updates
        if SoundLabelQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SoundLabelQuestion.frameNStart = frameN  # exact frame index
            SoundLabelQuestion.tStart = t  # local t and not account for scr refresh
            SoundLabelQuestion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SoundLabelQuestion, 'tStartRefresh')  # time at next scr refresh
            SoundLabelQuestion.setAutoDraw(True)
        # start/stop Sound
        if Sound.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Sound.frameNStart = frameN  # exact frame index
            Sound.tStart = t  # local t and not account for scr refresh
            Sound.tStartRefresh = tThisFlipGlobal  # on global time
            Sound.play(when=win)  # sync with win flip
        
        # *LabelingKey* updates
        waitOnFlip = False
        if LabelingKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LabelingKey.frameNStart = frameN  # exact frame index
            LabelingKey.tStart = t  # local t and not account for scr refresh
            LabelingKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LabelingKey, 'tStartRefresh')  # time at next scr refresh
            LabelingKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(LabelingKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(LabelingKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if LabelingKey.status == STARTED and not waitOnFlip:
            theseKeys = LabelingKey.getKeys(keyList=['space'], waitRelease=False)
            _LabelingKey_allKeys.extend(theseKeys)
            if len(_LabelingKey_allKeys):
                LabelingKey.keys = _LabelingKey_allKeys[-1].name  # just the last key pressed
                LabelingKey.rt = _LabelingKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SoundLabelingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SoundLabeling"-------
    for thisComponent in SoundLabelingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SoundLabelLoop.addData('SoundLabelQuestion.started', SoundLabelQuestion.tStartRefresh)
    SoundLabelLoop.addData('SoundLabelQuestion.stopped', SoundLabelQuestion.tStopRefresh)
    Sound.stop()  # ensure sound has stopped at end of routine
    SoundLabelLoop.addData('Sound.started', Sound.tStartRefresh)
    SoundLabelLoop.addData('Sound.stopped', Sound.tStopRefresh)
    # check responses
    if LabelingKey.keys in ['', [], None]:  # No response was made
        LabelingKey.keys = None
    SoundLabelLoop.addData('LabelingKey.keys',LabelingKey.keys)
    if LabelingKey.keys != None:  # we had a response
        SoundLabelLoop.addData('LabelingKey.rt', LabelingKey.rt)
    SoundLabelLoop.addData('LabelingKey.started', LabelingKey.tStartRefresh)
    SoundLabelLoop.addData('LabelingKey.stopped', LabelingKey.tStopRefresh)
    # the Routine "SoundLabeling" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'SoundLabelLoop'


# ------Prepare to start Routine "End1"-------
continueRoutine = True
# update component parameters for each repeat
End1Cont.keys = []
End1Cont.rt = []
_End1Cont_allKeys = []
# keep track of which components have finished
End1Components = [EndMssg, End1Cont]
for thisComponent in End1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
End1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End1"-------
while continueRoutine:
    # get current time
    t = End1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=End1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndMssg* updates
    if EndMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndMssg.frameNStart = frameN  # exact frame index
        EndMssg.tStart = t  # local t and not account for scr refresh
        EndMssg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndMssg, 'tStartRefresh')  # time at next scr refresh
        EndMssg.setAutoDraw(True)
    
    # *End1Cont* updates
    waitOnFlip = False
    if End1Cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        End1Cont.frameNStart = frameN  # exact frame index
        End1Cont.tStart = t  # local t and not account for scr refresh
        End1Cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End1Cont, 'tStartRefresh')  # time at next scr refresh
        End1Cont.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(End1Cont.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(End1Cont.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if End1Cont.status == STARTED and not waitOnFlip:
        theseKeys = End1Cont.getKeys(keyList=['space'], waitRelease=False)
        _End1Cont_allKeys.extend(theseKeys)
        if len(_End1Cont_allKeys):
            End1Cont.keys = _End1Cont_allKeys[-1].name  # just the last key pressed
            End1Cont.rt = _End1Cont_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End1"-------
for thisComponent in End1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndMssg.started', EndMssg.tStartRefresh)
thisExp.addData('EndMssg.stopped', EndMssg.tStopRefresh)
# check responses
if End1Cont.keys in ['', [], None]:  # No response was made
    End1Cont.keys = None
thisExp.addData('End1Cont.keys',End1Cont.keys)
if End1Cont.keys != None:  # we had a response
    thisExp.addData('End1Cont.rt', End1Cont.rt)
thisExp.addData('End1Cont.started', End1Cont.tStartRefresh)
thisExp.addData('End1Cont.stopped', End1Cont.tStopRefresh)
thisExp.nextEntry()
# the Routine "End1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
