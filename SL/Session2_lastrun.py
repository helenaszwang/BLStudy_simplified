#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on December 20, 2022, at 21:39
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'AL'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
}
# --- Show participant info dialog --
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
    originPath='C:\\Users\\wangs\\OneDrive - The University of Western Ontario\\Desktop\\ProjectBL\\BLStudy\\Session2\\Session2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1504, 1003], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Welcome0" ---
Welcome0Mssg = visual.TextStim(win=win, name='Welcome0Mssg',
    text='Welcome to the experiment!',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Welcome0Continue = keyboard.Keyboard()

# --- Initialize components for Routine "HeadphonePlay" ---
CheckSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='CheckSound')
CheckSound.setVolume(1)
CheckTxt = visual.TextStim(win=win, name='CheckTxt',
    text='Which tone was the quietest?\n(Press the corresponding number on your keyboard)\n\n1 = First  2 = Second  3 = Third',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
CheckResp = keyboard.Keyboard()
TrialNumber = visual.TextStim(win=win, name='TrialNumber',
    text='',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
# Run 'Begin Experiment' code from code_5
counter = 1
checkcount = str(counter) + "/6"
Cross2 = visual.TextStim(win=win, name='Cross2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "HeadphoneFeedback" ---
FeedbackMssg = visual.TextStim(win=win, name='FeedbackMssg',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "SLWelcome" ---
WelcomeMssg = visual.TextStim(win=win, name='WelcomeMssg',
    text='Researchers from ZZZ University have recently collected some recordings of an alien speech from another planet. The speech consists of syllables that sound similar to English. The researchers need your help to study this speech. \n\nYou will first listen to a 6-minute recording of this speech and then complete three different tasks. In total, the study will take approximately 35 minutes to complete. You will be able to take short breaks in between tasks. ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ContinueButton = keyboard.Keyboard()

# --- Initialize components for Routine "ExposurePrep" ---
# Run 'Begin Experiment' code from selectcondition
# Choose the scrambling condition file
import random
c = random.randint(1, 3)
c = 1
cond = str(c) # Used as the file for the PlayTD loop


ExposureIntro = visual.TextStim(win=win, name='ExposureIntro',
    text='First, we will play a recording of this alien speech for 6 minutes with a short break every 2 minutes. \n\nThe recording is a little broken and the speech will stop playing from time to time. Please help the researchers mark the broken parts by pressing SPACE whenever the speech stops.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ExposureIntroKey = keyboard.Keyboard()

# --- Initialize components for Routine "Exposure" ---
# Run 'Begin Experiment' code from SoundCounter
scounter = 0
takebreak = 0
pausecheck = 0
# Run 'Begin Experiment' code from ExposureVolume
volume0 = 1
volumecounter0 = 0
ExposurePlay = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='ExposurePlay')
ExposurePlay.setVolume(1.0)
ExposureCross = visual.TextStim(win=win, name='ExposureCross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ExposureInstruction = visual.TextStim(win=win, name='ExposureInstruction',
    text='Press SPACE as soon as you can when the speech stops',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Pause" ---
PauseCheckKey = keyboard.Keyboard()
PauseCross = visual.TextStim(win=win, name='PauseCross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
PauseInstruction = visual.TextStim(win=win, name='PauseInstruction',
    text='Press SPACE as soon as you can when the speech stops',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "TakeABreak" ---
BreakRespSubmit = keyboard.Keyboard()
BreakTxt = visual.TextStim(win=win, name='BreakTxt',
    text="Let's take a break.\n\n\nHow many different syllables do you think were in the speech? Click the box below to type your response.\n(Press ENTER to submit your answer)",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
BreakResponse = visual.TextBox2(
     win, text='', font='Arial',
     pos=(0, -0.2),     letterHeight=0.03,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None, alignment='center',
     anchor='center',
     fillColor='white', borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='BreakResponse',
     autoLog=True,
)

# --- Initialize components for Routine "CallExperimenter" ---
CallExperimentertxt = visual.TextStim(win=win, name='CallExperimentertxt',
    text='Thank you! Please inform the experimenter that you have finished this part.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ExperimenterKey = keyboard.Keyboard()

# --- Initialize components for Routine "Part1Intro" ---
WelcomeTxt2 = visual.TextStim(win=win, name='WelcomeTxt2',
    text="In the next part, you will complete different tasks using your experience with the alien speech.\n\nFirst, the researchers would like you to mark the timing of when each syllable appears in the speech.\n\nWe will play you 36 short snippets of the speech. At the beginning of each recording, you will be given a 'Target Syllable'. Every time the target syllable appears in the recording, press SPACE as quickly and accurately as you can to record the precise syllable onset time.",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ContinueKey3 = keyboard.Keyboard()
# Run 'Begin Experiment' code from RepCount
repeatCount = 0
count = 0




# --- Initialize components for Routine "TDTrainingIntro" ---
TrainingBeginTxt = visual.TextStim(win=win, name='TrainingBeginTxt',
    text='We will begin with a training session using a fake speech created by the researchers.\n\nDuring the training, you will see the number of target syllables you recorded and your average response speed. ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
TrainingContinueKey = keyboard.Keyboard()

# --- Initialize components for Routine "TrainingSample" ---
SampleMssg2 = visual.TextStim(win=win, name='SampleMssg2',
    text='The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
TrainigTarget = visual.TextStim(win=win, name='TrainigTarget',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
# Run 'Begin Experiment' code from TD_trialcount
trainingcount = 0
TrainingNumber = visual.TextStim(win=win, name='TrainingNumber',
    text='',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
TrainingSampleContinue = visual.TextStim(win=win, name='TrainingSampleContinue',
    text='Press SPACE to listen to this syllable',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
TSContinueKey = keyboard.Keyboard()

# --- Initialize components for Routine "TrainingPlaySample" ---
TrainingSampleSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='TrainingSampleSound')
TrainingSampleSound.setVolume(0.3)
TraingRepeatSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='TraingRepeatSound')
TraingRepeatSound.setVolume(0.3)
TrainTargetTxt = visual.TextStim(win=win, name='TrainTargetTxt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
TrainingBeginSample = visual.TextStim(win=win, name='TrainingBeginSample',
    text='Press SPACE to begin listening',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
TrainingNumber2 = visual.TextStim(win=win, name='TrainingNumber2',
    text='',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
TrainEndSample = keyboard.Keyboard()

# --- Initialize components for Routine "TrainStart" ---
Three = visual.TextStim(win=win, name='Three',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Two = visual.TextStim(win=win, name='Two',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text = visual.TextStim(win=win, name='text',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "train" ---
# Run 'Begin Experiment' code from getRT_train
respOnset = 0 
TargetOnset = 0 # Target sound onset
previousOnset = 0 
respcount = 0 # Number of "hits"
TrainRT = 0 # Sum of all RTs

mytimer = core.Clock()
TDTrainSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='TDTrainSound')
TDTrainSound.setVolume(0.3)
TrainResp = keyboard.Keyboard()
TDTrainTxt = visual.TextStim(win=win, name='TDTrainTxt',
    text='\n\n\n\nPress SPACE as quickly as possible when you hear the target syllable',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Cross3 = visual.TextStim(win=win, name='Cross3',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Pause1sec" ---
PauseTxt2 = visual.TextStim(win=win, name='PauseTxt2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "TDTrainFeedback" ---
TDTrainFeedbackMssg = visual.TextStim(win=win, name='TDTrainFeedbackMssg',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
EndFeedback = keyboard.Keyboard()
TrainingContinue = visual.TextStim(win=win, name='TrainingContinue',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "P1IntroII" ---
P1Intro2Txt = visual.TextStim(win=win, name='P1Intro2Txt',
    text="Great job! \nLet's now work with the actual speech. Remember to try your best to press SPACE at the same time as the target syllable onset.\nThere will be no feedback given this time. \n\n\nThere are 36 recordings in total. You may take a short break at the beginning of each recording if you wish.",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='Press SPACE to begin',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()
# Run 'Begin Experiment' code from TD_randomize
partone = "0"
parttwo = "0"
partthree = "0"
OccurenceC = 1


# --- Initialize components for Routine "SampleIntro" ---
TargetMssg = visual.TextStim(win=win, name='TargetMssg',
    text='The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
PlayTargetKey = keyboard.Keyboard()
TargetTxt = visual.TextStim(win=win, name='TargetTxt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
# Run 'Begin Experiment' code from Count
repeatCount = 0
TrialNoTxt = visual.TextStim(win=win, name='TrialNoTxt',
    text='',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ContinueTxt4 = visual.TextStim(win=win, name='ContinueTxt4',
    text='Press SPACE to hear the syllable',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "PlaySample" ---
EndPlay = keyboard.Keyboard()
SyllableSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='SyllableSound')
SyllableSound.setVolume(1.0)
Repeat = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='Repeat')
Repeat.setVolume(1)
SoundTxt = visual.TextStim(win=win, name='SoundTxt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ContinueKey2 = visual.TextStim(win=win, name='ContinueKey2',
    text='Press SPACE to begin',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
TrialNoTxt2 = visual.TextStim(win=win, name='TrialNoTxt2',
    text='',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "TDStart" ---
Countdown1 = visual.TextStim(win=win, name='Countdown1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "trial_separate" ---
# Run 'Begin Experiment' code from TargetandRespTime
respOnsetP = 0 
respcountP = 0
previousOnsetP = 0
TargetOnsetP = 0 # Target sound onset
hit = 0
mytimerP = core.Clock()
PlaySound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='PlaySound')
PlaySound.setVolume(1)
PlayText = visual.TextStim(win=win, name='PlayText',
    text='\n\n\n\nPress SPACE as quickly as possible when you hear the target syllable',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
PlayResp = keyboard.Keyboard()
TargetSoundTxt = visual.TextStim(win=win, name='TargetSoundTxt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Pause1sec" ---
PauseTxt2 = visual.TextStim(win=win, name='PauseTxt2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "AddRespCountCode" ---

# --- Initialize components for Routine "OccurrenceCounter" ---

# --- Initialize components for Routine "SampleIntro" ---
TargetMssg = visual.TextStim(win=win, name='TargetMssg',
    text='The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
PlayTargetKey = keyboard.Keyboard()
TargetTxt = visual.TextStim(win=win, name='TargetTxt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
# Run 'Begin Experiment' code from Count
repeatCount = 0
TrialNoTxt = visual.TextStim(win=win, name='TrialNoTxt',
    text='',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ContinueTxt4 = visual.TextStim(win=win, name='ContinueTxt4',
    text='Press SPACE to hear the syllable',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "PlaySample" ---
EndPlay = keyboard.Keyboard()
SyllableSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='SyllableSound')
SyllableSound.setVolume(1.0)
Repeat = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='Repeat')
Repeat.setVolume(1)
SoundTxt = visual.TextStim(win=win, name='SoundTxt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ContinueKey2 = visual.TextStim(win=win, name='ContinueKey2',
    text='Press SPACE to begin',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
TrialNoTxt2 = visual.TextStim(win=win, name='TrialNoTxt2',
    text='',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "TDStart" ---
Countdown1 = visual.TextStim(win=win, name='Countdown1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "trial_separate" ---
# Run 'Begin Experiment' code from TargetandRespTime
respOnsetP = 0 
respcountP = 0
previousOnsetP = 0
TargetOnsetP = 0 # Target sound onset
hit = 0
mytimerP = core.Clock()
PlaySound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='PlaySound')
PlaySound.setVolume(1)
PlayText = visual.TextStim(win=win, name='PlayText',
    text='\n\n\n\nPress SPACE as quickly as possible when you hear the target syllable',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
PlayResp = keyboard.Keyboard()
TargetSoundTxt = visual.TextStim(win=win, name='TargetSoundTxt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Pause1sec" ---
PauseTxt2 = visual.TextStim(win=win, name='PauseTxt2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "AddRespCountCode" ---

# --- Initialize components for Routine "OccurrenceCounter" ---

# --- Initialize components for Routine "SampleIntro" ---
TargetMssg = visual.TextStim(win=win, name='TargetMssg',
    text='The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
PlayTargetKey = keyboard.Keyboard()
TargetTxt = visual.TextStim(win=win, name='TargetTxt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
# Run 'Begin Experiment' code from Count
repeatCount = 0
TrialNoTxt = visual.TextStim(win=win, name='TrialNoTxt',
    text='',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ContinueTxt4 = visual.TextStim(win=win, name='ContinueTxt4',
    text='Press SPACE to hear the syllable',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "PlaySample" ---
EndPlay = keyboard.Keyboard()
SyllableSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='SyllableSound')
SyllableSound.setVolume(1.0)
Repeat = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='Repeat')
Repeat.setVolume(1)
SoundTxt = visual.TextStim(win=win, name='SoundTxt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ContinueKey2 = visual.TextStim(win=win, name='ContinueKey2',
    text='Press SPACE to begin',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
TrialNoTxt2 = visual.TextStim(win=win, name='TrialNoTxt2',
    text='',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "TDStart" ---
Countdown1 = visual.TextStim(win=win, name='Countdown1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "trial_separate" ---
# Run 'Begin Experiment' code from TargetandRespTime
respOnsetP = 0 
respcountP = 0
previousOnsetP = 0
TargetOnsetP = 0 # Target sound onset
hit = 0
mytimerP = core.Clock()
PlaySound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='PlaySound')
PlaySound.setVolume(1)
PlayText = visual.TextStim(win=win, name='PlayText',
    text='\n\n\n\nPress SPACE as quickly as possible when you hear the target syllable',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
PlayResp = keyboard.Keyboard()
TargetSoundTxt = visual.TextStim(win=win, name='TargetSoundTxt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "Pause1sec" ---
PauseTxt2 = visual.TextStim(win=win, name='PauseTxt2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "AddRespCountCode" ---

# --- Initialize components for Routine "CallExperimenter" ---
CallExperimentertxt = visual.TextStim(win=win, name='CallExperimentertxt',
    text='Thank you! Please inform the experimenter that you have finished this part.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ExperimenterKey = keyboard.Keyboard()

# --- Initialize components for Routine "P2Welcome" ---
P2WelcomeTxt = visual.TextStim(win=win, name='P2WelcomeTxt',
    text="It seems like the alien speech contains regularly repeating 'words'. In the next part of this study, you will be asked to distinguish these alien words from other sounds.",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
P2WelcomeContKey = keyboard.Keyboard()

# --- Initialize components for Routine "FamRatingIntro" ---
FamRateIntroTxt = visual.TextStim(win=win, name='FamRateIntroTxt',
    text='In this part, you will listen to short speech sounds. Some of these may sound familiar to you, as they were spoken in the first part of the study. Others may sound unfamiliar, as they were not spoken in the first part of the study.\n\nYour job is to listen carefully to these short sounds and rate how familiar they sound to you on a scale of 1 (Not familiar) to 4 (Very familiar).\n\nThere will be 12 trials in total.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
FamRateIntroKey = keyboard.Keyboard()

# --- Initialize components for Routine "Pause1sec" ---
PauseTxt2 = visual.TextStim(win=win, name='PauseTxt2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "FamRating" ---
FamRatePrompt = visual.TextStim(win=win, name='FamRatePrompt',
    text='How familiar does this word sound?',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
RatingScale = visual.TextStim(win=win, name='RatingScale',
    text='1 ----------------- 2 ----------------- 3 ----------------- 4',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
RatingScale2 = visual.TextStim(win=win, name='RatingScale2',
    text='\n\n(Not familiar)                                                                     (Very familiar)',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
FamRatingResp = keyboard.Keyboard()
Syllab1 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Syllab1')
Syllab1.setVolume(1)
Syllab2 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Syllab2')
Syllab2.setVolume(1)
Syllab3 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Syllab3')
Syllab3.setVolume(1)

# --- Initialize components for Routine "Part2Intro2" ---
P2IntroTxt2 = visual.TextStim(win=win, name='P2IntroTxt2',
    text='In the next part, you will hear two speech sounds. Your task is to indicate whether the first or the second one sounds like a word from the language you just listened to.\n\nThere will be 16 trials in total.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ContinueKey7 = keyboard.Keyboard()

# --- Initialize components for Routine "count" ---
# Run 'Begin Experiment' code from AFC_trialcount
AFCcount = 0

# --- Initialize components for Routine "AFCStart" ---
QuestionNoTxt = visual.TextStim(win=win, name='QuestionNoTxt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "AFCFirst" ---
Word1No = visual.TextStim(win=win, name='Word1No',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Word_1_1 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Word_1_1')
Word_1_1.setVolume(1)
Word_1_2 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Word_1_2')
Word_1_2.setVolume(1)
Word_1_3 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Word_1_3')
Word_1_3.setVolume(1)

# --- Initialize components for Routine "AFCSecond" ---
Word2No = visual.TextStim(win=win, name='Word2No',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Word_2_1 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Word_2_1')
Word_2_1.setVolume(1)
Word_2_2 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Word_2_2')
Word_2_2.setVolume(1)
Word_2_3 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Word_2_3')
Word_2_3.setVolume(1)

# --- Initialize components for Routine "AFCQuestion" ---
QuestionTxt = visual.TextStim(win=win, name='QuestionTxt',
    text='Which word sounded correct?',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
AFCResp = keyboard.Keyboard()

# --- Initialize components for Routine "HearingCheckIntro" ---
HearingCheckTxt = visual.TextStim(win=win, name='HearingCheckTxt',
    text='Thank you for helping the researchers!\n\nLastly, we will play you a few short speech sounds. In each trial, please select the syllable that matches with the sound you hear.\n\n\n\n\n\nPress SPACE to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
EndKey2 = keyboard.Keyboard()

# --- Initialize components for Routine "Pause1sec" ---
PauseTxt2 = visual.TextStim(win=win, name='PauseTxt2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "HearingCheck" ---
CheckWord = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='CheckWord')
CheckWord.setVolume(1)
WordOptions = visual.TextStim(win=win, name='WordOptions',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
CheckQuestion = visual.TextStim(win=win, name='CheckQuestion',
    text='Which sound did you hear?\n(Press the corresponding number on your keyboard)',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
CheckRespKey = keyboard.Keyboard()

# --- Initialize components for Routine "P2End" ---
EndMssg = visual.TextStim(win=win, name='EndMssg',
    text='You have now completed all the tasks.\nWe appreciate your time and cooporation. \n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
EndAllKey = keyboard.Keyboard()

# --- Initialize components for Routine "Blank" ---
BlankEndKey = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome0" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Welcome0Continue.keys = []
Welcome0Continue.rt = []
_Welcome0Continue_allKeys = []
# keep track of which components have finished
Welcome0Components = [Welcome0Mssg, Welcome0Continue]
for thisComponent in Welcome0Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome0" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome0Mssg* updates
    if Welcome0Mssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome0Mssg.frameNStart = frameN  # exact frame index
        Welcome0Mssg.tStart = t  # local t and not account for scr refresh
        Welcome0Mssg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome0Mssg, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Welcome0Mssg.started')
        Welcome0Mssg.setAutoDraw(True)
    
    # *Welcome0Continue* updates
    waitOnFlip = False
    if Welcome0Continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome0Continue.frameNStart = frameN  # exact frame index
        Welcome0Continue.tStart = t  # local t and not account for scr refresh
        Welcome0Continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome0Continue, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Welcome0Continue.started')
        Welcome0Continue.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Welcome0Continue.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Welcome0Continue.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Welcome0Continue.status == STARTED and not waitOnFlip:
        theseKeys = Welcome0Continue.getKeys(keyList=['space',], waitRelease=False)
        _Welcome0Continue_allKeys.extend(theseKeys)
        if len(_Welcome0Continue_allKeys):
            Welcome0Continue.keys = _Welcome0Continue_allKeys[-1].name  # just the last key pressed
            Welcome0Continue.rt = _Welcome0Continue_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome0Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome0" ---
for thisComponent in Welcome0Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Welcome0Continue.keys in ['', [], None]:  # No response was made
    Welcome0Continue.keys = None
thisExp.addData('Welcome0Continue.keys',Welcome0Continue.keys)
if Welcome0Continue.keys != None:  # we had a response
    thisExp.addData('Welcome0Continue.rt', Welcome0Continue.rt)
thisExp.nextEntry()
# the Routine "Welcome0" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
HeadphoneLoop = data.TrialHandler(nReps=0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Headphone_check.xlsx'),
    seed=None, name='HeadphoneLoop')
thisExp.addLoop(HeadphoneLoop)  # add the loop to the experiment
thisHeadphoneLoop = HeadphoneLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisHeadphoneLoop.rgb)
if thisHeadphoneLoop != None:
    for paramName in thisHeadphoneLoop:
        exec('{} = thisHeadphoneLoop[paramName]'.format(paramName))

for thisHeadphoneLoop in HeadphoneLoop:
    currentLoop = HeadphoneLoop
    # abbreviate parameter names if possible (e.g. rgb = thisHeadphoneLoop.rgb)
    if thisHeadphoneLoop != None:
        for paramName in thisHeadphoneLoop:
            exec('{} = thisHeadphoneLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "HeadphonePlay" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    CheckSound.setSound(File, hamming=True)
    CheckSound.setVolume(1, log=False)
    CheckResp.keys = []
    CheckResp.rt = []
    _CheckResp_allKeys = []
    TrialNumber.setText(checkcount)
    # Run 'Begin Routine' code from code_5
    counter += 1
    checkcount = str(counter) + "/6"
    # keep track of which components have finished
    HeadphonePlayComponents = [CheckSound, CheckTxt, CheckResp, TrialNumber, Cross2]
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
    frameN = -1
    
    # --- Run Routine "HeadphonePlay" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop CheckSound
        if CheckSound.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            CheckSound.frameNStart = frameN  # exact frame index
            CheckSound.tStart = t  # local t and not account for scr refresh
            CheckSound.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('CheckSound.started', tThisFlipGlobal)
            CheckSound.play(when=win)  # sync with win flip
        
        # *CheckTxt* updates
        if CheckTxt.status == NOT_STARTED and tThisFlip >= CheckSound.getDuration() + 0.5-frameTolerance:
            # keep track of start time/frame for later
            CheckTxt.frameNStart = frameN  # exact frame index
            CheckTxt.tStart = t  # local t and not account for scr refresh
            CheckTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CheckTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CheckTxt.started')
            CheckTxt.setAutoDraw(True)
        
        # *CheckResp* updates
        waitOnFlip = False
        if CheckResp.status == NOT_STARTED and tThisFlip >= CheckSound.getDuration() + 0.5-frameTolerance:
            # keep track of start time/frame for later
            CheckResp.frameNStart = frameN  # exact frame index
            CheckResp.tStart = t  # local t and not account for scr refresh
            CheckResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CheckResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CheckResp.started')
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
        
        # *TrialNumber* updates
        if TrialNumber.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrialNumber.frameNStart = frameN  # exact frame index
            TrialNumber.tStart = t  # local t and not account for scr refresh
            TrialNumber.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrialNumber, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TrialNumber.started')
            TrialNumber.setAutoDraw(True)
        if TrialNumber.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > TrialNumber.tStartRefresh + CheckSound.getDuration() + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                TrialNumber.tStop = t  # not accounting for scr refresh
                TrialNumber.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TrialNumber.stopped')
                TrialNumber.setAutoDraw(False)
        
        # *Cross2* updates
        if Cross2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cross2.frameNStart = frameN  # exact frame index
            Cross2.tStart = t  # local t and not account for scr refresh
            Cross2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cross2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Cross2.started')
            Cross2.setAutoDraw(True)
        if Cross2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cross2.tStartRefresh + CheckSound.getDuration() + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Cross2.tStop = t  # not accounting for scr refresh
                Cross2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Cross2.stopped')
                Cross2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in HeadphonePlayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "HeadphonePlay" ---
    for thisComponent in HeadphonePlayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    CheckSound.stop()  # ensure sound has stopped at end of routine
    # check responses
    if CheckResp.keys in ['', [], None]:  # No response was made
        CheckResp.keys = None
        # was no response the correct answer?!
        if str(Correct).lower() == 'none':
           CheckResp.corr = 1;  # correct non-response
        else:
           CheckResp.corr = 0;  # failed to respond (incorrectly)
    # store data for HeadphoneLoop (TrialHandler)
    HeadphoneLoop.addData('CheckResp.keys',CheckResp.keys)
    HeadphoneLoop.addData('CheckResp.corr', CheckResp.corr)
    if CheckResp.keys != None:  # we had a response
        HeadphoneLoop.addData('CheckResp.rt', CheckResp.rt)
    # Run 'End Routine' code from code_5
    if CheckResp.corr == 1:
        message = "CORRECT"
    else:
        message = "INCORRECT"
    # the Routine "HeadphonePlay" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "HeadphoneFeedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    FeedbackMssg.setText(message)
    # keep track of which components have finished
    HeadphoneFeedbackComponents = [FeedbackMssg]
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
    frameN = -1
    
    # --- Run Routine "HeadphoneFeedback" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FeedbackMssg* updates
        if FeedbackMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FeedbackMssg.frameNStart = frameN  # exact frame index
            FeedbackMssg.tStart = t  # local t and not account for scr refresh
            FeedbackMssg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FeedbackMssg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FeedbackMssg.started')
            FeedbackMssg.setAutoDraw(True)
        if FeedbackMssg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FeedbackMssg.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                FeedbackMssg.tStop = t  # not accounting for scr refresh
                FeedbackMssg.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FeedbackMssg.stopped')
                FeedbackMssg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in HeadphoneFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "HeadphoneFeedback" ---
    for thisComponent in HeadphoneFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 0 repeats of 'HeadphoneLoop'


# --- Prepare to start Routine "SLWelcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ContinueButton.keys = []
ContinueButton.rt = []
_ContinueButton_allKeys = []
# keep track of which components have finished
SLWelcomeComponents = [WelcomeMssg, ContinueButton]
for thisComponent in SLWelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "SLWelcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeMssg* updates
    if WelcomeMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeMssg.frameNStart = frameN  # exact frame index
        WelcomeMssg.tStart = t  # local t and not account for scr refresh
        WelcomeMssg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeMssg, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'WelcomeMssg.started')
        WelcomeMssg.setAutoDraw(True)
    
    # *ContinueButton* updates
    waitOnFlip = False
    if ContinueButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueButton.frameNStart = frameN  # exact frame index
        ContinueButton.tStart = t  # local t and not account for scr refresh
        ContinueButton.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueButton, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ContinueButton.started')
        ContinueButton.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ContinueButton.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ContinueButton.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ContinueButton.status == STARTED and not waitOnFlip:
        theseKeys = ContinueButton.getKeys(keyList=['space'], waitRelease=False)
        _ContinueButton_allKeys.extend(theseKeys)
        if len(_ContinueButton_allKeys):
            ContinueButton.keys = _ContinueButton_allKeys[-1].name  # just the last key pressed
            ContinueButton.rt = _ContinueButton_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SLWelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "SLWelcome" ---
for thisComponent in SLWelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ContinueButton.keys in ['', [], None]:  # No response was made
    ContinueButton.keys = None
thisExp.addData('ContinueButton.keys',ContinueButton.keys)
if ContinueButton.keys != None:  # we had a response
    thisExp.addData('ContinueButton.rt', ContinueButton.rt)
thisExp.nextEntry()
# the Routine "SLWelcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "ExposurePrep" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ExposureIntroKey.keys = []
ExposureIntroKey.rt = []
_ExposureIntroKey_allKeys = []
# keep track of which components have finished
ExposurePrepComponents = [ExposureIntro, ExposureIntroKey]
for thisComponent in ExposurePrepComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ExposurePrep" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ExposureIntro* updates
    if ExposureIntro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ExposureIntro.frameNStart = frameN  # exact frame index
        ExposureIntro.tStart = t  # local t and not account for scr refresh
        ExposureIntro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ExposureIntro, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ExposureIntro.started')
        ExposureIntro.setAutoDraw(True)
    
    # *ExposureIntroKey* updates
    waitOnFlip = False
    if ExposureIntroKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ExposureIntroKey.frameNStart = frameN  # exact frame index
        ExposureIntroKey.tStart = t  # local t and not account for scr refresh
        ExposureIntroKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ExposureIntroKey, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ExposureIntroKey.started')
        ExposureIntroKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ExposureIntroKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ExposureIntroKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ExposureIntroKey.status == STARTED and not waitOnFlip:
        theseKeys = ExposureIntroKey.getKeys(keyList=['space'], waitRelease=False)
        _ExposureIntroKey_allKeys.extend(theseKeys)
        if len(_ExposureIntroKey_allKeys):
            ExposureIntroKey.keys = _ExposureIntroKey_allKeys[-1].name  # just the last key pressed
            ExposureIntroKey.rt = _ExposureIntroKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExposurePrepComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ExposurePrep" ---
for thisComponent in ExposurePrepComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ExposureIntroKey.keys in ['', [], None]:  # No response was made
    ExposureIntroKey.keys = None
thisExp.addData('ExposureIntroKey.keys',ExposureIntroKey.keys)
if ExposureIntroKey.keys != None:  # we had a response
    thisExp.addData('ExposureIntroKey.rt', ExposureIntroKey.rt)
thisExp.nextEntry()
# the Routine "ExposurePrep" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ExposureLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(cond + "_exposure.xlsx", selection='0:1080'),
    seed=None, name='ExposureLoop')
thisExp.addLoop(ExposureLoop)  # add the loop to the experiment
thisExposureLoop = ExposureLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExposureLoop.rgb)
if thisExposureLoop != None:
    for paramName in thisExposureLoop:
        exec('{} = thisExposureLoop[paramName]'.format(paramName))

for thisExposureLoop in ExposureLoop:
    currentLoop = ExposureLoop
    # abbreviate parameter names if possible (e.g. rgb = thisExposureLoop.rgb)
    if thisExposureLoop != None:
        for paramName in thisExposureLoop:
            exec('{} = thisExposureLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Exposure" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from SoundCounter
    scounter += 1
    
    if scounter == 123 or scounter == 267:
        pausecheck = 1
    else:
        pausecheck = 0
    
    if scounter == 360: #Restart counting every two minutes
        takebreak = 1
        scounter = 0
        volumecounter0 = 0
    else:
        takebreak = 0
    # Run 'Begin Routine' code from ExposureVolume
    volumecounter0 += 1
    if volumecounter0 == 1 or volumecounter0 == 360:
        volume0 = 0.03
    elif volumecounter0 == 2 or volumecounter0 == 359:
        volume0 = 0.06
    elif volumecounter0 == 3 or volumecounter0 == 358:
        volume0 = 0.09
    elif volumecounter0 == 4 or volumecounter0 == 357:
        volume0 = 0.2
    elif volumecounter0 == 5 or volumecounter0 == 356:
        volume0 = 0.3
    elif volumecounter0 == 6 or volumecounter0 == 355:
        volume0 = 0.5
    else:
        volume0 = 1
    ExposurePlay.setSound(SyllableFile, hamming=True)
    ExposurePlay.setVolume(volume0, log=False)
    # keep track of which components have finished
    ExposureComponents = [ExposurePlay, ExposureCross, ExposureInstruction]
    for thisComponent in ExposureComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Exposure" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop ExposurePlay
        if ExposurePlay.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ExposurePlay.frameNStart = frameN  # exact frame index
            ExposurePlay.tStart = t  # local t and not account for scr refresh
            ExposurePlay.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('ExposurePlay.started', tThisFlipGlobal)
            ExposurePlay.play(when=win)  # sync with win flip
        
        # *ExposureCross* updates
        if ExposureCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ExposureCross.frameNStart = frameN  # exact frame index
            ExposureCross.tStart = t  # local t and not account for scr refresh
            ExposureCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExposureCross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExposureCross.started')
            ExposureCross.setAutoDraw(True)
        if ExposureCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ExposureCross.tStartRefresh + 0.38-frameTolerance:
                # keep track of stop time/frame for later
                ExposureCross.tStop = t  # not accounting for scr refresh
                ExposureCross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ExposureCross.stopped')
                ExposureCross.setAutoDraw(False)
        
        # *ExposureInstruction* updates
        if ExposureInstruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ExposureInstruction.frameNStart = frameN  # exact frame index
            ExposureInstruction.tStart = t  # local t and not account for scr refresh
            ExposureInstruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ExposureInstruction, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ExposureInstruction.started')
            ExposureInstruction.setAutoDraw(True)
        if ExposureInstruction.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ExposureInstruction.tStartRefresh + 0.38-frameTolerance:
                # keep track of stop time/frame for later
                ExposureInstruction.tStop = t  # not accounting for scr refresh
                ExposureInstruction.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ExposureInstruction.stopped')
                ExposureInstruction.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ExposureComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Exposure" ---
    for thisComponent in ExposureComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ExposurePlay.stop()  # ensure sound has stopped at end of routine
    # the Routine "Exposure" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    PauseOnOff = data.TrialHandler(nReps=pausecheck, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='PauseOnOff')
    thisExp.addLoop(PauseOnOff)  # add the loop to the experiment
    thisPauseOnOff = PauseOnOff.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPauseOnOff.rgb)
    if thisPauseOnOff != None:
        for paramName in thisPauseOnOff:
            exec('{} = thisPauseOnOff[paramName]'.format(paramName))
    
    for thisPauseOnOff in PauseOnOff:
        currentLoop = PauseOnOff
        # abbreviate parameter names if possible (e.g. rgb = thisPauseOnOff.rgb)
        if thisPauseOnOff != None:
            for paramName in thisPauseOnOff:
                exec('{} = thisPauseOnOff[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Pause" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        PauseCheckKey.keys = []
        PauseCheckKey.rt = []
        _PauseCheckKey_allKeys = []
        # keep track of which components have finished
        PauseComponents = [PauseCheckKey, PauseCross, PauseInstruction]
        for thisComponent in PauseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Pause" ---
        while continueRoutine and routineTimer.getTime() < 15.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *PauseCheckKey* updates
            waitOnFlip = False
            if PauseCheckKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PauseCheckKey.frameNStart = frameN  # exact frame index
                PauseCheckKey.tStart = t  # local t and not account for scr refresh
                PauseCheckKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PauseCheckKey, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PauseCheckKey.started')
                PauseCheckKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(PauseCheckKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(PauseCheckKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if PauseCheckKey.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > PauseCheckKey.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    PauseCheckKey.tStop = t  # not accounting for scr refresh
                    PauseCheckKey.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PauseCheckKey.stopped')
                    PauseCheckKey.status = FINISHED
            if PauseCheckKey.status == STARTED and not waitOnFlip:
                theseKeys = PauseCheckKey.getKeys(keyList=['space',], waitRelease=False)
                _PauseCheckKey_allKeys.extend(theseKeys)
                if len(_PauseCheckKey_allKeys):
                    PauseCheckKey.keys = _PauseCheckKey_allKeys[-1].name  # just the last key pressed
                    PauseCheckKey.rt = _PauseCheckKey_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *PauseCross* updates
            if PauseCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PauseCross.frameNStart = frameN  # exact frame index
                PauseCross.tStart = t  # local t and not account for scr refresh
                PauseCross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PauseCross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PauseCross.started')
                PauseCross.setAutoDraw(True)
            if PauseCross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > PauseCross.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    PauseCross.tStop = t  # not accounting for scr refresh
                    PauseCross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PauseCross.stopped')
                    PauseCross.setAutoDraw(False)
            
            # *PauseInstruction* updates
            if PauseInstruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PauseInstruction.frameNStart = frameN  # exact frame index
                PauseInstruction.tStart = t  # local t and not account for scr refresh
                PauseInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PauseInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PauseInstruction.started')
                PauseInstruction.setAutoDraw(True)
            if PauseInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > PauseInstruction.tStartRefresh + 15-frameTolerance:
                    # keep track of stop time/frame for later
                    PauseInstruction.tStop = t  # not accounting for scr refresh
                    PauseInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PauseInstruction.stopped')
                    PauseInstruction.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PauseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Pause" ---
        for thisComponent in PauseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if PauseCheckKey.keys in ['', [], None]:  # No response was made
            PauseCheckKey.keys = None
        PauseOnOff.addData('PauseCheckKey.keys',PauseCheckKey.keys)
        if PauseCheckKey.keys != None:  # we had a response
            PauseOnOff.addData('PauseCheckKey.rt', PauseCheckKey.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-15.000000)
        thisExp.nextEntry()
        
    # completed pausecheck repeats of 'PauseOnOff'
    
    
    # set up handler to look after randomisation of conditions etc
    BreakOnOff = data.TrialHandler(nReps=takebreak, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='BreakOnOff')
    thisExp.addLoop(BreakOnOff)  # add the loop to the experiment
    thisBreakOnOff = BreakOnOff.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBreakOnOff.rgb)
    if thisBreakOnOff != None:
        for paramName in thisBreakOnOff:
            exec('{} = thisBreakOnOff[paramName]'.format(paramName))
    
    for thisBreakOnOff in BreakOnOff:
        currentLoop = BreakOnOff
        # abbreviate parameter names if possible (e.g. rgb = thisBreakOnOff.rgb)
        if thisBreakOnOff != None:
            for paramName in thisBreakOnOff:
                exec('{} = thisBreakOnOff[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "TakeABreak" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        BreakRespSubmit.keys = []
        BreakRespSubmit.rt = []
        _BreakRespSubmit_allKeys = []
        BreakResponse.reset()
        BreakResponse.setText(' \n')
        # keep track of which components have finished
        TakeABreakComponents = [BreakRespSubmit, BreakTxt, BreakResponse]
        for thisComponent in TakeABreakComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TakeABreak" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *BreakRespSubmit* updates
            waitOnFlip = False
            if BreakRespSubmit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BreakRespSubmit.frameNStart = frameN  # exact frame index
                BreakRespSubmit.tStart = t  # local t and not account for scr refresh
                BreakRespSubmit.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BreakRespSubmit, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BreakRespSubmit.started')
                BreakRespSubmit.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(BreakRespSubmit.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(BreakRespSubmit.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if BreakRespSubmit.status == STARTED and not waitOnFlip:
                theseKeys = BreakRespSubmit.getKeys(keyList=['return'], waitRelease=False)
                _BreakRespSubmit_allKeys.extend(theseKeys)
                if len(_BreakRespSubmit_allKeys):
                    BreakRespSubmit.keys = _BreakRespSubmit_allKeys[-1].name  # just the last key pressed
                    BreakRespSubmit.rt = _BreakRespSubmit_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *BreakTxt* updates
            if BreakTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BreakTxt.frameNStart = frameN  # exact frame index
                BreakTxt.tStart = t  # local t and not account for scr refresh
                BreakTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BreakTxt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BreakTxt.started')
                BreakTxt.setAutoDraw(True)
            
            # *BreakResponse* updates
            if BreakResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BreakResponse.frameNStart = frameN  # exact frame index
                BreakResponse.tStart = t  # local t and not account for scr refresh
                BreakResponse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BreakResponse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'BreakResponse.started')
                BreakResponse.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TakeABreakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TakeABreak" ---
        for thisComponent in TakeABreakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if BreakRespSubmit.keys in ['', [], None]:  # No response was made
            BreakRespSubmit.keys = None
        BreakOnOff.addData('BreakRespSubmit.keys',BreakRespSubmit.keys)
        if BreakRespSubmit.keys != None:  # we had a response
            BreakOnOff.addData('BreakRespSubmit.rt', BreakRespSubmit.rt)
        BreakOnOff.addData('BreakResponse.text',BreakResponse.text)
        # the Routine "TakeABreak" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed takebreak repeats of 'BreakOnOff'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'ExposureLoop'


# --- Prepare to start Routine "CallExperimenter" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ExperimenterKey.keys = []
ExperimenterKey.rt = []
_ExperimenterKey_allKeys = []
# keep track of which components have finished
CallExperimenterComponents = [CallExperimentertxt, ExperimenterKey]
for thisComponent in CallExperimenterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "CallExperimenter" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CallExperimentertxt* updates
    if CallExperimentertxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        CallExperimentertxt.frameNStart = frameN  # exact frame index
        CallExperimentertxt.tStart = t  # local t and not account for scr refresh
        CallExperimentertxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(CallExperimentertxt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'CallExperimentertxt.started')
        CallExperimentertxt.setAutoDraw(True)
    
    # *ExperimenterKey* updates
    waitOnFlip = False
    if ExperimenterKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ExperimenterKey.frameNStart = frameN  # exact frame index
        ExperimenterKey.tStart = t  # local t and not account for scr refresh
        ExperimenterKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ExperimenterKey, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ExperimenterKey.started')
        ExperimenterKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ExperimenterKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ExperimenterKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ExperimenterKey.status == STARTED and not waitOnFlip:
        theseKeys = ExperimenterKey.getKeys(keyList=['0'], waitRelease=False)
        _ExperimenterKey_allKeys.extend(theseKeys)
        if len(_ExperimenterKey_allKeys):
            ExperimenterKey.keys = _ExperimenterKey_allKeys[-1].name  # just the last key pressed
            ExperimenterKey.rt = _ExperimenterKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CallExperimenterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "CallExperimenter" ---
for thisComponent in CallExperimenterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "CallExperimenter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Part1Intro" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ContinueKey3.keys = []
ContinueKey3.rt = []
_ContinueKey3_allKeys = []
# keep track of which components have finished
Part1IntroComponents = [WelcomeTxt2, ContinueKey3]
for thisComponent in Part1IntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Part1Intro" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeTxt2* updates
    if WelcomeTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeTxt2.frameNStart = frameN  # exact frame index
        WelcomeTxt2.tStart = t  # local t and not account for scr refresh
        WelcomeTxt2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeTxt2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'WelcomeTxt2.started')
        WelcomeTxt2.setAutoDraw(True)
    
    # *ContinueKey3* updates
    waitOnFlip = False
    if ContinueKey3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueKey3.frameNStart = frameN  # exact frame index
        ContinueKey3.tStart = t  # local t and not account for scr refresh
        ContinueKey3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueKey3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ContinueKey3.started')
        ContinueKey3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ContinueKey3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ContinueKey3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ContinueKey3.status == STARTED and not waitOnFlip:
        theseKeys = ContinueKey3.getKeys(keyList=['space'], waitRelease=False)
        _ContinueKey3_allKeys.extend(theseKeys)
        if len(_ContinueKey3_allKeys):
            ContinueKey3.keys = _ContinueKey3_allKeys[-1].name  # just the last key pressed
            ContinueKey3.rt = _ContinueKey3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part1IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Part1Intro" ---
for thisComponent in Part1IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ContinueKey3.keys in ['', [], None]:  # No response was made
    ContinueKey3.keys = None
thisExp.addData('ContinueKey3.keys',ContinueKey3.keys)
if ContinueKey3.keys != None:  # we had a response
    thisExp.addData('ContinueKey3.rt', ContinueKey3.rt)
thisExp.nextEntry()
# the Routine "Part1Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "TDTrainingIntro" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
TrainingContinueKey.keys = []
TrainingContinueKey.rt = []
_TrainingContinueKey_allKeys = []
# keep track of which components have finished
TDTrainingIntroComponents = [TrainingBeginTxt, TrainingContinueKey]
for thisComponent in TDTrainingIntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "TDTrainingIntro" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TrainingBeginTxt* updates
    if TrainingBeginTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TrainingBeginTxt.frameNStart = frameN  # exact frame index
        TrainingBeginTxt.tStart = t  # local t and not account for scr refresh
        TrainingBeginTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TrainingBeginTxt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TrainingBeginTxt.started')
        TrainingBeginTxt.setAutoDraw(True)
    
    # *TrainingContinueKey* updates
    waitOnFlip = False
    if TrainingContinueKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TrainingContinueKey.frameNStart = frameN  # exact frame index
        TrainingContinueKey.tStart = t  # local t and not account for scr refresh
        TrainingContinueKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TrainingContinueKey, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TrainingContinueKey.started')
        TrainingContinueKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(TrainingContinueKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(TrainingContinueKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if TrainingContinueKey.status == STARTED and not waitOnFlip:
        theseKeys = TrainingContinueKey.getKeys(keyList=['space'], waitRelease=False)
        _TrainingContinueKey_allKeys.extend(theseKeys)
        if len(_TrainingContinueKey_allKeys):
            TrainingContinueKey.keys = _TrainingContinueKey_allKeys[-1].name  # just the last key pressed
            TrainingContinueKey.rt = _TrainingContinueKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TDTrainingIntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "TDTrainingIntro" ---
for thisComponent in TDTrainingIntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if TrainingContinueKey.keys in ['', [], None]:  # No response was made
    TrainingContinueKey.keys = None
thisExp.addData('TrainingContinueKey.keys',TrainingContinueKey.keys)
if TrainingContinueKey.keys != None:  # we had a response
    thisExp.addData('TrainingContinueKey.rt', TrainingContinueKey.rt)
thisExp.nextEntry()
# the Routine "TDTrainingIntro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
TrainTDLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TargetSyllables.xlsx', selection='216:218'),
    seed=None, name='TrainTDLoop')
thisExp.addLoop(TrainTDLoop)  # add the loop to the experiment
thisTrainTDLoop = TrainTDLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrainTDLoop.rgb)
if thisTrainTDLoop != None:
    for paramName in thisTrainTDLoop:
        exec('{} = thisTrainTDLoop[paramName]'.format(paramName))

for thisTrainTDLoop in TrainTDLoop:
    currentLoop = TrainTDLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTrainTDLoop.rgb)
    if thisTrainTDLoop != None:
        for paramName in thisTrainTDLoop:
            exec('{} = thisTrainTDLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "TrainingSample" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    TrainigTarget.setText(Target)
    # Run 'Begin Routine' code from TD_trialcount
    trainingcount += 1
    
    TrainingNumber.setText('Training ' + str(trainingcount) )
    TSContinueKey.keys = []
    TSContinueKey.rt = []
    _TSContinueKey_allKeys = []
    # keep track of which components have finished
    TrainingSampleComponents = [SampleMssg2, TrainigTarget, TrainingNumber, TrainingSampleContinue, TSContinueKey]
    for thisComponent in TrainingSampleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "TrainingSample" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *SampleMssg2* updates
        if SampleMssg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SampleMssg2.frameNStart = frameN  # exact frame index
            SampleMssg2.tStart = t  # local t and not account for scr refresh
            SampleMssg2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SampleMssg2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SampleMssg2.started')
            SampleMssg2.setAutoDraw(True)
        
        # *TrainigTarget* updates
        if TrainigTarget.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrainigTarget.frameNStart = frameN  # exact frame index
            TrainigTarget.tStart = t  # local t and not account for scr refresh
            TrainigTarget.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrainigTarget, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TrainigTarget.started')
            TrainigTarget.setAutoDraw(True)
        
        # *TrainingNumber* updates
        if TrainingNumber.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrainingNumber.frameNStart = frameN  # exact frame index
            TrainingNumber.tStart = t  # local t and not account for scr refresh
            TrainingNumber.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrainingNumber, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TrainingNumber.started')
            TrainingNumber.setAutoDraw(True)
        
        # *TrainingSampleContinue* updates
        if TrainingSampleContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrainingSampleContinue.frameNStart = frameN  # exact frame index
            TrainingSampleContinue.tStart = t  # local t and not account for scr refresh
            TrainingSampleContinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrainingSampleContinue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TrainingSampleContinue.started')
            TrainingSampleContinue.setAutoDraw(True)
        
        # *TSContinueKey* updates
        waitOnFlip = False
        if TSContinueKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TSContinueKey.frameNStart = frameN  # exact frame index
            TSContinueKey.tStart = t  # local t and not account for scr refresh
            TSContinueKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TSContinueKey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TSContinueKey.started')
            TSContinueKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(TSContinueKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(TSContinueKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if TSContinueKey.status == STARTED and not waitOnFlip:
            theseKeys = TSContinueKey.getKeys(keyList=['space'], waitRelease=False)
            _TSContinueKey_allKeys.extend(theseKeys)
            if len(_TSContinueKey_allKeys):
                TSContinueKey.keys = _TSContinueKey_allKeys[-1].name  # just the last key pressed
                TSContinueKey.rt = _TSContinueKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrainingSampleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "TrainingSample" ---
    for thisComponent in TrainingSampleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if TSContinueKey.keys in ['', [], None]:  # No response was made
        TSContinueKey.keys = None
    TrainTDLoop.addData('TSContinueKey.keys',TSContinueKey.keys)
    if TSContinueKey.keys != None:  # we had a response
        TrainTDLoop.addData('TSContinueKey.rt', TSContinueKey.rt)
    # the Routine "TrainingSample" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "TrainingPlaySample" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    TrainingSampleSound.setSound(TargetFile, hamming=True)
    TrainingSampleSound.setVolume(0.3, log=False)
    TraingRepeatSound.setSound(TargetFile, hamming=True)
    TraingRepeatSound.setVolume(0.3, log=False)
    TrainTargetTxt.setText(Target)
    TrainingNumber2.setText('Training ' + str(trainingcount) )
    TrainEndSample.keys = []
    TrainEndSample.rt = []
    _TrainEndSample_allKeys = []
    # keep track of which components have finished
    TrainingPlaySampleComponents = [TrainingSampleSound, TraingRepeatSound, TrainTargetTxt, text_5, TrainingBeginSample, TrainingNumber2, TrainEndSample]
    for thisComponent in TrainingPlaySampleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "TrainingPlaySample" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop TrainingSampleSound
        if TrainingSampleSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrainingSampleSound.frameNStart = frameN  # exact frame index
            TrainingSampleSound.tStart = t  # local t and not account for scr refresh
            TrainingSampleSound.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('TrainingSampleSound.started', tThisFlipGlobal)
            TrainingSampleSound.play(when=win)  # sync with win flip
        # start/stop TraingRepeatSound
        if TraingRepeatSound.status == NOT_STARTED and tThisFlip >= TrainingSampleSound.getDuration() + 1-frameTolerance:
            # keep track of start time/frame for later
            TraingRepeatSound.frameNStart = frameN  # exact frame index
            TraingRepeatSound.tStart = t  # local t and not account for scr refresh
            TraingRepeatSound.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('TraingRepeatSound.started', tThisFlipGlobal)
            TraingRepeatSound.play(when=win)  # sync with win flip
        
        # *TrainTargetTxt* updates
        if TrainTargetTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrainTargetTxt.frameNStart = frameN  # exact frame index
            TrainTargetTxt.tStart = t  # local t and not account for scr refresh
            TrainTargetTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrainTargetTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TrainTargetTxt.started')
            TrainTargetTxt.setAutoDraw(True)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            text_5.setAutoDraw(True)
        
        # *TrainingBeginSample* updates
        if TrainingBeginSample.status == NOT_STARTED and tThisFlip >= TrainingSampleSound.getDuration() +1-frameTolerance:
            # keep track of start time/frame for later
            TrainingBeginSample.frameNStart = frameN  # exact frame index
            TrainingBeginSample.tStart = t  # local t and not account for scr refresh
            TrainingBeginSample.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrainingBeginSample, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TrainingBeginSample.started')
            TrainingBeginSample.setAutoDraw(True)
        
        # *TrainingNumber2* updates
        if TrainingNumber2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrainingNumber2.frameNStart = frameN  # exact frame index
            TrainingNumber2.tStart = t  # local t and not account for scr refresh
            TrainingNumber2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrainingNumber2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TrainingNumber2.started')
            TrainingNumber2.setAutoDraw(True)
        
        # *TrainEndSample* updates
        waitOnFlip = False
        if TrainEndSample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrainEndSample.frameNStart = frameN  # exact frame index
            TrainEndSample.tStart = t  # local t and not account for scr refresh
            TrainEndSample.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrainEndSample, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TrainEndSample.started')
            TrainEndSample.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(TrainEndSample.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(TrainEndSample.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if TrainEndSample.status == STARTED and not waitOnFlip:
            theseKeys = TrainEndSample.getKeys(keyList=['space'], waitRelease=False)
            _TrainEndSample_allKeys.extend(theseKeys)
            if len(_TrainEndSample_allKeys):
                TrainEndSample.keys = _TrainEndSample_allKeys[-1].name  # just the last key pressed
                TrainEndSample.rt = _TrainEndSample_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrainingPlaySampleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "TrainingPlaySample" ---
    for thisComponent in TrainingPlaySampleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    TrainingSampleSound.stop()  # ensure sound has stopped at end of routine
    TraingRepeatSound.stop()  # ensure sound has stopped at end of routine
    # check responses
    if TrainEndSample.keys in ['', [], None]:  # No response was made
        TrainEndSample.keys = None
    TrainTDLoop.addData('TrainEndSample.keys',TrainEndSample.keys)
    if TrainEndSample.keys != None:  # we had a response
        TrainTDLoop.addData('TrainEndSample.rt', TrainEndSample.rt)
    # the Routine "TrainingPlaySample" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "TrainStart" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    TrainStartComponents = [Three, Two, text]
    for thisComponent in TrainStartComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "TrainStart" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Three* updates
        if Three.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Three.frameNStart = frameN  # exact frame index
            Three.tStart = t  # local t and not account for scr refresh
            Three.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Three, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Three.started')
            Three.setAutoDraw(True)
        if Three.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Three.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Three.tStop = t  # not accounting for scr refresh
                Three.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Three.stopped')
                Three.setAutoDraw(False)
        
        # *Two* updates
        if Two.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            Two.frameNStart = frameN  # exact frame index
            Two.tStart = t  # local t and not account for scr refresh
            Two.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Two, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Two.started')
            Two.setAutoDraw(True)
        if Two.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Two.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Two.tStop = t  # not accounting for scr refresh
                Two.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Two.stopped')
                Two.setAutoDraw(False)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrainStartComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "TrainStart" ---
    for thisComponent in TrainStartComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # set up handler to look after randomisation of conditions etc
    TrainTD = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TDTrainList.xlsx', selection='0:45'),
        seed=None, name='TrainTD')
    thisExp.addLoop(TrainTD)  # add the loop to the experiment
    thisTrainTD = TrainTD.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrainTD.rgb)
    if thisTrainTD != None:
        for paramName in thisTrainTD:
            exec('{} = thisTrainTD[paramName]'.format(paramName))
    
    for thisTrainTD in TrainTD:
        currentLoop = TrainTD
        # abbreviate parameter names if possible (e.g. rgb = thisTrainTD.rgb)
        if thisTrainTD != None:
            for paramName in thisTrainTD:
                exec('{} = thisTrainTD[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "train" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from getRT_train
        if Sound == Target:
            TargetOnset = mytimer.getTime()
        soundOnset = mytimer.getTime()
        
        TDTrainSound.setSound(File, hamming=True)
        TDTrainSound.setVolume(0.3, log=False)
        TrainResp.keys = []
        TrainResp.rt = []
        _TrainResp_allKeys = []
        Cross3.setText(Target)
        # keep track of which components have finished
        trainComponents = [TDTrainSound, TrainResp, TDTrainTxt, Cross3]
        for thisComponent in trainComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "train" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop TDTrainSound
            if TDTrainSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TDTrainSound.frameNStart = frameN  # exact frame index
                TDTrainSound.tStart = t  # local t and not account for scr refresh
                TDTrainSound.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('TDTrainSound.started', tThisFlipGlobal)
                TDTrainSound.play(when=win)  # sync with win flip
            
            # *TrainResp* updates
            waitOnFlip = False
            if TrainResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrainResp.frameNStart = frameN  # exact frame index
                TrainResp.tStart = t  # local t and not account for scr refresh
                TrainResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrainResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TrainResp.started')
                TrainResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(TrainResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(TrainResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if TrainResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > TrainResp.tStartRefresh + TDTrainSound.getDuration()+0.03-frameTolerance:
                    # keep track of stop time/frame for later
                    TrainResp.tStop = t  # not accounting for scr refresh
                    TrainResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'TrainResp.stopped')
                    TrainResp.status = FINISHED
            if TrainResp.status == STARTED and not waitOnFlip:
                theseKeys = TrainResp.getKeys(keyList=['space',], waitRelease=False)
                _TrainResp_allKeys.extend(theseKeys)
                if len(_TrainResp_allKeys):
                    TrainResp.keys = [key.name for key in _TrainResp_allKeys]  # storing all keys
                    TrainResp.rt = [key.rt for key in _TrainResp_allKeys]
            
            # *TDTrainTxt* updates
            if TDTrainTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TDTrainTxt.frameNStart = frameN  # exact frame index
                TDTrainTxt.tStart = t  # local t and not account for scr refresh
                TDTrainTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TDTrainTxt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TDTrainTxt.started')
                TDTrainTxt.setAutoDraw(True)
            if TDTrainTxt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > TDTrainTxt.tStartRefresh + TDTrainSound.getDuration()+0.05-frameTolerance:
                    # keep track of stop time/frame for later
                    TDTrainTxt.tStop = t  # not accounting for scr refresh
                    TDTrainTxt.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'TDTrainTxt.stopped')
                    TDTrainTxt.setAutoDraw(False)
            
            # *Cross3* updates
            if Cross3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Cross3.frameNStart = frameN  # exact frame index
                Cross3.tStart = t  # local t and not account for scr refresh
                Cross3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Cross3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Cross3.started')
                Cross3.setAutoDraw(True)
            if Cross3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Cross3.tStartRefresh + TDTrainSound.getDuration()+0.05-frameTolerance:
                    # keep track of stop time/frame for later
                    Cross3.tStop = t  # not accounting for scr refresh
                    Cross3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Cross3.stopped')
                    Cross3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "train" ---
        for thisComponent in trainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from getRT_train
        # Set Target Onset time
        #if Sound == Target:
        #    TargetOnset = TDTrainSound.tStartRefresh
        TrainTD.addData('TargetOnset', TargetOnset)
        # Check if keyboard has been pressed
        if TrainResp.keys in ['', [], None]:
            TrainResp.keys = None
        if TrainResp.keys != None: # we had a response
            #respOnset = TrainResp.rt[0] + TDTrainSound.tStartRefresh
            respOnset = TrainResp.rt[0] + soundOnset
            TrainTD.addData('RespOnset', respOnset)
            # Check if the response is too close to the previous valid response
            if respOnset - previousOnset > 1.2:
                # Calculate RT
                reactiontime = respOnset - TargetOnset
                TrainTD.addData('ReactionTime', reactiontime)
                # Check if RT is below the cutoff
                if reactiontime < 1.2:
                    # Count it as a valid "hit"
                    respcount += 1
                    # Count the RT toward total RTs
                    TrainRT += reactiontime
                    # Use this as the latest valid response
                    previousOnset = respOnset
        # Calculate the mean RT
        if respcount > 0:
            meanRT = TrainRT/respcount
            TrainTD.addData('mean.rt', meanRT)
        else: # If no response was made
            meanRT = 0
        # If too many responses were made     
        if respcount > 5:
            respcount = 5
            
        TrainTD.addData('RespOnset', respOnset)
        TrainTD.addData('Respcount', respcount)
        
        TDTrainSound.stop()  # ensure sound has stopped at end of routine
        # check responses
        if TrainResp.keys in ['', [], None]:  # No response was made
            TrainResp.keys = None
        TrainTD.addData('TrainResp.keys',TrainResp.keys)
        if TrainResp.keys != None:  # we had a response
            TrainTD.addData('TrainResp.rt', TrainResp.rt)
        # the Routine "train" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'TrainTD'
    
    
    # --- Prepare to start Routine "Pause1sec" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    Pause1secComponents = [PauseTxt2]
    for thisComponent in Pause1secComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Pause1sec" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PauseTxt2* updates
        if PauseTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PauseTxt2.frameNStart = frameN  # exact frame index
            PauseTxt2.tStart = t  # local t and not account for scr refresh
            PauseTxt2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PauseTxt2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PauseTxt2.started')
            PauseTxt2.setAutoDraw(True)
        if PauseTxt2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > PauseTxt2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                PauseTxt2.tStop = t  # not accounting for scr refresh
                PauseTxt2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PauseTxt2.stopped')
                PauseTxt2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pause1secComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Pause1sec" ---
    for thisComponent in Pause1secComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "TDTrainFeedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    TDTrainFeedbackMssg.setText('You correctly responded to ' + str(respcount) + ' of the 5 target syllables. Your average response time was '+ str(round(meanRT, 2)) + 's.'  )
    EndFeedback.keys = []
    EndFeedback.rt = []
    _EndFeedback_allKeys = []
    # keep track of which components have finished
    TDTrainFeedbackComponents = [TDTrainFeedbackMssg, EndFeedback, TrainingContinue]
    for thisComponent in TDTrainFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "TDTrainFeedback" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TDTrainFeedbackMssg* updates
        if TDTrainFeedbackMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TDTrainFeedbackMssg.frameNStart = frameN  # exact frame index
            TDTrainFeedbackMssg.tStart = t  # local t and not account for scr refresh
            TDTrainFeedbackMssg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TDTrainFeedbackMssg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TDTrainFeedbackMssg.started')
            TDTrainFeedbackMssg.setAutoDraw(True)
        
        # *EndFeedback* updates
        waitOnFlip = False
        if EndFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EndFeedback.frameNStart = frameN  # exact frame index
            EndFeedback.tStart = t  # local t and not account for scr refresh
            EndFeedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EndFeedback, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EndFeedback.started')
            EndFeedback.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(EndFeedback.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(EndFeedback.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if EndFeedback.status == STARTED and not waitOnFlip:
            theseKeys = EndFeedback.getKeys(keyList=['space'], waitRelease=False)
            _EndFeedback_allKeys.extend(theseKeys)
            if len(_EndFeedback_allKeys):
                EndFeedback.keys = _EndFeedback_allKeys[-1].name  # just the last key pressed
                EndFeedback.rt = _EndFeedback_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *TrainingContinue* updates
        if TrainingContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrainingContinue.frameNStart = frameN  # exact frame index
            TrainingContinue.tStart = t  # local t and not account for scr refresh
            TrainingContinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrainingContinue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TrainingContinue.started')
            TrainingContinue.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TDTrainFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "TDTrainFeedback" ---
    for thisComponent in TDTrainFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if EndFeedback.keys in ['', [], None]:  # No response was made
        EndFeedback.keys = None
    TrainTDLoop.addData('EndFeedback.keys',EndFeedback.keys)
    if EndFeedback.keys != None:  # we had a response
        TrainTDLoop.addData('EndFeedback.rt', EndFeedback.rt)
    # Run 'End Routine' code from code_10
    respcount = 0
    reactiontime = 0
    TrainRT = 0
    # the Routine "TDTrainFeedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'TrainTDLoop'


# --- Prepare to start Routine "P1IntroII" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# Run 'Begin Routine' code from TD_randomize
if cond == "1":
    partone = "0:12"
    parttwo = "12:24"
    partthree = "24:36"
elif cond == "X":
    partone = "36:48"
    parttwo = "48:60"
    partthree = "60:72"
elif cond == "2":
    partone = "72:84"
    parttwo = "84:96"
    partthree = "96:108"
elif cond == "4":
    partone = "108:120"
    parttwo = "120:132"
    partthree = "132:144"
elif cond == "3":
    partone = "144:156"
    parttwo = "156:168"
    partthree = "168:180"
elif cond == "6":
    partone = "180:192"
    parttwo = "192:204"
    partthree = "204:216"

import random
partlist = [partone, parttwo, partthree]
random.shuffle(partlist)
first = partlist[0] 
second = partlist[1]
third = partlist[2]
    
# keep track of which components have finished
P1IntroIIComponents = [P1Intro2Txt, text_4, key_resp]
for thisComponent in P1IntroIIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "P1IntroII" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *P1Intro2Txt* updates
    if P1Intro2Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P1Intro2Txt.frameNStart = frameN  # exact frame index
        P1Intro2Txt.tStart = t  # local t and not account for scr refresh
        P1Intro2Txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P1Intro2Txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'P1Intro2Txt.started')
        P1Intro2Txt.setAutoDraw(True)
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_4.started')
        text_4.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in P1IntroIIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "P1IntroII" ---
for thisComponent in P1IntroIIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "P1IntroII" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
TD = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='TD')
thisExp.addLoop(TD)  # add the loop to the experiment
thisTD = TD.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTD.rgb)
if thisTD != None:
    for paramName in thisTD:
        exec('{} = thisTD[paramName]'.format(paramName))

for thisTD in TD:
    currentLoop = TD
    # abbreviate parameter names if possible (e.g. rgb = thisTD.rgb)
    if thisTD != None:
        for paramName in thisTD:
            exec('{} = thisTD[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    FirstTDLoop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TargetSyllables.xlsx', selection=first),
        seed=None, name='FirstTDLoop')
    thisExp.addLoop(FirstTDLoop)  # add the loop to the experiment
    thisFirstTDLoop = FirstTDLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFirstTDLoop.rgb)
    if thisFirstTDLoop != None:
        for paramName in thisFirstTDLoop:
            exec('{} = thisFirstTDLoop[paramName]'.format(paramName))
    
    for thisFirstTDLoop in FirstTDLoop:
        currentLoop = FirstTDLoop
        # abbreviate parameter names if possible (e.g. rgb = thisFirstTDLoop.rgb)
        if thisFirstTDLoop != None:
            for paramName in thisFirstTDLoop:
                exec('{} = thisFirstTDLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "SampleIntro" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        PlayTargetKey.keys = []
        PlayTargetKey.rt = []
        _PlayTargetKey_allKeys = []
        TargetTxt.setText(Target)
        # Run 'Begin Routine' code from Count
        repeatCount += 1
        TrialNo = "Recording " + str(repeatCount) + " of 36"
        TrialNoTxt.setText(TrialNo)
        # keep track of which components have finished
        SampleIntroComponents = [TargetMssg, PlayTargetKey, TargetTxt, TrialNoTxt, ContinueTxt4]
        for thisComponent in SampleIntroComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "SampleIntro" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TargetMssg* updates
            if TargetMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TargetMssg.frameNStart = frameN  # exact frame index
                TargetMssg.tStart = t  # local t and not account for scr refresh
                TargetMssg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TargetMssg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TargetMssg.started')
                TargetMssg.setAutoDraw(True)
            
            # *PlayTargetKey* updates
            waitOnFlip = False
            if PlayTargetKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PlayTargetKey.frameNStart = frameN  # exact frame index
                PlayTargetKey.tStart = t  # local t and not account for scr refresh
                PlayTargetKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PlayTargetKey, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PlayTargetKey.started')
                PlayTargetKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(PlayTargetKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(PlayTargetKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if PlayTargetKey.status == STARTED and not waitOnFlip:
                theseKeys = PlayTargetKey.getKeys(keyList=['space'], waitRelease=False)
                _PlayTargetKey_allKeys.extend(theseKeys)
                if len(_PlayTargetKey_allKeys):
                    PlayTargetKey.keys = _PlayTargetKey_allKeys[-1].name  # just the last key pressed
                    PlayTargetKey.rt = _PlayTargetKey_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *TargetTxt* updates
            if TargetTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TargetTxt.frameNStart = frameN  # exact frame index
                TargetTxt.tStart = t  # local t and not account for scr refresh
                TargetTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TargetTxt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TargetTxt.started')
                TargetTxt.setAutoDraw(True)
            
            # *TrialNoTxt* updates
            if TrialNoTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialNoTxt.frameNStart = frameN  # exact frame index
                TrialNoTxt.tStart = t  # local t and not account for scr refresh
                TrialNoTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialNoTxt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TrialNoTxt.started')
                TrialNoTxt.setAutoDraw(True)
            
            # *ContinueTxt4* updates
            if ContinueTxt4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ContinueTxt4.frameNStart = frameN  # exact frame index
                ContinueTxt4.tStart = t  # local t and not account for scr refresh
                ContinueTxt4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueTxt4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ContinueTxt4.started')
                ContinueTxt4.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SampleIntroComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "SampleIntro" ---
        for thisComponent in SampleIntroComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if PlayTargetKey.keys in ['', [], None]:  # No response was made
            PlayTargetKey.keys = None
        FirstTDLoop.addData('PlayTargetKey.keys',PlayTargetKey.keys)
        if PlayTargetKey.keys != None:  # we had a response
            FirstTDLoop.addData('PlayTargetKey.rt', PlayTargetKey.rt)
        # the Routine "SampleIntro" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "PlaySample" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        EndPlay.keys = []
        EndPlay.rt = []
        _EndPlay_allKeys = []
        SyllableSound.setSound(TargetFile, hamming=True)
        SyllableSound.setVolume(1, log=False)
        Repeat.setSound(TargetFile, hamming=True)
        Repeat.setVolume(1, log=False)
        SoundTxt.setText(Target
)
        TrialNoTxt2.setText(TrialNo
)
        # keep track of which components have finished
        PlaySampleComponents = [EndPlay, SyllableSound, Repeat, SoundTxt, ContinueKey2, text_2, TrialNoTxt2]
        for thisComponent in PlaySampleComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "PlaySample" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *EndPlay* updates
            waitOnFlip = False
            if EndPlay.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                # keep track of start time/frame for later
                EndPlay.frameNStart = frameN  # exact frame index
                EndPlay.tStart = t  # local t and not account for scr refresh
                EndPlay.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EndPlay, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EndPlay.started')
                EndPlay.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(EndPlay.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(EndPlay.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if EndPlay.status == STARTED and not waitOnFlip:
                theseKeys = EndPlay.getKeys(keyList=['space',], waitRelease=False)
                _EndPlay_allKeys.extend(theseKeys)
                if len(_EndPlay_allKeys):
                    EndPlay.keys = _EndPlay_allKeys[-1].name  # just the last key pressed
                    EndPlay.rt = _EndPlay_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # start/stop SyllableSound
            if SyllableSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SyllableSound.frameNStart = frameN  # exact frame index
                SyllableSound.tStart = t  # local t and not account for scr refresh
                SyllableSound.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('SyllableSound.started', tThisFlipGlobal)
                SyllableSound.play(when=win)  # sync with win flip
            # start/stop Repeat
            if Repeat.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                # keep track of start time/frame for later
                Repeat.frameNStart = frameN  # exact frame index
                Repeat.tStart = t  # local t and not account for scr refresh
                Repeat.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('Repeat.started', tThisFlipGlobal)
                Repeat.play(when=win)  # sync with win flip
            
            # *SoundTxt* updates
            if SoundTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SoundTxt.frameNStart = frameN  # exact frame index
                SoundTxt.tStart = t  # local t and not account for scr refresh
                SoundTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SoundTxt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SoundTxt.started')
                SoundTxt.setAutoDraw(True)
            
            # *ContinueKey2* updates
            if ContinueKey2.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                # keep track of start time/frame for later
                ContinueKey2.frameNStart = frameN  # exact frame index
                ContinueKey2.tStart = t  # local t and not account for scr refresh
                ContinueKey2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueKey2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ContinueKey2.started')
                ContinueKey2.setAutoDraw(True)
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                text_2.setAutoDraw(True)
            
            # *TrialNoTxt2* updates
            if TrialNoTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialNoTxt2.frameNStart = frameN  # exact frame index
                TrialNoTxt2.tStart = t  # local t and not account for scr refresh
                TrialNoTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialNoTxt2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TrialNoTxt2.started')
                TrialNoTxt2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PlaySampleComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PlaySample" ---
        for thisComponent in PlaySampleComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SyllableSound.stop()  # ensure sound has stopped at end of routine
        Repeat.stop()  # ensure sound has stopped at end of routine
        # the Routine "PlaySample" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "TDStart" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from RandCond
        ## Randomize between 6 randomizations
        opt1 = "0:48" #ta
        opt2 = "48:96" #ta
        opt3 = "96:144" #ta
        opt4 = "144:192" #fe
        opt5 = "192:240" #fe
        opt6 = "240:288" #fe
        opt7 = "288:336" #re
        opt8 = "336:384" #re
        opt9 = "384:432" #re
        opt10 = "432:480" #ru
        opt11 = "480:528" #ru
        opt12 = "528:576" #ru
        
        if Target == "ru" or Target == "pu" or Target == "ni":
            rows = random.choice([opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9])
        elif Target == "re" or Target == "ge" or Target == "me":
            rows = random.choice([opt1, opt2, opt3, opt4, opt5, opt6, opt10, opt11, opt12])
        elif Target == "fe" or Target == "ti" or Target == "su":
            rows = random.choice([opt1, opt2, opt3, opt10, opt11, opt12, opt7, opt8, opt9])
        else:
            rows = random.choice([opt10, opt11, opt12, opt4, opt5, opt6, opt7, opt8, opt9])
        # keep track of which components have finished
        TDStartComponents = [Countdown1]
        for thisComponent in TDStartComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TDStart" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Countdown1* updates
            if Countdown1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Countdown1.frameNStart = frameN  # exact frame index
                Countdown1.tStart = t  # local t and not account for scr refresh
                Countdown1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Countdown1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Countdown1.started')
                Countdown1.setAutoDraw(True)
            if Countdown1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Countdown1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Countdown1.tStop = t  # not accounting for scr refresh
                    Countdown1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Countdown1.stopped')
                    Countdown1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TDStartComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TDStart" ---
        for thisComponent in TDStartComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # set up handler to look after randomisation of conditions etc
        FirstTD = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(cond + "_TD_list.xlsx", selection=rows),
            seed=None, name='FirstTD')
        thisExp.addLoop(FirstTD)  # add the loop to the experiment
        thisFirstTD = FirstTD.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisFirstTD.rgb)
        if thisFirstTD != None:
            for paramName in thisFirstTD:
                exec('{} = thisFirstTD[paramName]'.format(paramName))
        
        for thisFirstTD in FirstTD:
            currentLoop = FirstTD
            # abbreviate parameter names if possible (e.g. rgb = thisFirstTD.rgb)
            if thisFirstTD != None:
                for paramName in thisFirstTD:
                    exec('{} = thisFirstTD[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "trial_separate" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from TargetandRespTime
            if TDSound == Target:
                TargetOnsetP = mytimerP.getTime()
            soundOnsetP = mytimerP.getTime()
            
            
            PlaySound.setSound(TDSoundFile, hamming=True)
            PlaySound.setVolume(1, log=False)
            PlayResp.keys = []
            PlayResp.rt = []
            _PlayResp_allKeys = []
            TargetSoundTxt.setText(Target)
            # keep track of which components have finished
            trial_separateComponents = [PlaySound, PlayText, PlayResp, TargetSoundTxt]
            for thisComponent in trial_separateComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_separate" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # start/stop PlaySound
                if PlaySound.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    PlaySound.frameNStart = frameN  # exact frame index
                    PlaySound.tStart = t  # local t and not account for scr refresh
                    PlaySound.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('PlaySound.started', tThisFlipGlobal)
                    PlaySound.play(when=win)  # sync with win flip
                
                # *PlayText* updates
                if PlayText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    PlayText.frameNStart = frameN  # exact frame index
                    PlayText.tStart = t  # local t and not account for scr refresh
                    PlayText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PlayText, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PlayText.started')
                    PlayText.setAutoDraw(True)
                if PlayText.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > PlayText.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        PlayText.tStop = t  # not accounting for scr refresh
                        PlayText.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'PlayText.stopped')
                        PlayText.setAutoDraw(False)
                
                # *PlayResp* updates
                waitOnFlip = False
                if PlayResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    PlayResp.frameNStart = frameN  # exact frame index
                    PlayResp.tStart = t  # local t and not account for scr refresh
                    PlayResp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PlayResp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PlayResp.started')
                    PlayResp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(PlayResp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(PlayResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if PlayResp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > PlayResp.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        PlayResp.tStop = t  # not accounting for scr refresh
                        PlayResp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'PlayResp.stopped')
                        PlayResp.status = FINISHED
                if PlayResp.status == STARTED and not waitOnFlip:
                    theseKeys = PlayResp.getKeys(keyList=['space',], waitRelease=False)
                    _PlayResp_allKeys.extend(theseKeys)
                    if len(_PlayResp_allKeys):
                        PlayResp.keys = [key.name for key in _PlayResp_allKeys]  # storing all keys
                        PlayResp.rt = [key.rt for key in _PlayResp_allKeys]
                
                # *TargetSoundTxt* updates
                if TargetSoundTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TargetSoundTxt.frameNStart = frameN  # exact frame index
                    TargetSoundTxt.tStart = t  # local t and not account for scr refresh
                    TargetSoundTxt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TargetSoundTxt, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'TargetSoundTxt.started')
                    TargetSoundTxt.setAutoDraw(True)
                if TargetSoundTxt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > TargetSoundTxt.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        TargetSoundTxt.tStop = t  # not accounting for scr refresh
                        TargetSoundTxt.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'TargetSoundTxt.stopped')
                        TargetSoundTxt.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_separateComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_separate" ---
            for thisComponent in trial_separateComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from TargetandRespTime
            # Set Target Onset time
            TD.addData('TargetOnsetP', TargetOnsetP)
            # Check if keyboard has been pressed
            if PlayResp.keys in ['', [], None]:
                PlayResp.keys = None
            if PlayResp.keys != None: # we had a response
                respcountP += 1
                #respOnset = TrainResp.rt[0] + TDTrainSound.tStartRefresh
                respOnsetP = PlayResp.rt[0] + soundOnsetP    
                # Check if the response is too close to the previous valid response
                if respOnsetP - previousOnsetP > 1.2:
                    # Calculate RT
                    reactiontimeP = respOnsetP - TargetOnsetP
                    # Check if RT is below the cutoff
                    if reactiontimeP < 1.2:
                        TD.addData('ReactionTimeP', reactiontimeP)
                        TD.addData('TargetSyllable', Target)
                        TD.addData('TargetPosition', Position)
                        TD.addData('TargetOccurence', OccurenceC)
                        # Count it as a valid "hit"
                        hit += 1
                        # Use this as the latest valid response
                        previousOnsetP = respOnsetP
            
            PlaySound.stop()  # ensure sound has stopped at end of routine
            # check responses
            if PlayResp.keys in ['', [], None]:  # No response was made
                PlayResp.keys = None
            FirstTD.addData('PlayResp.keys',PlayResp.keys)
            if PlayResp.keys != None:  # we had a response
                FirstTD.addData('PlayResp.rt', PlayResp.rt)
            # the Routine "trial_separate" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'FirstTD'
        
        
        # --- Prepare to start Routine "Pause1sec" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        Pause1secComponents = [PauseTxt2]
        for thisComponent in Pause1secComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Pause1sec" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *PauseTxt2* updates
            if PauseTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PauseTxt2.frameNStart = frameN  # exact frame index
                PauseTxt2.tStart = t  # local t and not account for scr refresh
                PauseTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PauseTxt2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PauseTxt2.started')
                PauseTxt2.setAutoDraw(True)
            if PauseTxt2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > PauseTxt2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    PauseTxt2.tStop = t  # not accounting for scr refresh
                    PauseTxt2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PauseTxt2.stopped')
                    PauseTxt2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Pause1secComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Pause1sec" ---
        for thisComponent in Pause1secComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "AddRespCountCode" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        AddRespCountCodeComponents = []
        for thisComponent in AddRespCountCodeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "AddRespCountCode" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AddRespCountCodeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "AddRespCountCode" ---
        for thisComponent in AddRespCountCodeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from AddRespCount
        falsealarm = 0
        hitrate = 0
        if hit != 0:
            falsealarm = 1-(hit/respcountP)
            hitrate = hit/4
        
        TD.addData("RespCountP", respcountP)
        TD.addData("FalseAlarmRate", falsealarm)
        TD.addData("HitRate", hitrate)
        hit = 0
        respcountP = 0
        # the Routine "AddRespCountCode" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'FirstTDLoop'
    
    
    # --- Prepare to start Routine "OccurrenceCounter" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    OccurrenceCounterComponents = []
    for thisComponent in OccurrenceCounterComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "OccurrenceCounter" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in OccurrenceCounterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "OccurrenceCounter" ---
    for thisComponent in OccurrenceCounterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from Block
    OccurenceC += 1
    # the Routine "OccurrenceCounter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    SecondTDLoop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TargetSyllables.xlsx', selection=second),
        seed=None, name='SecondTDLoop')
    thisExp.addLoop(SecondTDLoop)  # add the loop to the experiment
    thisSecondTDLoop = SecondTDLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSecondTDLoop.rgb)
    if thisSecondTDLoop != None:
        for paramName in thisSecondTDLoop:
            exec('{} = thisSecondTDLoop[paramName]'.format(paramName))
    
    for thisSecondTDLoop in SecondTDLoop:
        currentLoop = SecondTDLoop
        # abbreviate parameter names if possible (e.g. rgb = thisSecondTDLoop.rgb)
        if thisSecondTDLoop != None:
            for paramName in thisSecondTDLoop:
                exec('{} = thisSecondTDLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "SampleIntro" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        PlayTargetKey.keys = []
        PlayTargetKey.rt = []
        _PlayTargetKey_allKeys = []
        TargetTxt.setText(Target)
        # Run 'Begin Routine' code from Count
        repeatCount += 1
        TrialNo = "Recording " + str(repeatCount) + " of 36"
        TrialNoTxt.setText(TrialNo)
        # keep track of which components have finished
        SampleIntroComponents = [TargetMssg, PlayTargetKey, TargetTxt, TrialNoTxt, ContinueTxt4]
        for thisComponent in SampleIntroComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "SampleIntro" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TargetMssg* updates
            if TargetMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TargetMssg.frameNStart = frameN  # exact frame index
                TargetMssg.tStart = t  # local t and not account for scr refresh
                TargetMssg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TargetMssg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TargetMssg.started')
                TargetMssg.setAutoDraw(True)
            
            # *PlayTargetKey* updates
            waitOnFlip = False
            if PlayTargetKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PlayTargetKey.frameNStart = frameN  # exact frame index
                PlayTargetKey.tStart = t  # local t and not account for scr refresh
                PlayTargetKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PlayTargetKey, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PlayTargetKey.started')
                PlayTargetKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(PlayTargetKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(PlayTargetKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if PlayTargetKey.status == STARTED and not waitOnFlip:
                theseKeys = PlayTargetKey.getKeys(keyList=['space'], waitRelease=False)
                _PlayTargetKey_allKeys.extend(theseKeys)
                if len(_PlayTargetKey_allKeys):
                    PlayTargetKey.keys = _PlayTargetKey_allKeys[-1].name  # just the last key pressed
                    PlayTargetKey.rt = _PlayTargetKey_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *TargetTxt* updates
            if TargetTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TargetTxt.frameNStart = frameN  # exact frame index
                TargetTxt.tStart = t  # local t and not account for scr refresh
                TargetTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TargetTxt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TargetTxt.started')
                TargetTxt.setAutoDraw(True)
            
            # *TrialNoTxt* updates
            if TrialNoTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialNoTxt.frameNStart = frameN  # exact frame index
                TrialNoTxt.tStart = t  # local t and not account for scr refresh
                TrialNoTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialNoTxt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TrialNoTxt.started')
                TrialNoTxt.setAutoDraw(True)
            
            # *ContinueTxt4* updates
            if ContinueTxt4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ContinueTxt4.frameNStart = frameN  # exact frame index
                ContinueTxt4.tStart = t  # local t and not account for scr refresh
                ContinueTxt4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueTxt4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ContinueTxt4.started')
                ContinueTxt4.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SampleIntroComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "SampleIntro" ---
        for thisComponent in SampleIntroComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if PlayTargetKey.keys in ['', [], None]:  # No response was made
            PlayTargetKey.keys = None
        SecondTDLoop.addData('PlayTargetKey.keys',PlayTargetKey.keys)
        if PlayTargetKey.keys != None:  # we had a response
            SecondTDLoop.addData('PlayTargetKey.rt', PlayTargetKey.rt)
        # the Routine "SampleIntro" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "PlaySample" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        EndPlay.keys = []
        EndPlay.rt = []
        _EndPlay_allKeys = []
        SyllableSound.setSound(TargetFile, hamming=True)
        SyllableSound.setVolume(1, log=False)
        Repeat.setSound(TargetFile, hamming=True)
        Repeat.setVolume(1, log=False)
        SoundTxt.setText(Target
)
        TrialNoTxt2.setText(TrialNo
)
        # keep track of which components have finished
        PlaySampleComponents = [EndPlay, SyllableSound, Repeat, SoundTxt, ContinueKey2, text_2, TrialNoTxt2]
        for thisComponent in PlaySampleComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "PlaySample" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *EndPlay* updates
            waitOnFlip = False
            if EndPlay.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                # keep track of start time/frame for later
                EndPlay.frameNStart = frameN  # exact frame index
                EndPlay.tStart = t  # local t and not account for scr refresh
                EndPlay.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EndPlay, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EndPlay.started')
                EndPlay.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(EndPlay.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(EndPlay.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if EndPlay.status == STARTED and not waitOnFlip:
                theseKeys = EndPlay.getKeys(keyList=['space',], waitRelease=False)
                _EndPlay_allKeys.extend(theseKeys)
                if len(_EndPlay_allKeys):
                    EndPlay.keys = _EndPlay_allKeys[-1].name  # just the last key pressed
                    EndPlay.rt = _EndPlay_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # start/stop SyllableSound
            if SyllableSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SyllableSound.frameNStart = frameN  # exact frame index
                SyllableSound.tStart = t  # local t and not account for scr refresh
                SyllableSound.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('SyllableSound.started', tThisFlipGlobal)
                SyllableSound.play(when=win)  # sync with win flip
            # start/stop Repeat
            if Repeat.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                # keep track of start time/frame for later
                Repeat.frameNStart = frameN  # exact frame index
                Repeat.tStart = t  # local t and not account for scr refresh
                Repeat.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('Repeat.started', tThisFlipGlobal)
                Repeat.play(when=win)  # sync with win flip
            
            # *SoundTxt* updates
            if SoundTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SoundTxt.frameNStart = frameN  # exact frame index
                SoundTxt.tStart = t  # local t and not account for scr refresh
                SoundTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SoundTxt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SoundTxt.started')
                SoundTxt.setAutoDraw(True)
            
            # *ContinueKey2* updates
            if ContinueKey2.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                # keep track of start time/frame for later
                ContinueKey2.frameNStart = frameN  # exact frame index
                ContinueKey2.tStart = t  # local t and not account for scr refresh
                ContinueKey2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueKey2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ContinueKey2.started')
                ContinueKey2.setAutoDraw(True)
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                text_2.setAutoDraw(True)
            
            # *TrialNoTxt2* updates
            if TrialNoTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialNoTxt2.frameNStart = frameN  # exact frame index
                TrialNoTxt2.tStart = t  # local t and not account for scr refresh
                TrialNoTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialNoTxt2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TrialNoTxt2.started')
                TrialNoTxt2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PlaySampleComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PlaySample" ---
        for thisComponent in PlaySampleComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SyllableSound.stop()  # ensure sound has stopped at end of routine
        Repeat.stop()  # ensure sound has stopped at end of routine
        # the Routine "PlaySample" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "TDStart" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from RandCond
        ## Randomize between 6 randomizations
        opt1 = "0:48" #ta
        opt2 = "48:96" #ta
        opt3 = "96:144" #ta
        opt4 = "144:192" #fe
        opt5 = "192:240" #fe
        opt6 = "240:288" #fe
        opt7 = "288:336" #re
        opt8 = "336:384" #re
        opt9 = "384:432" #re
        opt10 = "432:480" #ru
        opt11 = "480:528" #ru
        opt12 = "528:576" #ru
        
        if Target == "ru" or Target == "pu" or Target == "ni":
            rows = random.choice([opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9])
        elif Target == "re" or Target == "ge" or Target == "me":
            rows = random.choice([opt1, opt2, opt3, opt4, opt5, opt6, opt10, opt11, opt12])
        elif Target == "fe" or Target == "ti" or Target == "su":
            rows = random.choice([opt1, opt2, opt3, opt10, opt11, opt12, opt7, opt8, opt9])
        else:
            rows = random.choice([opt10, opt11, opt12, opt4, opt5, opt6, opt7, opt8, opt9])
        # keep track of which components have finished
        TDStartComponents = [Countdown1]
        for thisComponent in TDStartComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TDStart" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Countdown1* updates
            if Countdown1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Countdown1.frameNStart = frameN  # exact frame index
                Countdown1.tStart = t  # local t and not account for scr refresh
                Countdown1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Countdown1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Countdown1.started')
                Countdown1.setAutoDraw(True)
            if Countdown1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Countdown1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Countdown1.tStop = t  # not accounting for scr refresh
                    Countdown1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Countdown1.stopped')
                    Countdown1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TDStartComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TDStart" ---
        for thisComponent in TDStartComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # set up handler to look after randomisation of conditions etc
        SecondTD = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(cond+ "_TD_list.xlsx", selection=rows),
            seed=None, name='SecondTD')
        thisExp.addLoop(SecondTD)  # add the loop to the experiment
        thisSecondTD = SecondTD.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSecondTD.rgb)
        if thisSecondTD != None:
            for paramName in thisSecondTD:
                exec('{} = thisSecondTD[paramName]'.format(paramName))
        
        for thisSecondTD in SecondTD:
            currentLoop = SecondTD
            # abbreviate parameter names if possible (e.g. rgb = thisSecondTD.rgb)
            if thisSecondTD != None:
                for paramName in thisSecondTD:
                    exec('{} = thisSecondTD[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "trial_separate" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from TargetandRespTime
            if TDSound == Target:
                TargetOnsetP = mytimerP.getTime()
            soundOnsetP = mytimerP.getTime()
            
            
            PlaySound.setSound(TDSoundFile, hamming=True)
            PlaySound.setVolume(1, log=False)
            PlayResp.keys = []
            PlayResp.rt = []
            _PlayResp_allKeys = []
            TargetSoundTxt.setText(Target)
            # keep track of which components have finished
            trial_separateComponents = [PlaySound, PlayText, PlayResp, TargetSoundTxt]
            for thisComponent in trial_separateComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_separate" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # start/stop PlaySound
                if PlaySound.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    PlaySound.frameNStart = frameN  # exact frame index
                    PlaySound.tStart = t  # local t and not account for scr refresh
                    PlaySound.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('PlaySound.started', tThisFlipGlobal)
                    PlaySound.play(when=win)  # sync with win flip
                
                # *PlayText* updates
                if PlayText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    PlayText.frameNStart = frameN  # exact frame index
                    PlayText.tStart = t  # local t and not account for scr refresh
                    PlayText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PlayText, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PlayText.started')
                    PlayText.setAutoDraw(True)
                if PlayText.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > PlayText.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        PlayText.tStop = t  # not accounting for scr refresh
                        PlayText.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'PlayText.stopped')
                        PlayText.setAutoDraw(False)
                
                # *PlayResp* updates
                waitOnFlip = False
                if PlayResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    PlayResp.frameNStart = frameN  # exact frame index
                    PlayResp.tStart = t  # local t and not account for scr refresh
                    PlayResp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PlayResp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PlayResp.started')
                    PlayResp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(PlayResp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(PlayResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if PlayResp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > PlayResp.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        PlayResp.tStop = t  # not accounting for scr refresh
                        PlayResp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'PlayResp.stopped')
                        PlayResp.status = FINISHED
                if PlayResp.status == STARTED and not waitOnFlip:
                    theseKeys = PlayResp.getKeys(keyList=['space',], waitRelease=False)
                    _PlayResp_allKeys.extend(theseKeys)
                    if len(_PlayResp_allKeys):
                        PlayResp.keys = [key.name for key in _PlayResp_allKeys]  # storing all keys
                        PlayResp.rt = [key.rt for key in _PlayResp_allKeys]
                
                # *TargetSoundTxt* updates
                if TargetSoundTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TargetSoundTxt.frameNStart = frameN  # exact frame index
                    TargetSoundTxt.tStart = t  # local t and not account for scr refresh
                    TargetSoundTxt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TargetSoundTxt, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'TargetSoundTxt.started')
                    TargetSoundTxt.setAutoDraw(True)
                if TargetSoundTxt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > TargetSoundTxt.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        TargetSoundTxt.tStop = t  # not accounting for scr refresh
                        TargetSoundTxt.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'TargetSoundTxt.stopped')
                        TargetSoundTxt.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_separateComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_separate" ---
            for thisComponent in trial_separateComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from TargetandRespTime
            # Set Target Onset time
            TD.addData('TargetOnsetP', TargetOnsetP)
            # Check if keyboard has been pressed
            if PlayResp.keys in ['', [], None]:
                PlayResp.keys = None
            if PlayResp.keys != None: # we had a response
                respcountP += 1
                #respOnset = TrainResp.rt[0] + TDTrainSound.tStartRefresh
                respOnsetP = PlayResp.rt[0] + soundOnsetP    
                # Check if the response is too close to the previous valid response
                if respOnsetP - previousOnsetP > 1.2:
                    # Calculate RT
                    reactiontimeP = respOnsetP - TargetOnsetP
                    # Check if RT is below the cutoff
                    if reactiontimeP < 1.2:
                        TD.addData('ReactionTimeP', reactiontimeP)
                        TD.addData('TargetSyllable', Target)
                        TD.addData('TargetPosition', Position)
                        TD.addData('TargetOccurence', OccurenceC)
                        # Count it as a valid "hit"
                        hit += 1
                        # Use this as the latest valid response
                        previousOnsetP = respOnsetP
            
            PlaySound.stop()  # ensure sound has stopped at end of routine
            # check responses
            if PlayResp.keys in ['', [], None]:  # No response was made
                PlayResp.keys = None
            SecondTD.addData('PlayResp.keys',PlayResp.keys)
            if PlayResp.keys != None:  # we had a response
                SecondTD.addData('PlayResp.rt', PlayResp.rt)
            # the Routine "trial_separate" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'SecondTD'
        
        
        # --- Prepare to start Routine "Pause1sec" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        Pause1secComponents = [PauseTxt2]
        for thisComponent in Pause1secComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Pause1sec" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *PauseTxt2* updates
            if PauseTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PauseTxt2.frameNStart = frameN  # exact frame index
                PauseTxt2.tStart = t  # local t and not account for scr refresh
                PauseTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PauseTxt2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PauseTxt2.started')
                PauseTxt2.setAutoDraw(True)
            if PauseTxt2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > PauseTxt2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    PauseTxt2.tStop = t  # not accounting for scr refresh
                    PauseTxt2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PauseTxt2.stopped')
                    PauseTxt2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Pause1secComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Pause1sec" ---
        for thisComponent in Pause1secComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "AddRespCountCode" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        AddRespCountCodeComponents = []
        for thisComponent in AddRespCountCodeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "AddRespCountCode" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AddRespCountCodeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "AddRespCountCode" ---
        for thisComponent in AddRespCountCodeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from AddRespCount
        falsealarm = 0
        hitrate = 0
        if hit != 0:
            falsealarm = 1-(hit/respcountP)
            hitrate = hit/4
        
        TD.addData("RespCountP", respcountP)
        TD.addData("FalseAlarmRate", falsealarm)
        TD.addData("HitRate", hitrate)
        hit = 0
        respcountP = 0
        # the Routine "AddRespCountCode" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'SecondTDLoop'
    
    
    # --- Prepare to start Routine "OccurrenceCounter" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    OccurrenceCounterComponents = []
    for thisComponent in OccurrenceCounterComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "OccurrenceCounter" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in OccurrenceCounterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "OccurrenceCounter" ---
    for thisComponent in OccurrenceCounterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from Block
    OccurenceC += 1
    # the Routine "OccurrenceCounter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    thirdTDLoop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TargetSyllables.xlsx', selection=third),
        seed=None, name='thirdTDLoop')
    thisExp.addLoop(thirdTDLoop)  # add the loop to the experiment
    thisThirdTDLoop = thirdTDLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisThirdTDLoop.rgb)
    if thisThirdTDLoop != None:
        for paramName in thisThirdTDLoop:
            exec('{} = thisThirdTDLoop[paramName]'.format(paramName))
    
    for thisThirdTDLoop in thirdTDLoop:
        currentLoop = thirdTDLoop
        # abbreviate parameter names if possible (e.g. rgb = thisThirdTDLoop.rgb)
        if thisThirdTDLoop != None:
            for paramName in thisThirdTDLoop:
                exec('{} = thisThirdTDLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "SampleIntro" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        PlayTargetKey.keys = []
        PlayTargetKey.rt = []
        _PlayTargetKey_allKeys = []
        TargetTxt.setText(Target)
        # Run 'Begin Routine' code from Count
        repeatCount += 1
        TrialNo = "Recording " + str(repeatCount) + " of 36"
        TrialNoTxt.setText(TrialNo)
        # keep track of which components have finished
        SampleIntroComponents = [TargetMssg, PlayTargetKey, TargetTxt, TrialNoTxt, ContinueTxt4]
        for thisComponent in SampleIntroComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "SampleIntro" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TargetMssg* updates
            if TargetMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TargetMssg.frameNStart = frameN  # exact frame index
                TargetMssg.tStart = t  # local t and not account for scr refresh
                TargetMssg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TargetMssg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TargetMssg.started')
                TargetMssg.setAutoDraw(True)
            
            # *PlayTargetKey* updates
            waitOnFlip = False
            if PlayTargetKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PlayTargetKey.frameNStart = frameN  # exact frame index
                PlayTargetKey.tStart = t  # local t and not account for scr refresh
                PlayTargetKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PlayTargetKey, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PlayTargetKey.started')
                PlayTargetKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(PlayTargetKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(PlayTargetKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if PlayTargetKey.status == STARTED and not waitOnFlip:
                theseKeys = PlayTargetKey.getKeys(keyList=['space'], waitRelease=False)
                _PlayTargetKey_allKeys.extend(theseKeys)
                if len(_PlayTargetKey_allKeys):
                    PlayTargetKey.keys = _PlayTargetKey_allKeys[-1].name  # just the last key pressed
                    PlayTargetKey.rt = _PlayTargetKey_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *TargetTxt* updates
            if TargetTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TargetTxt.frameNStart = frameN  # exact frame index
                TargetTxt.tStart = t  # local t and not account for scr refresh
                TargetTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TargetTxt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TargetTxt.started')
                TargetTxt.setAutoDraw(True)
            
            # *TrialNoTxt* updates
            if TrialNoTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialNoTxt.frameNStart = frameN  # exact frame index
                TrialNoTxt.tStart = t  # local t and not account for scr refresh
                TrialNoTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialNoTxt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TrialNoTxt.started')
                TrialNoTxt.setAutoDraw(True)
            
            # *ContinueTxt4* updates
            if ContinueTxt4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ContinueTxt4.frameNStart = frameN  # exact frame index
                ContinueTxt4.tStart = t  # local t and not account for scr refresh
                ContinueTxt4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueTxt4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ContinueTxt4.started')
                ContinueTxt4.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SampleIntroComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "SampleIntro" ---
        for thisComponent in SampleIntroComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if PlayTargetKey.keys in ['', [], None]:  # No response was made
            PlayTargetKey.keys = None
        thirdTDLoop.addData('PlayTargetKey.keys',PlayTargetKey.keys)
        if PlayTargetKey.keys != None:  # we had a response
            thirdTDLoop.addData('PlayTargetKey.rt', PlayTargetKey.rt)
        # the Routine "SampleIntro" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "PlaySample" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        EndPlay.keys = []
        EndPlay.rt = []
        _EndPlay_allKeys = []
        SyllableSound.setSound(TargetFile, hamming=True)
        SyllableSound.setVolume(1, log=False)
        Repeat.setSound(TargetFile, hamming=True)
        Repeat.setVolume(1, log=False)
        SoundTxt.setText(Target
)
        TrialNoTxt2.setText(TrialNo
)
        # keep track of which components have finished
        PlaySampleComponents = [EndPlay, SyllableSound, Repeat, SoundTxt, ContinueKey2, text_2, TrialNoTxt2]
        for thisComponent in PlaySampleComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "PlaySample" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *EndPlay* updates
            waitOnFlip = False
            if EndPlay.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                # keep track of start time/frame for later
                EndPlay.frameNStart = frameN  # exact frame index
                EndPlay.tStart = t  # local t and not account for scr refresh
                EndPlay.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EndPlay, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EndPlay.started')
                EndPlay.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(EndPlay.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(EndPlay.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if EndPlay.status == STARTED and not waitOnFlip:
                theseKeys = EndPlay.getKeys(keyList=['space',], waitRelease=False)
                _EndPlay_allKeys.extend(theseKeys)
                if len(_EndPlay_allKeys):
                    EndPlay.keys = _EndPlay_allKeys[-1].name  # just the last key pressed
                    EndPlay.rt = _EndPlay_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # start/stop SyllableSound
            if SyllableSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SyllableSound.frameNStart = frameN  # exact frame index
                SyllableSound.tStart = t  # local t and not account for scr refresh
                SyllableSound.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('SyllableSound.started', tThisFlipGlobal)
                SyllableSound.play(when=win)  # sync with win flip
            # start/stop Repeat
            if Repeat.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                # keep track of start time/frame for later
                Repeat.frameNStart = frameN  # exact frame index
                Repeat.tStart = t  # local t and not account for scr refresh
                Repeat.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('Repeat.started', tThisFlipGlobal)
                Repeat.play(when=win)  # sync with win flip
            
            # *SoundTxt* updates
            if SoundTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SoundTxt.frameNStart = frameN  # exact frame index
                SoundTxt.tStart = t  # local t and not account for scr refresh
                SoundTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SoundTxt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SoundTxt.started')
                SoundTxt.setAutoDraw(True)
            
            # *ContinueKey2* updates
            if ContinueKey2.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                # keep track of start time/frame for later
                ContinueKey2.frameNStart = frameN  # exact frame index
                ContinueKey2.tStart = t  # local t and not account for scr refresh
                ContinueKey2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueKey2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ContinueKey2.started')
                ContinueKey2.setAutoDraw(True)
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                text_2.setAutoDraw(True)
            
            # *TrialNoTxt2* updates
            if TrialNoTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialNoTxt2.frameNStart = frameN  # exact frame index
                TrialNoTxt2.tStart = t  # local t and not account for scr refresh
                TrialNoTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialNoTxt2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TrialNoTxt2.started')
                TrialNoTxt2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PlaySampleComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PlaySample" ---
        for thisComponent in PlaySampleComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SyllableSound.stop()  # ensure sound has stopped at end of routine
        Repeat.stop()  # ensure sound has stopped at end of routine
        # the Routine "PlaySample" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "TDStart" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from RandCond
        ## Randomize between 6 randomizations
        opt1 = "0:48" #ta
        opt2 = "48:96" #ta
        opt3 = "96:144" #ta
        opt4 = "144:192" #fe
        opt5 = "192:240" #fe
        opt6 = "240:288" #fe
        opt7 = "288:336" #re
        opt8 = "336:384" #re
        opt9 = "384:432" #re
        opt10 = "432:480" #ru
        opt11 = "480:528" #ru
        opt12 = "528:576" #ru
        
        if Target == "ru" or Target == "pu" or Target == "ni":
            rows = random.choice([opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9])
        elif Target == "re" or Target == "ge" or Target == "me":
            rows = random.choice([opt1, opt2, opt3, opt4, opt5, opt6, opt10, opt11, opt12])
        elif Target == "fe" or Target == "ti" or Target == "su":
            rows = random.choice([opt1, opt2, opt3, opt10, opt11, opt12, opt7, opt8, opt9])
        else:
            rows = random.choice([opt10, opt11, opt12, opt4, opt5, opt6, opt7, opt8, opt9])
        # keep track of which components have finished
        TDStartComponents = [Countdown1]
        for thisComponent in TDStartComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TDStart" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Countdown1* updates
            if Countdown1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Countdown1.frameNStart = frameN  # exact frame index
                Countdown1.tStart = t  # local t and not account for scr refresh
                Countdown1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Countdown1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Countdown1.started')
                Countdown1.setAutoDraw(True)
            if Countdown1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Countdown1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Countdown1.tStop = t  # not accounting for scr refresh
                    Countdown1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Countdown1.stopped')
                    Countdown1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TDStartComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TDStart" ---
        for thisComponent in TDStartComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # set up handler to look after randomisation of conditions etc
        ThirdTD = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(cond + "_TD_list.xlsx", selection=rows),
            seed=None, name='ThirdTD')
        thisExp.addLoop(ThirdTD)  # add the loop to the experiment
        thisThirdTD = ThirdTD.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisThirdTD.rgb)
        if thisThirdTD != None:
            for paramName in thisThirdTD:
                exec('{} = thisThirdTD[paramName]'.format(paramName))
        
        for thisThirdTD in ThirdTD:
            currentLoop = ThirdTD
            # abbreviate parameter names if possible (e.g. rgb = thisThirdTD.rgb)
            if thisThirdTD != None:
                for paramName in thisThirdTD:
                    exec('{} = thisThirdTD[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "trial_separate" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from TargetandRespTime
            if TDSound == Target:
                TargetOnsetP = mytimerP.getTime()
            soundOnsetP = mytimerP.getTime()
            
            
            PlaySound.setSound(TDSoundFile, hamming=True)
            PlaySound.setVolume(1, log=False)
            PlayResp.keys = []
            PlayResp.rt = []
            _PlayResp_allKeys = []
            TargetSoundTxt.setText(Target)
            # keep track of which components have finished
            trial_separateComponents = [PlaySound, PlayText, PlayResp, TargetSoundTxt]
            for thisComponent in trial_separateComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_separate" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # start/stop PlaySound
                if PlaySound.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    PlaySound.frameNStart = frameN  # exact frame index
                    PlaySound.tStart = t  # local t and not account for scr refresh
                    PlaySound.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('PlaySound.started', tThisFlipGlobal)
                    PlaySound.play(when=win)  # sync with win flip
                
                # *PlayText* updates
                if PlayText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    PlayText.frameNStart = frameN  # exact frame index
                    PlayText.tStart = t  # local t and not account for scr refresh
                    PlayText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PlayText, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PlayText.started')
                    PlayText.setAutoDraw(True)
                if PlayText.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > PlayText.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        PlayText.tStop = t  # not accounting for scr refresh
                        PlayText.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'PlayText.stopped')
                        PlayText.setAutoDraw(False)
                
                # *PlayResp* updates
                waitOnFlip = False
                if PlayResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    PlayResp.frameNStart = frameN  # exact frame index
                    PlayResp.tStart = t  # local t and not account for scr refresh
                    PlayResp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PlayResp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PlayResp.started')
                    PlayResp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(PlayResp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(PlayResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if PlayResp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > PlayResp.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        PlayResp.tStop = t  # not accounting for scr refresh
                        PlayResp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'PlayResp.stopped')
                        PlayResp.status = FINISHED
                if PlayResp.status == STARTED and not waitOnFlip:
                    theseKeys = PlayResp.getKeys(keyList=['space',], waitRelease=False)
                    _PlayResp_allKeys.extend(theseKeys)
                    if len(_PlayResp_allKeys):
                        PlayResp.keys = [key.name for key in _PlayResp_allKeys]  # storing all keys
                        PlayResp.rt = [key.rt for key in _PlayResp_allKeys]
                
                # *TargetSoundTxt* updates
                if TargetSoundTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TargetSoundTxt.frameNStart = frameN  # exact frame index
                    TargetSoundTxt.tStart = t  # local t and not account for scr refresh
                    TargetSoundTxt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TargetSoundTxt, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'TargetSoundTxt.started')
                    TargetSoundTxt.setAutoDraw(True)
                if TargetSoundTxt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > TargetSoundTxt.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        TargetSoundTxt.tStop = t  # not accounting for scr refresh
                        TargetSoundTxt.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'TargetSoundTxt.stopped')
                        TargetSoundTxt.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_separateComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_separate" ---
            for thisComponent in trial_separateComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from TargetandRespTime
            # Set Target Onset time
            TD.addData('TargetOnsetP', TargetOnsetP)
            # Check if keyboard has been pressed
            if PlayResp.keys in ['', [], None]:
                PlayResp.keys = None
            if PlayResp.keys != None: # we had a response
                respcountP += 1
                #respOnset = TrainResp.rt[0] + TDTrainSound.tStartRefresh
                respOnsetP = PlayResp.rt[0] + soundOnsetP    
                # Check if the response is too close to the previous valid response
                if respOnsetP - previousOnsetP > 1.2:
                    # Calculate RT
                    reactiontimeP = respOnsetP - TargetOnsetP
                    # Check if RT is below the cutoff
                    if reactiontimeP < 1.2:
                        TD.addData('ReactionTimeP', reactiontimeP)
                        TD.addData('TargetSyllable', Target)
                        TD.addData('TargetPosition', Position)
                        TD.addData('TargetOccurence', OccurenceC)
                        # Count it as a valid "hit"
                        hit += 1
                        # Use this as the latest valid response
                        previousOnsetP = respOnsetP
            
            PlaySound.stop()  # ensure sound has stopped at end of routine
            # check responses
            if PlayResp.keys in ['', [], None]:  # No response was made
                PlayResp.keys = None
            ThirdTD.addData('PlayResp.keys',PlayResp.keys)
            if PlayResp.keys != None:  # we had a response
                ThirdTD.addData('PlayResp.rt', PlayResp.rt)
            # the Routine "trial_separate" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'ThirdTD'
        
        
        # --- Prepare to start Routine "Pause1sec" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        Pause1secComponents = [PauseTxt2]
        for thisComponent in Pause1secComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Pause1sec" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *PauseTxt2* updates
            if PauseTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PauseTxt2.frameNStart = frameN  # exact frame index
                PauseTxt2.tStart = t  # local t and not account for scr refresh
                PauseTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PauseTxt2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PauseTxt2.started')
                PauseTxt2.setAutoDraw(True)
            if PauseTxt2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > PauseTxt2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    PauseTxt2.tStop = t  # not accounting for scr refresh
                    PauseTxt2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'PauseTxt2.stopped')
                    PauseTxt2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Pause1secComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Pause1sec" ---
        for thisComponent in Pause1secComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "AddRespCountCode" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        AddRespCountCodeComponents = []
        for thisComponent in AddRespCountCodeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "AddRespCountCode" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AddRespCountCodeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "AddRespCountCode" ---
        for thisComponent in AddRespCountCodeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from AddRespCount
        falsealarm = 0
        hitrate = 0
        if hit != 0:
            falsealarm = 1-(hit/respcountP)
            hitrate = hit/4
        
        TD.addData("RespCountP", respcountP)
        TD.addData("FalseAlarmRate", falsealarm)
        TD.addData("HitRate", hitrate)
        hit = 0
        respcountP = 0
        # the Routine "AddRespCountCode" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'thirdTDLoop'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'TD'


# --- Prepare to start Routine "CallExperimenter" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ExperimenterKey.keys = []
ExperimenterKey.rt = []
_ExperimenterKey_allKeys = []
# keep track of which components have finished
CallExperimenterComponents = [CallExperimentertxt, ExperimenterKey]
for thisComponent in CallExperimenterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "CallExperimenter" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CallExperimentertxt* updates
    if CallExperimentertxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        CallExperimentertxt.frameNStart = frameN  # exact frame index
        CallExperimentertxt.tStart = t  # local t and not account for scr refresh
        CallExperimentertxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(CallExperimentertxt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'CallExperimentertxt.started')
        CallExperimentertxt.setAutoDraw(True)
    
    # *ExperimenterKey* updates
    waitOnFlip = False
    if ExperimenterKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ExperimenterKey.frameNStart = frameN  # exact frame index
        ExperimenterKey.tStart = t  # local t and not account for scr refresh
        ExperimenterKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ExperimenterKey, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ExperimenterKey.started')
        ExperimenterKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ExperimenterKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ExperimenterKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ExperimenterKey.status == STARTED and not waitOnFlip:
        theseKeys = ExperimenterKey.getKeys(keyList=['0'], waitRelease=False)
        _ExperimenterKey_allKeys.extend(theseKeys)
        if len(_ExperimenterKey_allKeys):
            ExperimenterKey.keys = _ExperimenterKey_allKeys[-1].name  # just the last key pressed
            ExperimenterKey.rt = _ExperimenterKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CallExperimenterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "CallExperimenter" ---
for thisComponent in CallExperimenterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "CallExperimenter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "P2Welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
P2WelcomeContKey.keys = []
P2WelcomeContKey.rt = []
_P2WelcomeContKey_allKeys = []
# keep track of which components have finished
P2WelcomeComponents = [P2WelcomeTxt, P2WelcomeContKey]
for thisComponent in P2WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "P2Welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *P2WelcomeTxt* updates
    if P2WelcomeTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P2WelcomeTxt.frameNStart = frameN  # exact frame index
        P2WelcomeTxt.tStart = t  # local t and not account for scr refresh
        P2WelcomeTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P2WelcomeTxt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'P2WelcomeTxt.started')
        P2WelcomeTxt.setAutoDraw(True)
    
    # *P2WelcomeContKey* updates
    waitOnFlip = False
    if P2WelcomeContKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P2WelcomeContKey.frameNStart = frameN  # exact frame index
        P2WelcomeContKey.tStart = t  # local t and not account for scr refresh
        P2WelcomeContKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P2WelcomeContKey, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'P2WelcomeContKey.started')
        P2WelcomeContKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(P2WelcomeContKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(P2WelcomeContKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if P2WelcomeContKey.status == STARTED and not waitOnFlip:
        theseKeys = P2WelcomeContKey.getKeys(keyList=['space',], waitRelease=False)
        _P2WelcomeContKey_allKeys.extend(theseKeys)
        if len(_P2WelcomeContKey_allKeys):
            P2WelcomeContKey.keys = _P2WelcomeContKey_allKeys[-1].name  # just the last key pressed
            P2WelcomeContKey.rt = _P2WelcomeContKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in P2WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "P2Welcome" ---
for thisComponent in P2WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if P2WelcomeContKey.keys in ['', [], None]:  # No response was made
    P2WelcomeContKey.keys = None
thisExp.addData('P2WelcomeContKey.keys',P2WelcomeContKey.keys)
if P2WelcomeContKey.keys != None:  # we had a response
    thisExp.addData('P2WelcomeContKey.rt', P2WelcomeContKey.rt)
thisExp.nextEntry()
# the Routine "P2Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "FamRatingIntro" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
FamRateIntroKey.keys = []
FamRateIntroKey.rt = []
_FamRateIntroKey_allKeys = []
# keep track of which components have finished
FamRatingIntroComponents = [FamRateIntroTxt, FamRateIntroKey]
for thisComponent in FamRatingIntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "FamRatingIntro" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *FamRateIntroTxt* updates
    if FamRateIntroTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FamRateIntroTxt.frameNStart = frameN  # exact frame index
        FamRateIntroTxt.tStart = t  # local t and not account for scr refresh
        FamRateIntroTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FamRateIntroTxt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'FamRateIntroTxt.started')
        FamRateIntroTxt.setAutoDraw(True)
    
    # *FamRateIntroKey* updates
    waitOnFlip = False
    if FamRateIntroKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FamRateIntroKey.frameNStart = frameN  # exact frame index
        FamRateIntroKey.tStart = t  # local t and not account for scr refresh
        FamRateIntroKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FamRateIntroKey, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'FamRateIntroKey.started')
        FamRateIntroKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(FamRateIntroKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(FamRateIntroKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if FamRateIntroKey.status == STARTED and not waitOnFlip:
        theseKeys = FamRateIntroKey.getKeys(keyList=['space'], waitRelease=False)
        _FamRateIntroKey_allKeys.extend(theseKeys)
        if len(_FamRateIntroKey_allKeys):
            FamRateIntroKey.keys = _FamRateIntroKey_allKeys[-1].name  # just the last key pressed
            FamRateIntroKey.rt = _FamRateIntroKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FamRatingIntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "FamRatingIntro" ---
for thisComponent in FamRatingIntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if FamRateIntroKey.keys in ['', [], None]:  # No response was made
    FamRateIntroKey.keys = None
thisExp.addData('FamRateIntroKey.keys',FamRateIntroKey.keys)
if FamRateIntroKey.keys != None:  # we had a response
    thisExp.addData('FamRateIntroKey.rt', FamRateIntroKey.rt)
thisExp.nextEntry()
# the Routine "FamRatingIntro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
FamRatingLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(cond + "_explicit.xlsx", selection='0:12'),
    seed=None, name='FamRatingLoop')
thisExp.addLoop(FamRatingLoop)  # add the loop to the experiment
thisFamRatingLoop = FamRatingLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFamRatingLoop.rgb)
if thisFamRatingLoop != None:
    for paramName in thisFamRatingLoop:
        exec('{} = thisFamRatingLoop[paramName]'.format(paramName))

for thisFamRatingLoop in FamRatingLoop:
    currentLoop = FamRatingLoop
    # abbreviate parameter names if possible (e.g. rgb = thisFamRatingLoop.rgb)
    if thisFamRatingLoop != None:
        for paramName in thisFamRatingLoop:
            exec('{} = thisFamRatingLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Pause1sec" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    Pause1secComponents = [PauseTxt2]
    for thisComponent in Pause1secComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Pause1sec" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PauseTxt2* updates
        if PauseTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PauseTxt2.frameNStart = frameN  # exact frame index
            PauseTxt2.tStart = t  # local t and not account for scr refresh
            PauseTxt2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PauseTxt2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PauseTxt2.started')
            PauseTxt2.setAutoDraw(True)
        if PauseTxt2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > PauseTxt2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                PauseTxt2.tStop = t  # not accounting for scr refresh
                PauseTxt2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PauseTxt2.stopped')
                PauseTxt2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pause1secComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Pause1sec" ---
    for thisComponent in Pause1secComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "FamRating" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    FamRatingResp.keys = []
    FamRatingResp.rt = []
    _FamRatingResp_allKeys = []
    Syllab1.setSound(Word11, secs=0.38, hamming=True)
    Syllab1.setVolume(1, log=False)
    Syllab2.setSound(Word12, secs=0.38, hamming=True)
    Syllab2.setVolume(1, log=False)
    Syllab3.setSound(Word13, secs=0.38, hamming=True)
    Syllab3.setVolume(1, log=False)
    # keep track of which components have finished
    FamRatingComponents = [FamRatePrompt, RatingScale, RatingScale2, FamRatingResp, Syllab1, Syllab2, Syllab3]
    for thisComponent in FamRatingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "FamRating" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FamRatePrompt* updates
        if FamRatePrompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FamRatePrompt.frameNStart = frameN  # exact frame index
            FamRatePrompt.tStart = t  # local t and not account for scr refresh
            FamRatePrompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FamRatePrompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FamRatePrompt.started')
            FamRatePrompt.setAutoDraw(True)
        
        # *RatingScale* updates
        if RatingScale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RatingScale.frameNStart = frameN  # exact frame index
            RatingScale.tStart = t  # local t and not account for scr refresh
            RatingScale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingScale, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingScale.started')
            RatingScale.setAutoDraw(True)
        
        # *RatingScale2* updates
        if RatingScale2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RatingScale2.frameNStart = frameN  # exact frame index
            RatingScale2.tStart = t  # local t and not account for scr refresh
            RatingScale2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RatingScale2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RatingScale2.started')
            RatingScale2.setAutoDraw(True)
        
        # *FamRatingResp* updates
        waitOnFlip = False
        if FamRatingResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FamRatingResp.frameNStart = frameN  # exact frame index
            FamRatingResp.tStart = t  # local t and not account for scr refresh
            FamRatingResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FamRatingResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FamRatingResp.started')
            FamRatingResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(FamRatingResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(FamRatingResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if FamRatingResp.status == STARTED and not waitOnFlip:
            theseKeys = FamRatingResp.getKeys(keyList=['1', '2', '3', '4',], waitRelease=False)
            _FamRatingResp_allKeys.extend(theseKeys)
            if len(_FamRatingResp_allKeys):
                FamRatingResp.keys = _FamRatingResp_allKeys[-1].name  # just the last key pressed
                FamRatingResp.rt = _FamRatingResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop Syllab1
        if Syllab1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Syllab1.frameNStart = frameN  # exact frame index
            Syllab1.tStart = t  # local t and not account for scr refresh
            Syllab1.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('Syllab1.started', tThisFlipGlobal)
            Syllab1.play(when=win)  # sync with win flip
        if Syllab1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Syllab1.tStartRefresh + 0.38-frameTolerance:
                # keep track of stop time/frame for later
                Syllab1.tStop = t  # not accounting for scr refresh
                Syllab1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Syllab1.stopped')
                Syllab1.stop()
        # start/stop Syllab2
        if Syllab2.status == NOT_STARTED and tThisFlip >= 0.88-frameTolerance:
            # keep track of start time/frame for later
            Syllab2.frameNStart = frameN  # exact frame index
            Syllab2.tStart = t  # local t and not account for scr refresh
            Syllab2.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('Syllab2.started', tThisFlipGlobal)
            Syllab2.play(when=win)  # sync with win flip
        if Syllab2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Syllab2.tStartRefresh + 0.38-frameTolerance:
                # keep track of stop time/frame for later
                Syllab2.tStop = t  # not accounting for scr refresh
                Syllab2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Syllab2.stopped')
                Syllab2.stop()
        # start/stop Syllab3
        if Syllab3.status == NOT_STARTED and tThisFlip >= 1.26-frameTolerance:
            # keep track of start time/frame for later
            Syllab3.frameNStart = frameN  # exact frame index
            Syllab3.tStart = t  # local t and not account for scr refresh
            Syllab3.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('Syllab3.started', tThisFlipGlobal)
            Syllab3.play(when=win)  # sync with win flip
        if Syllab3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Syllab3.tStartRefresh + 0.38-frameTolerance:
                # keep track of stop time/frame for later
                Syllab3.tStop = t  # not accounting for scr refresh
                Syllab3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Syllab3.stopped')
                Syllab3.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FamRatingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FamRating" ---
    for thisComponent in FamRatingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if FamRatingResp.keys in ['', [], None]:  # No response was made
        FamRatingResp.keys = None
    FamRatingLoop.addData('FamRatingResp.keys',FamRatingResp.keys)
    if FamRatingResp.keys != None:  # we had a response
        FamRatingLoop.addData('FamRatingResp.rt', FamRatingResp.rt)
    Syllab1.stop()  # ensure sound has stopped at end of routine
    Syllab2.stop()  # ensure sound has stopped at end of routine
    Syllab3.stop()  # ensure sound has stopped at end of routine
    # the Routine "FamRating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'FamRatingLoop'


# --- Prepare to start Routine "Part2Intro2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ContinueKey7.keys = []
ContinueKey7.rt = []
_ContinueKey7_allKeys = []
# keep track of which components have finished
Part2Intro2Components = [P2IntroTxt2, ContinueKey7]
for thisComponent in Part2Intro2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Part2Intro2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *P2IntroTxt2* updates
    if P2IntroTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        P2IntroTxt2.frameNStart = frameN  # exact frame index
        P2IntroTxt2.tStart = t  # local t and not account for scr refresh
        P2IntroTxt2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(P2IntroTxt2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'P2IntroTxt2.started')
        P2IntroTxt2.setAutoDraw(True)
    
    # *ContinueKey7* updates
    waitOnFlip = False
    if ContinueKey7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueKey7.frameNStart = frameN  # exact frame index
        ContinueKey7.tStart = t  # local t and not account for scr refresh
        ContinueKey7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueKey7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ContinueKey7.started')
        ContinueKey7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ContinueKey7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ContinueKey7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ContinueKey7.status == STARTED and not waitOnFlip:
        theseKeys = ContinueKey7.getKeys(keyList=['space'], waitRelease=False)
        _ContinueKey7_allKeys.extend(theseKeys)
        if len(_ContinueKey7_allKeys):
            ContinueKey7.keys = _ContinueKey7_allKeys[-1].name  # just the last key pressed
            ContinueKey7.rt = _ContinueKey7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Part2Intro2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Part2Intro2" ---
for thisComponent in Part2Intro2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ContinueKey7.keys in ['', [], None]:  # No response was made
    ContinueKey7.keys = None
thisExp.addData('ContinueKey7.keys',ContinueKey7.keys)
if ContinueKey7.keys != None:  # we had a response
    thisExp.addData('ContinueKey7.rt', ContinueKey7.rt)
thisExp.nextEntry()
# the Routine "Part2Intro2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
AFCTest = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(cond + "_explicit.xlsx", selection='12:28'),
    seed=None, name='AFCTest')
thisExp.addLoop(AFCTest)  # add the loop to the experiment
thisAFCTest = AFCTest.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAFCTest.rgb)
if thisAFCTest != None:
    for paramName in thisAFCTest:
        exec('{} = thisAFCTest[paramName]'.format(paramName))

for thisAFCTest in AFCTest:
    currentLoop = AFCTest
    # abbreviate parameter names if possible (e.g. rgb = thisAFCTest.rgb)
    if thisAFCTest != None:
        for paramName in thisAFCTest:
            exec('{} = thisAFCTest[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "count" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from AFC_trialcount
    AFCcount += 1
    QuestionNo = "Trial" + str(AFCcount) + " /16"
    # keep track of which components have finished
    countComponents = []
    for thisComponent in countComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "count" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in countComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "count" ---
    for thisComponent in countComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "count" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "AFCStart" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    QuestionNoTxt.setText(QuestionNo)
    # keep track of which components have finished
    AFCStartComponents = [QuestionNoTxt]
    for thisComponent in AFCStartComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "AFCStart" ---
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *QuestionNoTxt* updates
        if QuestionNoTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            QuestionNoTxt.frameNStart = frameN  # exact frame index
            QuestionNoTxt.tStart = t  # local t and not account for scr refresh
            QuestionNoTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(QuestionNoTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'QuestionNoTxt.started')
            QuestionNoTxt.setAutoDraw(True)
        if QuestionNoTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > QuestionNoTxt.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                QuestionNoTxt.tStop = t  # not accounting for scr refresh
                QuestionNoTxt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'QuestionNoTxt.stopped')
                QuestionNoTxt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AFCStartComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "AFCStart" ---
    for thisComponent in AFCStartComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    
    # --- Prepare to start Routine "AFCFirst" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Word1No.setText('1')
    Word_1_1.setSound(Word11, secs=0.38, hamming=True)
    Word_1_1.setVolume(1, log=False)
    Word_1_2.setSound(Word12, secs=0.38, hamming=True)
    Word_1_2.setVolume(1, log=False)
    Word_1_3.setSound(Word13, secs=0.38, hamming=True)
    Word_1_3.setVolume(1, log=False)
    # keep track of which components have finished
    AFCFirstComponents = [Word1No, Word_1_1, Word_1_2, Word_1_3]
    for thisComponent in AFCFirstComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "AFCFirst" ---
    while continueRoutine and routineTimer.getTime() < 2.14:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Word1No* updates
        if Word1No.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Word1No.frameNStart = frameN  # exact frame index
            Word1No.tStart = t  # local t and not account for scr refresh
            Word1No.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Word1No, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Word1No.started')
            Word1No.setAutoDraw(True)
        if Word1No.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Word1No.tStartRefresh + 2.07-frameTolerance:
                # keep track of stop time/frame for later
                Word1No.tStop = t  # not accounting for scr refresh
                Word1No.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Word1No.stopped')
                Word1No.setAutoDraw(False)
        # start/stop Word_1_1
        if Word_1_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            Word_1_1.frameNStart = frameN  # exact frame index
            Word_1_1.tStart = t  # local t and not account for scr refresh
            Word_1_1.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('Word_1_1.started', tThisFlipGlobal)
            Word_1_1.play(when=win)  # sync with win flip
        if Word_1_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Word_1_1.tStartRefresh + 0.38-frameTolerance:
                # keep track of stop time/frame for later
                Word_1_1.tStop = t  # not accounting for scr refresh
                Word_1_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Word_1_1.stopped')
                Word_1_1.stop()
        # start/stop Word_1_2
        if Word_1_2.status == NOT_STARTED and tThisFlip >= 1.38-frameTolerance:
            # keep track of start time/frame for later
            Word_1_2.frameNStart = frameN  # exact frame index
            Word_1_2.tStart = t  # local t and not account for scr refresh
            Word_1_2.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('Word_1_2.started', tThisFlipGlobal)
            Word_1_2.play(when=win)  # sync with win flip
        if Word_1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Word_1_2.tStartRefresh + 0.38-frameTolerance:
                # keep track of stop time/frame for later
                Word_1_2.tStop = t  # not accounting for scr refresh
                Word_1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Word_1_2.stopped')
                Word_1_2.stop()
        # start/stop Word_1_3
        if Word_1_3.status == NOT_STARTED and tThisFlip >= 1.76-frameTolerance:
            # keep track of start time/frame for later
            Word_1_3.frameNStart = frameN  # exact frame index
            Word_1_3.tStart = t  # local t and not account for scr refresh
            Word_1_3.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('Word_1_3.started', tThisFlipGlobal)
            Word_1_3.play(when=win)  # sync with win flip
        if Word_1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Word_1_3.tStartRefresh + 0.38-frameTolerance:
                # keep track of stop time/frame for later
                Word_1_3.tStop = t  # not accounting for scr refresh
                Word_1_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Word_1_3.stopped')
                Word_1_3.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AFCFirstComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "AFCFirst" ---
    for thisComponent in AFCFirstComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Word_1_1.stop()  # ensure sound has stopped at end of routine
    Word_1_2.stop()  # ensure sound has stopped at end of routine
    Word_1_3.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.140000)
    
    # --- Prepare to start Routine "AFCSecond" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    Word_2_1.setSound(Word21, secs=0.38, hamming=True)
    Word_2_1.setVolume(1, log=False)
    Word_2_2.setSound(Word22, secs=0.38, hamming=True)
    Word_2_2.setVolume(1, log=False)
    Word_2_3.setSound(Word23, secs=0.38, hamming=True)
    Word_2_3.setVolume(1, log=False)
    # keep track of which components have finished
    AFCSecondComponents = [Word2No, Word_2_1, Word_2_2, Word_2_3]
    for thisComponent in AFCSecondComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "AFCSecond" ---
    while continueRoutine and routineTimer.getTime() < 2.14:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Word2No* updates
        if Word2No.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Word2No.frameNStart = frameN  # exact frame index
            Word2No.tStart = t  # local t and not account for scr refresh
            Word2No.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Word2No, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Word2No.started')
            Word2No.setAutoDraw(True)
        if Word2No.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Word2No.tStartRefresh + 2.07-frameTolerance:
                # keep track of stop time/frame for later
                Word2No.tStop = t  # not accounting for scr refresh
                Word2No.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Word2No.stopped')
                Word2No.setAutoDraw(False)
        # start/stop Word_2_1
        if Word_2_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            Word_2_1.frameNStart = frameN  # exact frame index
            Word_2_1.tStart = t  # local t and not account for scr refresh
            Word_2_1.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('Word_2_1.started', tThisFlipGlobal)
            Word_2_1.play(when=win)  # sync with win flip
        if Word_2_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Word_2_1.tStartRefresh + 0.38-frameTolerance:
                # keep track of stop time/frame for later
                Word_2_1.tStop = t  # not accounting for scr refresh
                Word_2_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Word_2_1.stopped')
                Word_2_1.stop()
        # start/stop Word_2_2
        if Word_2_2.status == NOT_STARTED and tThisFlip >= 1.38-frameTolerance:
            # keep track of start time/frame for later
            Word_2_2.frameNStart = frameN  # exact frame index
            Word_2_2.tStart = t  # local t and not account for scr refresh
            Word_2_2.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('Word_2_2.started', tThisFlipGlobal)
            Word_2_2.play(when=win)  # sync with win flip
        if Word_2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Word_2_2.tStartRefresh + 0.38-frameTolerance:
                # keep track of stop time/frame for later
                Word_2_2.tStop = t  # not accounting for scr refresh
                Word_2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Word_2_2.stopped')
                Word_2_2.stop()
        # start/stop Word_2_3
        if Word_2_3.status == NOT_STARTED and tThisFlip >= 1.76-frameTolerance:
            # keep track of start time/frame for later
            Word_2_3.frameNStart = frameN  # exact frame index
            Word_2_3.tStart = t  # local t and not account for scr refresh
            Word_2_3.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('Word_2_3.started', tThisFlipGlobal)
            Word_2_3.play(when=win)  # sync with win flip
        if Word_2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Word_2_3.tStartRefresh + 0.38-frameTolerance:
                # keep track of stop time/frame for later
                Word_2_3.tStop = t  # not accounting for scr refresh
                Word_2_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Word_2_3.stopped')
                Word_2_3.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AFCSecondComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "AFCSecond" ---
    for thisComponent in AFCSecondComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Word_2_1.stop()  # ensure sound has stopped at end of routine
    Word_2_2.stop()  # ensure sound has stopped at end of routine
    Word_2_3.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.140000)
    
    # --- Prepare to start Routine "AFCQuestion" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    AFCResp.keys = []
    AFCResp.rt = []
    _AFCResp_allKeys = []
    # keep track of which components have finished
    AFCQuestionComponents = [QuestionTxt, AFCResp]
    for thisComponent in AFCQuestionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "AFCQuestion" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *QuestionTxt* updates
        if QuestionTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            QuestionTxt.frameNStart = frameN  # exact frame index
            QuestionTxt.tStart = t  # local t and not account for scr refresh
            QuestionTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(QuestionTxt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'QuestionTxt.started')
            QuestionTxt.setAutoDraw(True)
        
        # *AFCResp* updates
        waitOnFlip = False
        if AFCResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AFCResp.frameNStart = frameN  # exact frame index
            AFCResp.tStart = t  # local t and not account for scr refresh
            AFCResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AFCResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'AFCResp.started')
            AFCResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(AFCResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(AFCResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if AFCResp.status == STARTED and not waitOnFlip:
            theseKeys = AFCResp.getKeys(keyList=['1', '2',], waitRelease=False)
            _AFCResp_allKeys.extend(theseKeys)
            if len(_AFCResp_allKeys):
                AFCResp.keys = _AFCResp_allKeys[-1].name  # just the last key pressed
                AFCResp.rt = _AFCResp_allKeys[-1].rt
                # was this correct?
                if (AFCResp.keys == str(AFCCorrect)) or (AFCResp.keys == AFCCorrect):
                    AFCResp.corr = 1
                else:
                    AFCResp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AFCQuestionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "AFCQuestion" ---
    for thisComponent in AFCQuestionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if AFCResp.keys in ['', [], None]:  # No response was made
        AFCResp.keys = None
        # was no response the correct answer?!
        if str(AFCCorrect).lower() == 'none':
           AFCResp.corr = 1;  # correct non-response
        else:
           AFCResp.corr = 0;  # failed to respond (incorrectly)
    # store data for AFCTest (TrialHandler)
    AFCTest.addData('AFCResp.keys',AFCResp.keys)
    AFCTest.addData('AFCResp.corr', AFCResp.corr)
    if AFCResp.keys != None:  # we had a response
        AFCTest.addData('AFCResp.rt', AFCResp.rt)
    # the Routine "AFCQuestion" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'AFCTest'


# --- Prepare to start Routine "HearingCheckIntro" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
EndKey2.keys = []
EndKey2.rt = []
_EndKey2_allKeys = []
# keep track of which components have finished
HearingCheckIntroComponents = [HearingCheckTxt, EndKey2]
for thisComponent in HearingCheckIntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "HearingCheckIntro" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *HearingCheckTxt* updates
    if HearingCheckTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        HearingCheckTxt.frameNStart = frameN  # exact frame index
        HearingCheckTxt.tStart = t  # local t and not account for scr refresh
        HearingCheckTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(HearingCheckTxt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'HearingCheckTxt.started')
        HearingCheckTxt.setAutoDraw(True)
    
    # *EndKey2* updates
    waitOnFlip = False
    if EndKey2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndKey2.frameNStart = frameN  # exact frame index
        EndKey2.tStart = t  # local t and not account for scr refresh
        EndKey2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndKey2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EndKey2.started')
        EndKey2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EndKey2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EndKey2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EndKey2.status == STARTED and not waitOnFlip:
        theseKeys = EndKey2.getKeys(keyList=['space'], waitRelease=False)
        _EndKey2_allKeys.extend(theseKeys)
        if len(_EndKey2_allKeys):
            EndKey2.keys = _EndKey2_allKeys[-1].name  # just the last key pressed
            EndKey2.rt = _EndKey2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in HearingCheckIntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "HearingCheckIntro" ---
for thisComponent in HearingCheckIntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if EndKey2.keys in ['', [], None]:  # No response was made
    EndKey2.keys = None
thisExp.addData('EndKey2.keys',EndKey2.keys)
if EndKey2.keys != None:  # we had a response
    thisExp.addData('EndKey2.rt', EndKey2.rt)
thisExp.nextEntry()
# the Routine "HearingCheckIntro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
HearingcheckLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('HearingCheckSounds.xlsx'),
    seed=None, name='HearingcheckLoop')
thisExp.addLoop(HearingcheckLoop)  # add the loop to the experiment
thisHearingcheckLoop = HearingcheckLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisHearingcheckLoop.rgb)
if thisHearingcheckLoop != None:
    for paramName in thisHearingcheckLoop:
        exec('{} = thisHearingcheckLoop[paramName]'.format(paramName))

for thisHearingcheckLoop in HearingcheckLoop:
    currentLoop = HearingcheckLoop
    # abbreviate parameter names if possible (e.g. rgb = thisHearingcheckLoop.rgb)
    if thisHearingcheckLoop != None:
        for paramName in thisHearingcheckLoop:
            exec('{} = thisHearingcheckLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Pause1sec" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    Pause1secComponents = [PauseTxt2]
    for thisComponent in Pause1secComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Pause1sec" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PauseTxt2* updates
        if PauseTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PauseTxt2.frameNStart = frameN  # exact frame index
            PauseTxt2.tStart = t  # local t and not account for scr refresh
            PauseTxt2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PauseTxt2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PauseTxt2.started')
            PauseTxt2.setAutoDraw(True)
        if PauseTxt2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > PauseTxt2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                PauseTxt2.tStop = t  # not accounting for scr refresh
                PauseTxt2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PauseTxt2.stopped')
                PauseTxt2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pause1secComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Pause1sec" ---
    for thisComponent in Pause1secComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "HearingCheck" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    CheckWord.setSound(SoundFile, hamming=True)
    CheckWord.setVolume(1, log=False)
    WordOptions.setText("1. "+Word1 + "         2. " + Word2 + "         3. " + Word3)
    CheckRespKey.keys = []
    CheckRespKey.rt = []
    _CheckRespKey_allKeys = []
    # keep track of which components have finished
    HearingCheckComponents = [CheckWord, WordOptions, CheckQuestion, CheckRespKey]
    for thisComponent in HearingCheckComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "HearingCheck" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop CheckWord
        if CheckWord.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            CheckWord.frameNStart = frameN  # exact frame index
            CheckWord.tStart = t  # local t and not account for scr refresh
            CheckWord.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('CheckWord.started', tThisFlipGlobal)
            CheckWord.play(when=win)  # sync with win flip
        
        # *WordOptions* updates
        if WordOptions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            WordOptions.frameNStart = frameN  # exact frame index
            WordOptions.tStart = t  # local t and not account for scr refresh
            WordOptions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(WordOptions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'WordOptions.started')
            WordOptions.setAutoDraw(True)
        
        # *CheckQuestion* updates
        if CheckQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CheckQuestion.frameNStart = frameN  # exact frame index
            CheckQuestion.tStart = t  # local t and not account for scr refresh
            CheckQuestion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CheckQuestion, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CheckQuestion.started')
            CheckQuestion.setAutoDraw(True)
        
        # *CheckRespKey* updates
        waitOnFlip = False
        if CheckRespKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CheckRespKey.frameNStart = frameN  # exact frame index
            CheckRespKey.tStart = t  # local t and not account for scr refresh
            CheckRespKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CheckRespKey, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CheckRespKey.started')
            CheckRespKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(CheckRespKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(CheckRespKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if CheckRespKey.status == STARTED and not waitOnFlip:
            theseKeys = CheckRespKey.getKeys(keyList=['1', '2', '3',], waitRelease=False)
            _CheckRespKey_allKeys.extend(theseKeys)
            if len(_CheckRespKey_allKeys):
                CheckRespKey.keys = _CheckRespKey_allKeys[-1].name  # just the last key pressed
                CheckRespKey.rt = _CheckRespKey_allKeys[-1].rt
                # was this correct?
                if (CheckRespKey.keys == str(Correct)) or (CheckRespKey.keys == Correct):
                    CheckRespKey.corr = 1
                else:
                    CheckRespKey.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in HearingCheckComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "HearingCheck" ---
    for thisComponent in HearingCheckComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    CheckWord.stop()  # ensure sound has stopped at end of routine
    # check responses
    if CheckRespKey.keys in ['', [], None]:  # No response was made
        CheckRespKey.keys = None
        # was no response the correct answer?!
        if str(Correct).lower() == 'none':
           CheckRespKey.corr = 1;  # correct non-response
        else:
           CheckRespKey.corr = 0;  # failed to respond (incorrectly)
    # store data for HearingcheckLoop (TrialHandler)
    HearingcheckLoop.addData('CheckRespKey.keys',CheckRespKey.keys)
    HearingcheckLoop.addData('CheckRespKey.corr', CheckRespKey.corr)
    if CheckRespKey.keys != None:  # we had a response
        HearingcheckLoop.addData('CheckRespKey.rt', CheckRespKey.rt)
    # the Routine "HearingCheck" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'HearingcheckLoop'


# --- Prepare to start Routine "P2End" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
EndAllKey.keys = []
EndAllKey.rt = []
_EndAllKey_allKeys = []
# keep track of which components have finished
P2EndComponents = [EndMssg, EndAllKey]
for thisComponent in P2EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "P2End" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EndMssg.started')
        EndMssg.setAutoDraw(True)
    
    # *EndAllKey* updates
    waitOnFlip = False
    if EndAllKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndAllKey.frameNStart = frameN  # exact frame index
        EndAllKey.tStart = t  # local t and not account for scr refresh
        EndAllKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndAllKey, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'EndAllKey.started')
        EndAllKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EndAllKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EndAllKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EndAllKey.status == STARTED and not waitOnFlip:
        theseKeys = EndAllKey.getKeys(keyList=['return'], waitRelease=False)
        _EndAllKey_allKeys.extend(theseKeys)
        if len(_EndAllKey_allKeys):
            EndAllKey.keys = _EndAllKey_allKeys[-1].name  # just the last key pressed
            EndAllKey.rt = _EndAllKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in P2EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "P2End" ---
for thisComponent in P2EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if EndAllKey.keys in ['', [], None]:  # No response was made
    EndAllKey.keys = None
thisExp.addData('EndAllKey.keys',EndAllKey.keys)
if EndAllKey.keys != None:  # we had a response
    thisExp.addData('EndAllKey.rt', EndAllKey.rt)
thisExp.nextEntry()
# the Routine "P2End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Blank" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
BlankEndKey.keys = []
BlankEndKey.rt = []
_BlankEndKey_allKeys = []
# keep track of which components have finished
BlankComponents = [BlankEndKey]
for thisComponent in BlankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Blank" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *BlankEndKey* updates
    waitOnFlip = False
    if BlankEndKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BlankEndKey.frameNStart = frameN  # exact frame index
        BlankEndKey.tStart = t  # local t and not account for scr refresh
        BlankEndKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BlankEndKey, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'BlankEndKey.started')
        BlankEndKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(BlankEndKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(BlankEndKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if BlankEndKey.status == STARTED and not waitOnFlip:
        theseKeys = BlankEndKey.getKeys(keyList=['space'], waitRelease=False)
        _BlankEndKey_allKeys.extend(theseKeys)
        if len(_BlankEndKey_allKeys):
            BlankEndKey.keys = _BlankEndKey_allKeys[-1].name  # just the last key pressed
            BlankEndKey.rt = _BlankEndKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BlankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Blank" ---
for thisComponent in BlankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Blank" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
