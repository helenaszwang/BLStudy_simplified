/***************** 
 * Session2 Test *
 *****************/

import { PsychoJS } from './lib/core-2020.2.js';
import * as core from './lib/core-2020.2.js';
import { TrialHandler } from './lib/data-2020.2.js';
import { Scheduler } from './lib/util-2020.2.js';
import * as visual from './lib/visual-2020.2.js';
import * as sound from './lib/sound-2020.2.js';
import * as util from './lib/util-2020.2.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'Session2';  // from the Builder filename that created this script
let expInfo = {'participant': ''};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(Welcome0RoutineBegin());
flowScheduler.add(Welcome0RoutineEachFrame());
flowScheduler.add(Welcome0RoutineEnd());
const HeadphoneLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(HeadphoneLoopLoopBegin, HeadphoneLoopLoopScheduler);
flowScheduler.add(HeadphoneLoopLoopScheduler);
flowScheduler.add(HeadphoneLoopLoopEnd);
flowScheduler.add(SLWelcomeRoutineBegin());
flowScheduler.add(SLWelcomeRoutineEachFrame());
flowScheduler.add(SLWelcomeRoutineEnd());
flowScheduler.add(ExposurePrepRoutineBegin());
flowScheduler.add(ExposurePrepRoutineEachFrame());
flowScheduler.add(ExposurePrepRoutineEnd());
const ExposureLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(ExposureLoopLoopBegin, ExposureLoopLoopScheduler);
flowScheduler.add(ExposureLoopLoopScheduler);
flowScheduler.add(ExposureLoopLoopEnd);
flowScheduler.add(CallExperimenterRoutineBegin());
flowScheduler.add(CallExperimenterRoutineEachFrame());
flowScheduler.add(CallExperimenterRoutineEnd());
flowScheduler.add(Part1IntroRoutineBegin());
flowScheduler.add(Part1IntroRoutineEachFrame());
flowScheduler.add(Part1IntroRoutineEnd());
flowScheduler.add(TDTrainingIntroRoutineBegin());
flowScheduler.add(TDTrainingIntroRoutineEachFrame());
flowScheduler.add(TDTrainingIntroRoutineEnd());
const TrainTDLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(TrainTDLoopLoopBegin, TrainTDLoopLoopScheduler);
flowScheduler.add(TrainTDLoopLoopScheduler);
flowScheduler.add(TrainTDLoopLoopEnd);
flowScheduler.add(P1IntroIIRoutineBegin());
flowScheduler.add(P1IntroIIRoutineEachFrame());
flowScheduler.add(P1IntroIIRoutineEnd());
const TDLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(TDLoopBegin, TDLoopScheduler);
flowScheduler.add(TDLoopScheduler);
flowScheduler.add(TDLoopEnd);
flowScheduler.add(CallExperimenterRoutineBegin());
flowScheduler.add(CallExperimenterRoutineEachFrame());
flowScheduler.add(CallExperimenterRoutineEnd());
flowScheduler.add(P2WelcomeRoutineBegin());
flowScheduler.add(P2WelcomeRoutineEachFrame());
flowScheduler.add(P2WelcomeRoutineEnd());
flowScheduler.add(FamRatingIntroRoutineBegin());
flowScheduler.add(FamRatingIntroRoutineEachFrame());
flowScheduler.add(FamRatingIntroRoutineEnd());
const FamRatingLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(FamRatingLoopLoopBegin, FamRatingLoopLoopScheduler);
flowScheduler.add(FamRatingLoopLoopScheduler);
flowScheduler.add(FamRatingLoopLoopEnd);
flowScheduler.add(Part2Intro2RoutineBegin());
flowScheduler.add(Part2Intro2RoutineEachFrame());
flowScheduler.add(Part2Intro2RoutineEnd());
const AFCTestLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(AFCTestLoopBegin, AFCTestLoopScheduler);
flowScheduler.add(AFCTestLoopScheduler);
flowScheduler.add(AFCTestLoopEnd);
flowScheduler.add(HearingCheckIntroRoutineBegin());
flowScheduler.add(HearingCheckIntroRoutineEachFrame());
flowScheduler.add(HearingCheckIntroRoutineEnd());
const HearingcheckLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(HearingcheckLoopLoopBegin, HearingcheckLoopLoopScheduler);
flowScheduler.add(HearingcheckLoopLoopScheduler);
flowScheduler.add(HearingcheckLoopLoopEnd);
flowScheduler.add(P2EndRoutineBegin());
flowScheduler.add(P2EndRoutineEachFrame());
flowScheduler.add(P2EndRoutineEnd());
flowScheduler.add(BlankRoutineBegin());
flowScheduler.add(BlankRoutineEachFrame());
flowScheduler.add(BlankRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'SL_Sounds/My Syllables/PA.wav', 'path': 'SL_Sounds/My Syllables/PA.wav'},
    {'name': 'SL_Sounds/re.wav', 'path': 'SL_Sounds/re.wav'},
    {'name': 'SL_Sounds/My Syllables/LO.wav', 'path': 'SL_Sounds/My Syllables/LO.wav'},
    {'name': 'HearingCheckSounds.xlsx', 'path': 'HearingCheckSounds.xlsx'},
    {'name': 'SL_Sounds/My Syllables/DO.wav', 'path': 'SL_Sounds/My Syllables/DO.wav'},
    {'name': 'Headphone/t1_1.wav', 'path': 'Headphone/t1_1.wav'},
    {'name': 'SL_Sounds/My Syllables/PI.wav', 'path': 'SL_Sounds/My Syllables/PI.wav'},
    {'name': 'SL_Sounds/ru.wav', 'path': 'SL_Sounds/ru.wav'},
    {'name': 'TDTrainList.xlsx', 'path': 'TDTrainList.xlsx'},
    {'name': '1_exposure.xlsx', 'path': '1_exposure.xlsx'},
    {'name': 'SL_Sounds/ta.wav', 'path': 'SL_Sounds/ta.wav'},
    {'name': 'SL_Sounds/fe.wav', 'path': 'SL_Sounds/fe.wav'},
    {'name': '1_TD_list.xlsx', 'path': '1_TD_list.xlsx'},
    {'name': 'SL_Sounds/ko.wav', 'path': 'SL_Sounds/ko.wav'},
    {'name': '1_explicit.xlsx', 'path': '1_explicit.xlsx'},
    {'name': 'SL_Sounds/My Syllables/DA.wav', 'path': 'SL_Sounds/My Syllables/DA.wav'},
    {'name': 'SL_Sounds/My Syllables/KU.wav', 'path': 'SL_Sounds/My Syllables/KU.wav'},
    {'name': 'SL_Sounds/su.wav', 'path': 'SL_Sounds/su.wav'},
    {'name': 'Headphone/t2_2.wav', 'path': 'Headphone/t2_2.wav'},
    {'name': 'Headphone/t3_1.wav', 'path': 'Headphone/t3_1.wav'},
    {'name': 'SL_Sounds/My Syllables/TU.wav', 'path': 'SL_Sounds/My Syllables/TU.wav'},
    {'name': 'SL_Sounds/me.wav', 'path': 'SL_Sounds/me.wav'},
    {'name': 'Headphone_check.xlsx', 'path': 'Headphone_check.xlsx'},
    {'name': 'Headphone/t1_2.wav', 'path': 'Headphone/t1_2.wav'},
    {'name': 'TargetSyllables.xlsx', 'path': 'TargetSyllables.xlsx'},
    {'name': 'SL_Sounds/pu.wav', 'path': 'SL_Sounds/pu.wav'},
    {'name': 'SL_Sounds/ge.wav', 'path': 'SL_Sounds/ge.wav'},
    {'name': 'SL_Sounds/ni.wav', 'path': 'SL_Sounds/ni.wav'},
    {'name': 'Headphone/t3_2.wav', 'path': 'Headphone/t3_2.wav'},
    {'name': 'Headphone/t2_1.wav', 'path': 'Headphone/t2_1.wav'},
    {'name': 'SL_Sounds/fu.wav', 'path': 'SL_Sounds/fu.wav'},
    {'name': 'SL_Sounds/ti.wav', 'path': 'SL_Sounds/ti.wav'},
    {'name': 'SL_Sounds/My Syllables/TI.wav', 'path': 'SL_Sounds/My Syllables/TI.wav'},
    {'name': 'SL_Sounds/My Syllables/WI.wav', 'path': 'SL_Sounds/My Syllables/WI.wav'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.10';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://app.prolific.co/submissions/complete?cc=1B9FF7D8', '');

  return Scheduler.Event.NEXT;
}


var Welcome0Clock;
var Welcome0Mssg;
var Welcome0Continue;
var HeadphonePlayClock;
var CheckSound;
var CheckTxt;
var CheckResp;
var TrialNumber;
var counter;
var checkcount;
var Cross2;
var HeadphoneFeedbackClock;
var FeedbackMssg;
var SLWelcomeClock;
var WelcomeMssg;
var ContinueButton;
var ExposurePrepClock;
var c;
var cond;
var ExposureIntro;
var ExposureIntroKey;
var ExposureClock;
var scounter;
var takebreak;
var pausecheck;
var volume0;
var volumecounter0;
var ExposurePlay;
var ExposureCross;
var ExposureInstruction;
var PauseClock;
var PauseCheckKey;
var PauseCross;
var PauseInstruction;
var TakeABreakClock;
var BreakRespSubmit;
var BreakTxt;
var BreakResponse;
var CallExperimenterClock;
var CallExperimentertxt;
var ExperimenterKey;
var Part1IntroClock;
var WelcomeTxt2;
var ContinueKey3;
var repeatCount;
var count;
var TDTrainingIntroClock;
var TrainingBeginTxt;
var TrainingContinueKey;
var TrainingSampleClock;
var SampleMssg2;
var TrainigTarget;
var trainingcount;
var TrainingNumber;
var TrainingSampleContinue;
var TSContinueKey;
var TrainingPlaySampleClock;
var TrainingSampleSound;
var TraingRepeatSound;
var TrainTargetTxt;
var text_5;
var TrainingBeginSample;
var TrainingNumber2;
var TrainEndSample;
var TrainStartClock;
var Three;
var Two;
var text;
var trainClock;
var respOnset;
var TargetOnset;
var previousOnset;
var respcount;
var TrainRT;
var mytimer;
var TDTrainSound;
var TrainResp;
var TDTrainTxt;
var Cross3;
var Pause1secClock;
var PauseTxt2;
var TDTrainFeedbackClock;
var TDTrainFeedbackMssg;
var EndFeedback;
var TrainingContinue;
var P1IntroIIClock;
var P1Intro2Txt;
var text_4;
var key_resp;
var partone;
var parttwo;
var partthree;
var OccurenceC;
var SampleIntroClock;
var TargetMssg;
var PlayTargetKey;
var TargetTxt;
var TrialNoTxt;
var ContinueTxt4;
var PlaySampleClock;
var EndPlay;
var SyllableSound;
var Repeat;
var SoundTxt;
var ContinueKey2;
var text_2;
var TrialNoTxt2;
var TDStartClock;
var Countdown1;
var trial_separateClock;
var respOnsetP;
var respcountP;
var previousOnsetP;
var TargetOnsetP;
var hit;
var mytimerP;
var PlaySound;
var PlayText;
var PlayResp;
var TargetSoundTxt;
var AddRespCountCodeClock;
var OccurrenceCounterClock;
var P2WelcomeClock;
var P2WelcomeTxt;
var P2WelcomeContKey;
var FamRatingIntroClock;
var FamRateIntroTxt;
var FamRateIntroKey;
var FamRatingClock;
var FamRatePrompt;
var RatingScale;
var RatingScale2;
var FamRatingResp;
var Syllab1;
var Syllab2;
var Syllab3;
var Part2Intro2Clock;
var P2IntroTxt2;
var ContinueKey7;
var countClock;
var AFCcount;
var AFCStartClock;
var QuestionNoTxt;
var AFCFirstClock;
var Word1No;
var Word_1_1;
var Word_1_2;
var Word_1_3;
var AFCSecondClock;
var Word2No;
var Word_2_1;
var Word_2_2;
var Word_2_3;
var AFCQuestionClock;
var QuestionTxt;
var AFCResp;
var HearingCheckIntroClock;
var HearingCheckTxt;
var EndKey2;
var HearingCheckClock;
var CheckWord;
var WordOptions;
var CheckQuestion;
var CheckRespKey;
var P2EndClock;
var EndMssg;
var EndAllKey;
var FeedbackQ;
var BlankClock;
var BlankEndKey;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Welcome0"
  Welcome0Clock = new util.Clock();
  Welcome0Mssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'Welcome0Mssg',
    text: 'Welcome to the experiment!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Welcome0Continue = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "HeadphonePlay"
  HeadphonePlayClock = new util.Clock();
  CheckSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  CheckSound.setVolume(1);
  CheckTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'CheckTxt',
    text: 'Which tone was the quietest?\n(Press the corresponding number on your keyboard)\n\n1 = First  2 = Second  3 = Third',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  CheckResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  TrialNumber = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrialNumber',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  counter = 1;
  checkcount = (counter.toString() + "/6");
  
  Cross2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Cross2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "HeadphoneFeedback"
  HeadphoneFeedbackClock = new util.Clock();
  FeedbackMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'FeedbackMssg',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "SLWelcome"
  SLWelcomeClock = new util.Clock();
  WelcomeMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'WelcomeMssg',
    text: 'Researchers from ZZZ University have recently collected some recordings of an alien speech from another planet. The speech consists of syllables that sound similar to English. The researchers need your help to study this speech. \n\nYou will first listen to a 6-minute recording of this speech and then complete three different tasks. In total, the study will take approximately 35 minutes to complete. You will be able to take short breaks in between tasks. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  ContinueButton = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ExposurePrep"
  ExposurePrepClock = new util.Clock();
  c = Math.floor((Math.random() * 3)+1);
  c = 1;
  cond = c.toString();
  
  ExposureIntro = new visual.TextStim({
    win: psychoJS.window,
    name: 'ExposureIntro',
    text: 'First, we will play a recording of this alien speech for 6 minutes with a short break every 2 minutes. \n\nThe recording is a little broken and the speech will stop playing from time to time. Please help the researchers mark the broken parts by pressing SPACE whenever the speech stops.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  ExposureIntroKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Exposure"
  ExposureClock = new util.Clock();
  scounter = 0;
  takebreak = 0;
  pausecheck = 0;
  
  volume0 = 1;
  volumecounter0 = 0;
  
  ExposurePlay = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  ExposurePlay.setVolume(1.0);
  ExposureCross = new visual.TextStim({
    win: psychoJS.window,
    name: 'ExposureCross',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  ExposureInstruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'ExposureInstruction',
    text: 'Press SPACE as soon as you can when the speech stops',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "Pause"
  PauseClock = new util.Clock();
  PauseCheckKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  PauseCross = new visual.TextStim({
    win: psychoJS.window,
    name: 'PauseCross',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  PauseInstruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'PauseInstruction',
    text: 'Press SPACE as soon as you can when the speech stops',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "TakeABreak"
  TakeABreakClock = new util.Clock();
  BreakRespSubmit = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  BreakTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'BreakTxt',
    text: "Let's take a break.\n\n\nHow many different syllables do you think were in the speech? Click the box below to type your response.\n(Press ENTER to submit your answer)",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  BreakResponse = new visual.TextBox({
    win: psychoJS.window,
    name: 'BreakResponse',
    text: 'default text',
    font: 'Arial',
    pos: [0, (- 0.2)], letterHeight: 0.03,
    size: undefined,  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: undefined,
    bold: false, italic: false,
    opacity: 1,
    padding: undefined,
    editable: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  // Initialize components for Routine "CallExperimenter"
  CallExperimenterClock = new util.Clock();
  CallExperimentertxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'CallExperimentertxt',
    text: 'Thank you! Please inform the experimenter that you have finished this part.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  ExperimenterKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Part1Intro"
  Part1IntroClock = new util.Clock();
  WelcomeTxt2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'WelcomeTxt2',
    text: "In the next part, you will complete different tasks using your experience with the alien speech.\n\nFirst, the researchers would like you to mark the timing of when each syllable appears in the speech.\n\nWe will play you 36 short snippets of the speech. At the beginning of each recording, you will be given a 'Target Syllable'. Every time the target syllable appears in the recording, press SPACE as quickly and accurately as you can to record the precise syllable onset time.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  ContinueKey3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  repeatCount = 0;
  count = 0;
  
  // Initialize components for Routine "TDTrainingIntro"
  TDTrainingIntroClock = new util.Clock();
  TrainingBeginTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrainingBeginTxt',
    text: 'We will begin with a training session using a fake speech created by the researchers.\n\nDuring the training, you will see the number of target syllables you recorded and your average response speed. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  TrainingContinueKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "TrainingSample"
  TrainingSampleClock = new util.Clock();
  SampleMssg2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'SampleMssg2',
    text: 'The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  TrainigTarget = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrainigTarget',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  trainingcount = 0;
  
  TrainingNumber = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrainingNumber',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  TrainingSampleContinue = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrainingSampleContinue',
    text: 'Press SPACE to listen to this syllable',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  TSContinueKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "TrainingPlaySample"
  TrainingPlaySampleClock = new util.Clock();
  TrainingSampleSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  TrainingSampleSound.setVolume(0.3);
  TraingRepeatSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  TraingRepeatSound.setVolume(0.3);
  TrainTargetTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrainTargetTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  TrainingBeginSample = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrainingBeginSample',
    text: 'Press SPACE to begin listening',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  TrainingNumber2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrainingNumber2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  TrainEndSample = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "TrainStart"
  TrainStartClock = new util.Clock();
  Three = new visual.TextStim({
    win: psychoJS.window,
    name: 'Three',
    text: '3',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Two = new visual.TextStim({
    win: psychoJS.window,
    name: 'Two',
    text: '2',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '1',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "train"
  trainClock = new util.Clock();
  respOnset = 0;
  TargetOnset = 0;
  previousOnset = 0;
  respcount = 0;
  TrainRT = 0;
  
  mytimer = new util.Clock();
  
  TDTrainSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  TDTrainSound.setVolume(0.3);
  TrainResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  TDTrainTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'TDTrainTxt',
    text: '\n\n\n\nPress SPACE as quickly as possible when you hear the target syllable',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  Cross3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Cross3',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "Pause1sec"
  Pause1secClock = new util.Clock();
  PauseTxt2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'PauseTxt2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "TDTrainFeedback"
  TDTrainFeedbackClock = new util.Clock();
  TDTrainFeedbackMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'TDTrainFeedbackMssg',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  EndFeedback = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  TrainingContinue = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrainingContinue',
    text: 'Press SPACE to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "P1IntroII"
  P1IntroIIClock = new util.Clock();
  P1Intro2Txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'P1Intro2Txt',
    text: "Great job! \nLet's now work with the actual speech. Remember to try your best to press SPACE at the same time as the target syllable onset.\nThere will be no feedback given this time. \n\n\nThere are 36 recordings in total. You may take a short break at the beginning of each recording if you wish.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Press SPACE to begin',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  partone = "0";
  parttwo = "0";
  partthree = "0";
  OccurenceC = 1
  
  // Initialize components for Routine "SampleIntro"
  SampleIntroClock = new util.Clock();
  TargetMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'TargetMssg',
    text: 'The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  PlayTargetKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  TargetTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'TargetTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  repeatCount = 0;
  
  TrialNoTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrialNoTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  ContinueTxt4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ContinueTxt4',
    text: 'Press SPACE to hear the syllable',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "PlaySample"
  PlaySampleClock = new util.Clock();
  EndPlay = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  SyllableSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  SyllableSound.setVolume(1.0);
  Repeat = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  Repeat.setVolume(1);
  SoundTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'SoundTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  ContinueKey2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ContinueKey2',
    text: 'Press SPACE to begin',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  TrialNoTxt2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrialNoTxt2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "TDStart"
  TDStartClock = new util.Clock();
  Countdown1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Countdown1',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial_separate"
  trial_separateClock = new util.Clock();
  respOnsetP = 0;
  respcountP = 0;
  previousOnsetP = 0;
  TargetOnsetP = 0;
  hit = 0;
  mytimerP = new util.Clock();
  
  PlaySound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  PlaySound.setVolume(1);
  PlayText = new visual.TextStim({
    win: psychoJS.window,
    name: 'PlayText',
    text: '\n\n\n\nPress SPACE as quickly as possible when you hear the target syllable',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  PlayResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  TargetSoundTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'TargetSoundTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "Pause1sec"
  Pause1secClock = new util.Clock();
  PauseTxt2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'PauseTxt2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "AddRespCountCode"
  AddRespCountCodeClock = new util.Clock();
  // Initialize components for Routine "OccurrenceCounter"
  OccurrenceCounterClock = new util.Clock();
  // Initialize components for Routine "SampleIntro"
  SampleIntroClock = new util.Clock();
  TargetMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'TargetMssg',
    text: 'The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  PlayTargetKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  TargetTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'TargetTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  repeatCount = 0;
  
  TrialNoTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrialNoTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  ContinueTxt4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ContinueTxt4',
    text: 'Press SPACE to hear the syllable',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "PlaySample"
  PlaySampleClock = new util.Clock();
  EndPlay = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  SyllableSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  SyllableSound.setVolume(1.0);
  Repeat = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  Repeat.setVolume(1);
  SoundTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'SoundTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  ContinueKey2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ContinueKey2',
    text: 'Press SPACE to begin',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  TrialNoTxt2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrialNoTxt2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "TDStart"
  TDStartClock = new util.Clock();
  Countdown1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Countdown1',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial_separate"
  trial_separateClock = new util.Clock();
  respOnsetP = 0;
  respcountP = 0;
  previousOnsetP = 0;
  TargetOnsetP = 0;
  hit = 0;
  mytimerP = new util.Clock();
  
  PlaySound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  PlaySound.setVolume(1);
  PlayText = new visual.TextStim({
    win: psychoJS.window,
    name: 'PlayText',
    text: '\n\n\n\nPress SPACE as quickly as possible when you hear the target syllable',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  PlayResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  TargetSoundTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'TargetSoundTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "Pause1sec"
  Pause1secClock = new util.Clock();
  PauseTxt2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'PauseTxt2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "AddRespCountCode"
  AddRespCountCodeClock = new util.Clock();
  // Initialize components for Routine "OccurrenceCounter"
  OccurrenceCounterClock = new util.Clock();
  // Initialize components for Routine "SampleIntro"
  SampleIntroClock = new util.Clock();
  TargetMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'TargetMssg',
    text: 'The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  PlayTargetKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  TargetTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'TargetTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  repeatCount = 0;
  
  TrialNoTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrialNoTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  ContinueTxt4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ContinueTxt4',
    text: 'Press SPACE to hear the syllable',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "PlaySample"
  PlaySampleClock = new util.Clock();
  EndPlay = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  SyllableSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  SyllableSound.setVolume(1.0);
  Repeat = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  Repeat.setVolume(1);
  SoundTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'SoundTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  ContinueKey2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ContinueKey2',
    text: 'Press SPACE to begin',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  TrialNoTxt2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrialNoTxt2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "TDStart"
  TDStartClock = new util.Clock();
  Countdown1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Countdown1',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial_separate"
  trial_separateClock = new util.Clock();
  respOnsetP = 0;
  respcountP = 0;
  previousOnsetP = 0;
  TargetOnsetP = 0;
  hit = 0;
  mytimerP = new util.Clock();
  
  PlaySound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  PlaySound.setVolume(1);
  PlayText = new visual.TextStim({
    win: psychoJS.window,
    name: 'PlayText',
    text: '\n\n\n\nPress SPACE as quickly as possible when you hear the target syllable',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  PlayResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  TargetSoundTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'TargetSoundTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "Pause1sec"
  Pause1secClock = new util.Clock();
  PauseTxt2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'PauseTxt2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "AddRespCountCode"
  AddRespCountCodeClock = new util.Clock();
  // Initialize components for Routine "CallExperimenter"
  CallExperimenterClock = new util.Clock();
  CallExperimentertxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'CallExperimentertxt',
    text: 'Thank you! Please inform the experimenter that you have finished this part.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  ExperimenterKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "P2Welcome"
  P2WelcomeClock = new util.Clock();
  P2WelcomeTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'P2WelcomeTxt',
    text: "It seems like the alien speech contains regularly repeating 'words'. In the next part of this study, you will be asked to distinguish these alien words from other sounds.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  P2WelcomeContKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "FamRatingIntro"
  FamRatingIntroClock = new util.Clock();
  FamRateIntroTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'FamRateIntroTxt',
    text: 'In this part, you will listen to short speech sounds. Some of these may sound familiar to you, as they were spoken in the first part of the study. Others may sound unfamiliar, as they were not spoken in the first part of the study.\n\nYour job is to listen carefully to these short sounds and rate how familiar they sound to you on a scale of 1 (Not familiar) to 4 (Very familiar).\n\nThere will be 12 trials in total.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  FamRateIntroKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Pause1sec"
  Pause1secClock = new util.Clock();
  PauseTxt2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'PauseTxt2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "FamRating"
  FamRatingClock = new util.Clock();
  FamRatePrompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'FamRatePrompt',
    text: 'How familiar does this word sound?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  RatingScale = new visual.TextStim({
    win: psychoJS.window,
    name: 'RatingScale',
    text: '1 ----------------- 2 ----------------- 3 ----------------- 4',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  RatingScale2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'RatingScale2',
    text: '\n\n(Not familiar)                                                                     (Very familiar)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  FamRatingResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Syllab1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.38,
    });
  Syllab1.setVolume(1);
  Syllab2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.38,
    });
  Syllab2.setVolume(1);
  Syllab3 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.38,
    });
  Syllab3.setVolume(1);
  // Initialize components for Routine "Part2Intro2"
  Part2Intro2Clock = new util.Clock();
  P2IntroTxt2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'P2IntroTxt2',
    text: 'In the next part, you will hear two speech sounds. Your task is to indicate whether the first or the second one sounds like a word from the language you just listened to.\n\nThere will be 16 trials in total.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  ContinueKey7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "count"
  countClock = new util.Clock();
  AFCcount = 0;
  
  // Initialize components for Routine "AFCStart"
  AFCStartClock = new util.Clock();
  QuestionNoTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'QuestionNoTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "AFCFirst"
  AFCFirstClock = new util.Clock();
  Word1No = new visual.TextStim({
    win: psychoJS.window,
    name: 'Word1No',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Word_1_1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.38,
    });
  Word_1_1.setVolume(1);
  Word_1_2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.38,
    });
  Word_1_2.setVolume(1);
  Word_1_3 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.38,
    });
  Word_1_3.setVolume(1);
  // Initialize components for Routine "AFCSecond"
  AFCSecondClock = new util.Clock();
  Word2No = new visual.TextStim({
    win: psychoJS.window,
    name: 'Word2No',
    text: '2',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Word_2_1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.38,
    });
  Word_2_1.setVolume(1);
  Word_2_2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.38,
    });
  Word_2_2.setVolume(1);
  Word_2_3 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.38,
    });
  Word_2_3.setVolume(1);
  // Initialize components for Routine "AFCQuestion"
  AFCQuestionClock = new util.Clock();
  QuestionTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'QuestionTxt',
    text: 'Which word sounded correct?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  AFCResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "HearingCheckIntro"
  HearingCheckIntroClock = new util.Clock();
  HearingCheckTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'HearingCheckTxt',
    text: 'Thank you for helping the researchers!\n\nLastly, we will play you a few short speech sounds. In each trial, please select the syllable that matches with the sound you hear.\n\n\n\n\n\nPress SPACE to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  EndKey2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Pause1sec"
  Pause1secClock = new util.Clock();
  PauseTxt2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'PauseTxt2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "HearingCheck"
  HearingCheckClock = new util.Clock();
  CheckWord = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  CheckWord.setVolume(1);
  WordOptions = new visual.TextStim({
    win: psychoJS.window,
    name: 'WordOptions',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  CheckQuestion = new visual.TextStim({
    win: psychoJS.window,
    name: 'CheckQuestion',
    text: 'Which sound did you hear?\n(Press the corresponding number on your keyboard)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  CheckRespKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "P2End"
  P2EndClock = new util.Clock();
  EndMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'EndMssg',
    text: 'You have now completed all the tasks.\nWe appreciate your time and cooporation. \n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  EndAllKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  FeedbackQ = new visual.TextStim({
    win: psychoJS.window,
    name: 'FeedbackQ',
    text: '',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Blank"
  BlankClock = new util.Clock();
  BlankEndKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _Welcome0Continue_allKeys;
var Welcome0Components;
function Welcome0RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Welcome0'-------
    t = 0;
    Welcome0Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Welcome0Continue.keys = undefined;
    Welcome0Continue.rt = undefined;
    _Welcome0Continue_allKeys = [];
    // keep track of which components have finished
    Welcome0Components = [];
    Welcome0Components.push(Welcome0Mssg);
    Welcome0Components.push(Welcome0Continue);
    
    for (const thisComponent of Welcome0Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Welcome0RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Welcome0'-------
    // get current time
    t = Welcome0Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Welcome0Mssg* updates
    if (t >= 0.0 && Welcome0Mssg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Welcome0Mssg.tStart = t;  // (not accounting for frame time here)
      Welcome0Mssg.frameNStart = frameN;  // exact frame index
      
      Welcome0Mssg.setAutoDraw(true);
    }

    
    // *Welcome0Continue* updates
    if (t >= 0.0 && Welcome0Continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Welcome0Continue.tStart = t;  // (not accounting for frame time here)
      Welcome0Continue.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Welcome0Continue.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Welcome0Continue.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Welcome0Continue.clearEvents(); });
    }

    if (Welcome0Continue.status === PsychoJS.Status.STARTED) {
      let theseKeys = Welcome0Continue.getKeys({keyList: ['space'], waitRelease: false});
      _Welcome0Continue_allKeys = _Welcome0Continue_allKeys.concat(theseKeys);
      if (_Welcome0Continue_allKeys.length > 0) {
        Welcome0Continue.keys = _Welcome0Continue_allKeys[_Welcome0Continue_allKeys.length - 1].name;  // just the last key pressed
        Welcome0Continue.rt = _Welcome0Continue_allKeys[_Welcome0Continue_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Welcome0Components)
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


function Welcome0RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Welcome0'-------
    for (const thisComponent of Welcome0Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Welcome0Continue.keys', Welcome0Continue.keys);
    if (typeof Welcome0Continue.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Welcome0Continue.rt', Welcome0Continue.rt);
        routineTimer.reset();
        }
    
    Welcome0Continue.stop();
    // the Routine "Welcome0" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var HeadphoneLoop;
var currentLoop;
function HeadphoneLoopLoopBegin(HeadphoneLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  HeadphoneLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 0, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'Headphone_check.xlsx',
    seed: undefined, name: 'HeadphoneLoop'
  });
  psychoJS.experiment.addLoop(HeadphoneLoop); // add the loop to the experiment
  currentLoop = HeadphoneLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisHeadphoneLoop of HeadphoneLoop) {
    const snapshot = HeadphoneLoop.getSnapshot();
    HeadphoneLoopLoopScheduler.add(importConditions(snapshot));
    HeadphoneLoopLoopScheduler.add(HeadphonePlayRoutineBegin(snapshot));
    HeadphoneLoopLoopScheduler.add(HeadphonePlayRoutineEachFrame(snapshot));
    HeadphoneLoopLoopScheduler.add(HeadphonePlayRoutineEnd(snapshot));
    HeadphoneLoopLoopScheduler.add(HeadphoneFeedbackRoutineBegin(snapshot));
    HeadphoneLoopLoopScheduler.add(HeadphoneFeedbackRoutineEachFrame(snapshot));
    HeadphoneLoopLoopScheduler.add(HeadphoneFeedbackRoutineEnd(snapshot));
    HeadphoneLoopLoopScheduler.add(endLoopIteration(HeadphoneLoopLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function HeadphoneLoopLoopEnd() {
  psychoJS.experiment.removeLoop(HeadphoneLoop);

  return Scheduler.Event.NEXT;
}


var ExposureLoop;
function ExposureLoopLoopBegin(ExposureLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  ExposureLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, (cond + "_exposure.xlsx"), '0:1080'),
    seed: undefined, name: 'ExposureLoop'
  });
  psychoJS.experiment.addLoop(ExposureLoop); // add the loop to the experiment
  currentLoop = ExposureLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisExposureLoop of ExposureLoop) {
    const snapshot = ExposureLoop.getSnapshot();
    ExposureLoopLoopScheduler.add(importConditions(snapshot));
    ExposureLoopLoopScheduler.add(ExposureRoutineBegin(snapshot));
    ExposureLoopLoopScheduler.add(ExposureRoutineEachFrame(snapshot));
    ExposureLoopLoopScheduler.add(ExposureRoutineEnd(snapshot));
    const PauseOnOffLoopScheduler = new Scheduler(psychoJS);
    ExposureLoopLoopScheduler.add(PauseOnOffLoopBegin, PauseOnOffLoopScheduler);
    ExposureLoopLoopScheduler.add(PauseOnOffLoopScheduler);
    ExposureLoopLoopScheduler.add(PauseOnOffLoopEnd);
    const BreakOnOffLoopScheduler = new Scheduler(psychoJS);
    ExposureLoopLoopScheduler.add(BreakOnOffLoopBegin, BreakOnOffLoopScheduler);
    ExposureLoopLoopScheduler.add(BreakOnOffLoopScheduler);
    ExposureLoopLoopScheduler.add(BreakOnOffLoopEnd);
    ExposureLoopLoopScheduler.add(endLoopIteration(ExposureLoopLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var PauseOnOff;
function PauseOnOffLoopBegin(PauseOnOffLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  PauseOnOff = new TrialHandler({
    psychoJS: psychoJS,
    nReps: pausecheck, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'PauseOnOff'
  });
  psychoJS.experiment.addLoop(PauseOnOff); // add the loop to the experiment
  currentLoop = PauseOnOff;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPauseOnOff of PauseOnOff) {
    const snapshot = PauseOnOff.getSnapshot();
    PauseOnOffLoopScheduler.add(importConditions(snapshot));
    PauseOnOffLoopScheduler.add(PauseRoutineBegin(snapshot));
    PauseOnOffLoopScheduler.add(PauseRoutineEachFrame(snapshot));
    PauseOnOffLoopScheduler.add(PauseRoutineEnd(snapshot));
    PauseOnOffLoopScheduler.add(endLoopIteration(PauseOnOffLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function PauseOnOffLoopEnd() {
  psychoJS.experiment.removeLoop(PauseOnOff);

  return Scheduler.Event.NEXT;
}


var BreakOnOff;
function BreakOnOffLoopBegin(BreakOnOffLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  BreakOnOff = new TrialHandler({
    psychoJS: psychoJS,
    nReps: takebreak, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'BreakOnOff'
  });
  psychoJS.experiment.addLoop(BreakOnOff); // add the loop to the experiment
  currentLoop = BreakOnOff;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisBreakOnOff of BreakOnOff) {
    const snapshot = BreakOnOff.getSnapshot();
    BreakOnOffLoopScheduler.add(importConditions(snapshot));
    BreakOnOffLoopScheduler.add(TakeABreakRoutineBegin(snapshot));
    BreakOnOffLoopScheduler.add(TakeABreakRoutineEachFrame(snapshot));
    BreakOnOffLoopScheduler.add(TakeABreakRoutineEnd(snapshot));
    BreakOnOffLoopScheduler.add(endLoopIteration(BreakOnOffLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function BreakOnOffLoopEnd() {
  psychoJS.experiment.removeLoop(BreakOnOff);

  return Scheduler.Event.NEXT;
}


function ExposureLoopLoopEnd() {
  psychoJS.experiment.removeLoop(ExposureLoop);

  return Scheduler.Event.NEXT;
}


var TrainTDLoop;
function TrainTDLoopLoopBegin(TrainTDLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  TrainTDLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'TargetSyllables.xlsx', '216:218'),
    seed: undefined, name: 'TrainTDLoop'
  });
  psychoJS.experiment.addLoop(TrainTDLoop); // add the loop to the experiment
  currentLoop = TrainTDLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrainTDLoop of TrainTDLoop) {
    const snapshot = TrainTDLoop.getSnapshot();
    TrainTDLoopLoopScheduler.add(importConditions(snapshot));
    TrainTDLoopLoopScheduler.add(TrainingSampleRoutineBegin(snapshot));
    TrainTDLoopLoopScheduler.add(TrainingSampleRoutineEachFrame(snapshot));
    TrainTDLoopLoopScheduler.add(TrainingSampleRoutineEnd(snapshot));
    TrainTDLoopLoopScheduler.add(TrainingPlaySampleRoutineBegin(snapshot));
    TrainTDLoopLoopScheduler.add(TrainingPlaySampleRoutineEachFrame(snapshot));
    TrainTDLoopLoopScheduler.add(TrainingPlaySampleRoutineEnd(snapshot));
    TrainTDLoopLoopScheduler.add(TrainStartRoutineBegin(snapshot));
    TrainTDLoopLoopScheduler.add(TrainStartRoutineEachFrame(snapshot));
    TrainTDLoopLoopScheduler.add(TrainStartRoutineEnd(snapshot));
    const TrainTDLoopScheduler = new Scheduler(psychoJS);
    TrainTDLoopLoopScheduler.add(TrainTDLoopBegin, TrainTDLoopScheduler);
    TrainTDLoopLoopScheduler.add(TrainTDLoopScheduler);
    TrainTDLoopLoopScheduler.add(TrainTDLoopEnd);
    TrainTDLoopLoopScheduler.add(Pause1secRoutineBegin(snapshot));
    TrainTDLoopLoopScheduler.add(Pause1secRoutineEachFrame(snapshot));
    TrainTDLoopLoopScheduler.add(Pause1secRoutineEnd(snapshot));
    TrainTDLoopLoopScheduler.add(TDTrainFeedbackRoutineBegin(snapshot));
    TrainTDLoopLoopScheduler.add(TDTrainFeedbackRoutineEachFrame(snapshot));
    TrainTDLoopLoopScheduler.add(TDTrainFeedbackRoutineEnd(snapshot));
    TrainTDLoopLoopScheduler.add(endLoopIteration(TrainTDLoopLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var TrainTD;
function TrainTDLoopBegin(TrainTDLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  TrainTD = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'TDTrainList.xlsx', '0:45'),
    seed: undefined, name: 'TrainTD'
  });
  psychoJS.experiment.addLoop(TrainTD); // add the loop to the experiment
  currentLoop = TrainTD;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrainTD of TrainTD) {
    const snapshot = TrainTD.getSnapshot();
    TrainTDLoopScheduler.add(importConditions(snapshot));
    TrainTDLoopScheduler.add(trainRoutineBegin(snapshot));
    TrainTDLoopScheduler.add(trainRoutineEachFrame(snapshot));
    TrainTDLoopScheduler.add(trainRoutineEnd(snapshot));
    TrainTDLoopScheduler.add(endLoopIteration(TrainTDLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function TrainTDLoopEnd() {
  psychoJS.experiment.removeLoop(TrainTD);

  return Scheduler.Event.NEXT;
}


function TrainTDLoopLoopEnd() {
  psychoJS.experiment.removeLoop(TrainTDLoop);

  return Scheduler.Event.NEXT;
}


var TD;
function TDLoopBegin(TDLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  TD = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'TD'
  });
  psychoJS.experiment.addLoop(TD); // add the loop to the experiment
  currentLoop = TD;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTD of TD) {
    const snapshot = TD.getSnapshot();
    TDLoopScheduler.add(importConditions(snapshot));
    const FirstTDLoopLoopScheduler = new Scheduler(psychoJS);
    TDLoopScheduler.add(FirstTDLoopLoopBegin, FirstTDLoopLoopScheduler);
    TDLoopScheduler.add(FirstTDLoopLoopScheduler);
    TDLoopScheduler.add(FirstTDLoopLoopEnd);
    TDLoopScheduler.add(OccurrenceCounterRoutineBegin(snapshot));
    TDLoopScheduler.add(OccurrenceCounterRoutineEachFrame(snapshot));
    TDLoopScheduler.add(OccurrenceCounterRoutineEnd(snapshot));
    const SecondTDLoopLoopScheduler = new Scheduler(psychoJS);
    TDLoopScheduler.add(SecondTDLoopLoopBegin, SecondTDLoopLoopScheduler);
    TDLoopScheduler.add(SecondTDLoopLoopScheduler);
    TDLoopScheduler.add(SecondTDLoopLoopEnd);
    TDLoopScheduler.add(OccurrenceCounterRoutineBegin(snapshot));
    TDLoopScheduler.add(OccurrenceCounterRoutineEachFrame(snapshot));
    TDLoopScheduler.add(OccurrenceCounterRoutineEnd(snapshot));
    const thirdTDLoopLoopScheduler = new Scheduler(psychoJS);
    TDLoopScheduler.add(thirdTDLoopLoopBegin, thirdTDLoopLoopScheduler);
    TDLoopScheduler.add(thirdTDLoopLoopScheduler);
    TDLoopScheduler.add(thirdTDLoopLoopEnd);
    TDLoopScheduler.add(endLoopIteration(TDLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var FirstTDLoop;
function FirstTDLoopLoopBegin(FirstTDLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  FirstTDLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'TargetSyllables.xlsx', first),
    seed: undefined, name: 'FirstTDLoop'
  });
  psychoJS.experiment.addLoop(FirstTDLoop); // add the loop to the experiment
  currentLoop = FirstTDLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisFirstTDLoop of FirstTDLoop) {
    const snapshot = FirstTDLoop.getSnapshot();
    FirstTDLoopLoopScheduler.add(importConditions(snapshot));
    FirstTDLoopLoopScheduler.add(SampleIntroRoutineBegin(snapshot));
    FirstTDLoopLoopScheduler.add(SampleIntroRoutineEachFrame(snapshot));
    FirstTDLoopLoopScheduler.add(SampleIntroRoutineEnd(snapshot));
    FirstTDLoopLoopScheduler.add(PlaySampleRoutineBegin(snapshot));
    FirstTDLoopLoopScheduler.add(PlaySampleRoutineEachFrame(snapshot));
    FirstTDLoopLoopScheduler.add(PlaySampleRoutineEnd(snapshot));
    FirstTDLoopLoopScheduler.add(TDStartRoutineBegin(snapshot));
    FirstTDLoopLoopScheduler.add(TDStartRoutineEachFrame(snapshot));
    FirstTDLoopLoopScheduler.add(TDStartRoutineEnd(snapshot));
    const FirstTDLoopScheduler = new Scheduler(psychoJS);
    FirstTDLoopLoopScheduler.add(FirstTDLoopBegin, FirstTDLoopScheduler);
    FirstTDLoopLoopScheduler.add(FirstTDLoopScheduler);
    FirstTDLoopLoopScheduler.add(FirstTDLoopEnd);
    FirstTDLoopLoopScheduler.add(Pause1secRoutineBegin(snapshot));
    FirstTDLoopLoopScheduler.add(Pause1secRoutineEachFrame(snapshot));
    FirstTDLoopLoopScheduler.add(Pause1secRoutineEnd(snapshot));
    FirstTDLoopLoopScheduler.add(AddRespCountCodeRoutineBegin(snapshot));
    FirstTDLoopLoopScheduler.add(AddRespCountCodeRoutineEachFrame(snapshot));
    FirstTDLoopLoopScheduler.add(AddRespCountCodeRoutineEnd(snapshot));
    FirstTDLoopLoopScheduler.add(endLoopIteration(FirstTDLoopLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var FirstTD;
function FirstTDLoopBegin(FirstTDLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  FirstTD = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, (cond + "_TD_list.xlsx"), rows),
    seed: undefined, name: 'FirstTD'
  });
  psychoJS.experiment.addLoop(FirstTD); // add the loop to the experiment
  currentLoop = FirstTD;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisFirstTD of FirstTD) {
    const snapshot = FirstTD.getSnapshot();
    FirstTDLoopScheduler.add(importConditions(snapshot));
    FirstTDLoopScheduler.add(trial_separateRoutineBegin(snapshot));
    FirstTDLoopScheduler.add(trial_separateRoutineEachFrame(snapshot));
    FirstTDLoopScheduler.add(trial_separateRoutineEnd(snapshot));
    FirstTDLoopScheduler.add(endLoopIteration(FirstTDLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function FirstTDLoopEnd() {
  psychoJS.experiment.removeLoop(FirstTD);

  return Scheduler.Event.NEXT;
}


function FirstTDLoopLoopEnd() {
  psychoJS.experiment.removeLoop(FirstTDLoop);

  return Scheduler.Event.NEXT;
}


var SecondTDLoop;
function SecondTDLoopLoopBegin(SecondTDLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  SecondTDLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'TargetSyllables.xlsx', second),
    seed: undefined, name: 'SecondTDLoop'
  });
  psychoJS.experiment.addLoop(SecondTDLoop); // add the loop to the experiment
  currentLoop = SecondTDLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisSecondTDLoop of SecondTDLoop) {
    const snapshot = SecondTDLoop.getSnapshot();
    SecondTDLoopLoopScheduler.add(importConditions(snapshot));
    SecondTDLoopLoopScheduler.add(SampleIntroRoutineBegin(snapshot));
    SecondTDLoopLoopScheduler.add(SampleIntroRoutineEachFrame(snapshot));
    SecondTDLoopLoopScheduler.add(SampleIntroRoutineEnd(snapshot));
    SecondTDLoopLoopScheduler.add(PlaySampleRoutineBegin(snapshot));
    SecondTDLoopLoopScheduler.add(PlaySampleRoutineEachFrame(snapshot));
    SecondTDLoopLoopScheduler.add(PlaySampleRoutineEnd(snapshot));
    SecondTDLoopLoopScheduler.add(TDStartRoutineBegin(snapshot));
    SecondTDLoopLoopScheduler.add(TDStartRoutineEachFrame(snapshot));
    SecondTDLoopLoopScheduler.add(TDStartRoutineEnd(snapshot));
    const SecondTDLoopScheduler = new Scheduler(psychoJS);
    SecondTDLoopLoopScheduler.add(SecondTDLoopBegin, SecondTDLoopScheduler);
    SecondTDLoopLoopScheduler.add(SecondTDLoopScheduler);
    SecondTDLoopLoopScheduler.add(SecondTDLoopEnd);
    SecondTDLoopLoopScheduler.add(Pause1secRoutineBegin(snapshot));
    SecondTDLoopLoopScheduler.add(Pause1secRoutineEachFrame(snapshot));
    SecondTDLoopLoopScheduler.add(Pause1secRoutineEnd(snapshot));
    SecondTDLoopLoopScheduler.add(AddRespCountCodeRoutineBegin(snapshot));
    SecondTDLoopLoopScheduler.add(AddRespCountCodeRoutineEachFrame(snapshot));
    SecondTDLoopLoopScheduler.add(AddRespCountCodeRoutineEnd(snapshot));
    SecondTDLoopLoopScheduler.add(endLoopIteration(SecondTDLoopLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var SecondTD;
function SecondTDLoopBegin(SecondTDLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  SecondTD = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, (cond + "_TD_list.xlsx"), rows),
    seed: undefined, name: 'SecondTD'
  });
  psychoJS.experiment.addLoop(SecondTD); // add the loop to the experiment
  currentLoop = SecondTD;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisSecondTD of SecondTD) {
    const snapshot = SecondTD.getSnapshot();
    SecondTDLoopScheduler.add(importConditions(snapshot));
    SecondTDLoopScheduler.add(trial_separateRoutineBegin(snapshot));
    SecondTDLoopScheduler.add(trial_separateRoutineEachFrame(snapshot));
    SecondTDLoopScheduler.add(trial_separateRoutineEnd(snapshot));
    SecondTDLoopScheduler.add(endLoopIteration(SecondTDLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function SecondTDLoopEnd() {
  psychoJS.experiment.removeLoop(SecondTD);

  return Scheduler.Event.NEXT;
}


function SecondTDLoopLoopEnd() {
  psychoJS.experiment.removeLoop(SecondTDLoop);

  return Scheduler.Event.NEXT;
}


var thirdTDLoop;
function thirdTDLoopLoopBegin(thirdTDLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  thirdTDLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'TargetSyllables.xlsx', third),
    seed: undefined, name: 'thirdTDLoop'
  });
  psychoJS.experiment.addLoop(thirdTDLoop); // add the loop to the experiment
  currentLoop = thirdTDLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisThirdTDLoop of thirdTDLoop) {
    const snapshot = thirdTDLoop.getSnapshot();
    thirdTDLoopLoopScheduler.add(importConditions(snapshot));
    thirdTDLoopLoopScheduler.add(SampleIntroRoutineBegin(snapshot));
    thirdTDLoopLoopScheduler.add(SampleIntroRoutineEachFrame(snapshot));
    thirdTDLoopLoopScheduler.add(SampleIntroRoutineEnd(snapshot));
    thirdTDLoopLoopScheduler.add(PlaySampleRoutineBegin(snapshot));
    thirdTDLoopLoopScheduler.add(PlaySampleRoutineEachFrame(snapshot));
    thirdTDLoopLoopScheduler.add(PlaySampleRoutineEnd(snapshot));
    thirdTDLoopLoopScheduler.add(TDStartRoutineBegin(snapshot));
    thirdTDLoopLoopScheduler.add(TDStartRoutineEachFrame(snapshot));
    thirdTDLoopLoopScheduler.add(TDStartRoutineEnd(snapshot));
    const ThirdTDLoopScheduler = new Scheduler(psychoJS);
    thirdTDLoopLoopScheduler.add(ThirdTDLoopBegin, ThirdTDLoopScheduler);
    thirdTDLoopLoopScheduler.add(ThirdTDLoopScheduler);
    thirdTDLoopLoopScheduler.add(ThirdTDLoopEnd);
    thirdTDLoopLoopScheduler.add(Pause1secRoutineBegin(snapshot));
    thirdTDLoopLoopScheduler.add(Pause1secRoutineEachFrame(snapshot));
    thirdTDLoopLoopScheduler.add(Pause1secRoutineEnd(snapshot));
    thirdTDLoopLoopScheduler.add(AddRespCountCodeRoutineBegin(snapshot));
    thirdTDLoopLoopScheduler.add(AddRespCountCodeRoutineEachFrame(snapshot));
    thirdTDLoopLoopScheduler.add(AddRespCountCodeRoutineEnd(snapshot));
    thirdTDLoopLoopScheduler.add(endLoopIteration(thirdTDLoopLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var ThirdTD;
function ThirdTDLoopBegin(ThirdTDLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  ThirdTD = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, (cond + "_TD_list.xlsx"), rows),
    seed: undefined, name: 'ThirdTD'
  });
  psychoJS.experiment.addLoop(ThirdTD); // add the loop to the experiment
  currentLoop = ThirdTD;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisThirdTD of ThirdTD) {
    const snapshot = ThirdTD.getSnapshot();
    ThirdTDLoopScheduler.add(importConditions(snapshot));
    ThirdTDLoopScheduler.add(trial_separateRoutineBegin(snapshot));
    ThirdTDLoopScheduler.add(trial_separateRoutineEachFrame(snapshot));
    ThirdTDLoopScheduler.add(trial_separateRoutineEnd(snapshot));
    ThirdTDLoopScheduler.add(endLoopIteration(ThirdTDLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function ThirdTDLoopEnd() {
  psychoJS.experiment.removeLoop(ThirdTD);

  return Scheduler.Event.NEXT;
}


function thirdTDLoopLoopEnd() {
  psychoJS.experiment.removeLoop(thirdTDLoop);

  return Scheduler.Event.NEXT;
}


function TDLoopEnd() {
  psychoJS.experiment.removeLoop(TD);

  return Scheduler.Event.NEXT;
}


var FamRatingLoop;
function FamRatingLoopLoopBegin(FamRatingLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  FamRatingLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, (cond + "_explicit.xlsx"), '0:12'),
    seed: undefined, name: 'FamRatingLoop'
  });
  psychoJS.experiment.addLoop(FamRatingLoop); // add the loop to the experiment
  currentLoop = FamRatingLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisFamRatingLoop of FamRatingLoop) {
    const snapshot = FamRatingLoop.getSnapshot();
    FamRatingLoopLoopScheduler.add(importConditions(snapshot));
    FamRatingLoopLoopScheduler.add(Pause1secRoutineBegin(snapshot));
    FamRatingLoopLoopScheduler.add(Pause1secRoutineEachFrame(snapshot));
    FamRatingLoopLoopScheduler.add(Pause1secRoutineEnd(snapshot));
    FamRatingLoopLoopScheduler.add(FamRatingRoutineBegin(snapshot));
    FamRatingLoopLoopScheduler.add(FamRatingRoutineEachFrame(snapshot));
    FamRatingLoopLoopScheduler.add(FamRatingRoutineEnd(snapshot));
    FamRatingLoopLoopScheduler.add(endLoopIteration(FamRatingLoopLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function FamRatingLoopLoopEnd() {
  psychoJS.experiment.removeLoop(FamRatingLoop);

  return Scheduler.Event.NEXT;
}


var AFCTest;
function AFCTestLoopBegin(AFCTestLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  AFCTest = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, (cond + "_explicit.xlsx"), '12:28'),
    seed: undefined, name: 'AFCTest'
  });
  psychoJS.experiment.addLoop(AFCTest); // add the loop to the experiment
  currentLoop = AFCTest;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisAFCTest of AFCTest) {
    const snapshot = AFCTest.getSnapshot();
    AFCTestLoopScheduler.add(importConditions(snapshot));
    AFCTestLoopScheduler.add(countRoutineBegin(snapshot));
    AFCTestLoopScheduler.add(countRoutineEachFrame(snapshot));
    AFCTestLoopScheduler.add(countRoutineEnd(snapshot));
    AFCTestLoopScheduler.add(AFCStartRoutineBegin(snapshot));
    AFCTestLoopScheduler.add(AFCStartRoutineEachFrame(snapshot));
    AFCTestLoopScheduler.add(AFCStartRoutineEnd(snapshot));
    AFCTestLoopScheduler.add(AFCFirstRoutineBegin(snapshot));
    AFCTestLoopScheduler.add(AFCFirstRoutineEachFrame(snapshot));
    AFCTestLoopScheduler.add(AFCFirstRoutineEnd(snapshot));
    AFCTestLoopScheduler.add(AFCSecondRoutineBegin(snapshot));
    AFCTestLoopScheduler.add(AFCSecondRoutineEachFrame(snapshot));
    AFCTestLoopScheduler.add(AFCSecondRoutineEnd(snapshot));
    AFCTestLoopScheduler.add(AFCQuestionRoutineBegin(snapshot));
    AFCTestLoopScheduler.add(AFCQuestionRoutineEachFrame(snapshot));
    AFCTestLoopScheduler.add(AFCQuestionRoutineEnd(snapshot));
    AFCTestLoopScheduler.add(endLoopIteration(AFCTestLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function AFCTestLoopEnd() {
  psychoJS.experiment.removeLoop(AFCTest);

  return Scheduler.Event.NEXT;
}


var HearingcheckLoop;
function HearingcheckLoopLoopBegin(HearingcheckLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  HearingcheckLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'HearingCheckSounds.xlsx',
    seed: undefined, name: 'HearingcheckLoop'
  });
  psychoJS.experiment.addLoop(HearingcheckLoop); // add the loop to the experiment
  currentLoop = HearingcheckLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisHearingcheckLoop of HearingcheckLoop) {
    const snapshot = HearingcheckLoop.getSnapshot();
    HearingcheckLoopLoopScheduler.add(importConditions(snapshot));
    HearingcheckLoopLoopScheduler.add(Pause1secRoutineBegin(snapshot));
    HearingcheckLoopLoopScheduler.add(Pause1secRoutineEachFrame(snapshot));
    HearingcheckLoopLoopScheduler.add(Pause1secRoutineEnd(snapshot));
    HearingcheckLoopLoopScheduler.add(HearingCheckRoutineBegin(snapshot));
    HearingcheckLoopLoopScheduler.add(HearingCheckRoutineEachFrame(snapshot));
    HearingcheckLoopLoopScheduler.add(HearingCheckRoutineEnd(snapshot));
    HearingcheckLoopLoopScheduler.add(endLoopIteration(HearingcheckLoopLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function HearingcheckLoopLoopEnd() {
  psychoJS.experiment.removeLoop(HearingcheckLoop);

  return Scheduler.Event.NEXT;
}


var _CheckResp_allKeys;
var HeadphonePlayComponents;
function HeadphonePlayRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'HeadphonePlay'-------
    t = 0;
    HeadphonePlayClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    CheckSound = new sound.Sound({
    win: psychoJS.window,
    value: File,
    secs: -1,
    });
    CheckSound.setVolume(1);
    CheckResp.keys = undefined;
    CheckResp.rt = undefined;
    _CheckResp_allKeys = [];
    TrialNumber.setText(checkcount);
    counter += 1;
    checkcount = (counter.toString() + "/6");
    
    // keep track of which components have finished
    HeadphonePlayComponents = [];
    HeadphonePlayComponents.push(CheckSound);
    HeadphonePlayComponents.push(CheckTxt);
    HeadphonePlayComponents.push(CheckResp);
    HeadphonePlayComponents.push(TrialNumber);
    HeadphonePlayComponents.push(Cross2);
    
    for (const thisComponent of HeadphonePlayComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function HeadphonePlayRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'HeadphonePlay'-------
    // get current time
    t = HeadphonePlayClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop CheckSound
    if (t >= 0.5 && CheckSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CheckSound.tStart = t;  // (not accounting for frame time here)
      CheckSound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ CheckSound.play(); });  // screen flip
      CheckSound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (CheckSound.getDuration() + CheckSound.tStart)     && CheckSound.status === PsychoJS.Status.STARTED) {
      CheckSound.stop();  // stop the sound (if longer than duration)
      CheckSound.status = PsychoJS.Status.FINISHED;
    }
    
    // *CheckTxt* updates
    if (t >= (CheckSound.getDuration() + 0.5) && CheckTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CheckTxt.tStart = t;  // (not accounting for frame time here)
      CheckTxt.frameNStart = frameN;  // exact frame index
      
      CheckTxt.setAutoDraw(true);
    }

    
    // *CheckResp* updates
    if (t >= (CheckSound.getDuration() + 0.5) && CheckResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CheckResp.tStart = t;  // (not accounting for frame time here)
      CheckResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { CheckResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { CheckResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { CheckResp.clearEvents(); });
    }

    if (CheckResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = CheckResp.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _CheckResp_allKeys = _CheckResp_allKeys.concat(theseKeys);
      if (_CheckResp_allKeys.length > 0) {
        CheckResp.keys = _CheckResp_allKeys[_CheckResp_allKeys.length - 1].name;  // just the last key pressed
        CheckResp.rt = _CheckResp_allKeys[_CheckResp_allKeys.length - 1].rt;
        // was this correct?
        if (CheckResp.keys == Correct) {
            CheckResp.corr = 1;
        } else {
            CheckResp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *TrialNumber* updates
    if (t >= 0.0 && TrialNumber.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrialNumber.tStart = t;  // (not accounting for frame time here)
      TrialNumber.frameNStart = frameN;  // exact frame index
      
      TrialNumber.setAutoDraw(true);
    }

    frameRemains = 0.0 + (CheckSound.getDuration() + 0.5) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((TrialNumber.status === PsychoJS.Status.STARTED || TrialNumber.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      TrialNumber.setAutoDraw(false);
    }
    
    // *Cross2* updates
    if (t >= 0.0 && Cross2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Cross2.tStart = t;  // (not accounting for frame time here)
      Cross2.frameNStart = frameN;  // exact frame index
      
      Cross2.setAutoDraw(true);
    }

    frameRemains = 0.0 + (CheckSound.getDuration() + 0.5) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Cross2.status === PsychoJS.Status.STARTED || Cross2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      Cross2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of HeadphonePlayComponents)
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


var message;
function HeadphonePlayRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'HeadphonePlay'-------
    for (const thisComponent of HeadphonePlayComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    CheckSound.stop();  // ensure sound has stopped at end of routine
    // was no response the correct answer?!
    if (CheckResp.keys === undefined) {
      if (['None','none',undefined].includes(Correct)) {
         CheckResp.corr = 1;  // correct non-response
      } else {
         CheckResp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('CheckResp.keys', CheckResp.keys);
    psychoJS.experiment.addData('CheckResp.corr', CheckResp.corr);
    if (typeof CheckResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('CheckResp.rt', CheckResp.rt);
        routineTimer.reset();
        }
    
    CheckResp.stop();
    if ((CheckResp.corr === 1)) {
        message = "CORRECT";
    } else {
        message = "INCORRECT";
    }
    
    // the Routine "HeadphonePlay" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var HeadphoneFeedbackComponents;
function HeadphoneFeedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'HeadphoneFeedback'-------
    t = 0;
    HeadphoneFeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    FeedbackMssg.setText(message);
    // keep track of which components have finished
    HeadphoneFeedbackComponents = [];
    HeadphoneFeedbackComponents.push(FeedbackMssg);
    
    for (const thisComponent of HeadphoneFeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function HeadphoneFeedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'HeadphoneFeedback'-------
    // get current time
    t = HeadphoneFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *FeedbackMssg* updates
    if (t >= 0.0 && FeedbackMssg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FeedbackMssg.tStart = t;  // (not accounting for frame time here)
      FeedbackMssg.frameNStart = frameN;  // exact frame index
      
      FeedbackMssg.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((FeedbackMssg.status === PsychoJS.Status.STARTED || FeedbackMssg.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      FeedbackMssg.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of HeadphoneFeedbackComponents)
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


function HeadphoneFeedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'HeadphoneFeedback'-------
    for (const thisComponent of HeadphoneFeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _ContinueButton_allKeys;
var SLWelcomeComponents;
function SLWelcomeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SLWelcome'-------
    t = 0;
    SLWelcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    ContinueButton.keys = undefined;
    ContinueButton.rt = undefined;
    _ContinueButton_allKeys = [];
    // keep track of which components have finished
    SLWelcomeComponents = [];
    SLWelcomeComponents.push(WelcomeMssg);
    SLWelcomeComponents.push(ContinueButton);
    
    for (const thisComponent of SLWelcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SLWelcomeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SLWelcome'-------
    // get current time
    t = SLWelcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *WelcomeMssg* updates
    if (t >= 0.0 && WelcomeMssg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WelcomeMssg.tStart = t;  // (not accounting for frame time here)
      WelcomeMssg.frameNStart = frameN;  // exact frame index
      
      WelcomeMssg.setAutoDraw(true);
    }

    
    // *ContinueButton* updates
    if (t >= 0.0 && ContinueButton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ContinueButton.tStart = t;  // (not accounting for frame time here)
      ContinueButton.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { ContinueButton.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { ContinueButton.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { ContinueButton.clearEvents(); });
    }

    if (ContinueButton.status === PsychoJS.Status.STARTED) {
      let theseKeys = ContinueButton.getKeys({keyList: ['space'], waitRelease: false});
      _ContinueButton_allKeys = _ContinueButton_allKeys.concat(theseKeys);
      if (_ContinueButton_allKeys.length > 0) {
        ContinueButton.keys = _ContinueButton_allKeys[_ContinueButton_allKeys.length - 1].name;  // just the last key pressed
        ContinueButton.rt = _ContinueButton_allKeys[_ContinueButton_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SLWelcomeComponents)
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


function SLWelcomeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SLWelcome'-------
    for (const thisComponent of SLWelcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ContinueButton.keys', ContinueButton.keys);
    if (typeof ContinueButton.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('ContinueButton.rt', ContinueButton.rt);
        routineTimer.reset();
        }
    
    ContinueButton.stop();
    // the Routine "SLWelcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _ExposureIntroKey_allKeys;
var ExposurePrepComponents;
function ExposurePrepRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ExposurePrep'-------
    t = 0;
    ExposurePrepClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    ExposureIntroKey.keys = undefined;
    ExposureIntroKey.rt = undefined;
    _ExposureIntroKey_allKeys = [];
    // keep track of which components have finished
    ExposurePrepComponents = [];
    ExposurePrepComponents.push(ExposureIntro);
    ExposurePrepComponents.push(ExposureIntroKey);
    
    for (const thisComponent of ExposurePrepComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ExposurePrepRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ExposurePrep'-------
    // get current time
    t = ExposurePrepClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ExposureIntro* updates
    if (t >= 0.0 && ExposureIntro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExposureIntro.tStart = t;  // (not accounting for frame time here)
      ExposureIntro.frameNStart = frameN;  // exact frame index
      
      ExposureIntro.setAutoDraw(true);
    }

    
    // *ExposureIntroKey* updates
    if (t >= 0.0 && ExposureIntroKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExposureIntroKey.tStart = t;  // (not accounting for frame time here)
      ExposureIntroKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { ExposureIntroKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { ExposureIntroKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { ExposureIntroKey.clearEvents(); });
    }

    if (ExposureIntroKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = ExposureIntroKey.getKeys({keyList: ['space'], waitRelease: false});
      _ExposureIntroKey_allKeys = _ExposureIntroKey_allKeys.concat(theseKeys);
      if (_ExposureIntroKey_allKeys.length > 0) {
        ExposureIntroKey.keys = _ExposureIntroKey_allKeys[_ExposureIntroKey_allKeys.length - 1].name;  // just the last key pressed
        ExposureIntroKey.rt = _ExposureIntroKey_allKeys[_ExposureIntroKey_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ExposurePrepComponents)
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


function ExposurePrepRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ExposurePrep'-------
    for (const thisComponent of ExposurePrepComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ExposureIntroKey.keys', ExposureIntroKey.keys);
    if (typeof ExposureIntroKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('ExposureIntroKey.rt', ExposureIntroKey.rt);
        routineTimer.reset();
        }
    
    ExposureIntroKey.stop();
    // the Routine "ExposurePrep" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var ExposureComponents;
function ExposureRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Exposure'-------
    t = 0;
    ExposureClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    scounter += 1;
    if (((scounter === 123) || (scounter === 267))) {
        pausecheck = 1;
    } else {
        pausecheck = 0;
    }
    if ((scounter === 360)) {
        takebreak = 1;
        scounter = 0;
        volumecounter0 = 0;
    } else {
        takebreak = 0;
    }
    
    volumecounter0 += 1;
    if (((volumecounter0 === 1) || (volumecounter0 === 360))) {
        volume0 = 0.03;
    } else {
        if (((volumecounter0 === 2) || (volumecounter0 === 359))) {
            volume0 = 0.06;
        } else {
            if (((volumecounter0 === 3) || (volumecounter0 === 358))) {
                volume0 = 0.09;
            } else {
                if (((volumecounter0 === 4) || (volumecounter0 === 357))) {
                    volume0 = 0.2;
                } else {
                    if (((volumecounter0 === 5) || (volumecounter0 === 356))) {
                        volume0 = 0.3;
                    } else {
                        if (((volumecounter0 === 6) || (volumecounter0 === 355))) {
                            volume0 = 0.5;
                        } else {
                            volume0 = 1;
                        }
                    }
                }
            }
        }
    }
    
    ExposurePlay = new sound.Sound({
    win: psychoJS.window,
    value: SyllableFile,
    secs: -1,
    });
    ExposurePlay.setVolume(volume0);
    // keep track of which components have finished
    ExposureComponents = [];
    ExposureComponents.push(ExposurePlay);
    ExposureComponents.push(ExposureCross);
    ExposureComponents.push(ExposureInstruction);
    
    for (const thisComponent of ExposureComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ExposureRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Exposure'-------
    // get current time
    t = ExposureClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop ExposurePlay
    if (t >= 0.0 && ExposurePlay.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExposurePlay.tStart = t;  // (not accounting for frame time here)
      ExposurePlay.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ ExposurePlay.play(); });  // screen flip
      ExposurePlay.status = PsychoJS.Status.STARTED;
    }
    if (t >= (ExposurePlay.getDuration() + ExposurePlay.tStart)     && ExposurePlay.status === PsychoJS.Status.STARTED) {
      ExposurePlay.stop();  // stop the sound (if longer than duration)
      ExposurePlay.status = PsychoJS.Status.FINISHED;
    }
    
    // *ExposureCross* updates
    if (t >= 0.0 && ExposureCross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExposureCross.tStart = t;  // (not accounting for frame time here)
      ExposureCross.frameNStart = frameN;  // exact frame index
      
      ExposureCross.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.38 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ExposureCross.status === PsychoJS.Status.STARTED || ExposureCross.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ExposureCross.setAutoDraw(false);
    }
    
    // *ExposureInstruction* updates
    if (t >= 0.0 && ExposureInstruction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExposureInstruction.tStart = t;  // (not accounting for frame time here)
      ExposureInstruction.frameNStart = frameN;  // exact frame index
      
      ExposureInstruction.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.38 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ExposureInstruction.status === PsychoJS.Status.STARTED || ExposureInstruction.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ExposureInstruction.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ExposureComponents)
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


function ExposureRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Exposure'-------
    for (const thisComponent of ExposureComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    ExposurePlay.stop();  // ensure sound has stopped at end of routine
    // the Routine "Exposure" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _PauseCheckKey_allKeys;
var PauseComponents;
function PauseRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Pause'-------
    t = 0;
    PauseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(15.000000);
    // update component parameters for each repeat
    PauseCheckKey.keys = undefined;
    PauseCheckKey.rt = undefined;
    _PauseCheckKey_allKeys = [];
    // keep track of which components have finished
    PauseComponents = [];
    PauseComponents.push(PauseCheckKey);
    PauseComponents.push(PauseCross);
    PauseComponents.push(PauseInstruction);
    
    for (const thisComponent of PauseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function PauseRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Pause'-------
    // get current time
    t = PauseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *PauseCheckKey* updates
    if (t >= 0.0 && PauseCheckKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PauseCheckKey.tStart = t;  // (not accounting for frame time here)
      PauseCheckKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { PauseCheckKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { PauseCheckKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { PauseCheckKey.clearEvents(); });
    }

    frameRemains = 0.0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((PauseCheckKey.status === PsychoJS.Status.STARTED || PauseCheckKey.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      PauseCheckKey.status = PsychoJS.Status.FINISHED;
  }

    if (PauseCheckKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = PauseCheckKey.getKeys({keyList: ['space'], waitRelease: false});
      _PauseCheckKey_allKeys = _PauseCheckKey_allKeys.concat(theseKeys);
      if (_PauseCheckKey_allKeys.length > 0) {
        PauseCheckKey.keys = _PauseCheckKey_allKeys[_PauseCheckKey_allKeys.length - 1].name;  // just the last key pressed
        PauseCheckKey.rt = _PauseCheckKey_allKeys[_PauseCheckKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *PauseCross* updates
    if (t >= 0.0 && PauseCross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PauseCross.tStart = t;  // (not accounting for frame time here)
      PauseCross.frameNStart = frameN;  // exact frame index
      
      PauseCross.setAutoDraw(true);
    }

    frameRemains = 0.0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((PauseCross.status === PsychoJS.Status.STARTED || PauseCross.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      PauseCross.setAutoDraw(false);
    }
    
    // *PauseInstruction* updates
    if (t >= 0.0 && PauseInstruction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PauseInstruction.tStart = t;  // (not accounting for frame time here)
      PauseInstruction.frameNStart = frameN;  // exact frame index
      
      PauseInstruction.setAutoDraw(true);
    }

    frameRemains = 0.0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((PauseInstruction.status === PsychoJS.Status.STARTED || PauseInstruction.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      PauseInstruction.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PauseComponents)
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


function PauseRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Pause'-------
    for (const thisComponent of PauseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('PauseCheckKey.keys', PauseCheckKey.keys);
    if (typeof PauseCheckKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('PauseCheckKey.rt', PauseCheckKey.rt);
        routineTimer.reset();
        }
    
    PauseCheckKey.stop();
    return Scheduler.Event.NEXT;
  };
}


var _BreakRespSubmit_allKeys;
var TakeABreakComponents;
function TakeABreakRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'TakeABreak'-------
    t = 0;
    TakeABreakClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    BreakRespSubmit.keys = undefined;
    BreakRespSubmit.rt = undefined;
    _BreakRespSubmit_allKeys = [];
    BreakResponse.setText(' \n');
    // keep track of which components have finished
    TakeABreakComponents = [];
    TakeABreakComponents.push(BreakRespSubmit);
    TakeABreakComponents.push(BreakTxt);
    TakeABreakComponents.push(BreakResponse);
    
    for (const thisComponent of TakeABreakComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TakeABreakRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'TakeABreak'-------
    // get current time
    t = TakeABreakClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *BreakRespSubmit* updates
    if (t >= 0.0 && BreakRespSubmit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BreakRespSubmit.tStart = t;  // (not accounting for frame time here)
      BreakRespSubmit.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { BreakRespSubmit.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { BreakRespSubmit.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { BreakRespSubmit.clearEvents(); });
    }

    if (BreakRespSubmit.status === PsychoJS.Status.STARTED) {
      let theseKeys = BreakRespSubmit.getKeys({keyList: ['return'], waitRelease: false});
      _BreakRespSubmit_allKeys = _BreakRespSubmit_allKeys.concat(theseKeys);
      if (_BreakRespSubmit_allKeys.length > 0) {
        BreakRespSubmit.keys = _BreakRespSubmit_allKeys[_BreakRespSubmit_allKeys.length - 1].name;  // just the last key pressed
        BreakRespSubmit.rt = _BreakRespSubmit_allKeys[_BreakRespSubmit_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *BreakTxt* updates
    if (t >= 0.0 && BreakTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BreakTxt.tStart = t;  // (not accounting for frame time here)
      BreakTxt.frameNStart = frameN;  // exact frame index
      
      BreakTxt.setAutoDraw(true);
    }

    
    // *BreakResponse* updates
    if (t >= 0.0 && BreakResponse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BreakResponse.tStart = t;  // (not accounting for frame time here)
      BreakResponse.frameNStart = frameN;  // exact frame index
      
      BreakResponse.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TakeABreakComponents)
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


function TakeABreakRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'TakeABreak'-------
    for (const thisComponent of TakeABreakComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('BreakRespSubmit.keys', BreakRespSubmit.keys);
    if (typeof BreakRespSubmit.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('BreakRespSubmit.rt', BreakRespSubmit.rt);
        routineTimer.reset();
        }
    
    BreakRespSubmit.stop();
    psychoJS.experiment.addData('BreakResponse.text', BreakResponse.text);
    // the Routine "TakeABreak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _ExperimenterKey_allKeys;
var CallExperimenterComponents;
function CallExperimenterRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'CallExperimenter'-------
    t = 0;
    CallExperimenterClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    ExperimenterKey.keys = undefined;
    ExperimenterKey.rt = undefined;
    _ExperimenterKey_allKeys = [];
    // keep track of which components have finished
    CallExperimenterComponents = [];
    CallExperimenterComponents.push(CallExperimentertxt);
    CallExperimenterComponents.push(ExperimenterKey);
    
    for (const thisComponent of CallExperimenterComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function CallExperimenterRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'CallExperimenter'-------
    // get current time
    t = CallExperimenterClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *CallExperimentertxt* updates
    if (t >= 0.0 && CallExperimentertxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CallExperimentertxt.tStart = t;  // (not accounting for frame time here)
      CallExperimentertxt.frameNStart = frameN;  // exact frame index
      
      CallExperimentertxt.setAutoDraw(true);
    }

    
    // *ExperimenterKey* updates
    if (t >= 0.0 && ExperimenterKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExperimenterKey.tStart = t;  // (not accounting for frame time here)
      ExperimenterKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { ExperimenterKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { ExperimenterKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { ExperimenterKey.clearEvents(); });
    }

    if (ExperimenterKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = ExperimenterKey.getKeys({keyList: ['0'], waitRelease: false});
      _ExperimenterKey_allKeys = _ExperimenterKey_allKeys.concat(theseKeys);
      if (_ExperimenterKey_allKeys.length > 0) {
        ExperimenterKey.keys = _ExperimenterKey_allKeys[_ExperimenterKey_allKeys.length - 1].name;  // just the last key pressed
        ExperimenterKey.rt = _ExperimenterKey_allKeys[_ExperimenterKey_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of CallExperimenterComponents)
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


function CallExperimenterRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'CallExperimenter'-------
    for (const thisComponent of CallExperimenterComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "CallExperimenter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _ContinueKey3_allKeys;
var Part1IntroComponents;
function Part1IntroRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Part1Intro'-------
    t = 0;
    Part1IntroClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    ContinueKey3.keys = undefined;
    ContinueKey3.rt = undefined;
    _ContinueKey3_allKeys = [];
    // keep track of which components have finished
    Part1IntroComponents = [];
    Part1IntroComponents.push(WelcomeTxt2);
    Part1IntroComponents.push(ContinueKey3);
    
    for (const thisComponent of Part1IntroComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Part1IntroRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Part1Intro'-------
    // get current time
    t = Part1IntroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *WelcomeTxt2* updates
    if (t >= 0.0 && WelcomeTxt2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WelcomeTxt2.tStart = t;  // (not accounting for frame time here)
      WelcomeTxt2.frameNStart = frameN;  // exact frame index
      
      WelcomeTxt2.setAutoDraw(true);
    }

    
    // *ContinueKey3* updates
    if (t >= 0.0 && ContinueKey3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ContinueKey3.tStart = t;  // (not accounting for frame time here)
      ContinueKey3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { ContinueKey3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { ContinueKey3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { ContinueKey3.clearEvents(); });
    }

    if (ContinueKey3.status === PsychoJS.Status.STARTED) {
      let theseKeys = ContinueKey3.getKeys({keyList: ['space'], waitRelease: false});
      _ContinueKey3_allKeys = _ContinueKey3_allKeys.concat(theseKeys);
      if (_ContinueKey3_allKeys.length > 0) {
        ContinueKey3.keys = _ContinueKey3_allKeys[_ContinueKey3_allKeys.length - 1].name;  // just the last key pressed
        ContinueKey3.rt = _ContinueKey3_allKeys[_ContinueKey3_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Part1IntroComponents)
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


function Part1IntroRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Part1Intro'-------
    for (const thisComponent of Part1IntroComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ContinueKey3.keys', ContinueKey3.keys);
    if (typeof ContinueKey3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('ContinueKey3.rt', ContinueKey3.rt);
        routineTimer.reset();
        }
    
    ContinueKey3.stop();
    // the Routine "Part1Intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _TrainingContinueKey_allKeys;
var TDTrainingIntroComponents;
function TDTrainingIntroRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'TDTrainingIntro'-------
    t = 0;
    TDTrainingIntroClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    TrainingContinueKey.keys = undefined;
    TrainingContinueKey.rt = undefined;
    _TrainingContinueKey_allKeys = [];
    // keep track of which components have finished
    TDTrainingIntroComponents = [];
    TDTrainingIntroComponents.push(TrainingBeginTxt);
    TDTrainingIntroComponents.push(TrainingContinueKey);
    
    for (const thisComponent of TDTrainingIntroComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TDTrainingIntroRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'TDTrainingIntro'-------
    // get current time
    t = TDTrainingIntroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *TrainingBeginTxt* updates
    if (t >= 0.0 && TrainingBeginTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrainingBeginTxt.tStart = t;  // (not accounting for frame time here)
      TrainingBeginTxt.frameNStart = frameN;  // exact frame index
      
      TrainingBeginTxt.setAutoDraw(true);
    }

    
    // *TrainingContinueKey* updates
    if (t >= 0.0 && TrainingContinueKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrainingContinueKey.tStart = t;  // (not accounting for frame time here)
      TrainingContinueKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { TrainingContinueKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { TrainingContinueKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { TrainingContinueKey.clearEvents(); });
    }

    if (TrainingContinueKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = TrainingContinueKey.getKeys({keyList: ['space'], waitRelease: false});
      _TrainingContinueKey_allKeys = _TrainingContinueKey_allKeys.concat(theseKeys);
      if (_TrainingContinueKey_allKeys.length > 0) {
        TrainingContinueKey.keys = _TrainingContinueKey_allKeys[_TrainingContinueKey_allKeys.length - 1].name;  // just the last key pressed
        TrainingContinueKey.rt = _TrainingContinueKey_allKeys[_TrainingContinueKey_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TDTrainingIntroComponents)
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


function TDTrainingIntroRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'TDTrainingIntro'-------
    for (const thisComponent of TDTrainingIntroComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('TrainingContinueKey.keys', TrainingContinueKey.keys);
    if (typeof TrainingContinueKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('TrainingContinueKey.rt', TrainingContinueKey.rt);
        routineTimer.reset();
        }
    
    TrainingContinueKey.stop();
    // the Routine "TDTrainingIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _TSContinueKey_allKeys;
var TrainingSampleComponents;
function TrainingSampleRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'TrainingSample'-------
    t = 0;
    TrainingSampleClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    TrainigTarget.setText(Target);
    trainingcount += 1;
    
    TrainingNumber.setText(("Training " + trainingcount.toString()));
    TSContinueKey.keys = undefined;
    TSContinueKey.rt = undefined;
    _TSContinueKey_allKeys = [];
    // keep track of which components have finished
    TrainingSampleComponents = [];
    TrainingSampleComponents.push(SampleMssg2);
    TrainingSampleComponents.push(TrainigTarget);
    TrainingSampleComponents.push(TrainingNumber);
    TrainingSampleComponents.push(TrainingSampleContinue);
    TrainingSampleComponents.push(TSContinueKey);
    
    for (const thisComponent of TrainingSampleComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TrainingSampleRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'TrainingSample'-------
    // get current time
    t = TrainingSampleClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *SampleMssg2* updates
    if (t >= 0.0 && SampleMssg2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SampleMssg2.tStart = t;  // (not accounting for frame time here)
      SampleMssg2.frameNStart = frameN;  // exact frame index
      
      SampleMssg2.setAutoDraw(true);
    }

    
    // *TrainigTarget* updates
    if (t >= 0.0 && TrainigTarget.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrainigTarget.tStart = t;  // (not accounting for frame time here)
      TrainigTarget.frameNStart = frameN;  // exact frame index
      
      TrainigTarget.setAutoDraw(true);
    }

    
    // *TrainingNumber* updates
    if (t >= 0.0 && TrainingNumber.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrainingNumber.tStart = t;  // (not accounting for frame time here)
      TrainingNumber.frameNStart = frameN;  // exact frame index
      
      TrainingNumber.setAutoDraw(true);
    }

    
    // *TrainingSampleContinue* updates
    if (t >= 0.0 && TrainingSampleContinue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrainingSampleContinue.tStart = t;  // (not accounting for frame time here)
      TrainingSampleContinue.frameNStart = frameN;  // exact frame index
      
      TrainingSampleContinue.setAutoDraw(true);
    }

    
    // *TSContinueKey* updates
    if (t >= 0.0 && TSContinueKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TSContinueKey.tStart = t;  // (not accounting for frame time here)
      TSContinueKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { TSContinueKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { TSContinueKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { TSContinueKey.clearEvents(); });
    }

    if (TSContinueKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = TSContinueKey.getKeys({keyList: ['space'], waitRelease: false});
      _TSContinueKey_allKeys = _TSContinueKey_allKeys.concat(theseKeys);
      if (_TSContinueKey_allKeys.length > 0) {
        TSContinueKey.keys = _TSContinueKey_allKeys[_TSContinueKey_allKeys.length - 1].name;  // just the last key pressed
        TSContinueKey.rt = _TSContinueKey_allKeys[_TSContinueKey_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TrainingSampleComponents)
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


function TrainingSampleRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'TrainingSample'-------
    for (const thisComponent of TrainingSampleComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('TSContinueKey.keys', TSContinueKey.keys);
    if (typeof TSContinueKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('TSContinueKey.rt', TSContinueKey.rt);
        routineTimer.reset();
        }
    
    TSContinueKey.stop();
    // the Routine "TrainingSample" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _TrainEndSample_allKeys;
var TrainingPlaySampleComponents;
function TrainingPlaySampleRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'TrainingPlaySample'-------
    t = 0;
    TrainingPlaySampleClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    TrainingSampleSound = new sound.Sound({
    win: psychoJS.window,
    value: TargetFile,
    secs: -1,
    });
    TrainingSampleSound.setVolume(0.3);
    TraingRepeatSound = new sound.Sound({
    win: psychoJS.window,
    value: TargetFile,
    secs: -1,
    });
    TraingRepeatSound.setVolume(0.3);
    TrainTargetTxt.setText(Target);
    TrainingNumber2.setText(("Training " + trainingcount.toString()));
    TrainEndSample.keys = undefined;
    TrainEndSample.rt = undefined;
    _TrainEndSample_allKeys = [];
    // keep track of which components have finished
    TrainingPlaySampleComponents = [];
    TrainingPlaySampleComponents.push(TrainingSampleSound);
    TrainingPlaySampleComponents.push(TraingRepeatSound);
    TrainingPlaySampleComponents.push(TrainTargetTxt);
    TrainingPlaySampleComponents.push(text_5);
    TrainingPlaySampleComponents.push(TrainingBeginSample);
    TrainingPlaySampleComponents.push(TrainingNumber2);
    TrainingPlaySampleComponents.push(TrainEndSample);
    
    for (const thisComponent of TrainingPlaySampleComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TrainingPlaySampleRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'TrainingPlaySample'-------
    // get current time
    t = TrainingPlaySampleClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop TrainingSampleSound
    if (t >= 0.0 && TrainingSampleSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrainingSampleSound.tStart = t;  // (not accounting for frame time here)
      TrainingSampleSound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ TrainingSampleSound.play(); });  // screen flip
      TrainingSampleSound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (TrainingSampleSound.getDuration() + TrainingSampleSound.tStart)     && TrainingSampleSound.status === PsychoJS.Status.STARTED) {
      TrainingSampleSound.stop();  // stop the sound (if longer than duration)
      TrainingSampleSound.status = PsychoJS.Status.FINISHED;
    }
    // start/stop TraingRepeatSound
    if (t >= (TrainingSampleSound.getDuration() + 1) && TraingRepeatSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TraingRepeatSound.tStart = t;  // (not accounting for frame time here)
      TraingRepeatSound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ TraingRepeatSound.play(); });  // screen flip
      TraingRepeatSound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (TraingRepeatSound.getDuration() + TraingRepeatSound.tStart)     && TraingRepeatSound.status === PsychoJS.Status.STARTED) {
      TraingRepeatSound.stop();  // stop the sound (if longer than duration)
      TraingRepeatSound.status = PsychoJS.Status.FINISHED;
    }
    
    // *TrainTargetTxt* updates
    if (t >= 0.0 && TrainTargetTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrainTargetTxt.tStart = t;  // (not accounting for frame time here)
      TrainTargetTxt.frameNStart = frameN;  // exact frame index
      
      TrainTargetTxt.setAutoDraw(true);
    }

    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    
    // *TrainingBeginSample* updates
    if (t >= (TrainingSampleSound.getDuration() + 1) && TrainingBeginSample.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrainingBeginSample.tStart = t;  // (not accounting for frame time here)
      TrainingBeginSample.frameNStart = frameN;  // exact frame index
      
      TrainingBeginSample.setAutoDraw(true);
    }

    
    // *TrainingNumber2* updates
    if (t >= 0.0 && TrainingNumber2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrainingNumber2.tStart = t;  // (not accounting for frame time here)
      TrainingNumber2.frameNStart = frameN;  // exact frame index
      
      TrainingNumber2.setAutoDraw(true);
    }

    
    // *TrainEndSample* updates
    if (t >= 0.0 && TrainEndSample.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrainEndSample.tStart = t;  // (not accounting for frame time here)
      TrainEndSample.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { TrainEndSample.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { TrainEndSample.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { TrainEndSample.clearEvents(); });
    }

    if (TrainEndSample.status === PsychoJS.Status.STARTED) {
      let theseKeys = TrainEndSample.getKeys({keyList: ['space'], waitRelease: false});
      _TrainEndSample_allKeys = _TrainEndSample_allKeys.concat(theseKeys);
      if (_TrainEndSample_allKeys.length > 0) {
        TrainEndSample.keys = _TrainEndSample_allKeys[_TrainEndSample_allKeys.length - 1].name;  // just the last key pressed
        TrainEndSample.rt = _TrainEndSample_allKeys[_TrainEndSample_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TrainingPlaySampleComponents)
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


function TrainingPlaySampleRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'TrainingPlaySample'-------
    for (const thisComponent of TrainingPlaySampleComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    TrainingSampleSound.stop();  // ensure sound has stopped at end of routine
    TraingRepeatSound.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('TrainEndSample.keys', TrainEndSample.keys);
    if (typeof TrainEndSample.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('TrainEndSample.rt', TrainEndSample.rt);
        routineTimer.reset();
        }
    
    TrainEndSample.stop();
    // the Routine "TrainingPlaySample" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var TrainStartComponents;
function TrainStartRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'TrainStart'-------
    t = 0;
    TrainStartClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    TrainStartComponents = [];
    TrainStartComponents.push(Three);
    TrainStartComponents.push(Two);
    TrainStartComponents.push(text);
    
    for (const thisComponent of TrainStartComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TrainStartRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'TrainStart'-------
    // get current time
    t = TrainStartClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Three* updates
    if (t >= 0.0 && Three.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Three.tStart = t;  // (not accounting for frame time here)
      Three.frameNStart = frameN;  // exact frame index
      
      Three.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Three.status === PsychoJS.Status.STARTED || Three.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      Three.setAutoDraw(false);
    }
    
    // *Two* updates
    if (t >= 1 && Two.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Two.tStart = t;  // (not accounting for frame time here)
      Two.frameNStart = frameN;  // exact frame index
      
      Two.setAutoDraw(true);
    }

    frameRemains = 1 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Two.status === PsychoJS.Status.STARTED || Two.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      Two.setAutoDraw(false);
    }
    
    // *text* updates
    if (t >= 2 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 2 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((text.status === PsychoJS.Status.STARTED || text.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TrainStartComponents)
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


function TrainStartRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'TrainStart'-------
    for (const thisComponent of TrainStartComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var soundOnset;
var _TrainResp_allKeys;
var trainComponents;
function trainRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'train'-------
    t = 0;
    trainClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    if ((Sound === Target)) {
        TargetOnset = mytimer.getTime();
    }
    soundOnset = mytimer.getTime();
    
    TDTrainSound = new sound.Sound({
    win: psychoJS.window,
    value: File,
    secs: -1,
    });
    TDTrainSound.setVolume(0.3);
    TrainResp.keys = undefined;
    TrainResp.rt = undefined;
    _TrainResp_allKeys = [];
    Cross3.setText(Target);
    // keep track of which components have finished
    trainComponents = [];
    trainComponents.push(TDTrainSound);
    trainComponents.push(TrainResp);
    trainComponents.push(TDTrainTxt);
    trainComponents.push(Cross3);
    
    for (const thisComponent of trainComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trainRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'train'-------
    // get current time
    t = trainClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop TDTrainSound
    if (t >= 0.0 && TDTrainSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TDTrainSound.tStart = t;  // (not accounting for frame time here)
      TDTrainSound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ TDTrainSound.play(); });  // screen flip
      TDTrainSound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (TDTrainSound.getDuration() + TDTrainSound.tStart)     && TDTrainSound.status === PsychoJS.Status.STARTED) {
      TDTrainSound.stop();  // stop the sound (if longer than duration)
      TDTrainSound.status = PsychoJS.Status.FINISHED;
    }
    
    // *TrainResp* updates
    if (t >= 0.0 && TrainResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrainResp.tStart = t;  // (not accounting for frame time here)
      TrainResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { TrainResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { TrainResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { TrainResp.clearEvents(); });
    }

    frameRemains = 0.0 + (TDTrainSound.getDuration() + 0.03) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((TrainResp.status === PsychoJS.Status.STARTED || TrainResp.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      TrainResp.status = PsychoJS.Status.FINISHED;
  }

    if (TrainResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = TrainResp.getKeys({keyList: ['space'], waitRelease: false});
      _TrainResp_allKeys = _TrainResp_allKeys.concat(theseKeys);
      if (_TrainResp_allKeys.length > 0) {
        TrainResp.keys = _TrainResp_allKeys.map((key) => key.name);  // storing all keys
        TrainResp.rt = _TrainResp_allKeys.map((key) => key.rt);
      }
    }
    
    
    // *TDTrainTxt* updates
    if (t >= 0.0 && TDTrainTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TDTrainTxt.tStart = t;  // (not accounting for frame time here)
      TDTrainTxt.frameNStart = frameN;  // exact frame index
      
      TDTrainTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + (TDTrainSound.getDuration() + 0.05) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((TDTrainTxt.status === PsychoJS.Status.STARTED || TDTrainTxt.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      TDTrainTxt.setAutoDraw(false);
    }
    
    // *Cross3* updates
    if (t >= 0.0 && Cross3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Cross3.tStart = t;  // (not accounting for frame time here)
      Cross3.frameNStart = frameN;  // exact frame index
      
      Cross3.setAutoDraw(true);
    }

    frameRemains = 0.0 + (TDTrainSound.getDuration() + 0.05) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Cross3.status === PsychoJS.Status.STARTED || Cross3.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      Cross3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trainComponents)
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


var reactiontime;
var meanRT;
function trainRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'train'-------
    for (const thisComponent of trainComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    TrainTD.addData("TargetOnset", TargetOnset);
    
    if (typeof TrainResp.keys !== 'undefined') {  // we had a response
        respOnset = (TrainResp.rt[0] + soundOnset);
        TrainTD.addData("RespOnset", respOnset);
        if (((respOnset - previousOnset) > 1.2)) {
            reactiontime = (respOnset - TargetOnset);
            TrainTD.addData("ReactionTime", reactiontime);
            if ((reactiontime < 1.2)) {
                respcount += 1;
                TrainRT += reactiontime;
                previousOnset = respOnset;
            }
        }
    }
    if ((respcount > 0)) {
        meanRT = (TrainRT / respcount);
        TrainTD.addData("mean.rt", meanRT);
    } else {
        meanRT = 0;
    }
    if ((respcount > 5)) {
        respcount = 5;
    }
    TrainTD.addData("RespOnset", respOnset);
    TrainTD.addData("Respcount", respcount);
    
    TDTrainSound.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('TrainResp.keys', TrainResp.keys);
    if (typeof TrainResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('TrainResp.rt', TrainResp.rt);
        }
    
    TrainResp.stop();
    // the Routine "train" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Pause1secComponents;
function Pause1secRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Pause1sec'-------
    t = 0;
    Pause1secClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    Pause1secComponents = [];
    Pause1secComponents.push(PauseTxt2);
    
    for (const thisComponent of Pause1secComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Pause1secRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Pause1sec'-------
    // get current time
    t = Pause1secClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *PauseTxt2* updates
    if (t >= 0.0 && PauseTxt2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PauseTxt2.tStart = t;  // (not accounting for frame time here)
      PauseTxt2.frameNStart = frameN;  // exact frame index
      
      PauseTxt2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((PauseTxt2.status === PsychoJS.Status.STARTED || PauseTxt2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      PauseTxt2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Pause1secComponents)
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


function Pause1secRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Pause1sec'-------
    for (const thisComponent of Pause1secComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _EndFeedback_allKeys;
var TDTrainFeedbackComponents;
function TDTrainFeedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'TDTrainFeedback'-------
    t = 0;
    TDTrainFeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    TDTrainFeedbackMssg.setText((((("You correctly responded to " + respcount.toString()) + " of the 5 target syllables. Your average response time was ") + util.round(meanRT, 2).toString()) + "s."));
    EndFeedback.keys = undefined;
    EndFeedback.rt = undefined;
    _EndFeedback_allKeys = [];
    // keep track of which components have finished
    TDTrainFeedbackComponents = [];
    TDTrainFeedbackComponents.push(TDTrainFeedbackMssg);
    TDTrainFeedbackComponents.push(EndFeedback);
    TDTrainFeedbackComponents.push(TrainingContinue);
    
    for (const thisComponent of TDTrainFeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TDTrainFeedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'TDTrainFeedback'-------
    // get current time
    t = TDTrainFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *TDTrainFeedbackMssg* updates
    if (t >= 0.0 && TDTrainFeedbackMssg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TDTrainFeedbackMssg.tStart = t;  // (not accounting for frame time here)
      TDTrainFeedbackMssg.frameNStart = frameN;  // exact frame index
      
      TDTrainFeedbackMssg.setAutoDraw(true);
    }

    
    // *EndFeedback* updates
    if (t >= 0.0 && EndFeedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EndFeedback.tStart = t;  // (not accounting for frame time here)
      EndFeedback.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { EndFeedback.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { EndFeedback.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { EndFeedback.clearEvents(); });
    }

    if (EndFeedback.status === PsychoJS.Status.STARTED) {
      let theseKeys = EndFeedback.getKeys({keyList: ['space'], waitRelease: false});
      _EndFeedback_allKeys = _EndFeedback_allKeys.concat(theseKeys);
      if (_EndFeedback_allKeys.length > 0) {
        EndFeedback.keys = _EndFeedback_allKeys[_EndFeedback_allKeys.length - 1].name;  // just the last key pressed
        EndFeedback.rt = _EndFeedback_allKeys[_EndFeedback_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *TrainingContinue* updates
    if (t >= 0.0 && TrainingContinue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrainingContinue.tStart = t;  // (not accounting for frame time here)
      TrainingContinue.frameNStart = frameN;  // exact frame index
      
      TrainingContinue.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TDTrainFeedbackComponents)
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


function TDTrainFeedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'TDTrainFeedback'-------
    for (const thisComponent of TDTrainFeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('EndFeedback.keys', EndFeedback.keys);
    if (typeof EndFeedback.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('EndFeedback.rt', EndFeedback.rt);
        routineTimer.reset();
        }
    
    EndFeedback.stop();
    respcount = 0;
    reactiontime = 0;
    TrainRT = 0;
    
    // the Routine "TDTrainFeedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var partlist;
var first;
var second;
var third;
var P1IntroIIComponents;
function P1IntroIIRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'P1IntroII'-------
    t = 0;
    P1IntroIIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // Equivalent js function to random shuffle
    function shuffle(array) {
      var currentIndex = array.length, temporaryValue, randomIndex;
    
      // While there remain elements to shuffle...
      while (0 !== currentIndex) {
    
        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;
    
        // And swap it with the current element.
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
      }
    
      return array;
    }
    
    if ((cond === "1")) {
        partone = "0:12";
        parttwo = "12:24";
        partthree = "24:36";
    } else {
        if ((cond === "X")) {
            partone = "36:48";
            parttwo = "48:60";
            partthree = "60:72";
        } else {
            if ((cond === "2")) {
                partone = "72:84";
                parttwo = "84:96";
                partthree = "96:108";
            } else {
                if ((cond === "4")) {
                    partone = "108:120";
                    parttwo = "120:132";
                    partthree = "132:144";
                } else {
                    if ((cond === "3")) {
                        partone = "144:156";
                        parttwo = "156:168";
                        partthree = "168:180";
                    } else {
                        if ((cond === "6")) {
                            partone = "180:192";
                            parttwo = "192:204";
                            partthree = "204:216";
                        }
                    }
                }
            }
        }
    }
    partlist = [partone, parttwo, partthree];
    // Random shuffle partlist using function 'shuffle'
    shuffle(partlist);
    console.log(partlist);
    
    first = partlist[0];
    second = partlist[1];
    third = partlist[2];
    
    // keep track of which components have finished
    P1IntroIIComponents = [];
    P1IntroIIComponents.push(P1Intro2Txt);
    P1IntroIIComponents.push(text_4);
    P1IntroIIComponents.push(key_resp);
    
    for (const thisComponent of P1IntroIIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function P1IntroIIRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'P1IntroII'-------
    // get current time
    t = P1IntroIIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *P1Intro2Txt* updates
    if (t >= 0.0 && P1Intro2Txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      P1Intro2Txt.tStart = t;  // (not accounting for frame time here)
      P1Intro2Txt.frameNStart = frameN;  // exact frame index
      
      P1Intro2Txt.setAutoDraw(true);
    }

    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of P1IntroIIComponents)
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


function P1IntroIIRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'P1IntroII'-------
    for (const thisComponent of P1IntroIIComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "P1IntroII" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _PlayTargetKey_allKeys;
var TrialNo;
var SampleIntroComponents;
function SampleIntroRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SampleIntro'-------
    t = 0;
    SampleIntroClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    PlayTargetKey.keys = undefined;
    PlayTargetKey.rt = undefined;
    _PlayTargetKey_allKeys = [];
    TargetTxt.setText(Target);
    repeatCount += 1;
    TrialNo = (("Recording " + repeatCount.toString()) + " of 36");
    
    TrialNoTxt.setText(TrialNo);
    // keep track of which components have finished
    SampleIntroComponents = [];
    SampleIntroComponents.push(TargetMssg);
    SampleIntroComponents.push(PlayTargetKey);
    SampleIntroComponents.push(TargetTxt);
    SampleIntroComponents.push(TrialNoTxt);
    SampleIntroComponents.push(ContinueTxt4);
    
    for (const thisComponent of SampleIntroComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SampleIntroRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SampleIntro'-------
    // get current time
    t = SampleIntroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *TargetMssg* updates
    if (t >= 0.0 && TargetMssg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TargetMssg.tStart = t;  // (not accounting for frame time here)
      TargetMssg.frameNStart = frameN;  // exact frame index
      
      TargetMssg.setAutoDraw(true);
    }

    
    // *PlayTargetKey* updates
    if (t >= 0.0 && PlayTargetKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PlayTargetKey.tStart = t;  // (not accounting for frame time here)
      PlayTargetKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { PlayTargetKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { PlayTargetKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { PlayTargetKey.clearEvents(); });
    }

    if (PlayTargetKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = PlayTargetKey.getKeys({keyList: ['space'], waitRelease: false});
      _PlayTargetKey_allKeys = _PlayTargetKey_allKeys.concat(theseKeys);
      if (_PlayTargetKey_allKeys.length > 0) {
        PlayTargetKey.keys = _PlayTargetKey_allKeys[_PlayTargetKey_allKeys.length - 1].name;  // just the last key pressed
        PlayTargetKey.rt = _PlayTargetKey_allKeys[_PlayTargetKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *TargetTxt* updates
    if (t >= 0.0 && TargetTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TargetTxt.tStart = t;  // (not accounting for frame time here)
      TargetTxt.frameNStart = frameN;  // exact frame index
      
      TargetTxt.setAutoDraw(true);
    }

    
    // *TrialNoTxt* updates
    if (t >= 0.0 && TrialNoTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrialNoTxt.tStart = t;  // (not accounting for frame time here)
      TrialNoTxt.frameNStart = frameN;  // exact frame index
      
      TrialNoTxt.setAutoDraw(true);
    }

    
    // *ContinueTxt4* updates
    if (t >= 0.0 && ContinueTxt4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ContinueTxt4.tStart = t;  // (not accounting for frame time here)
      ContinueTxt4.frameNStart = frameN;  // exact frame index
      
      ContinueTxt4.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SampleIntroComponents)
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


function SampleIntroRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SampleIntro'-------
    for (const thisComponent of SampleIntroComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('PlayTargetKey.keys', PlayTargetKey.keys);
    if (typeof PlayTargetKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('PlayTargetKey.rt', PlayTargetKey.rt);
        routineTimer.reset();
        }
    
    PlayTargetKey.stop();
    // the Routine "SampleIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _EndPlay_allKeys;
var PlaySampleComponents;
function PlaySampleRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'PlaySample'-------
    t = 0;
    PlaySampleClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    EndPlay.keys = undefined;
    EndPlay.rt = undefined;
    _EndPlay_allKeys = [];
    SyllableSound = new sound.Sound({
    win: psychoJS.window,
    value: TargetFile,
    secs: -1,
    });
    SyllableSound.setVolume(1);
    Repeat = new sound.Sound({
    win: psychoJS.window,
    value: TargetFile,
    secs: -1,
    });
    Repeat.setVolume(1);
    SoundTxt.setText(Target);
    TrialNoTxt2.setText(TrialNo);
    // keep track of which components have finished
    PlaySampleComponents = [];
    PlaySampleComponents.push(EndPlay);
    PlaySampleComponents.push(SyllableSound);
    PlaySampleComponents.push(Repeat);
    PlaySampleComponents.push(SoundTxt);
    PlaySampleComponents.push(ContinueKey2);
    PlaySampleComponents.push(text_2);
    PlaySampleComponents.push(TrialNoTxt2);
    
    for (const thisComponent of PlaySampleComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function PlaySampleRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'PlaySample'-------
    // get current time
    t = PlaySampleClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *EndPlay* updates
    if (t >= (SyllableSound.getDuration() + 1) && EndPlay.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EndPlay.tStart = t;  // (not accounting for frame time here)
      EndPlay.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { EndPlay.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { EndPlay.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { EndPlay.clearEvents(); });
    }

    if (EndPlay.status === PsychoJS.Status.STARTED) {
      let theseKeys = EndPlay.getKeys({keyList: ['space'], waitRelease: false});
      _EndPlay_allKeys = _EndPlay_allKeys.concat(theseKeys);
      if (_EndPlay_allKeys.length > 0) {
        EndPlay.keys = _EndPlay_allKeys[_EndPlay_allKeys.length - 1].name;  // just the last key pressed
        EndPlay.rt = _EndPlay_allKeys[_EndPlay_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // start/stop SyllableSound
    if (t >= 0.0 && SyllableSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SyllableSound.tStart = t;  // (not accounting for frame time here)
      SyllableSound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ SyllableSound.play(); });  // screen flip
      SyllableSound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (SyllableSound.getDuration() + SyllableSound.tStart)     && SyllableSound.status === PsychoJS.Status.STARTED) {
      SyllableSound.stop();  // stop the sound (if longer than duration)
      SyllableSound.status = PsychoJS.Status.FINISHED;
    }
    // start/stop Repeat
    if (t >= (SyllableSound.getDuration() + 1) && Repeat.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Repeat.tStart = t;  // (not accounting for frame time here)
      Repeat.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ Repeat.play(); });  // screen flip
      Repeat.status = PsychoJS.Status.STARTED;
    }
    if (t >= (Repeat.getDuration() + Repeat.tStart)     && Repeat.status === PsychoJS.Status.STARTED) {
      Repeat.stop();  // stop the sound (if longer than duration)
      Repeat.status = PsychoJS.Status.FINISHED;
    }
    
    // *SoundTxt* updates
    if (t >= 0.0 && SoundTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SoundTxt.tStart = t;  // (not accounting for frame time here)
      SoundTxt.frameNStart = frameN;  // exact frame index
      
      SoundTxt.setAutoDraw(true);
    }

    
    // *ContinueKey2* updates
    if (t >= (SyllableSound.getDuration() + 1) && ContinueKey2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ContinueKey2.tStart = t;  // (not accounting for frame time here)
      ContinueKey2.frameNStart = frameN;  // exact frame index
      
      ContinueKey2.setAutoDraw(true);
    }

    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *TrialNoTxt2* updates
    if (t >= 0.0 && TrialNoTxt2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrialNoTxt2.tStart = t;  // (not accounting for frame time here)
      TrialNoTxt2.frameNStart = frameN;  // exact frame index
      
      TrialNoTxt2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PlaySampleComponents)
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


function PlaySampleRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'PlaySample'-------
    for (const thisComponent of PlaySampleComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    SyllableSound.stop();  // ensure sound has stopped at end of routine
    Repeat.stop();  // ensure sound has stopped at end of routine
    // the Routine "PlaySample" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var opt1;
var opt2;
var opt3;
var opt4;
var opt5;
var opt6;
var opt7;
var opt8;
var opt9;
var opt10;
var opt11;
var opt12;
var condlist;
var rows;
var TDStartComponents;
function TDStartRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'TDStart'-------
    t = 0;
    TDStartClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    opt1 = "0:48";
    opt2 = "48:96";
    opt3 = "96:144";
    opt4 = "144:192";
    opt5 = "192:240";
    opt6 = "240:288";
    opt7 = "288:336";
    opt8 = "336:384";
    opt9 = "384:432";
    opt10 = "432:480";
    opt11 = "480:528";
    opt12 = "528:576";
    
    if ((((Target === "ru") || (Target === "pu")) || (Target === "ni"))) {
        condlist = [opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9]; 
        rows = condlist[(Math.random() * condlist.length) | 0];
    } else {
        if ((((Target === "re") || (Target === "ge")) || (Target === "me"))) {
            condlist = [opt1, opt2, opt3, opt4, opt5, opt6, opt10, opt11, opt12]; 
            rows = condlist[(Math.random() * condlist.length) | 0];
        } else {
            if ((((Target === "fe") || (Target === "ti")) || (Target === "su"))) {
                condlist = [opt1, opt2, opt3, opt10, opt11, opt12, opt7, opt8, opt9]; 
                rows = condlist[(Math.random() * condlist.length) | 0];
            } else {
                condlist = [opt10, opt11, opt12, opt4, opt5, opt6, opt7, opt8, opt9]; 
                rows = condlist[(Math.random() * condlist.length) | 0];
            }
        }
    }
    
    // keep track of which components have finished
    TDStartComponents = [];
    TDStartComponents.push(Countdown1);
    
    for (const thisComponent of TDStartComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TDStartRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'TDStart'-------
    // get current time
    t = TDStartClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Countdown1* updates
    if (t >= 0 && Countdown1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Countdown1.tStart = t;  // (not accounting for frame time here)
      Countdown1.frameNStart = frameN;  // exact frame index
      
      Countdown1.setAutoDraw(true);
    }

    frameRemains = 0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Countdown1.status === PsychoJS.Status.STARTED || Countdown1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      Countdown1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TDStartComponents)
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


function TDStartRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'TDStart'-------
    for (const thisComponent of TDStartComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var soundOnsetP;
var _PlayResp_allKeys;
var trial_separateComponents;
function trial_separateRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial_separate'-------
    t = 0;
    trial_separateClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    if ((TDSound === Target)) {
        TargetOnsetP = mytimerP.getTime();
    }
    soundOnsetP = mytimerP.getTime();
    
    PlaySound = new sound.Sound({
    win: psychoJS.window,
    value: TDSoundFile,
    secs: -1,
    });
    PlaySound.setVolume(1);
    PlayResp.keys = undefined;
    PlayResp.rt = undefined;
    _PlayResp_allKeys = [];
    TargetSoundTxt.setText(Target);
    // keep track of which components have finished
    trial_separateComponents = [];
    trial_separateComponents.push(PlaySound);
    trial_separateComponents.push(PlayText);
    trial_separateComponents.push(PlayResp);
    trial_separateComponents.push(TargetSoundTxt);
    
    for (const thisComponent of trial_separateComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trial_separateRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial_separate'-------
    // get current time
    t = trial_separateClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop PlaySound
    if (t >= 0 && PlaySound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PlaySound.tStart = t;  // (not accounting for frame time here)
      PlaySound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ PlaySound.play(); });  // screen flip
      PlaySound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (PlaySound.getDuration() + PlaySound.tStart)     && PlaySound.status === PsychoJS.Status.STARTED) {
      PlaySound.stop();  // stop the sound (if longer than duration)
      PlaySound.status = PsychoJS.Status.FINISHED;
    }
    
    // *PlayText* updates
    if (t >= 0 && PlayText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PlayText.tStart = t;  // (not accounting for frame time here)
      PlayText.frameNStart = frameN;  // exact frame index
      
      PlayText.setAutoDraw(true);
    }

    frameRemains = 0 + 0.38 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((PlayText.status === PsychoJS.Status.STARTED || PlayText.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      PlayText.setAutoDraw(false);
    }
    
    // *PlayResp* updates
    if (t >= 0.0 && PlayResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PlayResp.tStart = t;  // (not accounting for frame time here)
      PlayResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { PlayResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { PlayResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { PlayResp.clearEvents(); });
    }

    frameRemains = 0.0 + 0.38 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((PlayResp.status === PsychoJS.Status.STARTED || PlayResp.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      PlayResp.status = PsychoJS.Status.FINISHED;
  }

    if (PlayResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = PlayResp.getKeys({keyList: ['space'], waitRelease: false});
      _PlayResp_allKeys = _PlayResp_allKeys.concat(theseKeys);
      if (_PlayResp_allKeys.length > 0) {
        PlayResp.keys = _PlayResp_allKeys.map((key) => key.name);  // storing all keys
        PlayResp.rt = _PlayResp_allKeys.map((key) => key.rt);
      }
    }
    
    
    // *TargetSoundTxt* updates
    if (t >= 0.0 && TargetSoundTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TargetSoundTxt.tStart = t;  // (not accounting for frame time here)
      TargetSoundTxt.frameNStart = frameN;  // exact frame index
      
      TargetSoundTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.38 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((TargetSoundTxt.status === PsychoJS.Status.STARTED || TargetSoundTxt.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      TargetSoundTxt.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trial_separateComponents)
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


var reactiontimeP;
function trial_separateRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial_separate'-------
    for (const thisComponent of trial_separateComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    TD.addData("TargetOnsetP", TargetOnsetP);
    if (typeof PlayResp.keys !== 'undefined') {  // we had a response
        respcountP += 1;
        respOnsetP = (PlayResp.rt[0] + soundOnsetP);
        if (((respOnsetP - previousOnsetP) > 1.2)) {
            reactiontimeP = (respOnsetP - TargetOnsetP);
            if ((reactiontimeP < 1.2)) {
                TD.addData("ReactionTimeP", reactiontimeP);
                TD.addData("TargetSyllable", Target);
                TD.addData("TargetPosition", Position);
                TD.addData("TargetOccurence", OccurenceC);
                hit += 1;
                previousOnsetP = respOnsetP;
            }
        }
    }
    PlaySound.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('PlayResp.keys', PlayResp.keys);
    if (typeof PlayResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('PlayResp.rt', PlayResp.rt);
        }
    
    PlayResp.stop();
    // the Routine "trial_separate" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var AddRespCountCodeComponents;
function AddRespCountCodeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'AddRespCountCode'-------
    t = 0;
    AddRespCountCodeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    AddRespCountCodeComponents = [];
    
    for (const thisComponent of AddRespCountCodeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function AddRespCountCodeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'AddRespCountCode'-------
    // get current time
    t = AddRespCountCodeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of AddRespCountCodeComponents)
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


var falsealarm;
var hitrate;
function AddRespCountCodeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'AddRespCountCode'-------
    for (const thisComponent of AddRespCountCodeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    falsealarm = 0;
    hitrate = 0;
    if ((hit !== 0)) {
        falsealarm = (1 - (hit / respcountP));
        hitrate = (hit / 4);
    }
    TD.addData("RespCountP", respcountP);
    TD.addData("FalseAlarmRate", falsealarm);
    TD.addData("HitRate", hitrate);
    hit = 0;
    respcountP = 0;
    
    // the Routine "AddRespCountCode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var OccurrenceCounterComponents;
function OccurrenceCounterRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'OccurrenceCounter'-------
    t = 0;
    OccurrenceCounterClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    OccurrenceCounterComponents = [];
    
    for (const thisComponent of OccurrenceCounterComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function OccurrenceCounterRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'OccurrenceCounter'-------
    // get current time
    t = OccurrenceCounterClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of OccurrenceCounterComponents)
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


function OccurrenceCounterRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'OccurrenceCounter'-------
    for (const thisComponent of OccurrenceCounterComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    OccurenceC += 1;
    
    // the Routine "OccurrenceCounter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _P2WelcomeContKey_allKeys;
var P2WelcomeComponents;
function P2WelcomeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'P2Welcome'-------
    t = 0;
    P2WelcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    P2WelcomeContKey.keys = undefined;
    P2WelcomeContKey.rt = undefined;
    _P2WelcomeContKey_allKeys = [];
    // keep track of which components have finished
    P2WelcomeComponents = [];
    P2WelcomeComponents.push(P2WelcomeTxt);
    P2WelcomeComponents.push(P2WelcomeContKey);
    
    for (const thisComponent of P2WelcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function P2WelcomeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'P2Welcome'-------
    // get current time
    t = P2WelcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *P2WelcomeTxt* updates
    if (t >= 0.0 && P2WelcomeTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      P2WelcomeTxt.tStart = t;  // (not accounting for frame time here)
      P2WelcomeTxt.frameNStart = frameN;  // exact frame index
      
      P2WelcomeTxt.setAutoDraw(true);
    }

    
    // *P2WelcomeContKey* updates
    if (t >= 0.0 && P2WelcomeContKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      P2WelcomeContKey.tStart = t;  // (not accounting for frame time here)
      P2WelcomeContKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { P2WelcomeContKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { P2WelcomeContKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { P2WelcomeContKey.clearEvents(); });
    }

    if (P2WelcomeContKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = P2WelcomeContKey.getKeys({keyList: ['space'], waitRelease: false});
      _P2WelcomeContKey_allKeys = _P2WelcomeContKey_allKeys.concat(theseKeys);
      if (_P2WelcomeContKey_allKeys.length > 0) {
        P2WelcomeContKey.keys = _P2WelcomeContKey_allKeys[_P2WelcomeContKey_allKeys.length - 1].name;  // just the last key pressed
        P2WelcomeContKey.rt = _P2WelcomeContKey_allKeys[_P2WelcomeContKey_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of P2WelcomeComponents)
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


function P2WelcomeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'P2Welcome'-------
    for (const thisComponent of P2WelcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('P2WelcomeContKey.keys', P2WelcomeContKey.keys);
    if (typeof P2WelcomeContKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('P2WelcomeContKey.rt', P2WelcomeContKey.rt);
        routineTimer.reset();
        }
    
    P2WelcomeContKey.stop();
    // the Routine "P2Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _FamRateIntroKey_allKeys;
var FamRatingIntroComponents;
function FamRatingIntroRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'FamRatingIntro'-------
    t = 0;
    FamRatingIntroClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    FamRateIntroKey.keys = undefined;
    FamRateIntroKey.rt = undefined;
    _FamRateIntroKey_allKeys = [];
    // keep track of which components have finished
    FamRatingIntroComponents = [];
    FamRatingIntroComponents.push(FamRateIntroTxt);
    FamRatingIntroComponents.push(FamRateIntroKey);
    
    for (const thisComponent of FamRatingIntroComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FamRatingIntroRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'FamRatingIntro'-------
    // get current time
    t = FamRatingIntroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *FamRateIntroTxt* updates
    if (t >= 0.0 && FamRateIntroTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FamRateIntroTxt.tStart = t;  // (not accounting for frame time here)
      FamRateIntroTxt.frameNStart = frameN;  // exact frame index
      
      FamRateIntroTxt.setAutoDraw(true);
    }

    
    // *FamRateIntroKey* updates
    if (t >= 0.0 && FamRateIntroKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FamRateIntroKey.tStart = t;  // (not accounting for frame time here)
      FamRateIntroKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { FamRateIntroKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { FamRateIntroKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { FamRateIntroKey.clearEvents(); });
    }

    if (FamRateIntroKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = FamRateIntroKey.getKeys({keyList: ['space'], waitRelease: false});
      _FamRateIntroKey_allKeys = _FamRateIntroKey_allKeys.concat(theseKeys);
      if (_FamRateIntroKey_allKeys.length > 0) {
        FamRateIntroKey.keys = _FamRateIntroKey_allKeys[_FamRateIntroKey_allKeys.length - 1].name;  // just the last key pressed
        FamRateIntroKey.rt = _FamRateIntroKey_allKeys[_FamRateIntroKey_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FamRatingIntroComponents)
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


function FamRatingIntroRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'FamRatingIntro'-------
    for (const thisComponent of FamRatingIntroComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('FamRateIntroKey.keys', FamRateIntroKey.keys);
    if (typeof FamRateIntroKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('FamRateIntroKey.rt', FamRateIntroKey.rt);
        routineTimer.reset();
        }
    
    FamRateIntroKey.stop();
    // the Routine "FamRatingIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _FamRatingResp_allKeys;
var FamRatingComponents;
function FamRatingRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'FamRating'-------
    t = 0;
    FamRatingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    FamRatingResp.keys = undefined;
    FamRatingResp.rt = undefined;
    _FamRatingResp_allKeys = [];
    Syllab1 = new sound.Sound({
    win: psychoJS.window,
    value: Word11,
    secs: 0.38,
    });
    Syllab1.secs=0.38;
    Syllab1.setVolume(1);
    Syllab2 = new sound.Sound({
    win: psychoJS.window,
    value: Word12,
    secs: 0.38,
    });
    Syllab2.secs=0.38;
    Syllab2.setVolume(1);
    Syllab3 = new sound.Sound({
    win: psychoJS.window,
    value: Word13,
    secs: 0.38,
    });
    Syllab3.secs=0.38;
    Syllab3.setVolume(1);
    // keep track of which components have finished
    FamRatingComponents = [];
    FamRatingComponents.push(FamRatePrompt);
    FamRatingComponents.push(RatingScale);
    FamRatingComponents.push(RatingScale2);
    FamRatingComponents.push(FamRatingResp);
    FamRatingComponents.push(Syllab1);
    FamRatingComponents.push(Syllab2);
    FamRatingComponents.push(Syllab3);
    
    for (const thisComponent of FamRatingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FamRatingRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'FamRating'-------
    // get current time
    t = FamRatingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *FamRatePrompt* updates
    if (t >= 0.0 && FamRatePrompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FamRatePrompt.tStart = t;  // (not accounting for frame time here)
      FamRatePrompt.frameNStart = frameN;  // exact frame index
      
      FamRatePrompt.setAutoDraw(true);
    }

    
    // *RatingScale* updates
    if (t >= 0.0 && RatingScale.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RatingScale.tStart = t;  // (not accounting for frame time here)
      RatingScale.frameNStart = frameN;  // exact frame index
      
      RatingScale.setAutoDraw(true);
    }

    
    // *RatingScale2* updates
    if (t >= 0.0 && RatingScale2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RatingScale2.tStart = t;  // (not accounting for frame time here)
      RatingScale2.frameNStart = frameN;  // exact frame index
      
      RatingScale2.setAutoDraw(true);
    }

    
    // *FamRatingResp* updates
    if (t >= 0.0 && FamRatingResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FamRatingResp.tStart = t;  // (not accounting for frame time here)
      FamRatingResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { FamRatingResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { FamRatingResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { FamRatingResp.clearEvents(); });
    }

    if (FamRatingResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = FamRatingResp.getKeys({keyList: ['1', '2', '3', '4'], waitRelease: false});
      _FamRatingResp_allKeys = _FamRatingResp_allKeys.concat(theseKeys);
      if (_FamRatingResp_allKeys.length > 0) {
        FamRatingResp.keys = _FamRatingResp_allKeys[_FamRatingResp_allKeys.length - 1].name;  // just the last key pressed
        FamRatingResp.rt = _FamRatingResp_allKeys[_FamRatingResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // start/stop Syllab1
    if (t >= 0.5 && Syllab1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Syllab1.tStart = t;  // (not accounting for frame time here)
      Syllab1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ Syllab1.play(); });  // screen flip
      Syllab1.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.5 + 0.38 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Syllab1.status === PsychoJS.Status.STARTED || Syllab1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      if (0.38 > 0.5) {  Syllab1.stop();  // stop the sound (if longer than duration)
        Syllab1.status = PsychoJS.Status.FINISHED;
      }
    }
    // start/stop Syllab2
    if (t >= 0.88 && Syllab2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Syllab2.tStart = t;  // (not accounting for frame time here)
      Syllab2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ Syllab2.play(); });  // screen flip
      Syllab2.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.88 + 0.38 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Syllab2.status === PsychoJS.Status.STARTED || Syllab2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      if (0.38 > 0.5) {  Syllab2.stop();  // stop the sound (if longer than duration)
        Syllab2.status = PsychoJS.Status.FINISHED;
      }
    }
    // start/stop Syllab3
    if (t >= 1.26 && Syllab3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Syllab3.tStart = t;  // (not accounting for frame time here)
      Syllab3.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ Syllab3.play(); });  // screen flip
      Syllab3.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 1.26 + 0.38 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Syllab3.status === PsychoJS.Status.STARTED || Syllab3.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      if (0.38 > 0.5) {  Syllab3.stop();  // stop the sound (if longer than duration)
        Syllab3.status = PsychoJS.Status.FINISHED;
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FamRatingComponents)
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


function FamRatingRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'FamRating'-------
    for (const thisComponent of FamRatingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('FamRatingResp.keys', FamRatingResp.keys);
    if (typeof FamRatingResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('FamRatingResp.rt', FamRatingResp.rt);
        routineTimer.reset();
        }
    
    FamRatingResp.stop();
    Syllab1.stop();  // ensure sound has stopped at end of routine
    Syllab2.stop();  // ensure sound has stopped at end of routine
    Syllab3.stop();  // ensure sound has stopped at end of routine
    // the Routine "FamRating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _ContinueKey7_allKeys;
var Part2Intro2Components;
function Part2Intro2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Part2Intro2'-------
    t = 0;
    Part2Intro2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    ContinueKey7.keys = undefined;
    ContinueKey7.rt = undefined;
    _ContinueKey7_allKeys = [];
    // keep track of which components have finished
    Part2Intro2Components = [];
    Part2Intro2Components.push(P2IntroTxt2);
    Part2Intro2Components.push(ContinueKey7);
    
    for (const thisComponent of Part2Intro2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Part2Intro2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Part2Intro2'-------
    // get current time
    t = Part2Intro2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *P2IntroTxt2* updates
    if (t >= 0.0 && P2IntroTxt2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      P2IntroTxt2.tStart = t;  // (not accounting for frame time here)
      P2IntroTxt2.frameNStart = frameN;  // exact frame index
      
      P2IntroTxt2.setAutoDraw(true);
    }

    
    // *ContinueKey7* updates
    if (t >= 0.0 && ContinueKey7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ContinueKey7.tStart = t;  // (not accounting for frame time here)
      ContinueKey7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { ContinueKey7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { ContinueKey7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { ContinueKey7.clearEvents(); });
    }

    if (ContinueKey7.status === PsychoJS.Status.STARTED) {
      let theseKeys = ContinueKey7.getKeys({keyList: ['space'], waitRelease: false});
      _ContinueKey7_allKeys = _ContinueKey7_allKeys.concat(theseKeys);
      if (_ContinueKey7_allKeys.length > 0) {
        ContinueKey7.keys = _ContinueKey7_allKeys[_ContinueKey7_allKeys.length - 1].name;  // just the last key pressed
        ContinueKey7.rt = _ContinueKey7_allKeys[_ContinueKey7_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Part2Intro2Components)
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


function Part2Intro2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Part2Intro2'-------
    for (const thisComponent of Part2Intro2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ContinueKey7.keys', ContinueKey7.keys);
    if (typeof ContinueKey7.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('ContinueKey7.rt', ContinueKey7.rt);
        routineTimer.reset();
        }
    
    ContinueKey7.stop();
    // the Routine "Part2Intro2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var QuestionNo;
var countComponents;
function countRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'count'-------
    t = 0;
    countClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    AFCcount += 1;
    QuestionNo = (("Trial" + AFCcount.toString()) + " /16");
    
    // keep track of which components have finished
    countComponents = [];
    
    for (const thisComponent of countComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function countRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'count'-------
    // get current time
    t = countClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of countComponents)
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


function countRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'count'-------
    for (const thisComponent of countComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "count" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var AFCStartComponents;
function AFCStartRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'AFCStart'-------
    t = 0;
    AFCStartClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    QuestionNoTxt.setText(QuestionNo);
    // keep track of which components have finished
    AFCStartComponents = [];
    AFCStartComponents.push(QuestionNoTxt);
    
    for (const thisComponent of AFCStartComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function AFCStartRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'AFCStart'-------
    // get current time
    t = AFCStartClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *QuestionNoTxt* updates
    if (t >= 0.0 && QuestionNoTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      QuestionNoTxt.tStart = t;  // (not accounting for frame time here)
      QuestionNoTxt.frameNStart = frameN;  // exact frame index
      
      QuestionNoTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((QuestionNoTxt.status === PsychoJS.Status.STARTED || QuestionNoTxt.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      QuestionNoTxt.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of AFCStartComponents)
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


function AFCStartRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'AFCStart'-------
    for (const thisComponent of AFCStartComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var AFCFirstComponents;
function AFCFirstRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'AFCFirst'-------
    t = 0;
    AFCFirstClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.140000);
    // update component parameters for each repeat
    Word1No.setText('1');
    Word_1_1 = new sound.Sound({
    win: psychoJS.window,
    value: Word11,
    secs: 0.38,
    });
    Word_1_1.secs=0.38;
    Word_1_1.setVolume(1);
    Word_1_2 = new sound.Sound({
    win: psychoJS.window,
    value: Word12,
    secs: 0.38,
    });
    Word_1_2.secs=0.38;
    Word_1_2.setVolume(1);
    Word_1_3 = new sound.Sound({
    win: psychoJS.window,
    value: Word13,
    secs: 0.38,
    });
    Word_1_3.secs=0.38;
    Word_1_3.setVolume(1);
    // keep track of which components have finished
    AFCFirstComponents = [];
    AFCFirstComponents.push(Word1No);
    AFCFirstComponents.push(Word_1_1);
    AFCFirstComponents.push(Word_1_2);
    AFCFirstComponents.push(Word_1_3);
    
    for (const thisComponent of AFCFirstComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function AFCFirstRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'AFCFirst'-------
    // get current time
    t = AFCFirstClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Word1No* updates
    if (t >= 0.0 && Word1No.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Word1No.tStart = t;  // (not accounting for frame time here)
      Word1No.frameNStart = frameN;  // exact frame index
      
      Word1No.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.07 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Word1No.status === PsychoJS.Status.STARTED || Word1No.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      Word1No.setAutoDraw(false);
    }
    // start/stop Word_1_1
    if (t >= 1 && Word_1_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Word_1_1.tStart = t;  // (not accounting for frame time here)
      Word_1_1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ Word_1_1.play(); });  // screen flip
      Word_1_1.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 1 + 0.38 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Word_1_1.status === PsychoJS.Status.STARTED || Word_1_1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      if (0.38 > 0.5) {  Word_1_1.stop();  // stop the sound (if longer than duration)
        Word_1_1.status = PsychoJS.Status.FINISHED;
      }
    }
    // start/stop Word_1_2
    if (t >= 1.38 && Word_1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Word_1_2.tStart = t;  // (not accounting for frame time here)
      Word_1_2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ Word_1_2.play(); });  // screen flip
      Word_1_2.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 1.38 + 0.38 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Word_1_2.status === PsychoJS.Status.STARTED || Word_1_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      if (0.38 > 0.5) {  Word_1_2.stop();  // stop the sound (if longer than duration)
        Word_1_2.status = PsychoJS.Status.FINISHED;
      }
    }
    // start/stop Word_1_3
    if (t >= 1.76 && Word_1_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Word_1_3.tStart = t;  // (not accounting for frame time here)
      Word_1_3.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ Word_1_3.play(); });  // screen flip
      Word_1_3.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 1.76 + 0.38 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Word_1_3.status === PsychoJS.Status.STARTED || Word_1_3.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      if (0.38 > 0.5) {  Word_1_3.stop();  // stop the sound (if longer than duration)
        Word_1_3.status = PsychoJS.Status.FINISHED;
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of AFCFirstComponents)
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


function AFCFirstRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'AFCFirst'-------
    for (const thisComponent of AFCFirstComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    Word_1_1.stop();  // ensure sound has stopped at end of routine
    Word_1_2.stop();  // ensure sound has stopped at end of routine
    Word_1_3.stop();  // ensure sound has stopped at end of routine
    return Scheduler.Event.NEXT;
  };
}


var AFCSecondComponents;
function AFCSecondRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'AFCSecond'-------
    t = 0;
    AFCSecondClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.140000);
    // update component parameters for each repeat
    Word_2_1 = new sound.Sound({
    win: psychoJS.window,
    value: Word21,
    secs: 0.38,
    });
    Word_2_1.secs=0.38;
    Word_2_1.setVolume(1);
    Word_2_2 = new sound.Sound({
    win: psychoJS.window,
    value: Word22,
    secs: 0.38,
    });
    Word_2_2.secs=0.38;
    Word_2_2.setVolume(1);
    Word_2_3 = new sound.Sound({
    win: psychoJS.window,
    value: Word23,
    secs: 0.38,
    });
    Word_2_3.secs=0.38;
    Word_2_3.setVolume(1);
    // keep track of which components have finished
    AFCSecondComponents = [];
    AFCSecondComponents.push(Word2No);
    AFCSecondComponents.push(Word_2_1);
    AFCSecondComponents.push(Word_2_2);
    AFCSecondComponents.push(Word_2_3);
    
    for (const thisComponent of AFCSecondComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function AFCSecondRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'AFCSecond'-------
    // get current time
    t = AFCSecondClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Word2No* updates
    if (t >= 0.0 && Word2No.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Word2No.tStart = t;  // (not accounting for frame time here)
      Word2No.frameNStart = frameN;  // exact frame index
      
      Word2No.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.07 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Word2No.status === PsychoJS.Status.STARTED || Word2No.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      Word2No.setAutoDraw(false);
    }
    // start/stop Word_2_1
    if (t >= 1 && Word_2_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Word_2_1.tStart = t;  // (not accounting for frame time here)
      Word_2_1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ Word_2_1.play(); });  // screen flip
      Word_2_1.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 1 + 0.38 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Word_2_1.status === PsychoJS.Status.STARTED || Word_2_1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      if (0.38 > 0.5) {  Word_2_1.stop();  // stop the sound (if longer than duration)
        Word_2_1.status = PsychoJS.Status.FINISHED;
      }
    }
    // start/stop Word_2_2
    if (t >= 1.38 && Word_2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Word_2_2.tStart = t;  // (not accounting for frame time here)
      Word_2_2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ Word_2_2.play(); });  // screen flip
      Word_2_2.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 1.38 + 0.38 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Word_2_2.status === PsychoJS.Status.STARTED || Word_2_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      if (0.38 > 0.5) {  Word_2_2.stop();  // stop the sound (if longer than duration)
        Word_2_2.status = PsychoJS.Status.FINISHED;
      }
    }
    // start/stop Word_2_3
    if (t >= 1.76 && Word_2_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Word_2_3.tStart = t;  // (not accounting for frame time here)
      Word_2_3.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ Word_2_3.play(); });  // screen flip
      Word_2_3.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 1.76 + 0.38 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Word_2_3.status === PsychoJS.Status.STARTED || Word_2_3.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      if (0.38 > 0.5) {  Word_2_3.stop();  // stop the sound (if longer than duration)
        Word_2_3.status = PsychoJS.Status.FINISHED;
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of AFCSecondComponents)
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


function AFCSecondRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'AFCSecond'-------
    for (const thisComponent of AFCSecondComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    Word_2_1.stop();  // ensure sound has stopped at end of routine
    Word_2_2.stop();  // ensure sound has stopped at end of routine
    Word_2_3.stop();  // ensure sound has stopped at end of routine
    return Scheduler.Event.NEXT;
  };
}


var _AFCResp_allKeys;
var AFCQuestionComponents;
function AFCQuestionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'AFCQuestion'-------
    t = 0;
    AFCQuestionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    AFCResp.keys = undefined;
    AFCResp.rt = undefined;
    _AFCResp_allKeys = [];
    // keep track of which components have finished
    AFCQuestionComponents = [];
    AFCQuestionComponents.push(QuestionTxt);
    AFCQuestionComponents.push(AFCResp);
    
    for (const thisComponent of AFCQuestionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function AFCQuestionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'AFCQuestion'-------
    // get current time
    t = AFCQuestionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *QuestionTxt* updates
    if (t >= 0.0 && QuestionTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      QuestionTxt.tStart = t;  // (not accounting for frame time here)
      QuestionTxt.frameNStart = frameN;  // exact frame index
      
      QuestionTxt.setAutoDraw(true);
    }

    
    // *AFCResp* updates
    if (t >= 0.0 && AFCResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AFCResp.tStart = t;  // (not accounting for frame time here)
      AFCResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { AFCResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { AFCResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { AFCResp.clearEvents(); });
    }

    if (AFCResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = AFCResp.getKeys({keyList: ['1', '2'], waitRelease: false});
      _AFCResp_allKeys = _AFCResp_allKeys.concat(theseKeys);
      if (_AFCResp_allKeys.length > 0) {
        AFCResp.keys = _AFCResp_allKeys[_AFCResp_allKeys.length - 1].name;  // just the last key pressed
        AFCResp.rt = _AFCResp_allKeys[_AFCResp_allKeys.length - 1].rt;
        // was this correct?
        if (AFCResp.keys == AFCCorrect) {
            AFCResp.corr = 1;
        } else {
            AFCResp.corr = 0;
        }
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of AFCQuestionComponents)
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


function AFCQuestionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'AFCQuestion'-------
    for (const thisComponent of AFCQuestionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (AFCResp.keys === undefined) {
      if (['None','none',undefined].includes(AFCCorrect)) {
         AFCResp.corr = 1;  // correct non-response
      } else {
         AFCResp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('AFCResp.keys', AFCResp.keys);
    psychoJS.experiment.addData('AFCResp.corr', AFCResp.corr);
    if (typeof AFCResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('AFCResp.rt', AFCResp.rt);
        routineTimer.reset();
        }
    
    AFCResp.stop();
    // the Routine "AFCQuestion" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _EndKey2_allKeys;
var HearingCheckIntroComponents;
function HearingCheckIntroRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'HearingCheckIntro'-------
    t = 0;
    HearingCheckIntroClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    EndKey2.keys = undefined;
    EndKey2.rt = undefined;
    _EndKey2_allKeys = [];
    // keep track of which components have finished
    HearingCheckIntroComponents = [];
    HearingCheckIntroComponents.push(HearingCheckTxt);
    HearingCheckIntroComponents.push(EndKey2);
    
    for (const thisComponent of HearingCheckIntroComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function HearingCheckIntroRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'HearingCheckIntro'-------
    // get current time
    t = HearingCheckIntroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HearingCheckTxt* updates
    if (t >= 0.0 && HearingCheckTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HearingCheckTxt.tStart = t;  // (not accounting for frame time here)
      HearingCheckTxt.frameNStart = frameN;  // exact frame index
      
      HearingCheckTxt.setAutoDraw(true);
    }

    
    // *EndKey2* updates
    if (t >= 0.0 && EndKey2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EndKey2.tStart = t;  // (not accounting for frame time here)
      EndKey2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { EndKey2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { EndKey2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { EndKey2.clearEvents(); });
    }

    if (EndKey2.status === PsychoJS.Status.STARTED) {
      let theseKeys = EndKey2.getKeys({keyList: ['space'], waitRelease: false});
      _EndKey2_allKeys = _EndKey2_allKeys.concat(theseKeys);
      if (_EndKey2_allKeys.length > 0) {
        EndKey2.keys = _EndKey2_allKeys[_EndKey2_allKeys.length - 1].name;  // just the last key pressed
        EndKey2.rt = _EndKey2_allKeys[_EndKey2_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of HearingCheckIntroComponents)
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


function HearingCheckIntroRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'HearingCheckIntro'-------
    for (const thisComponent of HearingCheckIntroComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('EndKey2.keys', EndKey2.keys);
    if (typeof EndKey2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('EndKey2.rt', EndKey2.rt);
        routineTimer.reset();
        }
    
    EndKey2.stop();
    // the Routine "HearingCheckIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _CheckRespKey_allKeys;
var HearingCheckComponents;
function HearingCheckRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'HearingCheck'-------
    t = 0;
    HearingCheckClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    CheckWord = new sound.Sound({
    win: psychoJS.window,
    value: SoundFile,
    secs: -1,
    });
    CheckWord.setVolume(1);
    WordOptions.setText(((((("1. " + Word1) + "         2. ") + Word2) + "         3. ") + Word3));
    CheckRespKey.keys = undefined;
    CheckRespKey.rt = undefined;
    _CheckRespKey_allKeys = [];
    // keep track of which components have finished
    HearingCheckComponents = [];
    HearingCheckComponents.push(CheckWord);
    HearingCheckComponents.push(WordOptions);
    HearingCheckComponents.push(CheckQuestion);
    HearingCheckComponents.push(CheckRespKey);
    
    for (const thisComponent of HearingCheckComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function HearingCheckRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'HearingCheck'-------
    // get current time
    t = HearingCheckClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop CheckWord
    if (t >= 0.5 && CheckWord.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CheckWord.tStart = t;  // (not accounting for frame time here)
      CheckWord.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ CheckWord.play(); });  // screen flip
      CheckWord.status = PsychoJS.Status.STARTED;
    }
    if (t >= (CheckWord.getDuration() + CheckWord.tStart)     && CheckWord.status === PsychoJS.Status.STARTED) {
      CheckWord.stop();  // stop the sound (if longer than duration)
      CheckWord.status = PsychoJS.Status.FINISHED;
    }
    
    // *WordOptions* updates
    if (t >= 0.0 && WordOptions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WordOptions.tStart = t;  // (not accounting for frame time here)
      WordOptions.frameNStart = frameN;  // exact frame index
      
      WordOptions.setAutoDraw(true);
    }

    
    // *CheckQuestion* updates
    if (t >= 0.0 && CheckQuestion.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CheckQuestion.tStart = t;  // (not accounting for frame time here)
      CheckQuestion.frameNStart = frameN;  // exact frame index
      
      CheckQuestion.setAutoDraw(true);
    }

    
    // *CheckRespKey* updates
    if (t >= 0.0 && CheckRespKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CheckRespKey.tStart = t;  // (not accounting for frame time here)
      CheckRespKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { CheckRespKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { CheckRespKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { CheckRespKey.clearEvents(); });
    }

    if (CheckRespKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = CheckRespKey.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _CheckRespKey_allKeys = _CheckRespKey_allKeys.concat(theseKeys);
      if (_CheckRespKey_allKeys.length > 0) {
        CheckRespKey.keys = _CheckRespKey_allKeys[_CheckRespKey_allKeys.length - 1].name;  // just the last key pressed
        CheckRespKey.rt = _CheckRespKey_allKeys[_CheckRespKey_allKeys.length - 1].rt;
        // was this correct?
        if (CheckRespKey.keys == Correct) {
            CheckRespKey.corr = 1;
        } else {
            CheckRespKey.corr = 0;
        }
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of HearingCheckComponents)
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


function HearingCheckRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'HearingCheck'-------
    for (const thisComponent of HearingCheckComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    CheckWord.stop();  // ensure sound has stopped at end of routine
    // was no response the correct answer?!
    if (CheckRespKey.keys === undefined) {
      if (['None','none',undefined].includes(Correct)) {
         CheckRespKey.corr = 1;  // correct non-response
      } else {
         CheckRespKey.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('CheckRespKey.keys', CheckRespKey.keys);
    psychoJS.experiment.addData('CheckRespKey.corr', CheckRespKey.corr);
    if (typeof CheckRespKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('CheckRespKey.rt', CheckRespKey.rt);
        routineTimer.reset();
        }
    
    CheckRespKey.stop();
    // the Routine "HearingCheck" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _EndAllKey_allKeys;
var P2EndComponents;
function P2EndRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'P2End'-------
    t = 0;
    P2EndClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    EndAllKey.keys = undefined;
    EndAllKey.rt = undefined;
    _EndAllKey_allKeys = [];
    // keep track of which components have finished
    P2EndComponents = [];
    P2EndComponents.push(EndMssg);
    P2EndComponents.push(EndAllKey);
    P2EndComponents.push(FeedbackQ);
    
    for (const thisComponent of P2EndComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function P2EndRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'P2End'-------
    // get current time
    t = P2EndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *EndMssg* updates
    if (t >= 0.0 && EndMssg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EndMssg.tStart = t;  // (not accounting for frame time here)
      EndMssg.frameNStart = frameN;  // exact frame index
      
      EndMssg.setAutoDraw(true);
    }

    
    // *EndAllKey* updates
    if (t >= 0.0 && EndAllKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EndAllKey.tStart = t;  // (not accounting for frame time here)
      EndAllKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { EndAllKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { EndAllKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { EndAllKey.clearEvents(); });
    }

    if (EndAllKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = EndAllKey.getKeys({keyList: ['return'], waitRelease: false});
      _EndAllKey_allKeys = _EndAllKey_allKeys.concat(theseKeys);
      if (_EndAllKey_allKeys.length > 0) {
        EndAllKey.keys = _EndAllKey_allKeys[_EndAllKey_allKeys.length - 1].name;  // just the last key pressed
        EndAllKey.rt = _EndAllKey_allKeys[_EndAllKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *FeedbackQ* updates
    if (t >= 0.0 && FeedbackQ.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FeedbackQ.tStart = t;  // (not accounting for frame time here)
      FeedbackQ.frameNStart = frameN;  // exact frame index
      
      FeedbackQ.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of P2EndComponents)
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


function P2EndRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'P2End'-------
    for (const thisComponent of P2EndComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('EndAllKey.keys', EndAllKey.keys);
    if (typeof EndAllKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('EndAllKey.rt', EndAllKey.rt);
        routineTimer.reset();
        }
    
    EndAllKey.stop();
    // the Routine "P2End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _BlankEndKey_allKeys;
var BlankComponents;
function BlankRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Blank'-------
    t = 0;
    BlankClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    BlankEndKey.keys = undefined;
    BlankEndKey.rt = undefined;
    _BlankEndKey_allKeys = [];
    // keep track of which components have finished
    BlankComponents = [];
    BlankComponents.push(BlankEndKey);
    
    for (const thisComponent of BlankComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function BlankRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Blank'-------
    // get current time
    t = BlankClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *BlankEndKey* updates
    if (t >= 0.0 && BlankEndKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BlankEndKey.tStart = t;  // (not accounting for frame time here)
      BlankEndKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { BlankEndKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { BlankEndKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { BlankEndKey.clearEvents(); });
    }

    if (BlankEndKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = BlankEndKey.getKeys({keyList: ['space'], waitRelease: false});
      _BlankEndKey_allKeys = _BlankEndKey_allKeys.concat(theseKeys);
      if (_BlankEndKey_allKeys.length > 0) {
        BlankEndKey.keys = _BlankEndKey_allKeys[_BlankEndKey_allKeys.length - 1].name;  // just the last key pressed
        BlankEndKey.rt = _BlankEndKey_allKeys[_BlankEndKey_allKeys.length - 1].rt;
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
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of BlankComponents)
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


function BlankRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Blank'-------
    for (const thisComponent of BlankComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Blank" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
