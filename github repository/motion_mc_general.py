/****************** 
 * Motion_Mc *
 ******************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2026.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'motion_mc';  // from the Builder filename that created this script
let expInfo = {
    'participant': '123',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1), (- 1), (- 1)]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(main_instructionsRoutineBegin());
flowScheduler.add(main_instructionsRoutineEachFrame());
flowScheduler.add(main_instructionsRoutineEnd());
const BlocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(BlocksLoopBegin(BlocksLoopScheduler));
flowScheduler.add(BlocksLoopScheduler);
flowScheduler.add(BlocksLoopEnd);












flowScheduler.add(BonusRoutineBegin());
flowScheduler.add(BonusRoutineEachFrame());
flowScheduler.add(BonusRoutineEnd());
flowScheduler.add(thanksRoutineBegin());
flowScheduler.add(thanksRoutineEachFrame());
flowScheduler.add(thanksRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'blocks_ot.csv', 'path': 'blocks_ot.csv'},
    {'name': 'motionTrials_ot.csv', 'path': 'motionTrials_ot.csv'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2026.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('www.danielyon.com', '');


  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "main_instructions"
  main_instructionsClock = new util.Clock();
  main_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'main_text',
    text: 'Welcome to the experiment!\n\nIn this task, we will show you patterns of moving dots - and you will make judgments about the direction in which the dots are moving.\n\nAt some point in the experiment, we will also ask you to provide an additional rating.\n\nPress SPACE to continue. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  main_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "block_instructions"
  block_instructionsClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Placeholder',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  block_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Comprehension_check"
  Comprehension_checkClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'I understand that at some point I may be asked to make an additional rating, and that this will be used to calculate my bonus payment. \n\nPlease indicate your response by pressing one of the following:\n\nn = No\ny = Yes',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Comprehension = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  polygon = new visual.ShapeStim ({
    win: psychoJS.window, name: 'polygon', 
    vertices: 'cross', size:[0.03, 0.03],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: 0, 
    interpolate: true, 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  import * as numpy from 'numpy';
  step = 0.04;
  signal1 = 0.04;
  signal2 = 0.2;
  signal3 = 0.36;
  signal4 = 0.5;
  trial_count = 0;
  
  d1 = new visual.Polygon({
    win: psychoJS.window, name: 'd1', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -1, 
    interpolate: true, 
  });
  
  d2 = new visual.Polygon({
    win: psychoJS.window, name: 'd2', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -2, 
    interpolate: true, 
  });
  
  d3 = new visual.Polygon({
    win: psychoJS.window, name: 'd3', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -3, 
    interpolate: true, 
  });
  
  d4 = new visual.Polygon({
    win: psychoJS.window, name: 'd4', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -4, 
    interpolate: true, 
  });
  
  d5 = new visual.Polygon({
    win: psychoJS.window, name: 'd5', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -5, 
    interpolate: true, 
  });
  
  d6 = new visual.Polygon({
    win: psychoJS.window, name: 'd6', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -6, 
    interpolate: true, 
  });
  
  d7 = new visual.Polygon({
    win: psychoJS.window, name: 'd7', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -7, 
    interpolate: true, 
  });
  
  d8 = new visual.Polygon({
    win: psychoJS.window, name: 'd8', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -8, 
    interpolate: true, 
  });
  
  d9 = new visual.Polygon({
    win: psychoJS.window, name: 'd9', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -9, 
    interpolate: true, 
  });
  
  d10 = new visual.Polygon({
    win: psychoJS.window, name: 'd10', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -10, 
    interpolate: true, 
  });
  
  d11 = new visual.Polygon({
    win: psychoJS.window, name: 'd11', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -11, 
    interpolate: true, 
  });
  
  d12 = new visual.Polygon({
    win: psychoJS.window, name: 'd12', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -12, 
    interpolate: true, 
  });
  
  d13 = new visual.Polygon({
    win: psychoJS.window, name: 'd13', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -13, 
    interpolate: true, 
  });
  
  d14 = new visual.Polygon({
    win: psychoJS.window, name: 'd14', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -14, 
    interpolate: true, 
  });
  
  d15 = new visual.Polygon({
    win: psychoJS.window, name: 'd15', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -15, 
    interpolate: true, 
  });
  
  d16 = new visual.Polygon({
    win: psychoJS.window, name: 'd16', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -16, 
    interpolate: true, 
  });
  
  d17 = new visual.Polygon({
    win: psychoJS.window, name: 'd17', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -17, 
    interpolate: true, 
  });
  
  d18 = new visual.Polygon({
    win: psychoJS.window, name: 'd18', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -18, 
    interpolate: true, 
  });
  
  d19 = new visual.Polygon({
    win: psychoJS.window, name: 'd19', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -19, 
    interpolate: true, 
  });
  
  d20 = new visual.Polygon({
    win: psychoJS.window, name: 'd20', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -20, 
    interpolate: true, 
  });
  
  d21 = new visual.Polygon({
    win: psychoJS.window, name: 'd21', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -21, 
    interpolate: true, 
  });
  
  d22 = new visual.Polygon({
    win: psychoJS.window, name: 'd22', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -22, 
    interpolate: true, 
  });
  
  d23 = new visual.Polygon({
    win: psychoJS.window, name: 'd23', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -23, 
    interpolate: true, 
  });
  
  d24 = new visual.Polygon({
    win: psychoJS.window, name: 'd24', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -24, 
    interpolate: true, 
  });
  
  d25 = new visual.Polygon({
    win: psychoJS.window, name: 'd25', 
    edges: 100, size:[0.01, 0.01],
    ori: 0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([1, 1, 1]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -25, 
    interpolate: true, 
  });
  
  q_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'q_text',
    text: 'Moving LEFT or RIGHT?\n\n(1 = Left, 2 = Right)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -26.0 
  });
  
  q_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "blank"
  blankClock = new util.Clock();
  blank_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank_text',
    text: ' ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "type2_q"
  type2_qClock = new util.Clock();
  type2_q_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'type2_q_text',
    text: 'How confident are you that YOUR LAST MOTION DECISION was correct?\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_below = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_below',
    text: '(Adjust with mouse, press SPACE to submit)\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  type2_q_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  line = new visual.Rect ({
    win: psychoJS.window, name: 'line', 
    width: [0.005, 0.15][0], height: [0.005, 0.15][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -3, 
    interpolate: true, 
  });
  
  marker = new visual.Polygon({
    win: psychoJS.window, name: 'marker', 
    edges: 100, size:[0.02, 0.02],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('red'), 
    fillColor: new util.Color('red'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -4, 
    interpolate: true, 
  });
  
  type2_mouse = new core.Mouse({
    win: psychoJS.window,
  });
  type2_mouse.mouseClock = new util.Clock();
  low_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'low_text',
    text: 'Lowest\nConfidence',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.12)], draggable: false, height: 0.02,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  high_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'high_text',
    text: 'Highest\nConfidence',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.12], draggable: false, height: 0.02,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: 'placeholder',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Bonus"
  BonusClock = new util.Clock();
  bonus_sum = new visual.TextStim({
    win: psychoJS.window,
    name: 'bonus_sum',
    text: 'Placeholder',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Run 'Begin Experiment' code from code_9
  bonus_score = 0;
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'This is the end of the study.\n\nThank you for taking part.\n\nYou will shortly be automatically redirected to Prolific. Do not close this window before you are prompted, or your data will not be recorded. \n\nIf you would like to get in touch with the research team, please email Prof Daniel Yon at d.yon@bbk.ac.uk\n\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function main_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'main_instructions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    main_instructionsClock.reset();
    routineTimer.reset();
    main_instructionsMaxDurationReached = false;
    // update component parameters for each repeat
    main_resp.keys = undefined;
    main_resp.rt = undefined;
    _main_resp_allKeys = [];
    psychoJS.experiment.addData('main_instructions.started', globalClock.getTime());
    main_instructionsMaxDuration = null
    // keep track of which components have finished
    main_instructionsComponents = [];
    main_instructionsComponents.push(main_text);
    main_instructionsComponents.push(main_resp);
    
    for (const thisComponent of main_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function main_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'main_instructions' ---
    // get current time
    t = main_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *main_text* updates
    if (t >= 0.0 && main_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      main_text.tStart = t;  // (not accounting for frame time here)
      main_text.frameNStart = frameN;  // exact frame index
      
      main_text.setAutoDraw(true);
    }
    
    
    // if main_text is active this frame...
    if (main_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *main_resp* updates
    if (t >= 0.0 && main_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      main_resp.tStart = t;  // (not accounting for frame time here)
      main_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { main_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { main_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { main_resp.clearEvents(); });
    }
    
    // if main_resp is active this frame...
    if (main_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = main_resp.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _main_resp_allKeys = _main_resp_allKeys.concat(theseKeys);
      if (_main_resp_allKeys.length > 0) {
        main_resp.keys = _main_resp_allKeys[_main_resp_allKeys.length - 1].name;  // just the last key pressed
        main_resp.rt = _main_resp_allKeys[_main_resp_allKeys.length - 1].rt;
        main_resp.duration = _main_resp_allKeys[_main_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of main_instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function main_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'main_instructions' ---
    for (const thisComponent of main_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('main_instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(main_resp.corr, level);
    }
    psychoJS.experiment.addData('main_resp.keys', main_resp.keys);
    if (typeof main_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('main_resp.rt', main_resp.rt);
        psychoJS.experiment.addData('main_resp.duration', main_resp.duration);
        routineTimer.reset();
        }
    
    main_resp.stop();
    // the Routine "main_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function BlocksLoopBegin(BlocksLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Blocks = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'blocks_ot.csv',
      seed: undefined, name: 'Blocks'
    });
    psychoJS.experiment.addLoop(Blocks); // add the loop to the experiment
    currentLoop = Blocks;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBlock of Blocks) {
      snapshot = Blocks.getSnapshot();
      BlocksLoopScheduler.add(importConditions(snapshot));
      const trials_2LoopScheduler = new Scheduler(psychoJS);
      BlocksLoopScheduler.add(trials_2LoopBegin(trials_2LoopScheduler, snapshot));
      BlocksLoopScheduler.add(trials_2LoopScheduler);
      BlocksLoopScheduler.add(trials_2LoopEnd);
      const trialsLoopScheduler = new Scheduler(psychoJS);
      BlocksLoopScheduler.add(trialsLoopBegin(trialsLoopScheduler, snapshot));
      BlocksLoopScheduler.add(trialsLoopScheduler);
      BlocksLoopScheduler.add(trialsLoopEnd);
      BlocksLoopScheduler.add(BlocksLoopEndIteration(BlocksLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_2 of trials_2) {
      snapshot = trials_2.getSnapshot();
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(block_instructionsRoutineBegin(snapshot));
      trials_2LoopScheduler.add(block_instructionsRoutineEachFrame());
      trials_2LoopScheduler.add(block_instructionsRoutineEnd(snapshot));
      trials_2LoopScheduler.add(Comprehension_checkRoutineBegin(snapshot));
      trials_2LoopScheduler.add(Comprehension_checkRoutineEachFrame());
      trials_2LoopScheduler.add(Comprehension_checkRoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: trialReps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'motionTrials_ot.csv', rowsUsed),
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(fixationRoutineBegin(snapshot));
      trialsLoopScheduler.add(fixationRoutineEachFrame());
      trialsLoopScheduler.add(fixationRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(blankRoutineBegin(snapshot));
      trialsLoopScheduler.add(blankRoutineEachFrame());
      trialsLoopScheduler.add(blankRoutineEnd(snapshot));
      trialsLoopScheduler.add(type2_qRoutineBegin(snapshot));
      trialsLoopScheduler.add(type2_qRoutineEachFrame());
      trialsLoopScheduler.add(type2_qRoutineEnd(snapshot));
      trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
      trialsLoopScheduler.add(feedbackRoutineEachFrame());
      trialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function BlocksLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Blocks);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function BlocksLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function block_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'block_instructions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    block_instructionsClock.reset();
    routineTimer.reset();
    block_instructionsMaxDurationReached = false;
    // update component parameters for each repeat
    block_resp.keys = undefined;
    block_resp.rt = undefined;
    _block_resp_allKeys = [];
    // Run 'Begin Routine' code from code_3
    if ((blockCode === 2)) {
        continueRoutine = false;
    }
    if ((blockCode === (- 1))) {
        block_str = "First we will practice making judgments about the dot clouds. \n\n You will see a brief cloud of moving dots and have to judge whether the dots moved mostly LEFT or RIGHT using the 1 and 2 keys on your keyboard. \n\n Press SPACE to continue";
    } else {
        if ((blockCode === 1)) {
            block_str = "Now we will begin the main task. This will be same as practice. \n\n However, you will no longer receive trial-by-trial feedback. \n\n IMPORTANTLY, at one point in the task, we will ask you to make an additional rating. \n\n How well your rating matches the accuracy of your answer will determine the performance-related bonus you receive on Prolific. \n\n Press SPACE to continue";
        }
    }
    text.setText(block_str);
    
    psychoJS.experiment.addData('block_instructions.started', globalClock.getTime());
    block_instructionsMaxDuration = null
    // keep track of which components have finished
    block_instructionsComponents = [];
    block_instructionsComponents.push(text);
    block_instructionsComponents.push(block_resp);
    
    for (const thisComponent of block_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function block_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'block_instructions' ---
    // get current time
    t = block_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // if text is active this frame...
    if (text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *block_resp* updates
    if (t >= 0.0 && block_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      block_resp.tStart = t;  // (not accounting for frame time here)
      block_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { block_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { block_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { block_resp.clearEvents(); });
    }
    
    // if block_resp is active this frame...
    if (block_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = block_resp.getKeys({
        keyList: typeof ['space','y','n'] === 'string' ? [['space','y','n']] : ['space','y','n'], 
        waitRelease: false
      });
      _block_resp_allKeys = _block_resp_allKeys.concat(theseKeys);
      if (_block_resp_allKeys.length > 0) {
        block_resp.keys = _block_resp_allKeys[_block_resp_allKeys.length - 1].name;  // just the last key pressed
        block_resp.rt = _block_resp_allKeys[_block_resp_allKeys.length - 1].rt;
        block_resp.duration = _block_resp_allKeys[_block_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of block_instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function block_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'block_instructions' ---
    for (const thisComponent of block_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('block_instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(block_resp.corr, level);
    }
    psychoJS.experiment.addData('block_resp.keys', block_resp.keys);
    if (typeof block_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('block_resp.rt', block_resp.rt);
        psychoJS.experiment.addData('block_resp.duration', block_resp.duration);
        routineTimer.reset();
        }
    
    block_resp.stop();
    // the Routine "block_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function Comprehension_checkRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Comprehension_check' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    Comprehension_checkClock.reset();
    routineTimer.reset();
    Comprehension_checkMaxDurationReached = false;
    // update component parameters for each repeat
    Comprehension.keys = undefined;
    Comprehension.rt = undefined;
    _Comprehension_allKeys = [];
    // Run 'Begin Routine' code from code_8
    if ((blockCode !== 1)) {
        continueRoutine = false;
    }
    
    psychoJS.experiment.addData('Comprehension_check.started', globalClock.getTime());
    Comprehension_checkMaxDuration = null
    // keep track of which components have finished
    Comprehension_checkComponents = [];
    Comprehension_checkComponents.push(text_2);
    Comprehension_checkComponents.push(Comprehension);
    
    for (const thisComponent of Comprehension_checkComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function Comprehension_checkRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Comprehension_check' ---
    // get current time
    t = Comprehension_checkClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    
    // if text_2 is active this frame...
    if (text_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *Comprehension* updates
    if (t >= 0.0 && Comprehension.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Comprehension.tStart = t;  // (not accounting for frame time here)
      Comprehension.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Comprehension.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Comprehension.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Comprehension.clearEvents(); });
    }
    
    // if Comprehension is active this frame...
    if (Comprehension.status === PsychoJS.Status.STARTED) {
      let theseKeys = Comprehension.getKeys({
        keyList: typeof ['y','n'] === 'string' ? [['y','n']] : ['y','n'], 
        waitRelease: false
      });
      _Comprehension_allKeys = _Comprehension_allKeys.concat(theseKeys);
      if (_Comprehension_allKeys.length > 0) {
        Comprehension.keys = _Comprehension_allKeys[_Comprehension_allKeys.length - 1].name;  // just the last key pressed
        Comprehension.rt = _Comprehension_allKeys[_Comprehension_allKeys.length - 1].rt;
        Comprehension.duration = _Comprehension_allKeys[_Comprehension_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Comprehension_checkComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Comprehension_checkRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Comprehension_check' ---
    for (const thisComponent of Comprehension_checkComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Comprehension_check.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Comprehension.corr, level);
    }
    psychoJS.experiment.addData('Comprehension.keys', Comprehension.keys);
    if (typeof Comprehension.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Comprehension.rt', Comprehension.rt);
        psychoJS.experiment.addData('Comprehension.duration', Comprehension.duration);
        routineTimer.reset();
        }
    
    Comprehension.stop();
    // Run 'End Routine' code from code_8
    if ((Comprehension.keys === "y")) {
        trials_2.finished = true;
    }
    
    // the Routine "Comprehension_check" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    fixationClock.reset(routineTimer.getTime());
    routineTimer.add(1.500000);
    fixationMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('fixation.started', globalClock.getTime());
    fixationMaxDuration = null
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(polygon);
    
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function fixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation' ---
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon* updates
    if (t >= 1 && polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon.tStart = t;  // (not accounting for frame time here)
      polygon.frameNStart = frameN;  // exact frame index
      
      polygon.setAutoDraw(true);
    }
    
    
    // if polygon is active this frame...
    if (polygon.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 1 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (polygon.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      polygon.tStop = t;  // not accounting for scr refresh
      polygon.frameNStop = frameN;  // exact frame index
      // update status
      polygon.status = PsychoJS.Status.FINISHED;
      polygon.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function fixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation' ---
    for (const thisComponent of fixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('fixation.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (fixationMaxDurationReached) {
        fixationClock.add(fixationMaxDuration);
    } else {
        fixationClock.add(1.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    trialClock.reset(routineTimer.getTime());
    routineTimer.add(4.000000);
    trialMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code
    trial_count = (trial_count + 1);
    frame = 0;
    mouse_x = ([0] * 10000);
    mouse_y = ([0] * 10000);
    r = 0.15;
    d = (r * 2);
    d1_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d1_dist = ((d * numpy.random.rand()) - r);
    d1_x = (numpy.cos(rand_ang) * d1_dist);
    d1_y = (numpy.sin(rand_ang) * d1_dist);
    d1.setPos([d1_x, d1_y]);
    d2_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d2_dist = ((d * numpy.random.rand()) - r);
    d2_x = (numpy.cos(rand_ang) * d2_dist);
    d2_y = (numpy.sin(rand_ang) * d2_dist);
    d2.setPos([d2_x, d2_y]);
    d3_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d3_dist = ((d * numpy.random.rand()) - r);
    d3_x = (numpy.cos(rand_ang) * d3_dist);
    d3_y = (numpy.sin(rand_ang) * d3_dist);
    d3.setPos([d3_x, d3_y]);
    d4_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d4_dist = ((d * numpy.random.rand()) - r);
    d4_x = (numpy.cos(rand_ang) * d4_dist);
    d4_y = (numpy.sin(rand_ang) * d4_dist);
    d4.setPos([d4_x, d4_y]);
    d5_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d5_dist = ((d * numpy.random.rand()) - r);
    d5_x = (numpy.cos(rand_ang) * d5_dist);
    d5_y = (numpy.sin(rand_ang) * d5_dist);
    d5.setPos([d5_x, d5_y]);
    d6_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d6_dist = ((d * numpy.random.rand()) - r);
    d6_x = (numpy.cos(rand_ang) * d6_dist);
    d6_y = (numpy.sin(rand_ang) * d6_dist);
    d6.setPos([d6_x, d6_y]);
    d7_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d7_dist = ((d * numpy.random.rand()) - r);
    d7_x = (numpy.cos(rand_ang) * d7_dist);
    d7_y = (numpy.sin(rand_ang) * d7_dist);
    d7.setPos([d7_x, d7_y]);
    d8_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d8_dist = ((d * numpy.random.rand()) - r);
    d8_x = (numpy.cos(rand_ang) * d8_dist);
    d8_y = (numpy.sin(rand_ang) * d8_dist);
    d8.setPos([d8_x, d8_y]);
    d9_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d9_dist = ((d * numpy.random.rand()) - r);
    d9_x = (numpy.cos(rand_ang) * d9_dist);
    d9_y = (numpy.sin(rand_ang) * d9_dist);
    d9.setPos([d9_x, d9_y]);
    d10_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d10_dist = ((d * numpy.random.rand()) - r);
    d10_x = (numpy.cos(rand_ang) * d10_dist);
    d10_y = (numpy.sin(rand_ang) * d10_dist);
    d10.setPos([d10_x, d10_y]);
    d11_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d11_dist = ((d * numpy.random.rand()) - r);
    d11_x = (numpy.cos(rand_ang) * d11_dist);
    d11_y = (numpy.sin(rand_ang) * d11_dist);
    d11.setPos([d11_x, d11_y]);
    d12_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d12_dist = ((d * numpy.random.rand()) - r);
    d12_x = (numpy.cos(rand_ang) * d12_dist);
    d12_y = (numpy.sin(rand_ang) * d12_dist);
    d12.setPos([d12_x, d12_y]);
    d13_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d13_dist = ((d * numpy.random.rand()) - r);
    d13_x = (numpy.cos(rand_ang) * d13_dist);
    d13_y = (numpy.sin(rand_ang) * d13_dist);
    d13.setPos([d13_x, d13_y]);
    d14_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d14_dist = ((d * numpy.random.rand()) - r);
    d14_x = (numpy.cos(rand_ang) * d14_dist);
    d14_y = (numpy.sin(rand_ang) * d14_dist);
    d14.setPos([d14_x, d14_y]);
    d15_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d15_dist = ((d * numpy.random.rand()) - r);
    d15_x = (numpy.cos(rand_ang) * d15_dist);
    d15_y = (numpy.sin(rand_ang) * d15_dist);
    d15.setPos([d15_x, d15_y]);
    d16_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d16_dist = ((d * numpy.random.rand()) - r);
    d16_x = (numpy.cos(rand_ang) * d16_dist);
    d16_y = (numpy.sin(rand_ang) * d16_dist);
    d16.setPos([d16_x, d16_y]);
    d17_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d17_dist = ((d * numpy.random.rand()) - r);
    d17_x = (numpy.cos(rand_ang) * d17_dist);
    d17_y = (numpy.sin(rand_ang) * d17_dist);
    d17.setPos([d17_x, d17_y]);
    d18_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d18_dist = ((d * numpy.random.rand()) - r);
    d18_x = (numpy.cos(rand_ang) * d18_dist);
    d18_y = (numpy.sin(rand_ang) * d18_dist);
    d18.setPos([d18_x, d18_y]);
    d19_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d19_dist = ((d * numpy.random.rand()) - r);
    d19_x = (numpy.cos(rand_ang) * d19_dist);
    d19_y = (numpy.sin(rand_ang) * d19_dist);
    d19.setPos([d19_x, d19_y]);
    d20_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d20_dist = ((d * numpy.random.rand()) - r);
    d20_x = (numpy.cos(rand_ang) * d20_dist);
    d20_y = (numpy.sin(rand_ang) * d20_dist);
    d20.setPos([d20_x, d20_y]);
    d21_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d21_dist = ((d * numpy.random.rand()) - r);
    d21_x = (numpy.cos(rand_ang) * d21_dist);
    d21_y = (numpy.sin(rand_ang) * d21_dist);
    d21.setPos([d21_x, d21_y]);
    d22_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d22_dist = ((d * numpy.random.rand()) - r);
    d22_x = (numpy.cos(rand_ang) * d22_dist);
    d22_y = (numpy.sin(rand_ang) * d22_dist);
    d22.setPos([d22_x, d22_y]);
    d23_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d23_dist = ((d * numpy.random.rand()) - r);
    d23_x = (numpy.cos(rand_ang) * d23_dist);
    d23_y = (numpy.sin(rand_ang) * d23_dist);
    d23.setPos([d23_x, d23_y]);
    d24_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d24_dist = ((d * numpy.random.rand()) - r);
    d24_x = (numpy.cos(rand_ang) * d24_dist);
    d24_y = (numpy.sin(rand_ang) * d24_dist);
    d24.setPos([d24_x, d24_y]);
    d25_angle = ((2 * 3.14) * numpy.random.rand());
    rand_ang = ((2 * 3.14) * numpy.random.rand());
    d25_dist = ((d * numpy.random.rand()) - r);
    d25_x = (numpy.cos(rand_ang) * d25_dist);
    d25_y = (numpy.sin(rand_ang) * d25_dist);
    d25.setPos([d25_x, d25_y]);
    if ((strength === 1)) {
        signal = signal1;
    } else {
        if ((strength === 2)) {
            signal = signal2;
        } else {
            if ((strength === 3)) {
                signal = signal3;
            } else {
                if ((strength === 4)) {
                    signal = signal4;
                }
            }
        }
    }
    if ((signal >= (1 * step))) {
        d1_angle = 0;
    }
    if ((signal >= (2 * step))) {
        d2_angle = 0;
    }
    if ((signal >= (3 * step))) {
        d3_angle = 0;
    }
    if ((signal >= (4 * step))) {
        d4_angle = 0;
    }
    if ((signal >= (5 * step))) {
        d5_angle = 0;
    }
    if ((signal >= (6 * step))) {
        d6_angle = 0;
    }
    if ((signal >= (7 * step))) {
        d7_angle = 0;
    }
    if ((signal >= (8 * step))) {
        d8_angle = 0;
    }
    if ((signal >= (9 * step))) {
        d9_angle = 0;
    }
    if ((signal >= (10 * step))) {
        d10_angle = 0;
    }
    if ((signal >= (11 * step))) {
        d11_angle = 0;
    }
    if ((signal >= (12 * step))) {
        d12_angle = 0;
    }
    if ((signal >= (13 * step))) {
        d13_angle = 0;
    }
    if ((signal >= (14 * step))) {
        d14_angle = 0;
    }
    if ((signal >= (15 * step))) {
        d15_angle = 0;
    }
    if ((signal >= (16 * step))) {
        d16_angle = 0;
    }
    if ((signal >= (17 * step))) {
        d17_angle = 0;
    }
    if ((signal >= (18 * step))) {
        d18_angle = 0;
    }
    if ((signal >= (19 * step))) {
        d19_angle = 0;
    }
    if ((signal >= (20 * step))) {
        d20_angle = 0;
    }
    if ((signal >= (21 * step))) {
        d21_angle = 0;
    }
    if ((signal >= (22 * step))) {
        d22_angle = 0;
    }
    if ((signal >= (23 * step))) {
        d23_angle = 0;
    }
    if ((signal >= (24 * step))) {
        d24_angle = 0;
    }
    if ((signal >= (25 * step))) {
        d25_angle = 0;
    }
    psychoJS.experiment.addData("signal", signal);
    
    q_resp.keys = undefined;
    q_resp.rt = undefined;
    _q_resp_allKeys = [];
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    trialMaxDuration = null
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(d1);
    trialComponents.push(d2);
    trialComponents.push(d3);
    trialComponents.push(d4);
    trialComponents.push(d5);
    trialComponents.push(d6);
    trialComponents.push(d7);
    trialComponents.push(d8);
    trialComponents.push(d9);
    trialComponents.push(d10);
    trialComponents.push(d11);
    trialComponents.push(d12);
    trialComponents.push(d13);
    trialComponents.push(d14);
    trialComponents.push(d15);
    trialComponents.push(d16);
    trialComponents.push(d17);
    trialComponents.push(d18);
    trialComponents.push(d19);
    trialComponents.push(d20);
    trialComponents.push(d21);
    trialComponents.push(d22);
    trialComponents.push(d23);
    trialComponents.push(d24);
    trialComponents.push(d25);
    trialComponents.push(q_text);
    trialComponents.push(q_resp);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code
    frame = (frame + 1);
    speed = (0.01 * direction);
    d1_p = d1.pos;
    d1_x = (d1_p[0] + (numpy.cos(d1_angle) * speed));
    d1_y = (d1_p[1] + (numpy.sin(d1_angle) * speed));
    if ((Math.pow((Math.pow(d1_p[0], 2) + Math.pow(d1_p[1], 2)), 0.5) > r)) {
        d1_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d1_x = (numpy.cos(rand_ang) * d1_dist);
        d1_y = (numpy.sin(rand_ang) * d1_dist);
        d1.setPos([d1_x, d1_y]);
    } else {
        d1.setPos([d1_x, d1_y]);
    }
    d2_p = d2.pos;
    d2_x = (d2_p[0] + (numpy.cos(d2_angle) * speed));
    d2_y = (d2_p[1] + (numpy.sin(d2_angle) * speed));
    if ((Math.pow((Math.pow(d2_p[0], 2) + Math.pow(d2_p[1], 2)), 0.5) > r)) {
        d2_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d2_x = (numpy.cos(rand_ang) * d2_dist);
        d2_y = (numpy.sin(rand_ang) * d2_dist);
        d2.setPos([d2_x, d2_y]);
    } else {
        d2.setPos([d2_x, d2_y]);
    }
    d3_p = d3.pos;
    d3_x = (d3_p[0] + (numpy.cos(d3_angle) * speed));
    d3_y = (d3_p[1] + (numpy.sin(d3_angle) * speed));
    if ((Math.pow((Math.pow(d3_p[0], 2) + Math.pow(d3_p[1], 2)), 0.5) > r)) {
        d3_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d3_x = (numpy.cos(rand_ang) * d3_dist);
        d3_y = (numpy.sin(rand_ang) * d3_dist);
        d3.setPos([d3_x, d3_y]);
    } else {
        d3.setPos([d3_x, d3_y]);
    }
    d4_p = d4.pos;
    d4_x = (d4_p[0] + (numpy.cos(d4_angle) * speed));
    d4_y = (d4_p[1] + (numpy.sin(d4_angle) * speed));
    if ((Math.pow((Math.pow(d4_p[0], 2) + Math.pow(d4_p[1], 2)), 0.5) > r)) {
        d4_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d4_x = (numpy.cos(rand_ang) * d4_dist);
        d4_y = (numpy.sin(rand_ang) * d4_dist);
        d4.setPos([d4_x, d4_y]);
    } else {
        d4.setPos([d4_x, d4_y]);
    }
    d5_p = d5.pos;
    d5_x = (d5_p[0] + (numpy.cos(d5_angle) * speed));
    d5_y = (d5_p[1] + (numpy.sin(d5_angle) * speed));
    if ((Math.pow((Math.pow(d5_p[0], 2) + Math.pow(d5_p[1], 2)), 0.5) > r)) {
        d5_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d5_x = (numpy.cos(rand_ang) * d5_dist);
        d5_y = (numpy.sin(rand_ang) * d5_dist);
        d5.setPos([d5_x, d5_y]);
    } else {
        d5.setPos([d5_x, d5_y]);
    }
    d6_p = d6.pos;
    d6_x = (d6_p[0] + (numpy.cos(d6_angle) * speed));
    d6_y = (d6_p[1] + (numpy.sin(d6_angle) * speed));
    if ((Math.pow((Math.pow(d6_p[0], 2) + Math.pow(d6_p[1], 2)), 0.5) > r)) {
        d6_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d6_x = (numpy.cos(rand_ang) * d6_dist);
        d6_y = (numpy.sin(rand_ang) * d6_dist);
        d6.setPos([d6_x, d6_y]);
    } else {
        d6.setPos([d6_x, d6_y]);
    }
    d7_p = d7.pos;
    d7_x = (d7_p[0] + (numpy.cos(d7_angle) * speed));
    d7_y = (d7_p[1] + (numpy.sin(d7_angle) * speed));
    if ((Math.pow((Math.pow(d7_p[0], 2) + Math.pow(d7_p[1], 2)), 0.5) > r)) {
        d7_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d7_x = (numpy.cos(rand_ang) * d7_dist);
        d7_y = (numpy.sin(rand_ang) * d7_dist);
        d7.setPos([d7_x, d7_y]);
    } else {
        d7.setPos([d7_x, d7_y]);
    }
    d8_p = d8.pos;
    d8_x = (d8_p[0] + (numpy.cos(d8_angle) * speed));
    d8_y = (d8_p[1] + (numpy.sin(d8_angle) * speed));
    if ((Math.pow((Math.pow(d8_p[0], 2) + Math.pow(d8_p[1], 2)), 0.5) > r)) {
        d8_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d8_x = (numpy.cos(rand_ang) * d8_dist);
        d8_y = (numpy.sin(rand_ang) * d8_dist);
        d8.setPos([d8_x, d8_y]);
    } else {
        d8.setPos([d8_x, d8_y]);
    }
    d9_p = d9.pos;
    d9_x = (d9_p[0] + (numpy.cos(d9_angle) * speed));
    d9_y = (d9_p[1] + (numpy.sin(d9_angle) * speed));
    if ((Math.pow((Math.pow(d9_p[0], 2) + Math.pow(d9_p[1], 2)), 0.5) > r)) {
        d9_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d9_x = (numpy.cos(rand_ang) * d9_dist);
        d9_y = (numpy.sin(rand_ang) * d9_dist);
        d9.setPos([d9_x, d9_y]);
    } else {
        d9.setPos([d9_x, d9_y]);
    }
    d10_p = d10.pos;
    d10_x = (d10_p[0] + (numpy.cos(d10_angle) * speed));
    d10_y = (d10_p[1] + (numpy.sin(d10_angle) * speed));
    if ((Math.pow((Math.pow(d10_p[0], 2) + Math.pow(d10_p[1], 2)), 0.5) > r)) {
        d10_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d10_x = (numpy.cos(rand_ang) * d10_dist);
        d10_y = (numpy.sin(rand_ang) * d10_dist);
        d10.setPos([d10_x, d10_y]);
    } else {
        d10.setPos([d10_x, d10_y]);
    }
    d11_p = d11.pos;
    d11_x = (d11_p[0] + (numpy.cos(d11_angle) * speed));
    d11_y = (d11_p[1] + (numpy.sin(d11_angle) * speed));
    if ((Math.pow((Math.pow(d11_p[0], 2) + Math.pow(d11_p[1], 2)), 0.5) > r)) {
        d11_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d11_x = (numpy.cos(rand_ang) * d11_dist);
        d11_y = (numpy.sin(rand_ang) * d11_dist);
        d11.setPos([d11_x, d11_y]);
    } else {
        d11.setPos([d11_x, d11_y]);
    }
    d12_p = d12.pos;
    d12_x = (d12_p[0] + (numpy.cos(d12_angle) * speed));
    d12_y = (d12_p[1] + (numpy.sin(d12_angle) * speed));
    if ((Math.pow((Math.pow(d12_p[0], 2) + Math.pow(d12_p[1], 2)), 0.5) > r)) {
        d12_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d12_x = (numpy.cos(rand_ang) * d12_dist);
        d12_y = (numpy.sin(rand_ang) * d12_dist);
        d12.setPos([d12_x, d12_y]);
    } else {
        d12.setPos([d12_x, d12_y]);
    }
    d13_p = d13.pos;
    d13_x = (d13_p[0] + (numpy.cos(d13_angle) * speed));
    d13_y = (d13_p[1] + (numpy.sin(d13_angle) * speed));
    if ((Math.pow((Math.pow(d13_p[0], 2) + Math.pow(d13_p[1], 2)), 0.5) > r)) {
        d13_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d13_x = (numpy.cos(rand_ang) * d13_dist);
        d13_y = (numpy.sin(rand_ang) * d13_dist);
        d13.setPos([d13_x, d13_y]);
    } else {
        d13.setPos([d13_x, d13_y]);
    }
    d14_p = d14.pos;
    d14_x = (d14_p[0] + (numpy.cos(d14_angle) * speed));
    d14_y = (d14_p[1] + (numpy.sin(d14_angle) * speed));
    if ((Math.pow((Math.pow(d14_p[0], 2) + Math.pow(d14_p[1], 2)), 0.5) > r)) {
        d14_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d14_x = (numpy.cos(rand_ang) * d14_dist);
        d14_y = (numpy.sin(rand_ang) * d14_dist);
        d14.setPos([d14_x, d14_y]);
    } else {
        d14.setPos([d14_x, d14_y]);
    }
    d15_p = d15.pos;
    d15_x = (d15_p[0] + (numpy.cos(d15_angle) * speed));
    d15_y = (d15_p[1] + (numpy.sin(d15_angle) * speed));
    if ((Math.pow((Math.pow(d15_p[0], 2) + Math.pow(d15_p[1], 2)), 0.5) > r)) {
        d15_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d15_x = (numpy.cos(rand_ang) * d15_dist);
        d15_y = (numpy.sin(rand_ang) * d15_dist);
        d15.setPos([d15_x, d15_y]);
    } else {
        d15.setPos([d15_x, d15_y]);
    }
    d16_p = d16.pos;
    d16_x = (d16_p[0] + (numpy.cos(d16_angle) * speed));
    d16_y = (d16_p[1] + (numpy.sin(d16_angle) * speed));
    if ((Math.pow((Math.pow(d16_p[0], 2) + Math.pow(d16_p[1], 2)), 0.5) > r)) {
        d16_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d16_x = (numpy.cos(rand_ang) * d16_dist);
        d16_y = (numpy.sin(rand_ang) * d16_dist);
        d16.setPos([d16_x, d16_y]);
    } else {
        d16.setPos([d16_x, d16_y]);
    }
    d17_p = d17.pos;
    d17_x = (d17_p[0] + (numpy.cos(d17_angle) * speed));
    d17_y = (d17_p[1] + (numpy.sin(d17_angle) * speed));
    if ((Math.pow((Math.pow(d17_p[0], 2) + Math.pow(d17_p[1], 2)), 0.5) > r)) {
        d17_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d17_x = (numpy.cos(rand_ang) * d17_dist);
        d17_y = (numpy.sin(rand_ang) * d17_dist);
        d17.setPos([d17_x, d17_y]);
    } else {
        d17.setPos([d17_x, d17_y]);
    }
    d18_p = d18.pos;
    d18_x = (d18_p[0] + (numpy.cos(d18_angle) * speed));
    d18_y = (d18_p[1] + (numpy.sin(d18_angle) * speed));
    if ((Math.pow((Math.pow(d18_p[0], 2) + Math.pow(d18_p[1], 2)), 0.5) > r)) {
        d18_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d18_x = (numpy.cos(rand_ang) * d18_dist);
        d18_y = (numpy.sin(rand_ang) * d18_dist);
        d18.setPos([d18_x, d18_y]);
    } else {
        d18.setPos([d18_x, d18_y]);
    }
    d19_p = d19.pos;
    d19_x = (d19_p[0] + (numpy.cos(d19_angle) * speed));
    d19_y = (d19_p[1] + (numpy.sin(d19_angle) * speed));
    if ((Math.pow((Math.pow(d19_p[0], 2) + Math.pow(d19_p[1], 2)), 0.5) > r)) {
        d19_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d19_x = (numpy.cos(rand_ang) * d19_dist);
        d19_y = (numpy.sin(rand_ang) * d19_dist);
        d19.setPos([d19_x, d19_y]);
    } else {
        d19.setPos([d19_x, d19_y]);
    }
    d20_p = d20.pos;
    d20_x = (d20_p[0] + (numpy.cos(d20_angle) * speed));
    d20_y = (d20_p[1] + (numpy.sin(d20_angle) * speed));
    if ((Math.pow((Math.pow(d20_p[0], 2) + Math.pow(d20_p[1], 2)), 0.5) > r)) {
        d20_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d20_x = (numpy.cos(rand_ang) * d20_dist);
        d20_y = (numpy.sin(rand_ang) * d20_dist);
        d20.setPos([d20_x, d20_y]);
    } else {
        d20.setPos([d20_x, d20_y]);
    }
    d21_p = d21.pos;
    d21_x = (d21_p[0] + (numpy.cos(d21_angle) * speed));
    d21_y = (d21_p[1] + (numpy.sin(d21_angle) * speed));
    if ((Math.pow((Math.pow(d21_p[0], 2) + Math.pow(d21_p[1], 2)), 0.5) > r)) {
        d21_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d21_x = (numpy.cos(rand_ang) * d21_dist);
        d21_y = (numpy.sin(rand_ang) * d21_dist);
        d21.setPos([d21_x, d21_y]);
    } else {
        d21.setPos([d21_x, d21_y]);
    }
    d22_p = d22.pos;
    d22_x = (d22_p[0] + (numpy.cos(d22_angle) * speed));
    d22_y = (d22_p[1] + (numpy.sin(d22_angle) * speed));
    if ((Math.pow((Math.pow(d22_p[0], 2) + Math.pow(d22_p[1], 2)), 0.5) > r)) {
        d22_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d22_x = (numpy.cos(rand_ang) * d22_dist);
        d22_y = (numpy.sin(rand_ang) * d22_dist);
        d22.setPos([d22_x, d22_y]);
    } else {
        d22.setPos([d22_x, d22_y]);
    }
    d23_p = d23.pos;
    d23_x = (d23_p[0] + (numpy.cos(d23_angle) * speed));
    d23_y = (d23_p[1] + (numpy.sin(d23_angle) * speed));
    if ((Math.pow((Math.pow(d23_p[0], 2) + Math.pow(d23_p[1], 2)), 0.5) > r)) {
        d23_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d23_x = (numpy.cos(rand_ang) * d23_dist);
        d23_y = (numpy.sin(rand_ang) * d23_dist);
        d23.setPos([d23_x, d23_y]);
    } else {
        d23.setPos([d23_x, d23_y]);
    }
    d24_p = d24.pos;
    d24_x = (d24_p[0] + (numpy.cos(d24_angle) * speed));
    d24_y = (d24_p[1] + (numpy.sin(d24_angle) * speed));
    if ((Math.pow((Math.pow(d24_p[0], 2) + Math.pow(d24_p[1], 2)), 0.5) > r)) {
        d24_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d24_x = (numpy.cos(rand_ang) * d24_dist);
        d24_y = (numpy.sin(rand_ang) * d24_dist);
        d24.setPos([d24_x, d24_y]);
    } else {
        d24.setPos([d24_x, d24_y]);
    }
    d25_p = d25.pos;
    d25_x = (d25_p[0] + (numpy.cos(d25_angle) * speed));
    d25_y = (d25_p[1] + (numpy.sin(d25_angle) * speed));
    if ((Math.pow((Math.pow(d25_p[0], 2) + Math.pow(d25_p[1], 2)), 0.5) > r)) {
        d25_dist = ((d * numpy.random.rand()) - r);
        rand_ang = ((2 * 3.14) * numpy.random.rand());
        d25_x = (numpy.cos(rand_ang) * d25_dist);
        d25_y = (numpy.sin(rand_ang) * d25_dist);
        d25.setPos([d25_x, d25_y]);
    } else {
        d25.setPos([d25_x, d25_y]);
    }
    
    
    // *d1* updates
    if (t >= 0.0 && d1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d1.tStart = t;  // (not accounting for frame time here)
      d1.frameNStart = frameN;  // exact frame index
      
      d1.setAutoDraw(true);
    }
    
    
    // if d1 is active this frame...
    if (d1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d1.tStop = t;  // not accounting for scr refresh
      d1.frameNStop = frameN;  // exact frame index
      // update status
      d1.status = PsychoJS.Status.FINISHED;
      d1.setAutoDraw(false);
    }
    
    
    // *d2* updates
    if (t >= 0.0 && d2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d2.tStart = t;  // (not accounting for frame time here)
      d2.frameNStart = frameN;  // exact frame index
      
      d2.setAutoDraw(true);
    }
    
    
    // if d2 is active this frame...
    if (d2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d2.tStop = t;  // not accounting for scr refresh
      d2.frameNStop = frameN;  // exact frame index
      // update status
      d2.status = PsychoJS.Status.FINISHED;
      d2.setAutoDraw(false);
    }
    
    
    // *d3* updates
    if (t >= 0.0 && d3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d3.tStart = t;  // (not accounting for frame time here)
      d3.frameNStart = frameN;  // exact frame index
      
      d3.setAutoDraw(true);
    }
    
    
    // if d3 is active this frame...
    if (d3.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d3.tStop = t;  // not accounting for scr refresh
      d3.frameNStop = frameN;  // exact frame index
      // update status
      d3.status = PsychoJS.Status.FINISHED;
      d3.setAutoDraw(false);
    }
    
    
    // *d4* updates
    if (t >= 0.0 && d4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d4.tStart = t;  // (not accounting for frame time here)
      d4.frameNStart = frameN;  // exact frame index
      
      d4.setAutoDraw(true);
    }
    
    
    // if d4 is active this frame...
    if (d4.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d4.tStop = t;  // not accounting for scr refresh
      d4.frameNStop = frameN;  // exact frame index
      // update status
      d4.status = PsychoJS.Status.FINISHED;
      d4.setAutoDraw(false);
    }
    
    
    // *d5* updates
    if (t >= 0.0 && d5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d5.tStart = t;  // (not accounting for frame time here)
      d5.frameNStart = frameN;  // exact frame index
      
      d5.setAutoDraw(true);
    }
    
    
    // if d5 is active this frame...
    if (d5.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d5.tStop = t;  // not accounting for scr refresh
      d5.frameNStop = frameN;  // exact frame index
      // update status
      d5.status = PsychoJS.Status.FINISHED;
      d5.setAutoDraw(false);
    }
    
    
    // *d6* updates
    if (t >= 0.0 && d6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d6.tStart = t;  // (not accounting for frame time here)
      d6.frameNStart = frameN;  // exact frame index
      
      d6.setAutoDraw(true);
    }
    
    
    // if d6 is active this frame...
    if (d6.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d6.tStop = t;  // not accounting for scr refresh
      d6.frameNStop = frameN;  // exact frame index
      // update status
      d6.status = PsychoJS.Status.FINISHED;
      d6.setAutoDraw(false);
    }
    
    
    // *d7* updates
    if (t >= 0.0 && d7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d7.tStart = t;  // (not accounting for frame time here)
      d7.frameNStart = frameN;  // exact frame index
      
      d7.setAutoDraw(true);
    }
    
    
    // if d7 is active this frame...
    if (d7.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d7.tStop = t;  // not accounting for scr refresh
      d7.frameNStop = frameN;  // exact frame index
      // update status
      d7.status = PsychoJS.Status.FINISHED;
      d7.setAutoDraw(false);
    }
    
    
    // *d8* updates
    if (t >= 0.0 && d8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d8.tStart = t;  // (not accounting for frame time here)
      d8.frameNStart = frameN;  // exact frame index
      
      d8.setAutoDraw(true);
    }
    
    
    // if d8 is active this frame...
    if (d8.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d8.tStop = t;  // not accounting for scr refresh
      d8.frameNStop = frameN;  // exact frame index
      // update status
      d8.status = PsychoJS.Status.FINISHED;
      d8.setAutoDraw(false);
    }
    
    
    // *d9* updates
    if (t >= 0.0 && d9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d9.tStart = t;  // (not accounting for frame time here)
      d9.frameNStart = frameN;  // exact frame index
      
      d9.setAutoDraw(true);
    }
    
    
    // if d9 is active this frame...
    if (d9.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d9.tStop = t;  // not accounting for scr refresh
      d9.frameNStop = frameN;  // exact frame index
      // update status
      d9.status = PsychoJS.Status.FINISHED;
      d9.setAutoDraw(false);
    }
    
    
    // *d10* updates
    if (t >= 0.0 && d10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d10.tStart = t;  // (not accounting for frame time here)
      d10.frameNStart = frameN;  // exact frame index
      
      d10.setAutoDraw(true);
    }
    
    
    // if d10 is active this frame...
    if (d10.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d10.tStop = t;  // not accounting for scr refresh
      d10.frameNStop = frameN;  // exact frame index
      // update status
      d10.status = PsychoJS.Status.FINISHED;
      d10.setAutoDraw(false);
    }
    
    
    // *d11* updates
    if (t >= 0.0 && d11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d11.tStart = t;  // (not accounting for frame time here)
      d11.frameNStart = frameN;  // exact frame index
      
      d11.setAutoDraw(true);
    }
    
    
    // if d11 is active this frame...
    if (d11.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d11.tStop = t;  // not accounting for scr refresh
      d11.frameNStop = frameN;  // exact frame index
      // update status
      d11.status = PsychoJS.Status.FINISHED;
      d11.setAutoDraw(false);
    }
    
    
    // *d12* updates
    if (t >= 0.0 && d12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d12.tStart = t;  // (not accounting for frame time here)
      d12.frameNStart = frameN;  // exact frame index
      
      d12.setAutoDraw(true);
    }
    
    
    // if d12 is active this frame...
    if (d12.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d12.tStop = t;  // not accounting for scr refresh
      d12.frameNStop = frameN;  // exact frame index
      // update status
      d12.status = PsychoJS.Status.FINISHED;
      d12.setAutoDraw(false);
    }
    
    
    // *d13* updates
    if (t >= 0.0 && d13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d13.tStart = t;  // (not accounting for frame time here)
      d13.frameNStart = frameN;  // exact frame index
      
      d13.setAutoDraw(true);
    }
    
    
    // if d13 is active this frame...
    if (d13.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d13.tStop = t;  // not accounting for scr refresh
      d13.frameNStop = frameN;  // exact frame index
      // update status
      d13.status = PsychoJS.Status.FINISHED;
      d13.setAutoDraw(false);
    }
    
    
    // *d14* updates
    if (t >= 0.0 && d14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d14.tStart = t;  // (not accounting for frame time here)
      d14.frameNStart = frameN;  // exact frame index
      
      d14.setAutoDraw(true);
    }
    
    
    // if d14 is active this frame...
    if (d14.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d14.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d14.tStop = t;  // not accounting for scr refresh
      d14.frameNStop = frameN;  // exact frame index
      // update status
      d14.status = PsychoJS.Status.FINISHED;
      d14.setAutoDraw(false);
    }
    
    
    // *d15* updates
    if (t >= 0.0 && d15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d15.tStart = t;  // (not accounting for frame time here)
      d15.frameNStart = frameN;  // exact frame index
      
      d15.setAutoDraw(true);
    }
    
    
    // if d15 is active this frame...
    if (d15.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d15.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d15.tStop = t;  // not accounting for scr refresh
      d15.frameNStop = frameN;  // exact frame index
      // update status
      d15.status = PsychoJS.Status.FINISHED;
      d15.setAutoDraw(false);
    }
    
    
    // *d16* updates
    if (t >= 0.0 && d16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d16.tStart = t;  // (not accounting for frame time here)
      d16.frameNStart = frameN;  // exact frame index
      
      d16.setAutoDraw(true);
    }
    
    
    // if d16 is active this frame...
    if (d16.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d16.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d16.tStop = t;  // not accounting for scr refresh
      d16.frameNStop = frameN;  // exact frame index
      // update status
      d16.status = PsychoJS.Status.FINISHED;
      d16.setAutoDraw(false);
    }
    
    
    // *d17* updates
    if (t >= 0.0 && d17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d17.tStart = t;  // (not accounting for frame time here)
      d17.frameNStart = frameN;  // exact frame index
      
      d17.setAutoDraw(true);
    }
    
    
    // if d17 is active this frame...
    if (d17.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d17.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d17.tStop = t;  // not accounting for scr refresh
      d17.frameNStop = frameN;  // exact frame index
      // update status
      d17.status = PsychoJS.Status.FINISHED;
      d17.setAutoDraw(false);
    }
    
    
    // *d18* updates
    if (t >= 0.0 && d18.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d18.tStart = t;  // (not accounting for frame time here)
      d18.frameNStart = frameN;  // exact frame index
      
      d18.setAutoDraw(true);
    }
    
    
    // if d18 is active this frame...
    if (d18.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d18.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d18.tStop = t;  // not accounting for scr refresh
      d18.frameNStop = frameN;  // exact frame index
      // update status
      d18.status = PsychoJS.Status.FINISHED;
      d18.setAutoDraw(false);
    }
    
    
    // *d19* updates
    if (t >= 0.0 && d19.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d19.tStart = t;  // (not accounting for frame time here)
      d19.frameNStart = frameN;  // exact frame index
      
      d19.setAutoDraw(true);
    }
    
    
    // if d19 is active this frame...
    if (d19.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d19.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d19.tStop = t;  // not accounting for scr refresh
      d19.frameNStop = frameN;  // exact frame index
      // update status
      d19.status = PsychoJS.Status.FINISHED;
      d19.setAutoDraw(false);
    }
    
    
    // *d20* updates
    if (t >= 0.0 && d20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d20.tStart = t;  // (not accounting for frame time here)
      d20.frameNStart = frameN;  // exact frame index
      
      d20.setAutoDraw(true);
    }
    
    
    // if d20 is active this frame...
    if (d20.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d20.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d20.tStop = t;  // not accounting for scr refresh
      d20.frameNStop = frameN;  // exact frame index
      // update status
      d20.status = PsychoJS.Status.FINISHED;
      d20.setAutoDraw(false);
    }
    
    
    // *d21* updates
    if (t >= 0.0 && d21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d21.tStart = t;  // (not accounting for frame time here)
      d21.frameNStart = frameN;  // exact frame index
      
      d21.setAutoDraw(true);
    }
    
    
    // if d21 is active this frame...
    if (d21.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d21.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d21.tStop = t;  // not accounting for scr refresh
      d21.frameNStop = frameN;  // exact frame index
      // update status
      d21.status = PsychoJS.Status.FINISHED;
      d21.setAutoDraw(false);
    }
    
    
    // *d22* updates
    if (t >= 0.0 && d22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d22.tStart = t;  // (not accounting for frame time here)
      d22.frameNStart = frameN;  // exact frame index
      
      d22.setAutoDraw(true);
    }
    
    
    // if d22 is active this frame...
    if (d22.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d22.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d22.tStop = t;  // not accounting for scr refresh
      d22.frameNStop = frameN;  // exact frame index
      // update status
      d22.status = PsychoJS.Status.FINISHED;
      d22.setAutoDraw(false);
    }
    
    
    // *d23* updates
    if (t >= 0.0 && d23.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d23.tStart = t;  // (not accounting for frame time here)
      d23.frameNStart = frameN;  // exact frame index
      
      d23.setAutoDraw(true);
    }
    
    
    // if d23 is active this frame...
    if (d23.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d23.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d23.tStop = t;  // not accounting for scr refresh
      d23.frameNStop = frameN;  // exact frame index
      // update status
      d23.status = PsychoJS.Status.FINISHED;
      d23.setAutoDraw(false);
    }
    
    
    // *d24* updates
    if (t >= 0.0 && d24.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d24.tStart = t;  // (not accounting for frame time here)
      d24.frameNStart = frameN;  // exact frame index
      
      d24.setAutoDraw(true);
    }
    
    
    // if d24 is active this frame...
    if (d24.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d24.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d24.tStop = t;  // not accounting for scr refresh
      d24.frameNStop = frameN;  // exact frame index
      // update status
      d24.status = PsychoJS.Status.FINISHED;
      d24.setAutoDraw(false);
    }
    
    
    // *d25* updates
    if (t >= 0.0 && d25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      d25.tStart = t;  // (not accounting for frame time here)
      d25.frameNStart = frameN;  // exact frame index
      
      d25.setAutoDraw(true);
    }
    
    
    // if d25 is active this frame...
    if (d25.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (d25.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      d25.tStop = t;  // not accounting for scr refresh
      d25.frameNStop = frameN;  // exact frame index
      // update status
      d25.status = PsychoJS.Status.FINISHED;
      d25.setAutoDraw(false);
    }
    
    
    // *q_text* updates
    if (t >= 0.0 && q_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      q_text.tStart = t;  // (not accounting for frame time here)
      q_text.frameNStart = frameN;  // exact frame index
      
      q_text.setAutoDraw(true);
    }
    
    
    // if q_text is active this frame...
    if (q_text.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (q_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      q_text.tStop = t;  // not accounting for scr refresh
      q_text.frameNStop = frameN;  // exact frame index
      // update status
      q_text.status = PsychoJS.Status.FINISHED;
      q_text.setAutoDraw(false);
    }
    
    
    // *q_resp* updates
    if (t >= 0.0 && q_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      q_resp.tStart = t;  // (not accounting for frame time here)
      q_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { q_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { q_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { q_resp.clearEvents(); });
    }
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (q_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      q_resp.tStop = t;  // not accounting for scr refresh
      q_resp.frameNStop = frameN;  // exact frame index
      // update status
      q_resp.status = PsychoJS.Status.FINISHED;
      frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (q_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        q_resp.tStop = t;  // not accounting for scr refresh
        q_resp.frameNStop = frameN;  // exact frame index
        // update status
        q_resp.status = PsychoJS.Status.FINISHED;
        q_resp.status = PsychoJS.Status.FINISHED;
          }
        
      }
      
      // if q_resp is active this frame...
      if (q_resp.status === PsychoJS.Status.STARTED) {
        let theseKeys = q_resp.getKeys({
          keyList: typeof ['1','2'] === 'string' ? [['1','2']] : ['1','2'], 
          waitRelease: false
        });
        _q_resp_allKeys = _q_resp_allKeys.concat(theseKeys);
        if (_q_resp_allKeys.length > 0) {
          q_resp.keys = _q_resp_allKeys[_q_resp_allKeys.length - 1].name;  // just the last key pressed
          q_resp.rt = _q_resp_allKeys[_q_resp_allKeys.length - 1].rt;
          q_resp.duration = _q_resp_allKeys[_q_resp_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of trialComponents)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  function trialRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'trial' ---
      for (const thisComponent of trialComponents) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
      // Run 'End Routine' code from code
      psychoJS.experiment.addData("d1_angle", d1_angle);
      psychoJS.experiment.addData("d2_angle", d2_angle);
      psychoJS.experiment.addData("d3_angle", d3_angle);
      psychoJS.experiment.addData("d4_angle", d4_angle);
      psychoJS.experiment.addData("d5_angle", d5_angle);
      psychoJS.experiment.addData("d6_angle", d6_angle);
      psychoJS.experiment.addData("d7_angle", d7_angle);
      psychoJS.experiment.addData("d8_angle", d8_angle);
      psychoJS.experiment.addData("d9_angle", d9_angle);
      psychoJS.experiment.addData("d10_angle", d10_angle);
      psychoJS.experiment.addData("d11_angle", d11_angle);
      psychoJS.experiment.addData("d12_angle", d12_angle);
      psychoJS.experiment.addData("d13_angle", d13_angle);
      psychoJS.experiment.addData("d14_angle", d14_angle);
      psychoJS.experiment.addData("d15_angle", d15_angle);
      psychoJS.experiment.addData("d16_angle", d16_angle);
      psychoJS.experiment.addData("d17_angle", d17_angle);
      psychoJS.experiment.addData("d18_angle", d18_angle);
      psychoJS.experiment.addData("d19_angle", d19_angle);
      psychoJS.experiment.addData("d20_angle", d20_angle);
      psychoJS.experiment.addData("d21_angle", d21_angle);
      psychoJS.experiment.addData("d22_angle", d22_angle);
      psychoJS.experiment.addData("d23_angle", d23_angle);
      psychoJS.experiment.addData("d24_angle", d24_angle);
      psychoJS.experiment.addData("d25_angle", d25_angle);
      type1_resp = 999;
      trial_correct = 999;
      if ((q_resp.keys === "1")) {
          type1_resp = (- 1);
      } else {
          if ((q_resp.keys === "2")) {
              type1_resp = 1;
          }
      }
      if ((type1_resp === 999)) {
          trial_correct = 999;
      } else {
          if ((type1_resp === direction)) {
              trial_correct = 1;
          } else {
              trial_correct = 0;
          }
      }
      psychoJS.experiment.addData("type1_resp", type1_resp);
      psychoJS.experiment.addData("trial_correct", trial_correct);
      
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(q_resp.corr, level);
      }
      psychoJS.experiment.addData('q_resp.keys', q_resp.keys);
      if (typeof q_resp.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('q_resp.rt', q_resp.rt);
          psychoJS.experiment.addData('q_resp.duration', q_resp.duration);
          routineTimer.reset();
          }
      
      q_resp.stop();
      if (routineForceEnded) {
          routineTimer.reset();} else if (trialMaxDurationReached) {
          trialClock.add(trialMaxDuration);
      } else {
          trialClock.add(4.000000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  function blankRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'blank' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      blankClock.reset(routineTimer.getTime());
      routineTimer.add(0.500000);
      blankMaxDurationReached = false;
      // update component parameters for each repeat
      psychoJS.experiment.addData('blank.started', globalClock.getTime());
      blankMaxDuration = null
      // keep track of which components have finished
      blankComponents = [];
      blankComponents.push(blank_text);
      
      for (const thisComponent of blankComponents)
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
      return Scheduler.Event.NEXT;
    }
  }
  
  function blankRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'blank' ---
      // get current time
      t = blankClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *blank_text* updates
      if (t >= 0.0 && blank_text.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        blank_text.tStart = t;  // (not accounting for frame time here)
        blank_text.frameNStart = frameN;  // exact frame index
        
        blank_text.setAutoDraw(true);
      }
      
      
      // if blank_text is active this frame...
      if (blank_text.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (blank_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        blank_text.tStop = t;  // not accounting for scr refresh
        blank_text.frameNStop = frameN;  // exact frame index
        // update status
        blank_text.status = PsychoJS.Status.FINISHED;
        blank_text.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of blankComponents)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  function blankRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'blank' ---
      for (const thisComponent of blankComponents) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('blank.stopped', globalClock.getTime());
      if (routineForceEnded) {
          routineTimer.reset();} else if (blankMaxDurationReached) {
          blankClock.add(blankMaxDuration);
      } else {
          blankClock.add(0.500000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  function type2_qRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'type2_q' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      type2_qClock.reset();
      routineTimer.reset();
      type2_qMaxDurationReached = false;
      // update component parameters for each repeat
      type2_q_key_resp.keys = undefined;
      type2_q_key_resp.rt = undefined;
      _type2_q_key_resp_allKeys = [];
      // Run 'Begin Routine' code from code_2
      confidence_marker = 999;
      confidence_submitted = 0;
      high_or_low = 0;
      if ((blockCode !== 2)) {
          continueRoutine = false;
      }
      
      // setup some python lists for storing info about the type2_mouse
      // current position of the mouse:
      type2_mouse.x = [];
      type2_mouse.y = [];
      type2_mouse.leftButton = [];
      type2_mouse.midButton = [];
      type2_mouse.rightButton = [];
      type2_mouse.time = [];
      gotValidClick = false; // until a click is received
      psychoJS.experiment.addData('type2_q.started', globalClock.getTime());
      type2_qMaxDuration = null
      // keep track of which components have finished
      type2_qComponents = [];
      type2_qComponents.push(type2_q_text);
      type2_qComponents.push(text_below);
      type2_qComponents.push(type2_q_key_resp);
      type2_qComponents.push(line);
      type2_qComponents.push(marker);
      type2_qComponents.push(type2_mouse);
      type2_qComponents.push(low_text);
      type2_qComponents.push(high_text);
      
      for (const thisComponent of type2_qComponents)
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
      return Scheduler.Event.NEXT;
    }
  }
  
  function type2_qRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'type2_q' ---
      // get current time
      t = type2_qClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *type2_q_text* updates
      if (t >= 0.0 && type2_q_text.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        type2_q_text.tStart = t;  // (not accounting for frame time here)
        type2_q_text.frameNStart = frameN;  // exact frame index
        
        type2_q_text.setAutoDraw(true);
      }
      
      
      // if type2_q_text is active this frame...
      if (type2_q_text.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *text_below* updates
      if (t >= 0.0 && text_below.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        text_below.tStart = t;  // (not accounting for frame time here)
        text_below.frameNStart = frameN;  // exact frame index
        
        text_below.setAutoDraw(true);
      }
      
      
      // if text_below is active this frame...
      if (text_below.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *type2_q_key_resp* updates
      if (t >= 0.0 && type2_q_key_resp.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        type2_q_key_resp.tStart = t;  // (not accounting for frame time here)
        type2_q_key_resp.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { type2_q_key_resp.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { type2_q_key_resp.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { type2_q_key_resp.clearEvents(); });
      }
      
      // if type2_q_key_resp is active this frame...
      if (type2_q_key_resp.status === PsychoJS.Status.STARTED) {
        let theseKeys = type2_q_key_resp.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _type2_q_key_resp_allKeys = _type2_q_key_resp_allKeys.concat(theseKeys);
        if (_type2_q_key_resp_allKeys.length > 0) {
          type2_q_key_resp.keys = _type2_q_key_resp_allKeys[_type2_q_key_resp_allKeys.length - 1].name;  // just the last key pressed
          type2_q_key_resp.rt = _type2_q_key_resp_allKeys[_type2_q_key_resp_allKeys.length - 1].rt;
          type2_q_key_resp.duration = _type2_q_key_resp_allKeys[_type2_q_key_resp_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      
      // *line* updates
      if (t >= 0.0 && line.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        line.tStart = t;  // (not accounting for frame time here)
        line.frameNStart = frameN;  // exact frame index
        
        line.setAutoDraw(true);
      }
      
      
      // if line is active this frame...
      if (line.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *marker* updates
      if (t >= 0.0 && marker.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        marker.tStart = t;  // (not accounting for frame time here)
        marker.frameNStart = frameN;  // exact frame index
        
        marker.setAutoDraw(true);
      }
      
      
      // if marker is active this frame...
      if (marker.status === PsychoJS.Status.STARTED) {
      }
      
      // Run 'Each Frame' code from code_2
      mouse_pos = type2_mouse.getPos();
      mouse_y = mouse_pos[1];
      if ((mouse_y > 0.075)) {
          mouse_y = 0.075;
      }
      if ((mouse_y < (- 0.075))) {
          mouse_y = (- 0.075);
      }
      marker.setPos([0, mouse_y]);
      
      // *type2_mouse* updates
      if (t >= 0.0 && type2_mouse.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        type2_mouse.tStart = t;  // (not accounting for frame time here)
        type2_mouse.frameNStart = frameN;  // exact frame index
        
        type2_mouse.status = PsychoJS.Status.STARTED;
        type2_mouse.mouseClock.reset();
        prevButtonState = [0, 0, 0];  // if now button is down we will treat as 'new' click
      }
      
      // if type2_mouse is active this frame...
      if (type2_mouse.status === PsychoJS.Status.STARTED) {
        _mouseButtons = type2_mouse.getPressed();
        if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
          prevButtonState = _mouseButtons;
          if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
            _mouseXYs = type2_mouse.getPos();
            type2_mouse.x.push(_mouseXYs[0]);
            type2_mouse.y.push(_mouseXYs[1]);
            type2_mouse.leftButton.push(_mouseButtons[0]);
            type2_mouse.midButton.push(_mouseButtons[1]);
            type2_mouse.rightButton.push(_mouseButtons[2]);
            type2_mouse.time.push(type2_mouse.mouseClock.getTime());
          }
        }
      }
      
      // *low_text* updates
      if (t >= 0.0 && low_text.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        low_text.tStart = t;  // (not accounting for frame time here)
        low_text.frameNStart = frameN;  // exact frame index
        
        low_text.setAutoDraw(true);
      }
      
      
      // if low_text is active this frame...
      if (low_text.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *high_text* updates
      if (t >= 0.0 && high_text.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        high_text.tStart = t;  // (not accounting for frame time here)
        high_text.frameNStart = frameN;  // exact frame index
        
        high_text.setAutoDraw(true);
      }
      
      
      // if high_text is active this frame...
      if (high_text.status === PsychoJS.Status.STARTED) {
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of type2_qComponents)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  function type2_qRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'type2_q' ---
      for (const thisComponent of type2_qComponents) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('type2_q.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(type2_q_key_resp.corr, level);
      }
      psychoJS.experiment.addData('type2_q_key_resp.keys', type2_q_key_resp.keys);
      if (typeof type2_q_key_resp.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('type2_q_key_resp.rt', type2_q_key_resp.rt);
          psychoJS.experiment.addData('type2_q_key_resp.duration', type2_q_key_resp.duration);
          routineTimer.reset();
          }
      
      type2_q_key_resp.stop();
      // Run 'End Routine' code from code_2
      if ((type2_q_key_resp.keys === "space")) {
          confidence_submitted = 1;
      }
      confidence_marker = mouse_y;
      /*
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
      */
      if ((blockCode !== (- 1))) {
          psychoJS.experiment.addData("confidence_marker", confidence_marker);
      }
      if ((blockCode === 2)) {
          if ((confidence_marker > 0)) {
              high_or_low = 1;
          }
          if ((confidence_marker < 0)) {
              high_or_low = (- 1);
          }
      }
      
      // store data for psychoJS.experiment (ExperimentHandler)
      psychoJS.experiment.addData('type2_mouse.x', type2_mouse.x);
      psychoJS.experiment.addData('type2_mouse.y', type2_mouse.y);
      psychoJS.experiment.addData('type2_mouse.leftButton', type2_mouse.leftButton);
      psychoJS.experiment.addData('type2_mouse.midButton', type2_mouse.midButton);
      psychoJS.experiment.addData('type2_mouse.rightButton', type2_mouse.rightButton);
      psychoJS.experiment.addData('type2_mouse.time', type2_mouse.time);
      
      // the Routine "type2_q" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  function feedbackRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'feedback' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      feedbackClock.reset(routineTimer.getTime());
      routineTimer.add(0.500000);
      feedbackMaxDurationReached = false;
      // update component parameters for each repeat
      // Run 'Begin Routine' code from code_6
      if ((blockCode > 0)) {
          continueRoutine = false;
      }
      if ((trial_correct === 1)) {
          feedback_str = "Correct!";
          points_str = "+10 points";
      } else {
          if ((trial_correct === 0)) {
              feedback_str = "Incorrect";
              points_str = "0 points";
          } else {
              if ((trial_correct === 999)) {
                  feedback_str = "Too slow!";
              }
          }
      }
      if ((confidence_submitted === 999)) {
          feedback_str = "Too slow!";
      }
      feedback_text.setText(feedback_str);
      
      psychoJS.experiment.addData('feedback.started', globalClock.getTime());
      feedbackMaxDuration = null
      // keep track of which components have finished
      feedbackComponents = [];
      feedbackComponents.push(feedback_text);
      
      for (const thisComponent of feedbackComponents)
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
      return Scheduler.Event.NEXT;
    }
  }
  
  function feedbackRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'feedback' ---
      // get current time
      t = feedbackClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *feedback_text* updates
      if (t >= 0.0 && feedback_text.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        feedback_text.tStart = t;  // (not accounting for frame time here)
        feedback_text.frameNStart = frameN;  // exact frame index
        
        feedback_text.setAutoDraw(true);
      }
      
      
      // if feedback_text is active this frame...
      if (feedback_text.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        feedback_text.tStop = t;  // not accounting for scr refresh
        feedback_text.frameNStop = frameN;  // exact frame index
        // update status
        feedback_text.status = PsychoJS.Status.FINISHED;
        feedback_text.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of feedbackComponents)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  function feedbackRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'feedback' ---
      for (const thisComponent of feedbackComponents) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('feedback.stopped', globalClock.getTime());
      if (routineForceEnded) {
          routineTimer.reset();} else if (feedbackMaxDurationReached) {
          feedbackClock.add(feedbackMaxDuration);
      } else {
          feedbackClock.add(0.500000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  function BonusRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'Bonus' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      BonusClock.reset();
      routineTimer.reset();
      BonusMaxDurationReached = false;
      // update component parameters for each repeat
      // Run 'Begin Routine' code from code_9
      if (((trial_correct === 1) && (high_or_low === 1))) {
          bonus_score += 1;
          bonus_str = "You have earned a 50p bonus! This will be added to your participation payment.Press SPACE to continue.";
      } else {
          if (((trial_correct === 1) && (high_or_low === (- 1)))) {
              bonus_score += 1;
              bonus_str = "You have earned a 50p bonus! This will be added to your participation payment. Press SPACE to continue.";
          } else {
              bonus_str = "Sorry, you did not get a bonus. Press SPACE to continue.";
          }
      }
      bonus_sum.setText(bonus_str);
      
      key_resp_3.keys = undefined;
      key_resp_3.rt = undefined;
      _key_resp_3_allKeys = [];
      psychoJS.experiment.addData('Bonus.started', globalClock.getTime());
      BonusMaxDuration = null
      // keep track of which components have finished
      BonusComponents = [];
      BonusComponents.push(bonus_sum);
      BonusComponents.push(key_resp_3);
      
      for (const thisComponent of BonusComponents)
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
      return Scheduler.Event.NEXT;
    }
  }
  
  function BonusRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'Bonus' ---
      // get current time
      t = BonusClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *bonus_sum* updates
      if (t >= 0.0 && bonus_sum.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        bonus_sum.tStart = t;  // (not accounting for frame time here)
        bonus_sum.frameNStart = frameN;  // exact frame index
        
        bonus_sum.setAutoDraw(true);
      }
      
      
      // if bonus_sum is active this frame...
      if (bonus_sum.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *key_resp_3* updates
      if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        key_resp_3.tStart = t;  // (not accounting for frame time here)
        key_resp_3.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
      }
      
      // if key_resp_3 is active this frame...
      if (key_resp_3.status === PsychoJS.Status.STARTED) {
        let theseKeys = key_resp_3.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
        if (_key_resp_3_allKeys.length > 0) {
          key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
          key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
          key_resp_3.duration = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of BonusComponents)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  function BonusRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'Bonus' ---
      for (const thisComponent of BonusComponents) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('Bonus.stopped', globalClock.getTime());
      // Run 'End Routine' code from code_9
      psychoJS.experiment.addData("bonus_score", bonus_score);
      psychoJS.experiment.addData("high_or_low", high_or_low);
      
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(key_resp_3.corr, level);
      }
      psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
      if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
          psychoJS.experiment.addData('key_resp_3.duration', key_resp_3.duration);
          routineTimer.reset();
          }
      
      key_resp_3.stop();
      // the Routine "Bonus" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  function thanksRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'thanks' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      thanksClock.reset(routineTimer.getTime());
      routineTimer.add(5.000000);
      thanksMaxDurationReached = false;
      // update component parameters for each repeat
      psychoJS.experiment.addData('thanks.started', globalClock.getTime());
      thanksMaxDuration = null
      // keep track of which components have finished
      thanksComponents = [];
      thanksComponents.push(text_3);
      
      for (const thisComponent of thanksComponents)
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
      return Scheduler.Event.NEXT;
    }
  }
  
  function thanksRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'thanks' ---
      // get current time
      t = thanksClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *text_3* updates
      if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        text_3.tStart = t;  // (not accounting for frame time here)
        text_3.frameNStart = frameN;  // exact frame index
        
        text_3.setAutoDraw(true);
      }
      
      
      // if text_3 is active this frame...
      if (text_3.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        text_3.tStop = t;  // not accounting for scr refresh
        text_3.frameNStop = frameN;  // exact frame index
        // update status
        text_3.status = PsychoJS.Status.FINISHED;
        text_3.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of thanksComponents)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  function thanksRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'thanks' ---
      for (const thisComponent of thanksComponents) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('thanks.stopped', globalClock.getTime());
      if (routineForceEnded) {
          routineTimer.reset();} else if (thanksMaxDurationReached) {
          thanksClock.add(thanksMaxDuration);
      } else {
          thanksClock.add(5.000000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  function importConditions(currentLoop) {
    return async function () {
      psychoJS.importAttributes(currentLoop.getCurrentTrial());
      return Scheduler.Event.NEXT;
      };
  }
  
  async function quitPsychoJS(message, isCompleted) {
    // Check for and save orphaned data
    if (psychoJS.experiment.isEntryEmpty()) {
      psychoJS.experiment.nextEntry();
    }
    psychoJS.window.close();
    psychoJS.quit({message: message, isCompleted: isCompleted});
    
    return Scheduler.Event.QUIT;
  }
