#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.2.4),
    on October 14, 2026, at 15:23
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.2.4'
expName = 'motion_mc'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': '123',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1536, 864]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\DondaWHITWORTH(Stude\\OneDrive - Birkbeck, University of London\\Documents\\Psychopy\\motion_mc.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1,-1,-1]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "main_instructions" ---
    main_text = visual.TextStim(win=win, name='main_text',
        text='Welcome to the experiment!\n\nIn this task, we will show you patterns of moving dots - and you will make judgements about direction the dots move in. \n\nSometimes, we will also ask you to report how confident you feel in the judgments you are making. \n\nPress SPACE to continue. ',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    main_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='ioHub')
    
    # --- Initialize components for Routine "block_instructions" ---
    text = visual.TextStim(win=win, name='text',
        text='Placeholder',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    block_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='ioHub')
    
    # --- Initialize components for Routine "Comprehension_check" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='I understand at some point I may be asked to make another judgment after the motion stimulus, and this will be used to calculate my bonus payment.\n\nn = No\ny = Yes',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Comprehension = keyboard.Keyboard(deviceName='defaultKeyboard', backend='ioHub')
    
    # --- Initialize components for Routine "fixation" ---
    polygon = visual.ShapeStim(
        win=win, name='polygon', vertices='cross',
        size=(0.03, 0.03),
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "trial" ---
    # Run 'Begin Experiment' code from code
    import numpy 
    #win.mouseVisible = False #controls whether the cursor is visible or not 
    step=.04 #spacing between two adjacent values (because there are 25 dots, the coherence values can only be set in steps of 4% (0.04)
    
    #h_signal= .8 #high motion coherence signal (80% of dots moving coherently) 
    #l_signal=.2 #low coherence signal (20% moving coherently) 
    
    signal1= 0.04 
    signal2= 0.20
    signal3= 0.36
    signal4= 0.50
    
    
    trial_count=0;
    d1 = visual.ShapeStim(
        win=win, name='d1',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-1.0, interpolate=True)
    d2 = visual.ShapeStim(
        win=win, name='d2',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-2.0, interpolate=True)
    d3 = visual.ShapeStim(
        win=win, name='d3',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-3.0, interpolate=True)
    d4 = visual.ShapeStim(
        win=win, name='d4',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-4.0, interpolate=True)
    d5 = visual.ShapeStim(
        win=win, name='d5',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-5.0, interpolate=True)
    d6 = visual.ShapeStim(
        win=win, name='d6',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-6.0, interpolate=True)
    d7 = visual.ShapeStim(
        win=win, name='d7',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-7.0, interpolate=True)
    d8 = visual.ShapeStim(
        win=win, name='d8',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-8.0, interpolate=True)
    d9 = visual.ShapeStim(
        win=win, name='d9',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-9.0, interpolate=True)
    d10 = visual.ShapeStim(
        win=win, name='d10',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-10.0, interpolate=True)
    d11 = visual.ShapeStim(
        win=win, name='d11',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-11.0, interpolate=True)
    d12 = visual.ShapeStim(
        win=win, name='d12',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-12.0, interpolate=True)
    d13 = visual.ShapeStim(
        win=win, name='d13',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-13.0, interpolate=True)
    d14 = visual.ShapeStim(
        win=win, name='d14',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-14.0, interpolate=True)
    d15 = visual.ShapeStim(
        win=win, name='d15',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-15.0, interpolate=True)
    d16 = visual.ShapeStim(
        win=win, name='d16',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-16.0, interpolate=True)
    d17 = visual.ShapeStim(
        win=win, name='d17',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-17.0, interpolate=True)
    d18 = visual.ShapeStim(
        win=win, name='d18',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-18.0, interpolate=True)
    d19 = visual.ShapeStim(
        win=win, name='d19',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-19.0, interpolate=True)
    d20 = visual.ShapeStim(
        win=win, name='d20',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-20.0, interpolate=True)
    d21 = visual.ShapeStim(
        win=win, name='d21',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-21.0, interpolate=True)
    d22 = visual.ShapeStim(
        win=win, name='d22',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-22.0, interpolate=True)
    d23 = visual.ShapeStim(
        win=win, name='d23',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-23.0, interpolate=True)
    d24 = visual.ShapeStim(
        win=win, name='d24',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-24.0, interpolate=True)
    d25 = visual.ShapeStim(
        win=win, name='d25',
        size=(0.01, 0.01), vertices='circle',
        ori=0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[1,1,1],
        opacity=1, depth=-25.0, interpolate=True)
    q_text = visual.TextStim(win=win, name='q_text',
        text='Moving LEFT or RIGHT?\n\n(1 = Left, 2 = Right)',
        font='Arial',
        pos=(0, 0.2), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-26.0);
    q_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='ioHub')
    
    # --- Initialize components for Routine "blank" ---
    blank_text = visual.TextStim(win=win, name='blank_text',
        text=' ',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "type2_q" ---
    type2_q_text = visual.TextStim(win=win, name='type2_q_text',
        text='How confident are you that YOUR LAST MOTION DECISION was correct?\n',
        font='Arial',
        pos=(0, 0.2), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_below = visual.TextStim(win=win, name='text_below',
        text='(Adjust with mouse, press SPACE to submit)\n',
        font='Arial',
        pos=(0, -0.3), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    type2_q_key_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='ioHub')
    line = visual.Rect(
        win=win, name='line',
        width=(0.005, 0.15)[0], height=(0.005, 0.15)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    marker = visual.ShapeStim(
        win=win, name='marker',
        size=(0.02, 0.02), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='red', fillColor='red',
        opacity=None, depth=-4.0, interpolate=True)
    type2_mouse = event.Mouse(win=win)
    x, y = [None, None]
    type2_mouse.mouseClock = core.Clock()
    low_text = visual.TextStim(win=win, name='low_text',
        text='Lowest\nConfidence',
        font='Arial',
        pos=(0, -0.12), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    high_text = visual.TextStim(win=win, name='high_text',
        text='Highest\nConfidence',
        font='Arial',
        pos=(0, 0.12), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    
    # --- Initialize components for Routine "feedback" ---
    feedback_text = visual.TextStim(win=win, name='feedback_text',
        text='placeholder',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Bonus" ---
    text_4 = visual.TextStim(win=win, name='text_4',
        text='That is the end of the experiment. \n\nYour bonus is',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    bonus_sum = visual.TextStim(win=win, name='bonus_sum',
        text='Placeholder',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    # Run 'Begin Experiment' code from code_9
    bonus_score = 0
    
    # --- Initialize components for Routine "thanks" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='This is the end of the study.\n\nThank you for taking part.\n\nYou will shortly be automatically redirected to Prolific. Do not close this window before you are prompted, or your data will not be recorded. \n\nIf you would like to get in touch with the research team, please email Prof Daniel Yon at d.yon@bbk.ac.uk\n\n\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "main_instructions" ---
    # create an object to store info about Routine main_instructions
    main_instructions = data.Routine(
        name='main_instructions',
        components=[main_text, main_resp],
    )
    main_instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for main_resp
    main_resp.keys = []
    main_resp.rt = []
    _main_resp_allKeys = []
    # store start times for main_instructions
    main_instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    main_instructions.tStart = globalClock.getTime(format='float')
    main_instructions.status = STARTED
    thisExp.addData('main_instructions.started', main_instructions.tStart)
    main_instructions.maxDuration = None
    # keep track of which components have finished
    main_instructionsComponents = main_instructions.components
    for thisComponent in main_instructions.components:
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
    
    # --- Run Routine "main_instructions" ---
    thisExp.currentRoutine = main_instructions
    main_instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *main_text* updates
        
        # if main_text is starting this frame...
        if main_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_text.frameNStart = frameN  # exact frame index
            main_text.tStart = t  # local t and not account for scr refresh
            main_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'main_text.started')
            # update status
            main_text.status = STARTED
            main_text.setAutoDraw(True)
        
        # if main_text is active this frame...
        if main_text.status == STARTED:
            # update params
            pass
        
        # *main_resp* updates
        waitOnFlip = False
        
        # if main_resp is starting this frame...
        if main_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_resp.frameNStart = frameN  # exact frame index
            main_resp.tStart = t  # local t and not account for scr refresh
            main_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'main_resp.started')
            # update status
            main_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(main_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(main_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if main_resp.status == STARTED and not waitOnFlip:
            theseKeys = main_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _main_resp_allKeys.extend(theseKeys)
            if len(_main_resp_allKeys):
                main_resp.keys = _main_resp_allKeys[-1].name  # just the last key pressed
                main_resp.rt = _main_resp_allKeys[-1].rt
                main_resp.duration = _main_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=main_instructions,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            main_instructions.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if main_instructions.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in main_instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "main_instructions" ---
    for thisComponent in main_instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for main_instructions
    main_instructions.tStop = globalClock.getTime(format='float')
    main_instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('main_instructions.stopped', main_instructions.tStop)
    # check responses
    if main_resp.keys in ['', [], None]:  # No response was made
        main_resp.keys = None
    thisExp.addData('main_resp.keys',main_resp.keys)
    if main_resp.keys != None:  # we had a response
        thisExp.addData('main_resp.rt', main_resp.rt)
        thisExp.addData('main_resp.duration', main_resp.duration)
    thisExp.nextEntry()
    # the Routine "main_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Blocks = data.TrialHandler2(
        name='Blocks',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('blocks_ot.csv'), 
        seed=None, 
        isTrials=False, 
    )
    thisExp.addLoop(Blocks)  # add the loop to the experiment
    thisBlock = Blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            globals()[paramName] = thisBlock[paramName]
    
    for thisBlock in Blocks:
        Blocks.status = STARTED
        if hasattr(thisBlock, 'status'):
            thisBlock.status = STARTED
        currentLoop = Blocks
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                globals()[paramName] = thisBlock[paramName]
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler2(
            name='trials_2',
            nReps=2, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
            isTrials=True, 
        )
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial_2 in trials_2:
            trials_2.status = STARTED
            if hasattr(thisTrial_2, 'status'):
                thisTrial_2.status = STARTED
            currentLoop = trials_2
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    globals()[paramName] = thisTrial_2[paramName]
            
            # --- Prepare to start Routine "block_instructions" ---
            # create an object to store info about Routine block_instructions
            block_instructions = data.Routine(
                name='block_instructions',
                components=[text, block_resp],
            )
            block_instructions.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for block_resp
            block_resp.keys = []
            block_resp.rt = []
            _block_resp_allKeys = []
            # Run 'Begin Routine' code from code_3
            if blockCode==2:
                continueRoutine=False; #don't show instructions again on final 'critical' trial
            if blockCode ==-1:
                block_str = "First we will practice making judgments about the dot clouds. \n\n You will see a brief cloud of moving dots and have to judge whether the dots moved mostly LEFT or RIGHT using the 1 and 2 keys on your keyboard. \n\n Press SPACE to continue" ;
            elif blockCode==1:
                block_str = "Now we will begin the main task. This will be same as practice. \n\n However, you no longer receive trial-by-trial feedback \n\n IMPORTANTLY, However, at one point in the task, we will ask you to make another additional judgment after the stimulus \n This judgment will determine the performance-related bonus you receive on Prolific \n\n Press SPACE to continue" ;
            text.setText(block_str)
            
            
            
            # store start times for block_instructions
            block_instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            block_instructions.tStart = globalClock.getTime(format='float')
            block_instructions.status = STARTED
            thisExp.addData('block_instructions.started', block_instructions.tStart)
            block_instructions.maxDuration = None
            # keep track of which components have finished
            block_instructionsComponents = block_instructions.components
            for thisComponent in block_instructions.components:
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
            
            # --- Run Routine "block_instructions" ---
            thisExp.currentRoutine = block_instructions
            block_instructions.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisTrial_2, 'status') and thisTrial_2.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text* updates
                
                # if text is starting this frame...
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.started')
                    # update status
                    text.status = STARTED
                    text.setAutoDraw(True)
                
                # if text is active this frame...
                if text.status == STARTED:
                    # update params
                    pass
                
                # *block_resp* updates
                waitOnFlip = False
                
                # if block_resp is starting this frame...
                if block_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    block_resp.frameNStart = frameN  # exact frame index
                    block_resp.tStart = t  # local t and not account for scr refresh
                    block_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(block_resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'block_resp.started')
                    # update status
                    block_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(block_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(block_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if block_resp.status == STARTED and not waitOnFlip:
                    theseKeys = block_resp.getKeys(keyList=['space','y', 'n'], ignoreKeys=["escape"], waitRelease=False)
                    _block_resp_allKeys.extend(theseKeys)
                    if len(_block_resp_allKeys):
                        block_resp.keys = _block_resp_allKeys[-1].name  # just the last key pressed
                        block_resp.rt = _block_resp_allKeys[-1].rt
                        block_resp.duration = _block_resp_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=block_instructions,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    block_instructions.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if block_instructions.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in block_instructions.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "block_instructions" ---
            for thisComponent in block_instructions.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for block_instructions
            block_instructions.tStop = globalClock.getTime(format='float')
            block_instructions.tStopRefresh = tThisFlipGlobal
            thisExp.addData('block_instructions.stopped', block_instructions.tStop)
            # check responses
            if block_resp.keys in ['', [], None]:  # No response was made
                block_resp.keys = None
            trials_2.addData('block_resp.keys',block_resp.keys)
            if block_resp.keys != None:  # we had a response
                trials_2.addData('block_resp.rt', block_resp.rt)
                trials_2.addData('block_resp.duration', block_resp.duration)
            # the Routine "block_instructions" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Comprehension_check" ---
            # create an object to store info about Routine Comprehension_check
            Comprehension_check = data.Routine(
                name='Comprehension_check',
                components=[text_2, Comprehension],
            )
            Comprehension_check.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for Comprehension
            Comprehension.keys = []
            Comprehension.rt = []
            _Comprehension_allKeys = []
            # Run 'Begin Routine' code from code_8
            if blockCode != 1: #only display this on the first block
                continueRoutine = False;
            
            # store start times for Comprehension_check
            Comprehension_check.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Comprehension_check.tStart = globalClock.getTime(format='float')
            Comprehension_check.status = STARTED
            thisExp.addData('Comprehension_check.started', Comprehension_check.tStart)
            Comprehension_check.maxDuration = None
            # keep track of which components have finished
            Comprehension_checkComponents = Comprehension_check.components
            for thisComponent in Comprehension_check.components:
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
            
            # --- Run Routine "Comprehension_check" ---
            thisExp.currentRoutine = Comprehension_check
            Comprehension_check.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisTrial_2, 'status') and thisTrial_2.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                
                # if text_2 is starting this frame...
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.started')
                    # update status
                    text_2.status = STARTED
                    text_2.setAutoDraw(True)
                
                # if text_2 is active this frame...
                if text_2.status == STARTED:
                    # update params
                    pass
                
                # *Comprehension* updates
                waitOnFlip = False
                
                # if Comprehension is starting this frame...
                if Comprehension.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Comprehension.frameNStart = frameN  # exact frame index
                    Comprehension.tStart = t  # local t and not account for scr refresh
                    Comprehension.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Comprehension, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Comprehension.started')
                    # update status
                    Comprehension.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Comprehension.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Comprehension.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Comprehension.status == STARTED and not waitOnFlip:
                    theseKeys = Comprehension.getKeys(keyList=['y','n'], ignoreKeys=["escape"], waitRelease=False)
                    _Comprehension_allKeys.extend(theseKeys)
                    if len(_Comprehension_allKeys):
                        Comprehension.keys = _Comprehension_allKeys[-1].name  # just the last key pressed
                        Comprehension.rt = _Comprehension_allKeys[-1].rt
                        Comprehension.duration = _Comprehension_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=Comprehension_check,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    Comprehension_check.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if Comprehension_check.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in Comprehension_check.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Comprehension_check" ---
            for thisComponent in Comprehension_check.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Comprehension_check
            Comprehension_check.tStop = globalClock.getTime(format='float')
            Comprehension_check.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Comprehension_check.stopped', Comprehension_check.tStop)
            # check responses
            if Comprehension.keys in ['', [], None]:  # No response was made
                Comprehension.keys = None
            trials_2.addData('Comprehension.keys',Comprehension.keys)
            if Comprehension.keys != None:  # we had a response
                trials_2.addData('Comprehension.rt', Comprehension.rt)
                trials_2.addData('Comprehension.duration', Comprehension.duration)
            # Run 'End Routine' code from code_8
            if Comprehension.keys =='y':
                trials_2.finished = True
            # the Routine "Comprehension_check" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            # mark thisTrial_2 as finished
            if hasattr(thisTrial_2, 'status'):
                thisTrial_2.status = FINISHED
            # if awaiting a pause, pause now
            if trials_2.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                trials_2.status = STARTED
            thisExp.nextEntry()
            
        # completed 2 repeats of 'trials_2'
        trials_2.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler2(
            name='trials',
            nReps=trialReps, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(
            'motionTrials_ot.csv', 
            selection=rowsUsed
        )
        , 
            seed=None, 
            isTrials=True, 
        )
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial in trials:
            trials.status = STARTED
            if hasattr(thisTrial, 'status'):
                thisTrial.status = STARTED
            currentLoop = trials
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    globals()[paramName] = thisTrial[paramName]
            
            # --- Prepare to start Routine "fixation" ---
            # create an object to store info about Routine fixation
            fixation = data.Routine(
                name='fixation',
                components=[polygon],
            )
            fixation.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for fixation
            fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            fixation.tStart = globalClock.getTime(format='float')
            fixation.status = STARTED
            thisExp.addData('fixation.started', fixation.tStart)
            fixation.maxDuration = None
            # keep track of which components have finished
            fixationComponents = fixation.components
            for thisComponent in fixation.components:
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
            
            # --- Run Routine "fixation" ---
            thisExp.currentRoutine = fixation
            fixation.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.5:
                # if trial has changed, end Routine now
                if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *polygon* updates
                
                # if polygon is starting this frame...
                if polygon.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    polygon.frameNStart = frameN  # exact frame index
                    polygon.tStart = t  # local t and not account for scr refresh
                    polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.started')
                    # update status
                    polygon.status = STARTED
                    polygon.setAutoDraw(True)
                
                # if polygon is active this frame...
                if polygon.status == STARTED:
                    # update params
                    pass
                
                # if polygon is stopping this frame...
                if polygon.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon.tStop = t  # not accounting for scr refresh
                        polygon.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon.stopped')
                        # update status
                        polygon.status = FINISHED
                        polygon.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=fixation,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    fixation.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if fixation.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in fixation.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fixation" ---
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for fixation
            fixation.tStop = globalClock.getTime(format='float')
            fixation.tStopRefresh = tThisFlipGlobal
            thisExp.addData('fixation.stopped', fixation.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if fixation.maxDurationReached:
                routineTimer.addTime(-fixation.maxDuration)
            elif fixation.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.500000)
            
            # --- Prepare to start Routine "trial" ---
            # create an object to store info about Routine trial
            trial = data.Routine(
                name='trial',
                components=[d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25, q_text, q_resp],
            )
            trial.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code
            trial_count=trial_count+1 
            frame=0
            mouse_x=[0]*10000
            mouse_y = [0]*10000
            r=0.15 #radius
            d=r*2 #diameter
            
            #setting the intial position of the 25 dots. REMEMBER we are working in radians, rather than degrees 
            d1_angle = 2*3.14*numpy.random.rand() #direction the dot will move in. 2*pi*redius value will give an angle value and therefore a direction that the dot will move in
            rand_ang = 2*3.14*numpy.random.rand() #random angle
            d1_dist = (d*numpy.random.rand())-r
            d1_x = (numpy.cos(rand_ang)*d1_dist) #funky maths to get the x and y coordinates for the dot
            d1_y = (numpy.sin(rand_ang)*d1_dist)
            d1.setPos([d1_x,d1_y]) #original position of the dot
            
            d2_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d2_dist = (d*numpy.random.rand())-r
            d2_x = (numpy.cos(rand_ang)*d2_dist)
            d2_y = (numpy.sin(rand_ang)*d2_dist)
            d2.setPos([d2_x,d2_y])
            
            d3_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d3_dist = (d*numpy.random.rand())-r
            d3_x = (numpy.cos(rand_ang)*d3_dist)
            d3_y = (numpy.sin(rand_ang)*d3_dist)
            d3.setPos([d3_x,d3_y])
            
            
            d4_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d4_dist = (d*numpy.random.rand())-r
            d4_x = (numpy.cos(rand_ang)*d4_dist)
            d4_y = (numpy.sin(rand_ang)*d4_dist)
            d4.setPos([d4_x,d4_y])
            
            d5_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d5_dist = (d*numpy.random.rand())-r
            d5_x = (numpy.cos(rand_ang)*d5_dist)
            d5_y = (numpy.sin(rand_ang)*d5_dist)
            d5.setPos([d5_x,d5_y])
            
            d6_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d6_dist = (d*numpy.random.rand())-r
            d6_x = (numpy.cos(rand_ang)*d6_dist)
            d6_y = (numpy.sin(rand_ang)*d6_dist)
            d6.setPos([d6_x,d6_y])
            
            d7_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d7_dist = (d*numpy.random.rand())-r
            d7_x = (numpy.cos(rand_ang)*d7_dist)
            d7_y = (numpy.sin(rand_ang)*d7_dist)
            d7.setPos([d7_x,d7_y])
            
            d8_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d8_dist = (d*numpy.random.rand())-r
            d8_x = (numpy.cos(rand_ang)*d8_dist)
            d8_y = (numpy.sin(rand_ang)*d8_dist)
            d8.setPos([d8_x,d8_y])
            
            d9_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d9_dist = (d*numpy.random.rand())-r
            d9_x = (numpy.cos(rand_ang)*d9_dist)
            d9_y = (numpy.sin(rand_ang)*d9_dist)
            d9.setPos([d9_x,d9_y])
            
            d10_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d10_dist = (d*numpy.random.rand())-r
            d10_x = (numpy.cos(rand_ang)*d10_dist)
            d10_y = (numpy.sin(rand_ang)*d10_dist)
            d10.setPos([d10_x,d10_y])
            
            d11_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d11_dist = (d*numpy.random.rand())-r
            d11_x = (numpy.cos(rand_ang)*d11_dist)
            d11_y = (numpy.sin(rand_ang)*d11_dist)
            d11.setPos([d11_x,d11_y])
            
            d12_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d12_dist = (d*numpy.random.rand())-r
            d12_x = (numpy.cos(rand_ang)*d12_dist)
            d12_y = (numpy.sin(rand_ang)*d12_dist)
            d12.setPos([d12_x,d12_y])
            
            d13_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d13_dist = (d*numpy.random.rand())-r
            d13_x = (numpy.cos(rand_ang)*d13_dist)
            d13_y = (numpy.sin(rand_ang)*d13_dist)
            d13.setPos([d13_x,d13_y])
            
            d14_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d14_dist = (d*numpy.random.rand())-r
            d14_x = (numpy.cos(rand_ang)*d14_dist)
            d14_y = (numpy.sin(rand_ang)*d14_dist)
            d14.setPos([d14_x,d14_y])
            
            d15_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d15_dist = (d*numpy.random.rand())-r
            d15_x = (numpy.cos(rand_ang)*d15_dist)
            d15_y = (numpy.sin(rand_ang)*d15_dist)
            d15.setPos([d15_x,d15_y])
            
            d16_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d16_dist = (d*numpy.random.rand())-r
            d16_x = (numpy.cos(rand_ang)*d16_dist)
            d16_y = (numpy.sin(rand_ang)*d16_dist)
            d16.setPos([d16_x,d16_y])
            
            d17_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d17_dist = (d*numpy.random.rand())-r
            d17_x = (numpy.cos(rand_ang)*d17_dist)
            d17_y = (numpy.sin(rand_ang)*d17_dist)
            d17.setPos([d17_x,d17_y])
            
            d18_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d18_dist = (d*numpy.random.rand())-r
            d18_x = (numpy.cos(rand_ang)*d18_dist)
            d18_y = (numpy.sin(rand_ang)*d18_dist)
            d18.setPos([d18_x,d18_y])
            
            d19_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d19_dist = (d*numpy.random.rand())-r
            d19_x = (numpy.cos(rand_ang)*d19_dist)
            d19_y = (numpy.sin(rand_ang)*d19_dist)
            d19.setPos([d19_x,d19_y])
            
            d20_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d20_dist = (d*numpy.random.rand())-r
            d20_x = (numpy.cos(rand_ang)*d20_dist)
            d20_y = (numpy.sin(rand_ang)*d20_dist)
            d20.setPos([d20_x,d20_y])
            
            d21_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d21_dist = (d*numpy.random.rand())-r
            d21_x = (numpy.cos(rand_ang)*d21_dist)
            d21_y = (numpy.sin(rand_ang)*d21_dist)
            d21.setPos([d21_x,d21_y])
            
            d22_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d22_dist = (d*numpy.random.rand())-r
            d22_x = (numpy.cos(rand_ang)*d22_dist)
            d22_y = (numpy.sin(rand_ang)*d22_dist)
            d22.setPos([d22_x,d22_y])
            
            d23_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d23_dist = (d*numpy.random.rand())-r
            d23_x = (numpy.cos(rand_ang)*d23_dist)
            d23_y = (numpy.sin(rand_ang)*d23_dist)
            d23.setPos([d23_x,d23_y])
            
            d24_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d24_dist = (d*numpy.random.rand())-r
            d24_x = (numpy.cos(rand_ang)*d24_dist)
            d24_y = (numpy.sin(rand_ang)*d24_dist)
            d24.setPos([d24_x,d24_y])
            
            d25_angle = 2*3.14*numpy.random.rand()
            rand_ang = 2*3.14*numpy.random.rand()
            d25_dist = (d*numpy.random.rand())-r
            d25_x = (numpy.cos(rand_ang)*d25_dist)
            d25_y = (numpy.sin(rand_ang)*d25_dist)
            d25.setPos([d25_x,d25_y])
            
            #if strength==1: #'Strength' variable found in motionTrial spreadsheet. Refers to the strength of the signal (weak or strong)
                #signal = h_signal #If strength=1 then there will be high motion coherence (h_signal, defined in Begin Exp tab)
            #elif strength==-1:
                #signal=l_signal
                
            if strength==1: 
                signal = signal1
            elif strength==2:
                signal=signal2
            elif strength==3:
                signal=signal3
            elif strength==4:
                signal=signal4
            
            
            #This section decides how many and which dots will move coherently
            if signal>=1*step: #e.g. if the signal was 0.8, this is >1*step (1*0.04)= 0.04. 
                d1_angle=0 #...therefore, d1_angle (or direction the dot will move in) will be changed to 0 (originally randomly set above). 0 = moving directly along the x axis.
            if signal>=2*step:
                d2_angle=0 #as soon as a threshold is reached (decided by signal), the dots will move in the random direction the variable d1_angle was originally allocated
            if signal>=3*step:
                d3_angle=0
            if signal>=4*step:
                d4_angle=0
            if signal>=5*step:
                d5_angle=0
            if signal>=6*step:
                d6_angle=0
            if signal>=7*step:
                d7_angle=0
            if signal>=8*step:
                d8_angle=0
            if signal>=9*step:
                d9_angle=0
            if signal>=10*step:
                d10_angle=0
            if signal>=11*step:
                d11_angle=0
            if signal>=12*step:
                d12_angle=0
            if signal>=13*step:
                d13_angle=0
            if signal>=14*step:
                d14_angle=0
            if signal>=15*step:
                d15_angle=0
            if signal>=16*step:
                d16_angle=0
            if signal>=17*step:
                d17_angle=0
            if signal>=18*step:
                d18_angle=0
            if signal>=19*step:
                d19_angle=0
            if signal>=20*step:
                d20_angle=0
            if signal>=21*step:
                d21_angle=0
            if signal>=22*step:
                d22_angle=0
            if signal>=23*step:
                d23_angle=0
            if signal>=24*step:
                d24_angle=0
            if signal>=25*step:
                d25_angle=0
            thisExp.addData('signal', signal) #saving out the data
            # create starting attributes for q_resp
            q_resp.keys = []
            q_resp.rt = []
            _q_resp_allKeys = []
            # store start times for trial
            trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial.tStart = globalClock.getTime(format='float')
            trial.status = STARTED
            thisExp.addData('trial.started', trial.tStart)
            trial.maxDuration = None
            # keep track of which components have finished
            trialComponents = trial.components
            for thisComponent in trial.components:
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
            
            # --- Run Routine "trial" ---
            thisExp.currentRoutine = trial
            trial.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 4.0:
                # if trial has changed, end Routine now
                if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from code
                frame=frame+1
                #Speed variable = how much the dot moves in each frame (pos no.= move right, neg no.=move left)
                speed = 0.01*direction #direction variable defined in motion trials spreadsheet
                
                #dot 1
                d1_p = d1.pos
                d1_x = d1_p[0]+(numpy.cos(d1_angle)*speed) #how much we are adding to x and y coordinates to decide the final location 
                d1_y = d1_p[1]+(numpy.sin(d1_angle)*speed)
                
                #below makes sure that the dot doesn't leave the ring, if it does go outside the ring the code will just draw the dot randomly somewhere else and then repeat the loop for each frame until the presentation time is over
                if ((d1_p[0]**2)+(d1_p[1]**2))**.5 >r:
                    d1_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d1_x = (numpy.cos(rand_ang)*d1_dist)
                    d1_y = (numpy.sin(rand_ang)*d1_dist)
                    d1.setPos([d1_x,d1_y])
                else:
                    d1.setPos([d1_x,d1_y])
                #dot2
                d2_p = d2.pos
                d2_x = d2_p[0]+(numpy.cos(d2_angle)*speed)
                d2_y = d2_p[1]+(numpy.sin(d2_angle)*speed)
                
                if ((d2_p[0]**2)+(d2_p[1]**2))**.5 >r:
                    d2_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d2_x = (numpy.cos(rand_ang)*d2_dist)
                    d2_y = (numpy.sin(rand_ang)*d2_dist)
                    d2.setPos([d2_x,d2_y])
                else:
                    d2.setPos([d2_x,d2_y])
                #dot3
                d3_p = d3.pos
                d3_x = d3_p[0]+(numpy.cos(d3_angle)*speed)
                d3_y = d3_p[1]+(numpy.sin(d3_angle)*speed)
                
                if ((d3_p[0]**2)+(d3_p[1]**2))**.5 >r:
                    d3_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d3_x = (numpy.cos(rand_ang)*d3_dist)
                    d3_y = (numpy.sin(rand_ang)*d3_dist)
                    d3.setPos([d3_x,d3_y])
                else:
                    d3.setPos([d3_x,d3_y])
                    
                #dot4
                d4_p = d4.pos
                d4_x = d4_p[0]+(numpy.cos(d4_angle)*speed)
                d4_y = d4_p[1]+(numpy.sin(d4_angle)*speed)
                
                if ((d4_p[0]**2)+(d4_p[1]**2))**.5 >r:
                    d4_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d4_x = (numpy.cos(rand_ang)*d4_dist)
                    d4_y = (numpy.sin(rand_ang)*d4_dist)
                    d4.setPos([d4_x,d4_y])
                else:
                    d4.setPos([d4_x,d4_y])
                
                #dot5
                d5_p = d5.pos
                d5_x = d5_p[0]+(numpy.cos(d5_angle)*speed)
                d5_y = d5_p[1]+(numpy.sin(d5_angle)*speed)
                
                if ((d5_p[0]**2)+(d5_p[1]**2))**.5 >r:
                    d5_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d5_x = (numpy.cos(rand_ang)*d5_dist)
                    d5_y = (numpy.sin(rand_ang)*d5_dist)
                    d5.setPos([d5_x,d5_y])
                else:
                    d5.setPos([d5_x,d5_y])
                
                #dot6
                d6_p = d6.pos
                d6_x = d6_p[0]+(numpy.cos(d6_angle)*speed)
                d6_y = d6_p[1]+(numpy.sin(d6_angle)*speed)
                
                if ((d6_p[0]**2)+(d6_p[1]**2))**.5 >r:
                    d6_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d6_x = (numpy.cos(rand_ang)*d6_dist)
                    d6_y = (numpy.sin(rand_ang)*d6_dist)
                    d6.setPos([d6_x,d6_y])
                else:
                    d6.setPos([d6_x,d6_y])
                
                #dot7
                d7_p = d7.pos
                d7_x = d7_p[0]+(numpy.cos(d7_angle)*speed)
                d7_y = d7_p[1]+(numpy.sin(d7_angle)*speed)
                
                if ((d7_p[0]**2)+(d7_p[1]**2))**.5 >r:
                    d7_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d7_x = (numpy.cos(rand_ang)*d7_dist)
                    d7_y = (numpy.sin(rand_ang)*d7_dist)
                    d7.setPos([d7_x,d7_y])
                else:
                    d7.setPos([d7_x,d7_y])
                
                #dot8
                d8_p = d8.pos
                d8_x = d8_p[0]+(numpy.cos(d8_angle)*speed)
                d8_y = d8_p[1]+(numpy.sin(d8_angle)*speed)
                
                if ((d8_p[0]**2)+(d8_p[1]**2))**.5 >r:
                    d8_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d8_x = (numpy.cos(rand_ang)*d8_dist)
                    d8_y = (numpy.sin(rand_ang)*d8_dist)
                    d8.setPos([d8_x,d8_y])
                else:
                    d8.setPos([d8_x,d8_y])
                
                #dot9
                d9_p = d9.pos
                d9_x = d9_p[0]+(numpy.cos(d9_angle)*speed)
                d9_y = d9_p[1]+(numpy.sin(d9_angle)*speed)
                
                if ((d9_p[0]**2)+(d9_p[1]**2))**.5 >r:
                    d9_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d9_x = (numpy.cos(rand_ang)*d9_dist)
                    d9_y = (numpy.sin(rand_ang)*d9_dist)
                    d9.setPos([d9_x,d9_y])
                else:
                    d9.setPos([d9_x,d9_y])
                
                #dot10
                d10_p = d10.pos
                d10_x = d10_p[0]+(numpy.cos(d10_angle)*speed)
                d10_y = d10_p[1]+(numpy.sin(d10_angle)*speed)
                
                if ((d10_p[0]**2)+(d10_p[1]**2))**.5 >r:
                    d10_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d10_x = (numpy.cos(rand_ang)*d10_dist)
                    d10_y = (numpy.sin(rand_ang)*d10_dist)
                    d10.setPos([d10_x,d10_y])
                else:
                    d10.setPos([d10_x,d10_y])
                
                #dot11
                d11_p = d11.pos
                d11_x = d11_p[0]+(numpy.cos(d11_angle)*speed)
                d11_y = d11_p[1]+(numpy.sin(d11_angle)*speed)
                
                if ((d11_p[0]**2)+(d11_p[1]**2))**.5 >r:
                    d11_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d11_x = (numpy.cos(rand_ang)*d11_dist)
                    d11_y = (numpy.sin(rand_ang)*d11_dist)
                    d11.setPos([d11_x,d11_y])
                else:
                    d11.setPos([d11_x,d11_y])
                
                #dot12
                d12_p = d12.pos
                d12_x = d12_p[0]+(numpy.cos(d12_angle)*speed)
                d12_y = d12_p[1]+(numpy.sin(d12_angle)*speed)
                
                if ((d12_p[0]**2)+(d12_p[1]**2))**.5 >r:
                    d12_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d12_x = (numpy.cos(rand_ang)*d12_dist)
                    d12_y = (numpy.sin(rand_ang)*d12_dist)
                    d12.setPos([d12_x,d12_y])
                else:
                    d12.setPos([d12_x,d12_y])
                
                #dot13
                d13_p = d13.pos
                d13_x = d13_p[0]+(numpy.cos(d13_angle)*speed)
                d13_y = d13_p[1]+(numpy.sin(d13_angle)*speed)
                
                if ((d13_p[0]**2)+(d13_p[1]**2))**.5 >r:
                    d13_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d13_x = (numpy.cos(rand_ang)*d13_dist)
                    d13_y = (numpy.sin(rand_ang)*d13_dist)
                    d13.setPos([d13_x,d13_y])
                else:
                    d13.setPos([d13_x,d13_y])
                
                #dot14
                d14_p = d14.pos
                d14_x = d14_p[0]+(numpy.cos(d14_angle)*speed)
                d14_y = d14_p[1]+(numpy.sin(d14_angle)*speed)
                
                if ((d14_p[0]**2)+(d14_p[1]**2))**.5 >r:
                    d14_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d14_x = (numpy.cos(rand_ang)*d14_dist)
                    d14_y = (numpy.sin(rand_ang)*d14_dist)
                    d14.setPos([d14_x,d14_y])
                else:
                    d14.setPos([d14_x,d14_y])
                
                #dot15
                d15_p = d15.pos
                d15_x = d15_p[0]+(numpy.cos(d15_angle)*speed)
                d15_y = d15_p[1]+(numpy.sin(d15_angle)*speed)
                
                if ((d15_p[0]**2)+(d15_p[1]**2))**.5 >r:
                    d15_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d15_x = (numpy.cos(rand_ang)*d15_dist)
                    d15_y = (numpy.sin(rand_ang)*d15_dist)
                    d15.setPos([d15_x,d15_y])
                else:
                    d15.setPos([d15_x,d15_y])
                
                #dot16
                d16_p = d16.pos
                d16_x = d16_p[0]+(numpy.cos(d16_angle)*speed)
                d16_y = d16_p[1]+(numpy.sin(d16_angle)*speed)
                
                if ((d16_p[0]**2)+(d16_p[1]**2))**.5 >r:
                    d16_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d16_x = (numpy.cos(rand_ang)*d16_dist)
                    d16_y = (numpy.sin(rand_ang)*d16_dist)
                    d16.setPos([d16_x,d16_y])
                else:
                    d16.setPos([d16_x,d16_y])
                
                #dot17
                d17_p = d17.pos
                d17_x = d17_p[0]+(numpy.cos(d17_angle)*speed)
                d17_y = d17_p[1]+(numpy.sin(d17_angle)*speed)
                
                if ((d17_p[0]**2)+(d17_p[1]**2))**.5 >r:
                    d17_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d17_x = (numpy.cos(rand_ang)*d17_dist)
                    d17_y = (numpy.sin(rand_ang)*d17_dist)
                    d17.setPos([d17_x,d17_y])
                else:
                    d17.setPos([d17_x,d17_y])
                
                #dot18
                d18_p = d18.pos
                d18_x = d18_p[0]+(numpy.cos(d18_angle)*speed)
                d18_y = d18_p[1]+(numpy.sin(d18_angle)*speed)
                
                if ((d18_p[0]**2)+(d18_p[1]**2))**.5 >r:
                    d18_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d18_x = (numpy.cos(rand_ang)*d18_dist)
                    d18_y = (numpy.sin(rand_ang)*d18_dist)
                    d18.setPos([d18_x,d18_y])
                else:
                    d18.setPos([d18_x,d18_y])
                
                #dot19
                d19_p = d19.pos
                d19_x = d19_p[0]+(numpy.cos(d19_angle)*speed)
                d19_y = d19_p[1]+(numpy.sin(d19_angle)*speed)
                
                if ((d19_p[0]**2)+(d19_p[1]**2))**.5 >r:
                    d19_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d19_x = (numpy.cos(rand_ang)*d19_dist)
                    d19_y = (numpy.sin(rand_ang)*d19_dist)
                    d19.setPos([d19_x,d19_y])
                else:
                    d19.setPos([d19_x,d19_y])
                
                #dot20
                d20_p = d20.pos
                d20_x = d20_p[0]+(numpy.cos(d20_angle)*speed)
                d20_y = d20_p[1]+(numpy.sin(d20_angle)*speed)
                
                if ((d20_p[0]**2)+(d20_p[1]**2))**.5 >r:
                    d20_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d20_x = (numpy.cos(rand_ang)*d20_dist)
                    d20_y = (numpy.sin(rand_ang)*d20_dist)
                    d20.setPos([d20_x,d20_y])
                else:
                    d20.setPos([d20_x,d20_y])
                
                #dot21
                d21_p = d21.pos
                d21_x = d21_p[0]+(numpy.cos(d21_angle)*speed)
                d21_y = d21_p[1]+(numpy.sin(d21_angle)*speed)
                
                if ((d21_p[0]**2)+(d21_p[1]**2))**.5 >r:
                    d21_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d21_x = (numpy.cos(rand_ang)*d21_dist)
                    d21_y = (numpy.sin(rand_ang)*d21_dist)
                    d21.setPos([d21_x,d21_y])
                else:
                    d21.setPos([d21_x,d21_y])
                
                #dot22
                d22_p = d22.pos
                d22_x = d22_p[0]+(numpy.cos(d22_angle)*speed)
                d22_y = d22_p[1]+(numpy.sin(d22_angle)*speed)
                
                if ((d22_p[0]**2)+(d22_p[1]**2))**.5 >r:
                    d22_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d22_x = (numpy.cos(rand_ang)*d22_dist)
                    d22_y = (numpy.sin(rand_ang)*d22_dist)
                    d22.setPos([d22_x,d22_y])
                else:
                    d22.setPos([d22_x,d22_y])
                
                #dot23
                d23_p = d23.pos
                d23_x = d23_p[0]+(numpy.cos(d23_angle)*speed)
                d23_y = d23_p[1]+(numpy.sin(d23_angle)*speed)
                
                if ((d23_p[0]**2)+(d23_p[1]**2))**.5 >r:
                    d23_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d23_x = (numpy.cos(rand_ang)*d23_dist)
                    d23_y = (numpy.sin(rand_ang)*d23_dist)
                    d23.setPos([d23_x,d23_y])
                else:
                    d23.setPos([d23_x,d23_y])
                
                #dot24
                d24_p = d24.pos
                d24_x = d24_p[0]+(numpy.cos(d24_angle)*speed)
                d24_y = d24_p[1]+(numpy.sin(d24_angle)*speed)
                
                if ((d24_p[0]**2)+(d24_p[1]**2))**.5 >r:
                    d24_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d24_x = (numpy.cos(rand_ang)*d24_dist)
                    d24_y = (numpy.sin(rand_ang)*d24_dist)
                    d24.setPos([d24_x,d24_y])
                else:
                    d24.setPos([d24_x,d24_y])
                
                #dot25
                d25_p = d25.pos
                d25_x = d25_p[0]+(numpy.cos(d25_angle)*speed)
                d25_y = d25_p[1]+(numpy.sin(d25_angle)*speed)
                
                if ((d25_p[0]**2)+(d25_p[1]**2))**.5 >r:
                    d25_dist = (d*numpy.random.rand())-r
                    rand_ang = 2*3.14*numpy.random.rand()
                    d25_x = (numpy.cos(rand_ang)*d25_dist)
                    d25_y = (numpy.sin(rand_ang)*d25_dist)
                    d25.setPos([d25_x,d25_y])
                else:
                    d25.setPos([d25_x,d25_y])
                
                #dots.setSpeed(speed)
                
                # *d1* updates
                
                # if d1 is starting this frame...
                if d1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d1.frameNStart = frameN  # exact frame index
                    d1.tStart = t  # local t and not account for scr refresh
                    d1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd1.started')
                    # update status
                    d1.status = STARTED
                    d1.setAutoDraw(True)
                
                # if d1 is active this frame...
                if d1.status == STARTED:
                    # update params
                    pass
                
                # if d1 is stopping this frame...
                if d1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d1.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d1.tStop = t  # not accounting for scr refresh
                        d1.tStopRefresh = tThisFlipGlobal  # on global time
                        d1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd1.stopped')
                        # update status
                        d1.status = FINISHED
                        d1.setAutoDraw(False)
                
                # *d2* updates
                
                # if d2 is starting this frame...
                if d2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d2.frameNStart = frameN  # exact frame index
                    d2.tStart = t  # local t and not account for scr refresh
                    d2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd2.started')
                    # update status
                    d2.status = STARTED
                    d2.setAutoDraw(True)
                
                # if d2 is active this frame...
                if d2.status == STARTED:
                    # update params
                    pass
                
                # if d2 is stopping this frame...
                if d2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d2.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d2.tStop = t  # not accounting for scr refresh
                        d2.tStopRefresh = tThisFlipGlobal  # on global time
                        d2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd2.stopped')
                        # update status
                        d2.status = FINISHED
                        d2.setAutoDraw(False)
                
                # *d3* updates
                
                # if d3 is starting this frame...
                if d3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d3.frameNStart = frameN  # exact frame index
                    d3.tStart = t  # local t and not account for scr refresh
                    d3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd3.started')
                    # update status
                    d3.status = STARTED
                    d3.setAutoDraw(True)
                
                # if d3 is active this frame...
                if d3.status == STARTED:
                    # update params
                    pass
                
                # if d3 is stopping this frame...
                if d3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d3.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d3.tStop = t  # not accounting for scr refresh
                        d3.tStopRefresh = tThisFlipGlobal  # on global time
                        d3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd3.stopped')
                        # update status
                        d3.status = FINISHED
                        d3.setAutoDraw(False)
                
                # *d4* updates
                
                # if d4 is starting this frame...
                if d4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d4.frameNStart = frameN  # exact frame index
                    d4.tStart = t  # local t and not account for scr refresh
                    d4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd4.started')
                    # update status
                    d4.status = STARTED
                    d4.setAutoDraw(True)
                
                # if d4 is active this frame...
                if d4.status == STARTED:
                    # update params
                    pass
                
                # if d4 is stopping this frame...
                if d4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d4.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d4.tStop = t  # not accounting for scr refresh
                        d4.tStopRefresh = tThisFlipGlobal  # on global time
                        d4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd4.stopped')
                        # update status
                        d4.status = FINISHED
                        d4.setAutoDraw(False)
                
                # *d5* updates
                
                # if d5 is starting this frame...
                if d5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d5.frameNStart = frameN  # exact frame index
                    d5.tStart = t  # local t and not account for scr refresh
                    d5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd5.started')
                    # update status
                    d5.status = STARTED
                    d5.setAutoDraw(True)
                
                # if d5 is active this frame...
                if d5.status == STARTED:
                    # update params
                    pass
                
                # if d5 is stopping this frame...
                if d5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d5.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d5.tStop = t  # not accounting for scr refresh
                        d5.tStopRefresh = tThisFlipGlobal  # on global time
                        d5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd5.stopped')
                        # update status
                        d5.status = FINISHED
                        d5.setAutoDraw(False)
                
                # *d6* updates
                
                # if d6 is starting this frame...
                if d6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d6.frameNStart = frameN  # exact frame index
                    d6.tStart = t  # local t and not account for scr refresh
                    d6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd6.started')
                    # update status
                    d6.status = STARTED
                    d6.setAutoDraw(True)
                
                # if d6 is active this frame...
                if d6.status == STARTED:
                    # update params
                    pass
                
                # if d6 is stopping this frame...
                if d6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d6.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d6.tStop = t  # not accounting for scr refresh
                        d6.tStopRefresh = tThisFlipGlobal  # on global time
                        d6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd6.stopped')
                        # update status
                        d6.status = FINISHED
                        d6.setAutoDraw(False)
                
                # *d7* updates
                
                # if d7 is starting this frame...
                if d7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d7.frameNStart = frameN  # exact frame index
                    d7.tStart = t  # local t and not account for scr refresh
                    d7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd7.started')
                    # update status
                    d7.status = STARTED
                    d7.setAutoDraw(True)
                
                # if d7 is active this frame...
                if d7.status == STARTED:
                    # update params
                    pass
                
                # if d7 is stopping this frame...
                if d7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d7.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d7.tStop = t  # not accounting for scr refresh
                        d7.tStopRefresh = tThisFlipGlobal  # on global time
                        d7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd7.stopped')
                        # update status
                        d7.status = FINISHED
                        d7.setAutoDraw(False)
                
                # *d8* updates
                
                # if d8 is starting this frame...
                if d8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d8.frameNStart = frameN  # exact frame index
                    d8.tStart = t  # local t and not account for scr refresh
                    d8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d8, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd8.started')
                    # update status
                    d8.status = STARTED
                    d8.setAutoDraw(True)
                
                # if d8 is active this frame...
                if d8.status == STARTED:
                    # update params
                    pass
                
                # if d8 is stopping this frame...
                if d8.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d8.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d8.tStop = t  # not accounting for scr refresh
                        d8.tStopRefresh = tThisFlipGlobal  # on global time
                        d8.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd8.stopped')
                        # update status
                        d8.status = FINISHED
                        d8.setAutoDraw(False)
                
                # *d9* updates
                
                # if d9 is starting this frame...
                if d9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d9.frameNStart = frameN  # exact frame index
                    d9.tStart = t  # local t and not account for scr refresh
                    d9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d9, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd9.started')
                    # update status
                    d9.status = STARTED
                    d9.setAutoDraw(True)
                
                # if d9 is active this frame...
                if d9.status == STARTED:
                    # update params
                    pass
                
                # if d9 is stopping this frame...
                if d9.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d9.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d9.tStop = t  # not accounting for scr refresh
                        d9.tStopRefresh = tThisFlipGlobal  # on global time
                        d9.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd9.stopped')
                        # update status
                        d9.status = FINISHED
                        d9.setAutoDraw(False)
                
                # *d10* updates
                
                # if d10 is starting this frame...
                if d10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d10.frameNStart = frameN  # exact frame index
                    d10.tStart = t  # local t and not account for scr refresh
                    d10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d10, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd10.started')
                    # update status
                    d10.status = STARTED
                    d10.setAutoDraw(True)
                
                # if d10 is active this frame...
                if d10.status == STARTED:
                    # update params
                    pass
                
                # if d10 is stopping this frame...
                if d10.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d10.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d10.tStop = t  # not accounting for scr refresh
                        d10.tStopRefresh = tThisFlipGlobal  # on global time
                        d10.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd10.stopped')
                        # update status
                        d10.status = FINISHED
                        d10.setAutoDraw(False)
                
                # *d11* updates
                
                # if d11 is starting this frame...
                if d11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d11.frameNStart = frameN  # exact frame index
                    d11.tStart = t  # local t and not account for scr refresh
                    d11.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d11, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd11.started')
                    # update status
                    d11.status = STARTED
                    d11.setAutoDraw(True)
                
                # if d11 is active this frame...
                if d11.status == STARTED:
                    # update params
                    pass
                
                # if d11 is stopping this frame...
                if d11.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d11.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d11.tStop = t  # not accounting for scr refresh
                        d11.tStopRefresh = tThisFlipGlobal  # on global time
                        d11.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd11.stopped')
                        # update status
                        d11.status = FINISHED
                        d11.setAutoDraw(False)
                
                # *d12* updates
                
                # if d12 is starting this frame...
                if d12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d12.frameNStart = frameN  # exact frame index
                    d12.tStart = t  # local t and not account for scr refresh
                    d12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d12, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd12.started')
                    # update status
                    d12.status = STARTED
                    d12.setAutoDraw(True)
                
                # if d12 is active this frame...
                if d12.status == STARTED:
                    # update params
                    pass
                
                # if d12 is stopping this frame...
                if d12.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d12.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d12.tStop = t  # not accounting for scr refresh
                        d12.tStopRefresh = tThisFlipGlobal  # on global time
                        d12.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd12.stopped')
                        # update status
                        d12.status = FINISHED
                        d12.setAutoDraw(False)
                
                # *d13* updates
                
                # if d13 is starting this frame...
                if d13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d13.frameNStart = frameN  # exact frame index
                    d13.tStart = t  # local t and not account for scr refresh
                    d13.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d13, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd13.started')
                    # update status
                    d13.status = STARTED
                    d13.setAutoDraw(True)
                
                # if d13 is active this frame...
                if d13.status == STARTED:
                    # update params
                    pass
                
                # if d13 is stopping this frame...
                if d13.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d13.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d13.tStop = t  # not accounting for scr refresh
                        d13.tStopRefresh = tThisFlipGlobal  # on global time
                        d13.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd13.stopped')
                        # update status
                        d13.status = FINISHED
                        d13.setAutoDraw(False)
                
                # *d14* updates
                
                # if d14 is starting this frame...
                if d14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d14.frameNStart = frameN  # exact frame index
                    d14.tStart = t  # local t and not account for scr refresh
                    d14.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d14, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd14.started')
                    # update status
                    d14.status = STARTED
                    d14.setAutoDraw(True)
                
                # if d14 is active this frame...
                if d14.status == STARTED:
                    # update params
                    pass
                
                # if d14 is stopping this frame...
                if d14.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d14.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d14.tStop = t  # not accounting for scr refresh
                        d14.tStopRefresh = tThisFlipGlobal  # on global time
                        d14.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd14.stopped')
                        # update status
                        d14.status = FINISHED
                        d14.setAutoDraw(False)
                
                # *d15* updates
                
                # if d15 is starting this frame...
                if d15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d15.frameNStart = frameN  # exact frame index
                    d15.tStart = t  # local t and not account for scr refresh
                    d15.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d15, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd15.started')
                    # update status
                    d15.status = STARTED
                    d15.setAutoDraw(True)
                
                # if d15 is active this frame...
                if d15.status == STARTED:
                    # update params
                    pass
                
                # if d15 is stopping this frame...
                if d15.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d15.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d15.tStop = t  # not accounting for scr refresh
                        d15.tStopRefresh = tThisFlipGlobal  # on global time
                        d15.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd15.stopped')
                        # update status
                        d15.status = FINISHED
                        d15.setAutoDraw(False)
                
                # *d16* updates
                
                # if d16 is starting this frame...
                if d16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d16.frameNStart = frameN  # exact frame index
                    d16.tStart = t  # local t and not account for scr refresh
                    d16.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d16, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd16.started')
                    # update status
                    d16.status = STARTED
                    d16.setAutoDraw(True)
                
                # if d16 is active this frame...
                if d16.status == STARTED:
                    # update params
                    pass
                
                # if d16 is stopping this frame...
                if d16.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d16.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d16.tStop = t  # not accounting for scr refresh
                        d16.tStopRefresh = tThisFlipGlobal  # on global time
                        d16.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd16.stopped')
                        # update status
                        d16.status = FINISHED
                        d16.setAutoDraw(False)
                
                # *d17* updates
                
                # if d17 is starting this frame...
                if d17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d17.frameNStart = frameN  # exact frame index
                    d17.tStart = t  # local t and not account for scr refresh
                    d17.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d17, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd17.started')
                    # update status
                    d17.status = STARTED
                    d17.setAutoDraw(True)
                
                # if d17 is active this frame...
                if d17.status == STARTED:
                    # update params
                    pass
                
                # if d17 is stopping this frame...
                if d17.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d17.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d17.tStop = t  # not accounting for scr refresh
                        d17.tStopRefresh = tThisFlipGlobal  # on global time
                        d17.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd17.stopped')
                        # update status
                        d17.status = FINISHED
                        d17.setAutoDraw(False)
                
                # *d18* updates
                
                # if d18 is starting this frame...
                if d18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d18.frameNStart = frameN  # exact frame index
                    d18.tStart = t  # local t and not account for scr refresh
                    d18.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d18, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd18.started')
                    # update status
                    d18.status = STARTED
                    d18.setAutoDraw(True)
                
                # if d18 is active this frame...
                if d18.status == STARTED:
                    # update params
                    pass
                
                # if d18 is stopping this frame...
                if d18.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d18.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d18.tStop = t  # not accounting for scr refresh
                        d18.tStopRefresh = tThisFlipGlobal  # on global time
                        d18.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd18.stopped')
                        # update status
                        d18.status = FINISHED
                        d18.setAutoDraw(False)
                
                # *d19* updates
                
                # if d19 is starting this frame...
                if d19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d19.frameNStart = frameN  # exact frame index
                    d19.tStart = t  # local t and not account for scr refresh
                    d19.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d19, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd19.started')
                    # update status
                    d19.status = STARTED
                    d19.setAutoDraw(True)
                
                # if d19 is active this frame...
                if d19.status == STARTED:
                    # update params
                    pass
                
                # if d19 is stopping this frame...
                if d19.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d19.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d19.tStop = t  # not accounting for scr refresh
                        d19.tStopRefresh = tThisFlipGlobal  # on global time
                        d19.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd19.stopped')
                        # update status
                        d19.status = FINISHED
                        d19.setAutoDraw(False)
                
                # *d20* updates
                
                # if d20 is starting this frame...
                if d20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d20.frameNStart = frameN  # exact frame index
                    d20.tStart = t  # local t and not account for scr refresh
                    d20.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d20, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd20.started')
                    # update status
                    d20.status = STARTED
                    d20.setAutoDraw(True)
                
                # if d20 is active this frame...
                if d20.status == STARTED:
                    # update params
                    pass
                
                # if d20 is stopping this frame...
                if d20.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d20.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d20.tStop = t  # not accounting for scr refresh
                        d20.tStopRefresh = tThisFlipGlobal  # on global time
                        d20.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd20.stopped')
                        # update status
                        d20.status = FINISHED
                        d20.setAutoDraw(False)
                
                # *d21* updates
                
                # if d21 is starting this frame...
                if d21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d21.frameNStart = frameN  # exact frame index
                    d21.tStart = t  # local t and not account for scr refresh
                    d21.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d21, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd21.started')
                    # update status
                    d21.status = STARTED
                    d21.setAutoDraw(True)
                
                # if d21 is active this frame...
                if d21.status == STARTED:
                    # update params
                    pass
                
                # if d21 is stopping this frame...
                if d21.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d21.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d21.tStop = t  # not accounting for scr refresh
                        d21.tStopRefresh = tThisFlipGlobal  # on global time
                        d21.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd21.stopped')
                        # update status
                        d21.status = FINISHED
                        d21.setAutoDraw(False)
                
                # *d22* updates
                
                # if d22 is starting this frame...
                if d22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d22.frameNStart = frameN  # exact frame index
                    d22.tStart = t  # local t and not account for scr refresh
                    d22.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d22, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd22.started')
                    # update status
                    d22.status = STARTED
                    d22.setAutoDraw(True)
                
                # if d22 is active this frame...
                if d22.status == STARTED:
                    # update params
                    pass
                
                # if d22 is stopping this frame...
                if d22.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d22.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d22.tStop = t  # not accounting for scr refresh
                        d22.tStopRefresh = tThisFlipGlobal  # on global time
                        d22.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd22.stopped')
                        # update status
                        d22.status = FINISHED
                        d22.setAutoDraw(False)
                
                # *d23* updates
                
                # if d23 is starting this frame...
                if d23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d23.frameNStart = frameN  # exact frame index
                    d23.tStart = t  # local t and not account for scr refresh
                    d23.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d23, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd23.started')
                    # update status
                    d23.status = STARTED
                    d23.setAutoDraw(True)
                
                # if d23 is active this frame...
                if d23.status == STARTED:
                    # update params
                    pass
                
                # if d23 is stopping this frame...
                if d23.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d23.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d23.tStop = t  # not accounting for scr refresh
                        d23.tStopRefresh = tThisFlipGlobal  # on global time
                        d23.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd23.stopped')
                        # update status
                        d23.status = FINISHED
                        d23.setAutoDraw(False)
                
                # *d24* updates
                
                # if d24 is starting this frame...
                if d24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d24.frameNStart = frameN  # exact frame index
                    d24.tStart = t  # local t and not account for scr refresh
                    d24.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d24, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd24.started')
                    # update status
                    d24.status = STARTED
                    d24.setAutoDraw(True)
                
                # if d24 is active this frame...
                if d24.status == STARTED:
                    # update params
                    pass
                
                # if d24 is stopping this frame...
                if d24.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d24.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d24.tStop = t  # not accounting for scr refresh
                        d24.tStopRefresh = tThisFlipGlobal  # on global time
                        d24.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd24.stopped')
                        # update status
                        d24.status = FINISHED
                        d24.setAutoDraw(False)
                
                # *d25* updates
                
                # if d25 is starting this frame...
                if d25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    d25.frameNStart = frameN  # exact frame index
                    d25.tStart = t  # local t and not account for scr refresh
                    d25.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(d25, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd25.started')
                    # update status
                    d25.status = STARTED
                    d25.setAutoDraw(True)
                
                # if d25 is active this frame...
                if d25.status == STARTED:
                    # update params
                    pass
                
                # if d25 is stopping this frame...
                if d25.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > d25.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        d25.tStop = t  # not accounting for scr refresh
                        d25.tStopRefresh = tThisFlipGlobal  # on global time
                        d25.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'd25.stopped')
                        # update status
                        d25.status = FINISHED
                        d25.setAutoDraw(False)
                
                # *q_text* updates
                
                # if q_text is starting this frame...
                if q_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    q_text.frameNStart = frameN  # exact frame index
                    q_text.tStart = t  # local t and not account for scr refresh
                    q_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(q_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'q_text.started')
                    # update status
                    q_text.status = STARTED
                    q_text.setAutoDraw(True)
                
                # if q_text is active this frame...
                if q_text.status == STARTED:
                    # update params
                    pass
                
                # if q_text is stopping this frame...
                if q_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > q_text.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        q_text.tStop = t  # not accounting for scr refresh
                        q_text.tStopRefresh = tThisFlipGlobal  # on global time
                        q_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'q_text.stopped')
                        # update status
                        q_text.status = FINISHED
                        q_text.setAutoDraw(False)
                
                # *q_resp* updates
                waitOnFlip = False
                
                # if q_resp is starting this frame...
                if q_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    q_resp.frameNStart = frameN  # exact frame index
                    q_resp.tStart = t  # local t and not account for scr refresh
                    q_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(q_resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'q_resp.started')
                    # update status
                    q_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(q_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(q_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if q_resp is stopping this frame...
                if q_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > q_resp.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        q_resp.tStop = t  # not accounting for scr refresh
                        q_resp.tStopRefresh = tThisFlipGlobal  # on global time
                        q_resp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'q_resp.stopped')
                        # update status
                        q_resp.status = FINISHED
                        q_resp.status = FINISHED
                if q_resp.status == STARTED and not waitOnFlip:
                    theseKeys = q_resp.getKeys(keyList=['1','2'], ignoreKeys=["escape"], waitRelease=False)
                    _q_resp_allKeys.extend(theseKeys)
                    if len(_q_resp_allKeys):
                        q_resp.keys = _q_resp_allKeys[-1].name  # just the last key pressed
                        q_resp.rt = _q_resp_allKeys[-1].rt
                        q_resp.duration = _q_resp_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=trial,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    trial.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if trial.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in trial.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial" ---
            for thisComponent in trial.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial
            trial.tStop = globalClock.getTime(format='float')
            trial.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial.stopped', trial.tStop)
            # Run 'End Routine' code from code
            thisExp.addData('d1_angle', d1_angle);
            thisExp.addData('d2_angle', d2_angle);
            thisExp.addData('d3_angle', d3_angle);
            thisExp.addData('d4_angle', d4_angle);
            thisExp.addData('d5_angle', d5_angle);
            thisExp.addData('d6_angle', d6_angle);
            thisExp.addData('d7_angle', d7_angle);
            thisExp.addData('d8_angle', d8_angle);
            thisExp.addData('d9_angle', d9_angle);
            thisExp.addData('d10_angle', d10_angle);
            thisExp.addData('d11_angle', d11_angle);
            thisExp.addData('d12_angle', d12_angle);
            thisExp.addData('d13_angle', d13_angle);
            thisExp.addData('d14_angle', d14_angle);
            thisExp.addData('d15_angle', d15_angle);
            thisExp.addData('d16_angle', d16_angle);
            thisExp.addData('d17_angle', d17_angle);
            thisExp.addData('d18_angle', d18_angle);
            thisExp.addData('d19_angle', d19_angle);
            thisExp.addData('d20_angle', d20_angle);
            thisExp.addData('d21_angle', d21_angle);
            thisExp.addData('d22_angle', d22_angle);
            thisExp.addData('d23_angle', d23_angle);
            thisExp.addData('d24_angle', d24_angle);
            thisExp.addData('d25_angle', d25_angle);
            
            type1_resp = 999; #placeholder for missed trial
            trial_correct = 999;
            if q_resp.keys =='1':
                type1_resp = -1;
            elif q_resp.keys == '2':
                type1_resp = 1;
            
            if type1_resp ==999:
                trial_correct = 999;
            elif type1_resp ==direction:
                trial_correct = 1;
            else:
                trial_correct = 0;
                
            thisExp.addData('type1_resp', type1_resp);
            thisExp.addData('trial_correct', trial_correct);
            # check responses
            if q_resp.keys in ['', [], None]:  # No response was made
                q_resp.keys = None
            trials.addData('q_resp.keys',q_resp.keys)
            if q_resp.keys != None:  # we had a response
                trials.addData('q_resp.rt', q_resp.rt)
                trials.addData('q_resp.duration', q_resp.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial.maxDurationReached:
                routineTimer.addTime(-trial.maxDuration)
            elif trial.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-4.000000)
            
            # --- Prepare to start Routine "blank" ---
            # create an object to store info about Routine blank
            blank = data.Routine(
                name='blank',
                components=[blank_text],
            )
            blank.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for blank
            blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            blank.tStart = globalClock.getTime(format='float')
            blank.status = STARTED
            thisExp.addData('blank.started', blank.tStart)
            blank.maxDuration = None
            # keep track of which components have finished
            blankComponents = blank.components
            for thisComponent in blank.components:
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
            
            # --- Run Routine "blank" ---
            thisExp.currentRoutine = blank
            blank.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.5:
                # if trial has changed, end Routine now
                if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *blank_text* updates
                
                # if blank_text is starting this frame...
                if blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blank_text.frameNStart = frameN  # exact frame index
                    blank_text.tStart = t  # local t and not account for scr refresh
                    blank_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blank_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'blank_text.started')
                    # update status
                    blank_text.status = STARTED
                    blank_text.setAutoDraw(True)
                
                # if blank_text is active this frame...
                if blank_text.status == STARTED:
                    # update params
                    pass
                
                # if blank_text is stopping this frame...
                if blank_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > blank_text.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        blank_text.tStop = t  # not accounting for scr refresh
                        blank_text.tStopRefresh = tThisFlipGlobal  # on global time
                        blank_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'blank_text.stopped')
                        # update status
                        blank_text.status = FINISHED
                        blank_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=blank,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    blank.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if blank.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in blank.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "blank" ---
            for thisComponent in blank.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for blank
            blank.tStop = globalClock.getTime(format='float')
            blank.tStopRefresh = tThisFlipGlobal
            thisExp.addData('blank.stopped', blank.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if blank.maxDurationReached:
                routineTimer.addTime(-blank.maxDuration)
            elif blank.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            
            # --- Prepare to start Routine "type2_q" ---
            # create an object to store info about Routine type2_q
            type2_q = data.Routine(
                name='type2_q',
                components=[type2_q_text, text_below, type2_q_key_resp, line, marker, type2_mouse, low_text, high_text],
            )
            type2_q.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for type2_q_key_resp
            type2_q_key_resp.keys = []
            type2_q_key_resp.rt = []
            _type2_q_key_resp_allKeys = []
            # Run 'Begin Routine' code from code_2
            confidence_marker = 999;
            confidence_submitted=0;
            high_or_low = 0;
            
            if blockCode!=2: #only display this routine in the final 'one trial' block, denoted as block code 2
                continueRoutine = False;
            
            # setup some python lists for storing info about the type2_mouse
            type2_mouse.x = []
            type2_mouse.y = []
            type2_mouse.leftButton = []
            type2_mouse.midButton = []
            type2_mouse.rightButton = []
            type2_mouse.time = []
            gotValidClick = False  # until a click is received
            # store start times for type2_q
            type2_q.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            type2_q.tStart = globalClock.getTime(format='float')
            type2_q.status = STARTED
            thisExp.addData('type2_q.started', type2_q.tStart)
            type2_q.maxDuration = None
            # keep track of which components have finished
            type2_qComponents = type2_q.components
            for thisComponent in type2_q.components:
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
            
            # --- Run Routine "type2_q" ---
            thisExp.currentRoutine = type2_q
            type2_q.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *type2_q_text* updates
                
                # if type2_q_text is starting this frame...
                if type2_q_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    type2_q_text.frameNStart = frameN  # exact frame index
                    type2_q_text.tStart = t  # local t and not account for scr refresh
                    type2_q_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(type2_q_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'type2_q_text.started')
                    # update status
                    type2_q_text.status = STARTED
                    type2_q_text.setAutoDraw(True)
                
                # if type2_q_text is active this frame...
                if type2_q_text.status == STARTED:
                    # update params
                    pass
                
                # *text_below* updates
                
                # if text_below is starting this frame...
                if text_below.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_below.frameNStart = frameN  # exact frame index
                    text_below.tStart = t  # local t and not account for scr refresh
                    text_below.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_below, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_below.started')
                    # update status
                    text_below.status = STARTED
                    text_below.setAutoDraw(True)
                
                # if text_below is active this frame...
                if text_below.status == STARTED:
                    # update params
                    pass
                
                # *type2_q_key_resp* updates
                waitOnFlip = False
                
                # if type2_q_key_resp is starting this frame...
                if type2_q_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    type2_q_key_resp.frameNStart = frameN  # exact frame index
                    type2_q_key_resp.tStart = t  # local t and not account for scr refresh
                    type2_q_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(type2_q_key_resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'type2_q_key_resp.started')
                    # update status
                    type2_q_key_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(type2_q_key_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(type2_q_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if type2_q_key_resp.status == STARTED and not waitOnFlip:
                    theseKeys = type2_q_key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _type2_q_key_resp_allKeys.extend(theseKeys)
                    if len(_type2_q_key_resp_allKeys):
                        type2_q_key_resp.keys = _type2_q_key_resp_allKeys[-1].name  # just the last key pressed
                        type2_q_key_resp.rt = _type2_q_key_resp_allKeys[-1].rt
                        type2_q_key_resp.duration = _type2_q_key_resp_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # *line* updates
                
                # if line is starting this frame...
                if line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    line.frameNStart = frameN  # exact frame index
                    line.tStart = t  # local t and not account for scr refresh
                    line.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(line, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'line.started')
                    # update status
                    line.status = STARTED
                    line.setAutoDraw(True)
                
                # if line is active this frame...
                if line.status == STARTED:
                    # update params
                    pass
                
                # *marker* updates
                
                # if marker is starting this frame...
                if marker.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    marker.frameNStart = frameN  # exact frame index
                    marker.tStart = t  # local t and not account for scr refresh
                    marker.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(marker, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'marker.started')
                    # update status
                    marker.status = STARTED
                    marker.setAutoDraw(True)
                
                # if marker is active this frame...
                if marker.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from code_2
                mouse_pos = type2_mouse.getPos();
                mouse_y = mouse_pos[1];
                if mouse_y>.075:
                    mouse_y=.075;
                
                if mouse_y<-.075:
                    mouse_y=-.075
                marker.setPos((0,mouse_y));
                # *type2_mouse* updates
                
                # if type2_mouse is starting this frame...
                if type2_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    type2_mouse.frameNStart = frameN  # exact frame index
                    type2_mouse.tStart = t  # local t and not account for scr refresh
                    type2_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(type2_mouse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('type2_mouse.started', t)
                    # update status
                    type2_mouse.status = STARTED
                    type2_mouse.mouseClock.reset()
                    # if now button is down we will treat as 'new' click
                    type2_mouse.prevButtonState = [0, 0, 0]
                if type2_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = type2_mouse.getPressed()
                    # button state changed?
                    if buttons != type2_mouse.prevButtonState:
                        type2_mouse.prevButtonState = buttons
                        # state changed to a new click
                        if sum(buttons) > 0:
                            pass
                            x, y = type2_mouse.getPos()
                            type2_mouse.x.append(float(x))
                            type2_mouse.y.append(float(y))
                            buttons = type2_mouse.getPressed()
                            type2_mouse.leftButton.append(buttons[0])
                            type2_mouse.midButton.append(buttons[1])
                            type2_mouse.rightButton.append(buttons[2])
                            type2_mouse.time.append(type2_mouse.mouseClock.getTime())
                
                # *low_text* updates
                
                # if low_text is starting this frame...
                if low_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    low_text.frameNStart = frameN  # exact frame index
                    low_text.tStart = t  # local t and not account for scr refresh
                    low_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(low_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'low_text.started')
                    # update status
                    low_text.status = STARTED
                    low_text.setAutoDraw(True)
                
                # if low_text is active this frame...
                if low_text.status == STARTED:
                    # update params
                    pass
                
                # *high_text* updates
                
                # if high_text is starting this frame...
                if high_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    high_text.frameNStart = frameN  # exact frame index
                    high_text.tStart = t  # local t and not account for scr refresh
                    high_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(high_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'high_text.started')
                    # update status
                    high_text.status = STARTED
                    high_text.setAutoDraw(True)
                
                # if high_text is active this frame...
                if high_text.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=type2_q,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    type2_q.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if type2_q.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in type2_q.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "type2_q" ---
            for thisComponent in type2_q.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for type2_q
            type2_q.tStop = globalClock.getTime(format='float')
            type2_q.tStopRefresh = tThisFlipGlobal
            thisExp.addData('type2_q.stopped', type2_q.tStop)
            # check responses
            if type2_q_key_resp.keys in ['', [], None]:  # No response was made
                type2_q_key_resp.keys = None
            trials.addData('type2_q_key_resp.keys',type2_q_key_resp.keys)
            if type2_q_key_resp.keys != None:  # we had a response
                trials.addData('type2_q_key_resp.rt', type2_q_key_resp.rt)
                trials.addData('type2_q_key_resp.duration', type2_q_key_resp.duration)
            # Run 'End Routine' code from code_2
            if type2_q_key_resp.keys =='space':
                confidence_submitted=1;
            
            confidence_marker = int(mouse_y[0])
            
            '''
            if blockCode!=-1:
                thisExp.addData('confidence_marker', confidence_marker)
            if confidence_marker >= 0.05625:
                high_confidence = high_confidence+0.5
            if confidence_marker == 0.075:
                high_confidence = high_confidence+1
            
            if confidence_marker <= -0.05625:
                low_confidence = low_confidence+0.05
            if confidence_marker == 0.05625:
                low_confidence = low_confidence+1
                '''
                
            if blockCode!=-1:
                thisExp.addData('confidence_marker', confidence_marker)
            if confidence_marker > 0:
                high_or_low = 1 #1 = high conf
            if confidence_marker < 0:
                high_or_low = -1
            # store data for trials (TrialHandler)
            trials.addData('type2_mouse.x', type2_mouse.x)
            trials.addData('type2_mouse.y', type2_mouse.y)
            trials.addData('type2_mouse.leftButton', type2_mouse.leftButton)
            trials.addData('type2_mouse.midButton', type2_mouse.midButton)
            trials.addData('type2_mouse.rightButton', type2_mouse.rightButton)
            trials.addData('type2_mouse.time', type2_mouse.time)
            # the Routine "type2_q" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback" ---
            # create an object to store info about Routine feedback
            feedback = data.Routine(
                name='feedback',
                components=[feedback_text],
            )
            feedback.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_6
            if blockCode>0:
                continueRoutine = False;
                
            
            
            
            if trial_correct ==1:
                feedback_str = 'Correct!';
                points_str = '+10 points';
            elif trial_correct==0:
                feedback_str = 'Incorrect';
                points_str = '0 points';
            elif trial_correct ==999:
                feedback_str = 'Too slow!';
                
            if confidence_submitted ==999:
                feedback_str = 'Too slow!';
            feedback_text.setText(feedback_str);
            # store start times for feedback
            feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback.tStart = globalClock.getTime(format='float')
            feedback.status = STARTED
            thisExp.addData('feedback.started', feedback.tStart)
            feedback.maxDuration = None
            # keep track of which components have finished
            feedbackComponents = feedback.components
            for thisComponent in feedback.components:
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
            
            # --- Run Routine "feedback" ---
            thisExp.currentRoutine = feedback
            feedback.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.5:
                # if trial has changed, end Routine now
                if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feedback_text* updates
                
                # if feedback_text is starting this frame...
                if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_text.frameNStart = frameN  # exact frame index
                    feedback_text.tStart = t  # local t and not account for scr refresh
                    feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text.started')
                    # update status
                    feedback_text.status = STARTED
                    feedback_text.setAutoDraw(True)
                
                # if feedback_text is active this frame...
                if feedback_text.status == STARTED:
                    # update params
                    pass
                
                # if feedback_text is stopping this frame...
                if feedback_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > feedback_text.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        feedback_text.tStop = t  # not accounting for scr refresh
                        feedback_text.tStopRefresh = tThisFlipGlobal  # on global time
                        feedback_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_text.stopped')
                        # update status
                        feedback_text.status = FINISHED
                        feedback_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=feedback,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    feedback.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if feedback.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in feedback.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback" ---
            for thisComponent in feedback.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback
            feedback.tStop = globalClock.getTime(format='float')
            feedback.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback.stopped', feedback.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if feedback.maxDurationReached:
                routineTimer.addTime(-feedback.maxDuration)
            elif feedback.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            # mark thisTrial as finished
            if hasattr(thisTrial, 'status'):
                thisTrial.status = FINISHED
            # if awaiting a pause, pause now
            if trials.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                trials.status = STARTED
            thisExp.nextEntry()
            
        # completed trialReps repeats of 'trials'
        trials.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # mark thisBlock as finished
        if hasattr(thisBlock, 'status'):
            thisBlock.status = FINISHED
        # if awaiting a pause, pause now
        if Blocks.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            Blocks.status = STARTED
    # completed 1.0 repeats of 'Blocks'
    Blocks.status = FINISHED
    
    
    # --- Prepare to start Routine "Bonus" ---
    # create an object to store info about Routine Bonus
    Bonus = data.Routine(
        name='Bonus',
        components=[text_4, bonus_sum],
    )
    Bonus.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_9
    
    if trial_correct == 1 and high_or_low == 1:
        bonus_score += 1
        bonus_str = '50p bonus';
    elif trial_correct==1 and high_or_low == -1:
        bonus_score += 1
        bonus_str = '50p bonus';
    else:
        bonus_str = 'Sorry no bonus'
    
    bonus_sum.setText(bonus_str);
    
    # store start times for Bonus
    Bonus.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Bonus.tStart = globalClock.getTime(format='float')
    Bonus.status = STARTED
    thisExp.addData('Bonus.started', Bonus.tStart)
    Bonus.maxDuration = None
    # keep track of which components have finished
    BonusComponents = Bonus.components
    for thisComponent in Bonus.components:
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
    
    # --- Run Routine "Bonus" ---
    thisExp.currentRoutine = Bonus
    Bonus.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.tStopRefresh = tThisFlipGlobal  # on global time
                text_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.stopped')
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # *bonus_sum* updates
        
        # if bonus_sum is starting this frame...
        if bonus_sum.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bonus_sum.frameNStart = frameN  # exact frame index
            bonus_sum.tStart = t  # local t and not account for scr refresh
            bonus_sum.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bonus_sum, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bonus_sum.started')
            # update status
            bonus_sum.status = STARTED
            bonus_sum.setAutoDraw(True)
        
        # if bonus_sum is active this frame...
        if bonus_sum.status == STARTED:
            # update params
            pass
        
        # if bonus_sum is stopping this frame...
        if bonus_sum.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bonus_sum.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                bonus_sum.tStop = t  # not accounting for scr refresh
                bonus_sum.tStopRefresh = tThisFlipGlobal  # on global time
                bonus_sum.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bonus_sum.stopped')
                # update status
                bonus_sum.status = FINISHED
                bonus_sum.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Bonus,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            Bonus.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if Bonus.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in Bonus.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Bonus" ---
    for thisComponent in Bonus.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Bonus
    Bonus.tStop = globalClock.getTime(format='float')
    Bonus.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Bonus.stopped', Bonus.tStop)
    # Run 'End Routine' code from code_9
    thisExp.addData('bonus_score', bonus_score);
    thisExp.addData('high_or_low', high_or_low);
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Bonus.maxDurationReached:
        routineTimer.addTime(-Bonus.maxDuration)
    elif Bonus.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "thanks" ---
    # create an object to store info about Routine thanks
    thanks = data.Routine(
        name='thanks',
        components=[text_3],
    )
    thanks.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for thanks
    thanks.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    thanks.tStart = globalClock.getTime(format='float')
    thanks.status = STARTED
    thisExp.addData('thanks.started', thanks.tStart)
    thanks.maxDuration = None
    # keep track of which components have finished
    thanksComponents = thanks.components
    for thisComponent in thanks.components:
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
    
    # --- Run Routine "thanks" ---
    thisExp.currentRoutine = thanks
    thanks.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=thanks,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            thanks.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if thanks.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in thanks.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "thanks" ---
    for thisComponent in thanks.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for thanks
    thanks.tStop = globalClock.getTime(format='float')
    thanks.tStopRefresh = tThisFlipGlobal
    thisExp.addData('thanks.stopped', thanks.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if thanks.maxDurationReached:
        routineTimer.addTime(-thanks.maxDuration)
    elif thanks.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
