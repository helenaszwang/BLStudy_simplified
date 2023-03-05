/***************** 
 * Session1 Test *
 *****************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'Session1';  // from the Builder filename that created this script
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
const HeadphoneLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(HeadphoneLoopBegin, HeadphoneLoopScheduler);
flowScheduler.add(HeadphoneLoopScheduler);
flowScheduler.add(HeadphoneLoopEnd);
const WordTaskLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(WordTaskLoopBegin, WordTaskLoopScheduler);
flowScheduler.add(WordTaskLoopScheduler);
flowScheduler.add(WordTaskLoopEnd);
flowScheduler.add(End1RoutineBegin());
flowScheduler.add(End1RoutineEachFrame());
flowScheduler.add(End1RoutineEnd());
const SoundTaskLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(SoundTaskLoopBegin, SoundTaskLoopScheduler);
flowScheduler.add(SoundTaskLoopScheduler);
flowScheduler.add(SoundTaskLoopEnd);
flowScheduler.add(End1RoutineBegin());
flowScheduler.add(End1RoutineEachFrame());
flowScheduler.add(End1RoutineEnd());
const SimilarityRatingTaskLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(SimilarityRatingTaskLoopBegin, SimilarityRatingTaskLoopScheduler);
flowScheduler.add(SimilarityRatingTaskLoopScheduler);
flowScheduler.add(SimilarityRatingTaskLoopEnd);
flowScheduler.add(End1RoutineBegin());
flowScheduler.add(End1RoutineEachFrame());
flowScheduler.add(End1RoutineEnd());
const LabelingTaskLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(LabelingTaskLoopBegin, LabelingTaskLoopScheduler);
flowScheduler.add(LabelingTaskLoopScheduler);
flowScheduler.add(LabelingTaskLoopEnd);
flowScheduler.add(End1RoutineBegin());
flowScheduler.add(End1RoutineEachFrame());
flowScheduler.add(End1RoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'Headphone/t3_1.wav', 'path': 'Headphone/t3_1.wav'},
    {'name': 'SoundMST/Trumpet_C.wav', 'path': 'SoundMST/Trumpet_C.wav'},
    {'name': 'SoundMST/Bird_C.wav', 'path': 'SoundMST/Bird_C.wav'},
    {'name': 'SoundMST/Fireworks.wav', 'path': 'SoundMST/Fireworks.wav'},
    {'name': 'WordMST/FU_ZO_RAI.wav', 'path': 'WordMST/FU_ZO_RAI.wav'},
    {'name': 'WordMST/GI_TAI_SA.wav', 'path': 'WordMST/GI_TAI_SA.wav'},
    {'name': 'WordMST/PU_DAY_MO.wav', 'path': 'WordMST/PU_DAY_MO.wav'},
    {'name': 'WordMST/KAI_LAY_TA.wav', 'path': 'WordMST/KAI_LAY_TA.wav'},
    {'name': 'WordMST/TAI_SA_GI.wav', 'path': 'WordMST/TAI_SA_GI.wav'},
    {'name': 'SoundMST/Bird_A.wav', 'path': 'SoundMST/Bird_A.wav'},
    {'name': 'SoundMST/Chicken_A.wav', 'path': 'SoundMST/Chicken_A.wav'},
    {'name': 'Task 1.jpg', 'path': 'Task 1.jpg'},
    {'name': 'SoundMST/Thunder_A.wav', 'path': 'SoundMST/Thunder_A.wav'},
    {'name': 'SoundMST/Bagpipe.wav', 'path': 'SoundMST/Bagpipe.wav'},
    {'name': 'WordMST/KAY_BA_LI.wav', 'path': 'WordMST/KAY_BA_LI.wav'},
    {'name': 'WordMST/PAI_LU_WA.wav', 'path': 'WordMST/PAI_LU_WA.wav'},
    {'name': 'WordMST/RAY_PA_TI.wav', 'path': 'WordMST/RAY_PA_TI.wav'},
    {'name': 'Headphone/t1_2.wav', 'path': 'Headphone/t1_2.wav'},
    {'name': 'SoundMST/Heartbeat.wav', 'path': 'SoundMST/Heartbeat.wav'},
    {'name': 'SoundMST/Piano_D.wav', 'path': 'SoundMST/Piano_D.wav'},
    {'name': 'WordMST/VU_NA_WAI.wav', 'path': 'WordMST/VU_NA_WAI.wav'},
    {'name': 'SoundMST/Puff_A.wav', 'path': 'SoundMST/Puff_A.wav'},
    {'name': 'SoundMST/Dog_I.wav', 'path': 'SoundMST/Dog_I.wav'},
    {'name': 'SoundMST/Droplet_B.wav', 'path': 'SoundMST/Droplet_B.wav'},
    {'name': 'SoundMST/Slurp.wav', 'path': 'SoundMST/Slurp.wav'},
    {'name': 'SoundMST/Camera.wav', 'path': 'SoundMST/Camera.wav'},
    {'name': 'WordMST/TAI_GI_SA.wav', 'path': 'WordMST/TAI_GI_SA.wav'},
    {'name': 'SoundMST/Chomp_C.wav', 'path': 'SoundMST/Chomp_C.wav'},
    {'name': 'SoundMST/Printer.wav', 'path': 'SoundMST/Printer.wav'},
    {'name': 'Headphone/t2_1.wav', 'path': 'Headphone/t2_1.wav'},
    {'name': 'Headphone_check.xlsx', 'path': 'Headphone_check.xlsx'},
    {'name': 'SoundMST/IceDrop.wav', 'path': 'SoundMST/IceDrop.wav'},
    {'name': 'SoundMST/Snore_E.wav', 'path': 'SoundMST/Snore_E.wav'},
    {'name': 'WordMST/HI_NAY_VA.wav', 'path': 'WordMST/HI_NAY_VA.wav'},
    {'name': 'Headphone/t2_2.wav', 'path': 'Headphone/t2_2.wav'},
    {'name': 'SoundMST_trials.xlsx', 'path': 'SoundMST_trials.xlsx'},
    {'name': 'WordMST/VU_WAI_NA.wav', 'path': 'WordMST/VU_WAI_NA.wav'},
    {'name': 'SoundMST/Phone_F.wav', 'path': 'SoundMST/Phone_F.wav'},
    {'name': 'SoundMST/Footsteps_C.wav', 'path': 'SoundMST/Footsteps_C.wav'},
    {'name': 'SoundMST/Clap_D.wav', 'path': 'SoundMST/Clap_D.wav'},
    {'name': 'SoundMST/CarStart_D.wav', 'path': 'SoundMST/CarStart_D.wav'},
    {'name': 'Task 3.jpg', 'path': 'Task 3.jpg'},
    {'name': 'SoundMST/Toilet_B.wav', 'path': 'SoundMST/Toilet_B.wav'},
    {'name': 'WordMST/NO_WA_BAY.wav', 'path': 'WordMST/NO_WA_BAY.wav'},
    {'name': 'Headphone/t1_1.wav', 'path': 'Headphone/t1_1.wav'},
    {'name': 'WordMST/NA_VU_WAI.wav', 'path': 'WordMST/NA_VU_WAI.wav'},
    {'name': 'SoundMST/CarStart_E.wav', 'path': 'SoundMST/CarStart_E.wav'},
    {'name': 'SoundMST/Duck_A.wav', 'path': 'SoundMST/Duck_A.wav'},
    {'name': 'SoundMST/Phone_E.wav', 'path': 'SoundMST/Phone_E.wav'},
    {'name': 'WordMST/LI_KAY_BA.wav', 'path': 'WordMST/LI_KAY_BA.wav'},
    {'name': 'WordMST/WAI_RO_JU.wav', 'path': 'WordMST/WAI_RO_JU.wav'},
    {'name': 'Similarity_trials.xlsx', 'path': 'Similarity_trials.xlsx'},
    {'name': 'SoundMST/Laugh_A.wav', 'path': 'SoundMST/Laugh_A.wav'},
    {'name': 'SoundMST/ManWhistle_E.wav', 'path': 'SoundMST/ManWhistle_E.wav'},
    {'name': 'SoundMST/Cough_J.wav', 'path': 'SoundMST/Cough_J.wav'},
    {'name': 'Task 4.jpg', 'path': 'Task 4.jpg'},
    {'name': 'WordMST/MO_DAY_PU.wav', 'path': 'WordMST/MO_DAY_PU.wav'},
    {'name': 'SoundMST/Buzz.wav', 'path': 'SoundMST/Buzz.wav'},
    {'name': 'WordMST/GU_CHAI_PI.wav', 'path': 'WordMST/GU_CHAI_PI.wav'},
    {'name': 'SoundMST/Growl_H.wav', 'path': 'SoundMST/Growl_H.wav'},
    {'name': 'SoundMST/Hammer_A.wav', 'path': 'SoundMST/Hammer_A.wav'},
    {'name': 'WordMSTPractice/FO_YI_LAY.wav', 'path': 'WordMSTPractice/FO_YI_LAY.wav'},
    {'name': 'SoundMSTPractice/Skid_B.wav', 'path': 'SoundMSTPractice/Skid_B.wav'},
    {'name': 'SoundMST/Chomp_A.wav', 'path': 'SoundMST/Chomp_A.wav'},
    {'name': 'WordMST/KO_SU_FAI.wav', 'path': 'WordMST/KO_SU_FAI.wav'},
    {'name': 'WordMST/SA_TAI_GI.wav', 'path': 'WordMST/SA_TAI_GI.wav'},
    {'name': 'WordMST/FI_GU_CHA.wav', 'path': 'WordMST/FI_GU_CHA.wav'},
    {'name': 'WordMST/DAY_MO_PU.wav', 'path': 'WordMST/DAY_MO_PU.wav'},
    {'name': 'SoundMST/DialTone.wav', 'path': 'SoundMST/DialTone.wav'},
    {'name': 'SoundMSTPractice/Seagull_A.wav', 'path': 'SoundMSTPractice/Seagull_A.wav'},
    {'name': 'WordMST_practicetrials.xlsx', 'path': 'WordMST_practicetrials.xlsx'},
    {'name': 'SoundMST/Bubbles_A.wav', 'path': 'SoundMST/Bubbles_A.wav'},
    {'name': 'SoundMST/Typing.wav', 'path': 'SoundMST/Typing.wav'},
    {'name': 'SoundMST/Helicopter_A.wav', 'path': 'SoundMST/Helicopter_A.wav'},
    {'name': 'SoundMST/Airhorn.wav', 'path': 'SoundMST/Airhorn.wav'},
    {'name': 'WordMST/LI_BA_KAY.wav', 'path': 'WordMST/LI_BA_KAY.wav'},
    {'name': 'SoundMST/Chime_A.wav', 'path': 'SoundMST/Chime_A.wav'},
    {'name': 'SoundMST/Donkey.wav', 'path': 'SoundMST/Donkey.wav'},
    {'name': 'SoundMST/Chime_D.wav', 'path': 'SoundMST/Chime_D.wav'},
    {'name': 'WordMSTPractice/JAY_YO_BU.wav', 'path': 'WordMSTPractice/JAY_YO_BU.wav'},
    {'name': 'WordMST/KAY_LI_BA.wav', 'path': 'WordMST/KAY_LI_BA.wav'},
    {'name': 'SoundMST/Bubbles_B.wav', 'path': 'SoundMST/Bubbles_B.wav'},
    {'name': 'WordMST/BA_KAY_LI.wav', 'path': 'WordMST/BA_KAY_LI.wav'},
    {'name': 'WordMST/CHU_LA_PAY.wav', 'path': 'WordMST/CHU_LA_PAY.wav'},
    {'name': 'SoundMST/Laugh_D.wav', 'path': 'SoundMST/Laugh_D.wav'},
    {'name': 'WordMST/HO_NAY_VA.wav', 'path': 'WordMST/HO_NAY_VA.wav'},
    {'name': 'SoundMST/Writing_C.wav', 'path': 'SoundMST/Writing_C.wav'},
    {'name': 'WordMST/RAI_ZO_FU.wav', 'path': 'WordMST/RAI_ZO_FU.wav'},
    {'name': 'Task 2.jpg', 'path': 'Task 2.jpg'},
    {'name': 'WordMST/RAI_FU_ZO.wav', 'path': 'WordMST/RAI_FU_ZO.wav'},
    {'name': 'WordMST/NA_WAI_VU.wav', 'path': 'WordMST/NA_WAI_VU.wav'},
    {'name': 'SoundMST/Snore_C.wav', 'path': 'SoundMST/Snore_C.wav'},
    {'name': 'SoundMST/Trumpet_B.wav', 'path': 'SoundMST/Trumpet_B.wav'},
    {'name': 'WordMST/LU_HAI_BO.wav', 'path': 'WordMST/LU_HAI_BO.wav'},
    {'name': 'SoundMST/Whistle_C.wav', 'path': 'SoundMST/Whistle_C.wav'},
    {'name': 'WordMST/WAI_VU_NA.wav', 'path': 'WordMST/WAI_VU_NA.wav'},
    {'name': 'WordMST/ZO_FU_RAI.wav', 'path': 'WordMST/ZO_FU_RAI.wav'},
    {'name': 'SoundMST/Siren_A.wav', 'path': 'SoundMST/Siren_A.wav'},
    {'name': 'WordMST/GA_MU_ZI.wav', 'path': 'WordMST/GA_MU_ZI.wav'},
    {'name': 'WordMST/LA_ZAY_CHAI.wav', 'path': 'WordMST/LA_ZAY_CHAI.wav'},
    {'name': 'SoundMST/Elephant_C.wav', 'path': 'SoundMST/Elephant_C.wav'},
    {'name': 'WordMST/BA_LI_KAY.wav', 'path': 'WordMST/BA_LI_KAY.wav'},
    {'name': 'SoundMSTPractice/Gargle_B.wav', 'path': 'SoundMSTPractice/Gargle_B.wav'},
    {'name': 'SoundMST/Coin_E.wav', 'path': 'SoundMST/Coin_E.wav'},
    {'name': 'SoundMST/Pour_F.wav', 'path': 'SoundMST/Pour_F.wav'},
    {'name': 'WordMST/PU_MO_DAY.wav', 'path': 'WordMST/PU_MO_DAY.wav'},
    {'name': 'SoundMST/Goat_C.wav', 'path': 'SoundMST/Goat_C.wav'},
    {'name': 'WordMST/DA_CHU_VAI.wav', 'path': 'WordMST/DA_CHU_VAI.wav'},
    {'name': 'SoundMSTPractice/Gargle_A.wav', 'path': 'SoundMSTPractice/Gargle_A.wav'},
    {'name': 'SoundMST/Elephant_A.wav', 'path': 'SoundMST/Elephant_A.wav'},
    {'name': 'SoundMST/Cough_I.wav', 'path': 'SoundMST/Cough_I.wav'},
    {'name': 'SoundMST/Duck_B.wav', 'path': 'SoundMST/Duck_B.wav'},
    {'name': 'WordMST/DAI_RU_CHI.wav', 'path': 'WordMST/DAI_RU_CHI.wav'},
    {'name': 'SoundMST/Writing_A.wav', 'path': 'SoundMST/Writing_A.wav'},
    {'name': 'SoundMST/Bowlingpins.wav', 'path': 'SoundMST/Bowlingpins.wav'},
    {'name': 'SoundMST/Clap_A.wav', 'path': 'SoundMST/Clap_A.wav'},
    {'name': 'SoundMST/Mosquito_B.wav', 'path': 'SoundMST/Mosquito_B.wav'},
    {'name': 'SoundMST/Cat_A.wav', 'path': 'SoundMST/Cat_A.wav'},
    {'name': 'SoundMST/Baby_C.wav', 'path': 'SoundMST/Baby_C.wav'},
    {'name': 'SoundMST/Pour_C.wav', 'path': 'SoundMST/Pour_C.wav'},
    {'name': 'SoundMST/Sneeze_B.wav', 'path': 'SoundMST/Sneeze_B.wav'},
    {'name': 'SoundMST/HairDryer_A.wav', 'path': 'SoundMST/HairDryer_A.wav'},
    {'name': 'SoundMST/Faucet_A.wav', 'path': 'SoundMST/Faucet_A.wav'},
    {'name': 'SoundMST/Coin_D.wav', 'path': 'SoundMST/Coin_D.wav'},
    {'name': 'SoundMST/Cow.wav', 'path': 'SoundMST/Cow.wav'},
    {'name': 'SoundMST/PaperRip.wav', 'path': 'SoundMST/PaperRip.wav'},
    {'name': 'SoundMST/Piano_C.wav', 'path': 'SoundMST/Piano_C.wav'},
    {'name': 'SoundMST/Horse.wav', 'path': 'SoundMST/Horse.wav'},
    {'name': 'WordMST/NU_CHAY_SO.wav', 'path': 'WordMST/NU_CHAY_SO.wav'},
    {'name': 'WordMST/VAI_HO_LA.wav', 'path': 'WordMST/VAI_HO_LA.wav'},
    {'name': 'WordMST/SI_VAI_CHU.wav', 'path': 'WordMST/SI_VAI_CHU.wav'},
    {'name': 'SoundMST/Footsteps_F.wav', 'path': 'SoundMST/Footsteps_F.wav'},
    {'name': 'WordMST/GI_SA_TAI.wav', 'path': 'WordMST/GI_SA_TAI.wav'},
    {'name': 'SoundMST/Airplane_B.wav', 'path': 'SoundMST/Airplane_B.wav'},
    {'name': 'SoundMST/Siren_E.wav', 'path': 'SoundMST/Siren_E.wav'},
    {'name': 'WordMST/FU_RAI_ZO.wav', 'path': 'WordMST/FU_RAI_ZO.wav'},
    {'name': 'SoundMST/Dog_H.wav', 'path': 'SoundMST/Dog_H.wav'},
    {'name': 'SoundMST/Cello.wav', 'path': 'SoundMST/Cello.wav'},
    {'name': 'WordMST/ZO_RAI_FU.wav', 'path': 'WordMST/ZO_RAI_FU.wav'},
    {'name': 'SoundMST/Faucet_C.wav', 'path': 'SoundMST/Faucet_C.wav'},
    {'name': 'WordMST/WAI_NA_VU.wav', 'path': 'WordMST/WAI_NA_VU.wav'},
    {'name': 'SoundMST/Bullfrog.wav', 'path': 'SoundMST/Bullfrog.wav'},
    {'name': 'SoundMST/Cup.wav', 'path': 'SoundMST/Cup.wav'},
    {'name': 'WordMST_trials.xlsx', 'path': 'WordMST_trials.xlsx'},
    {'name': 'SoundMST/Guitar_B.wav', 'path': 'SoundMST/Guitar_B.wav'},
    {'name': 'SoundMST/Steam.wav', 'path': 'SoundMST/Steam.wav'},
    {'name': 'SoundMST/Whistle_B.wav', 'path': 'SoundMST/Whistle_B.wav'},
    {'name': 'SoundMST/Sleighbells_B.wav', 'path': 'SoundMST/Sleighbells_B.wav'},
    {'name': 'SoundMST/Baby_B.wav', 'path': 'SoundMST/Baby_B.wav'},
    {'name': 'WordMST/HA_SI_JAI.wav', 'path': 'WordMST/HA_SI_JAI.wav'},
    {'name': 'Headphone/t3_2.wav', 'path': 'Headphone/t3_2.wav'},
    {'name': 'WordMST/DAY_PU_MO.wav', 'path': 'WordMST/DAY_PU_MO.wav'},
    {'name': 'WordMST/SA_GI_TAI.wav', 'path': 'WordMST/SA_GI_TAI.wav'},
    {'name': 'WordMSTPractice/YO_BU_JAY.wav', 'path': 'WordMSTPractice/YO_BU_JAY.wav'},
    {'name': 'SoundMST/ManWhistle.wav', 'path': 'SoundMST/ManWhistle.wav'},
    {'name': 'WordMST/MO_PU_DAY.wav', 'path': 'WordMST/MO_PU_DAY.wav'},
    {'name': 'SoundMST/Crow_A.wav', 'path': 'SoundMST/Crow_A.wav'},
    {'name': 'SoundMST/Howl.wav', 'path': 'SoundMST/Howl.wav'},
    {'name': 'SoundMST/Cuckoo_A.wav', 'path': 'SoundMST/Cuckoo_A.wav'},
    {'name': 'SoundMST/Wind_B.wav', 'path': 'SoundMST/Wind_B.wav'}
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
  
  return Scheduler.Event.NEXT;
}


var HeadphonePlayClock;
var CheckSound;
var counter;
var checkcount;
var QuestionTxt;
var CheckTrial;
var CrossHeadphone;
var CheckResp;
var HeadphoneFeedbackClock;
var FeedbackTxt;
var Welcome1Clock;
var Welcome1Continue;
var Task1Slide;
var PracticeBeginClock;
var WelcomeContinueKey2;
var PracticeText2;
var Practice1Clock;
var WTcount;
var TrialNumber;
var PracticeSound;
var PracticeCross;
var PracticeRespKey2;
var PracticeFeedbackClock;
var Practice_resp;
var PracticeMssg;
var FeedbackCross;
var StartClock;
var StartTxt;
var StartKey;
var CountdownClock;
var No3;
var No2;
var No1;
var Count1Clock;
var no_3;
var MSTWordClock;
var TargetSound;
var ItemNumber;
var MST_resp;
var Option2;
var End1Clock;
var EndMssg;
var End1Cont;
var Welcome2_2Clock;
var Welcome2Continue;
var Task2Slide;
var SoundPracticeClock;
var Tcount;
var PracticeSound2;
var PracticeCrossW;
var PracticeTrialNo;
var PracticeRespKey2II;
var SoundPracticeFeedbackClock;
var Message;
var PracticeCrossW2;
var PracticeSoundKey;
var MSTSoundStartClock;
var MSTSoundStrtMssg;
var MSTSoundStrtKey;
var Count2Clock;
var no2;
var MSTSoundClock;
var MSTSoundCount;
var MSTSoundPlay;
var MSTSoundCross;
var MSTSoundResponseClock;
var MSTSoundKey;
var Options2II;
var Welcome3Clock;
var Task3Slide;
var Welcome3Continue;
var Count3Clock;
var Cross1Sec;
var SimilarityPresentationClock;
var simcount;
var FirstSound;
var SecondSound;
var Cross;
var NumberOne;
var NumberTwo;
var SimTrialNumber;
var SimlarityResponseClock;
var SimilarityRatingScale;
var SimilarityRatingKey;
var Welcome4Clock;
var Task4Slide;
var Welcome4Continue;
var SoundLabelingClock;
var SoundLabelQuestion;
var Sound;
var LabelingKey;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "HeadphonePlay"
  HeadphonePlayClock = new util.Clock();
  CheckSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  CheckSound.setVolume(1);
  counter = 0;
  checkcount = (counter.toString() + "/6");
  
  QuestionTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'QuestionTxt',
    text: 'Which tone was the quietest?\n(Press the corresponding number on your keyboard)\n\n1 = First  2 = Second  3 = Third',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  CheckTrial = new visual.TextStim({
    win: psychoJS.window,
    name: 'CheckTrial',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  CrossHeadphone = new visual.TextStim({
    win: psychoJS.window,
    name: 'CrossHeadphone',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  CheckResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "HeadphoneFeedback"
  HeadphoneFeedbackClock = new util.Clock();
  FeedbackTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'FeedbackTxt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Welcome1"
  Welcome1Clock = new util.Clock();
  Welcome1Continue = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Task1Slide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Task1Slide', units : undefined, 
    image : 'Task 1.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.7, 0.9],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "PracticeBegin"
  PracticeBeginClock = new util.Clock();
  WelcomeContinueKey2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  PracticeText2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'PracticeText2',
    text: "Let's start with some practice",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "Practice1"
  Practice1Clock = new util.Clock();
  WTcount = 0;
  
  TrialNumber = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrialNumber',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  PracticeSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  PracticeSound.setVolume(1);
  PracticeCross = new visual.TextStim({
    win: psychoJS.window,
    name: 'PracticeCross',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  PracticeRespKey2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PracticeFeedback"
  PracticeFeedbackClock = new util.Clock();
  Practice_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  PracticeMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'PracticeMssg',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  FeedbackCross = new visual.TextStim({
    win: psychoJS.window,
    name: 'FeedbackCross',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "Start"
  StartClock = new util.Clock();
  StartTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'StartTxt',
    text: 'Great job! This is the end of the practice.\n\n\nWe will now begin the actual task. There are 100 sound files in total. The words from the practice are not part of the actual task. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  StartKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Countdown"
  CountdownClock = new util.Clock();
  No3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'No3',
    text: '3',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  No2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'No2',
    text: '2',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  No1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'No1',
    text: '1',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Count1"
  Count1Clock = new util.Clock();
  no_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'no_3',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "MSTWord"
  MSTWordClock = new util.Clock();
  TargetSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  TargetSound.setVolume(1);
  ItemNumber = new visual.TextStim({
    win: psychoJS.window,
    name: 'ItemNumber',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  MST_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Option2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Option2',
    text: 'Old or New?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "End1"
  End1Clock = new util.Clock();
  EndMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'EndMssg',
    text: 'Great job! This is the end of this component. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  End1Cont = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Welcome2_2"
  Welcome2_2Clock = new util.Clock();
  Welcome2Continue = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Task2Slide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Task2Slide', units : undefined, 
    image : 'Task 2.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.7, 0.9],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "PracticeBegin"
  PracticeBeginClock = new util.Clock();
  WelcomeContinueKey2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  PracticeText2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'PracticeText2',
    text: "Let's start with some practice",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "SoundPractice"
  SoundPracticeClock = new util.Clock();
  Tcount = 0;
  
  PracticeSound2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  PracticeSound2.setVolume(1);
  PracticeCrossW = new visual.TextStim({
    win: psychoJS.window,
    name: 'PracticeCrossW',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  PracticeTrialNo = new visual.TextStim({
    win: psychoJS.window,
    name: 'PracticeTrialNo',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  PracticeRespKey2II = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SoundPracticeFeedback"
  SoundPracticeFeedbackClock = new util.Clock();
  Message = new visual.TextStim({
    win: psychoJS.window,
    name: 'Message',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  PracticeCrossW2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'PracticeCrossW2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  PracticeSoundKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "MSTSoundStart"
  MSTSoundStartClock = new util.Clock();
  MSTSoundStrtMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'MSTSoundStrtMssg',
    text: 'Great job! This is the end of the practice.\n\n\nWe will now begin the actual task. There are 128 sound files in total. The sounds from the practice are not part of the actual task. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  MSTSoundStrtKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Countdown"
  CountdownClock = new util.Clock();
  No3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'No3',
    text: '3',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  No2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'No2',
    text: '2',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  No1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'No1',
    text: '1',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Count2"
  Count2Clock = new util.Clock();
  no2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'no2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "MSTSound"
  MSTSoundClock = new util.Clock();
  MSTSoundCount = new visual.TextStim({
    win: psychoJS.window,
    name: 'MSTSoundCount',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  MSTSoundPlay = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  MSTSoundPlay.setVolume(1);
  MSTSoundCross = new visual.TextStim({
    win: psychoJS.window,
    name: 'MSTSoundCross',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "MSTSoundResponse"
  MSTSoundResponseClock = new util.Clock();
  MSTSoundKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Options2II = new visual.TextStim({
    win: psychoJS.window,
    name: 'Options2II',
    text: 'Old or New?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "End1"
  End1Clock = new util.Clock();
  EndMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'EndMssg',
    text: 'Great job! This is the end of this component. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  End1Cont = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Welcome3"
  Welcome3Clock = new util.Clock();
  Task3Slide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Task3Slide', units : undefined, 
    image : 'Task 3.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.7, 0.9],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  Welcome3Continue = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Countdown"
  CountdownClock = new util.Clock();
  No3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'No3',
    text: '3',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  No2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'No2',
    text: '2',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  No1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'No1',
    text: '1',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Count3"
  Count3Clock = new util.Clock();
  Cross1Sec = new visual.TextStim({
    win: psychoJS.window,
    name: 'Cross1Sec',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "SimilarityPresentation"
  SimilarityPresentationClock = new util.Clock();
  simcount = 0;
  
  FirstSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  FirstSound.setVolume(1);
  SecondSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  SecondSound.setVolume(1);
  Cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'Cross',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  NumberOne = new visual.TextStim({
    win: psychoJS.window,
    name: 'NumberOne',
    text: 'Sound 1',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  NumberTwo = new visual.TextStim({
    win: psychoJS.window,
    name: 'NumberTwo',
    text: 'Sound 2',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  SimTrialNumber = new visual.TextStim({
    win: psychoJS.window,
    name: 'SimTrialNumber',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "SimlarityResponse"
  SimlarityResponseClock = new util.Clock();
  SimilarityRatingScale = new visual.TextStim({
    win: psychoJS.window,
    name: 'SimilarityRatingScale',
    text: '1 ----------------- 2 ----------------- 3 ----------------- 4 \nDifferent                                                   Same ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  SimilarityRatingKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "End1"
  End1Clock = new util.Clock();
  EndMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'EndMssg',
    text: 'Great job! This is the end of this component. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  End1Cont = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Welcome4"
  Welcome4Clock = new util.Clock();
  Task4Slide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Task4Slide', units : undefined, 
    image : 'Task 4.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.7, 0.9],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  Welcome4Continue = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Count3"
  Count3Clock = new util.Clock();
  Cross1Sec = new visual.TextStim({
    win: psychoJS.window,
    name: 'Cross1Sec',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "SoundLabeling"
  SoundLabelingClock = new util.Clock();
  SoundLabelQuestion = new visual.TextStim({
    win: psychoJS.window,
    name: 'SoundLabelQuestion',
    text: 'What is this sound?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Sound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  Sound.setVolume(1);
  LabelingKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "End1"
  End1Clock = new util.Clock();
  EndMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'EndMssg',
    text: 'Great job! This is the end of this component. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  End1Cont = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var Headphone;
var currentLoop;
function HeadphoneLoopBegin(HeadphoneLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  Headphone = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 0, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'Headphone_check.xlsx',
    seed: undefined, name: 'Headphone'
  });
  psychoJS.experiment.addLoop(Headphone); // add the loop to the experiment
  currentLoop = Headphone;  // we're now the current loop

  // Schedule all the trials in the trialList:
  Headphone.forEach(function() {
    const snapshot = Headphone.getSnapshot();

    HeadphoneLoopScheduler.add(importConditions(snapshot));
    HeadphoneLoopScheduler.add(HeadphonePlayRoutineBegin(snapshot));
    HeadphoneLoopScheduler.add(HeadphonePlayRoutineEachFrame(snapshot));
    HeadphoneLoopScheduler.add(HeadphonePlayRoutineEnd(snapshot));
    HeadphoneLoopScheduler.add(HeadphoneFeedbackRoutineBegin(snapshot));
    HeadphoneLoopScheduler.add(HeadphoneFeedbackRoutineEachFrame(snapshot));
    HeadphoneLoopScheduler.add(HeadphoneFeedbackRoutineEnd(snapshot));
    HeadphoneLoopScheduler.add(endLoopIteration(HeadphoneLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function HeadphoneLoopEnd() {
  psychoJS.experiment.removeLoop(Headphone);

  return Scheduler.Event.NEXT;
}


var WordTask;
function WordTaskLoopBegin(WordTaskLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  WordTask = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'WordTask'
  });
  psychoJS.experiment.addLoop(WordTask); // add the loop to the experiment
  currentLoop = WordTask;  // we're now the current loop

  // Schedule all the trials in the trialList:
  WordTask.forEach(function() {
    const snapshot = WordTask.getSnapshot();

    WordTaskLoopScheduler.add(importConditions(snapshot));
    WordTaskLoopScheduler.add(Welcome1RoutineBegin(snapshot));
    WordTaskLoopScheduler.add(Welcome1RoutineEachFrame(snapshot));
    WordTaskLoopScheduler.add(Welcome1RoutineEnd(snapshot));
    WordTaskLoopScheduler.add(PracticeBeginRoutineBegin(snapshot));
    WordTaskLoopScheduler.add(PracticeBeginRoutineEachFrame(snapshot));
    WordTaskLoopScheduler.add(PracticeBeginRoutineEnd(snapshot));
    const PracticeLoopLoopScheduler = new Scheduler(psychoJS);
    WordTaskLoopScheduler.add(PracticeLoopLoopBegin, PracticeLoopLoopScheduler);
    WordTaskLoopScheduler.add(PracticeLoopLoopScheduler);
    WordTaskLoopScheduler.add(PracticeLoopLoopEnd);
    WordTaskLoopScheduler.add(StartRoutineBegin(snapshot));
    WordTaskLoopScheduler.add(StartRoutineEachFrame(snapshot));
    WordTaskLoopScheduler.add(StartRoutineEnd(snapshot));
    WordTaskLoopScheduler.add(CountdownRoutineBegin(snapshot));
    WordTaskLoopScheduler.add(CountdownRoutineEachFrame(snapshot));
    WordTaskLoopScheduler.add(CountdownRoutineEnd(snapshot));
    const WordMSTLoopLoopScheduler = new Scheduler(psychoJS);
    WordTaskLoopScheduler.add(WordMSTLoopLoopBegin, WordMSTLoopLoopScheduler);
    WordTaskLoopScheduler.add(WordMSTLoopLoopScheduler);
    WordTaskLoopScheduler.add(WordMSTLoopLoopEnd);
    WordTaskLoopScheduler.add(endLoopIteration(WordTaskLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var PracticeLoop;
function PracticeLoopLoopBegin(PracticeLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  PracticeLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'WordMST_practicetrials.xlsx',
    seed: undefined, name: 'PracticeLoop'
  });
  psychoJS.experiment.addLoop(PracticeLoop); // add the loop to the experiment
  currentLoop = PracticeLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  PracticeLoop.forEach(function() {
    const snapshot = PracticeLoop.getSnapshot();

    PracticeLoopLoopScheduler.add(importConditions(snapshot));
    PracticeLoopLoopScheduler.add(Practice1RoutineBegin(snapshot));
    PracticeLoopLoopScheduler.add(Practice1RoutineEachFrame(snapshot));
    PracticeLoopLoopScheduler.add(Practice1RoutineEnd(snapshot));
    PracticeLoopLoopScheduler.add(PracticeFeedbackRoutineBegin(snapshot));
    PracticeLoopLoopScheduler.add(PracticeFeedbackRoutineEachFrame(snapshot));
    PracticeLoopLoopScheduler.add(PracticeFeedbackRoutineEnd(snapshot));
    PracticeLoopLoopScheduler.add(endLoopIteration(PracticeLoopLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function PracticeLoopLoopEnd() {
  psychoJS.experiment.removeLoop(PracticeLoop);

  return Scheduler.Event.NEXT;
}


var WordMSTLoop;
function WordMSTLoopLoopBegin(WordMSTLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  WordMSTLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'WordMST_trials.xlsx', '0:100'),
    seed: undefined, name: 'WordMSTLoop'
  });
  psychoJS.experiment.addLoop(WordMSTLoop); // add the loop to the experiment
  currentLoop = WordMSTLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  WordMSTLoop.forEach(function() {
    const snapshot = WordMSTLoop.getSnapshot();

    WordMSTLoopLoopScheduler.add(importConditions(snapshot));
    WordMSTLoopLoopScheduler.add(Count1RoutineBegin(snapshot));
    WordMSTLoopLoopScheduler.add(Count1RoutineEachFrame(snapshot));
    WordMSTLoopLoopScheduler.add(Count1RoutineEnd(snapshot));
    WordMSTLoopLoopScheduler.add(MSTWordRoutineBegin(snapshot));
    WordMSTLoopLoopScheduler.add(MSTWordRoutineEachFrame(snapshot));
    WordMSTLoopLoopScheduler.add(MSTWordRoutineEnd(snapshot));
    WordMSTLoopLoopScheduler.add(endLoopIteration(WordMSTLoopLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function WordMSTLoopLoopEnd() {
  psychoJS.experiment.removeLoop(WordMSTLoop);

  return Scheduler.Event.NEXT;
}


function WordTaskLoopEnd() {
  psychoJS.experiment.removeLoop(WordTask);

  return Scheduler.Event.NEXT;
}


var SoundTask;
function SoundTaskLoopBegin(SoundTaskLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  SoundTask = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'SoundTask'
  });
  psychoJS.experiment.addLoop(SoundTask); // add the loop to the experiment
  currentLoop = SoundTask;  // we're now the current loop

  // Schedule all the trials in the trialList:
  SoundTask.forEach(function() {
    const snapshot = SoundTask.getSnapshot();

    SoundTaskLoopScheduler.add(importConditions(snapshot));
    SoundTaskLoopScheduler.add(Welcome2_2RoutineBegin(snapshot));
    SoundTaskLoopScheduler.add(Welcome2_2RoutineEachFrame(snapshot));
    SoundTaskLoopScheduler.add(Welcome2_2RoutineEnd(snapshot));
    SoundTaskLoopScheduler.add(PracticeBeginRoutineBegin(snapshot));
    SoundTaskLoopScheduler.add(PracticeBeginRoutineEachFrame(snapshot));
    SoundTaskLoopScheduler.add(PracticeBeginRoutineEnd(snapshot));
    const SoundPracticeLoopLoopScheduler = new Scheduler(psychoJS);
    SoundTaskLoopScheduler.add(SoundPracticeLoopLoopBegin, SoundPracticeLoopLoopScheduler);
    SoundTaskLoopScheduler.add(SoundPracticeLoopLoopScheduler);
    SoundTaskLoopScheduler.add(SoundPracticeLoopLoopEnd);
    SoundTaskLoopScheduler.add(MSTSoundStartRoutineBegin(snapshot));
    SoundTaskLoopScheduler.add(MSTSoundStartRoutineEachFrame(snapshot));
    SoundTaskLoopScheduler.add(MSTSoundStartRoutineEnd(snapshot));
    SoundTaskLoopScheduler.add(CountdownRoutineBegin(snapshot));
    SoundTaskLoopScheduler.add(CountdownRoutineEachFrame(snapshot));
    SoundTaskLoopScheduler.add(CountdownRoutineEnd(snapshot));
    const MSTSoundLoopLoopScheduler = new Scheduler(psychoJS);
    SoundTaskLoopScheduler.add(MSTSoundLoopLoopBegin, MSTSoundLoopLoopScheduler);
    SoundTaskLoopScheduler.add(MSTSoundLoopLoopScheduler);
    SoundTaskLoopScheduler.add(MSTSoundLoopLoopEnd);
    SoundTaskLoopScheduler.add(endLoopIteration(SoundTaskLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var SoundPracticeLoop;
function SoundPracticeLoopLoopBegin(SoundPracticeLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  SoundPracticeLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'SoundMST_trials.xlsx', '0:5'),
    seed: undefined, name: 'SoundPracticeLoop'
  });
  psychoJS.experiment.addLoop(SoundPracticeLoop); // add the loop to the experiment
  currentLoop = SoundPracticeLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  SoundPracticeLoop.forEach(function() {
    const snapshot = SoundPracticeLoop.getSnapshot();

    SoundPracticeLoopLoopScheduler.add(importConditions(snapshot));
    SoundPracticeLoopLoopScheduler.add(SoundPracticeRoutineBegin(snapshot));
    SoundPracticeLoopLoopScheduler.add(SoundPracticeRoutineEachFrame(snapshot));
    SoundPracticeLoopLoopScheduler.add(SoundPracticeRoutineEnd(snapshot));
    SoundPracticeLoopLoopScheduler.add(SoundPracticeFeedbackRoutineBegin(snapshot));
    SoundPracticeLoopLoopScheduler.add(SoundPracticeFeedbackRoutineEachFrame(snapshot));
    SoundPracticeLoopLoopScheduler.add(SoundPracticeFeedbackRoutineEnd(snapshot));
    SoundPracticeLoopLoopScheduler.add(endLoopIteration(SoundPracticeLoopLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function SoundPracticeLoopLoopEnd() {
  psychoJS.experiment.removeLoop(SoundPracticeLoop);

  return Scheduler.Event.NEXT;
}


var MSTSoundLoop;
function MSTSoundLoopLoopBegin(MSTSoundLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  MSTSoundLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'SoundMST_trials.xlsx', '5:133'),
    seed: undefined, name: 'MSTSoundLoop'
  });
  psychoJS.experiment.addLoop(MSTSoundLoop); // add the loop to the experiment
  currentLoop = MSTSoundLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  MSTSoundLoop.forEach(function() {
    const snapshot = MSTSoundLoop.getSnapshot();

    MSTSoundLoopLoopScheduler.add(importConditions(snapshot));
    MSTSoundLoopLoopScheduler.add(Count2RoutineBegin(snapshot));
    MSTSoundLoopLoopScheduler.add(Count2RoutineEachFrame(snapshot));
    MSTSoundLoopLoopScheduler.add(Count2RoutineEnd(snapshot));
    MSTSoundLoopLoopScheduler.add(MSTSoundRoutineBegin(snapshot));
    MSTSoundLoopLoopScheduler.add(MSTSoundRoutineEachFrame(snapshot));
    MSTSoundLoopLoopScheduler.add(MSTSoundRoutineEnd(snapshot));
    MSTSoundLoopLoopScheduler.add(MSTSoundResponseRoutineBegin(snapshot));
    MSTSoundLoopLoopScheduler.add(MSTSoundResponseRoutineEachFrame(snapshot));
    MSTSoundLoopLoopScheduler.add(MSTSoundResponseRoutineEnd(snapshot));
    MSTSoundLoopLoopScheduler.add(endLoopIteration(MSTSoundLoopLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function MSTSoundLoopLoopEnd() {
  psychoJS.experiment.removeLoop(MSTSoundLoop);

  return Scheduler.Event.NEXT;
}


function SoundTaskLoopEnd() {
  psychoJS.experiment.removeLoop(SoundTask);

  return Scheduler.Event.NEXT;
}


var SimilarityRatingTask;
function SimilarityRatingTaskLoopBegin(SimilarityRatingTaskLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  SimilarityRatingTask = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'SimilarityRatingTask'
  });
  psychoJS.experiment.addLoop(SimilarityRatingTask); // add the loop to the experiment
  currentLoop = SimilarityRatingTask;  // we're now the current loop

  // Schedule all the trials in the trialList:
  SimilarityRatingTask.forEach(function() {
    const snapshot = SimilarityRatingTask.getSnapshot();

    SimilarityRatingTaskLoopScheduler.add(importConditions(snapshot));
    SimilarityRatingTaskLoopScheduler.add(Welcome3RoutineBegin(snapshot));
    SimilarityRatingTaskLoopScheduler.add(Welcome3RoutineEachFrame(snapshot));
    SimilarityRatingTaskLoopScheduler.add(Welcome3RoutineEnd(snapshot));
    SimilarityRatingTaskLoopScheduler.add(CountdownRoutineBegin(snapshot));
    SimilarityRatingTaskLoopScheduler.add(CountdownRoutineEachFrame(snapshot));
    SimilarityRatingTaskLoopScheduler.add(CountdownRoutineEnd(snapshot));
    const SimilarityRatingLoopLoopScheduler = new Scheduler(psychoJS);
    SimilarityRatingTaskLoopScheduler.add(SimilarityRatingLoopLoopBegin, SimilarityRatingLoopLoopScheduler);
    SimilarityRatingTaskLoopScheduler.add(SimilarityRatingLoopLoopScheduler);
    SimilarityRatingTaskLoopScheduler.add(SimilarityRatingLoopLoopEnd);
    SimilarityRatingTaskLoopScheduler.add(endLoopIteration(SimilarityRatingTaskLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var SimilarityRatingLoop;
function SimilarityRatingLoopLoopBegin(SimilarityRatingLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  SimilarityRatingLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Similarity_trials.xlsx', '0:83'),
    seed: undefined, name: 'SimilarityRatingLoop'
  });
  psychoJS.experiment.addLoop(SimilarityRatingLoop); // add the loop to the experiment
  currentLoop = SimilarityRatingLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  SimilarityRatingLoop.forEach(function() {
    const snapshot = SimilarityRatingLoop.getSnapshot();

    SimilarityRatingLoopLoopScheduler.add(importConditions(snapshot));
    SimilarityRatingLoopLoopScheduler.add(Count3RoutineBegin(snapshot));
    SimilarityRatingLoopLoopScheduler.add(Count3RoutineEachFrame(snapshot));
    SimilarityRatingLoopLoopScheduler.add(Count3RoutineEnd(snapshot));
    SimilarityRatingLoopLoopScheduler.add(SimilarityPresentationRoutineBegin(snapshot));
    SimilarityRatingLoopLoopScheduler.add(SimilarityPresentationRoutineEachFrame(snapshot));
    SimilarityRatingLoopLoopScheduler.add(SimilarityPresentationRoutineEnd(snapshot));
    SimilarityRatingLoopLoopScheduler.add(SimlarityResponseRoutineBegin(snapshot));
    SimilarityRatingLoopLoopScheduler.add(SimlarityResponseRoutineEachFrame(snapshot));
    SimilarityRatingLoopLoopScheduler.add(SimlarityResponseRoutineEnd(snapshot));
    SimilarityRatingLoopLoopScheduler.add(endLoopIteration(SimilarityRatingLoopLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function SimilarityRatingLoopLoopEnd() {
  psychoJS.experiment.removeLoop(SimilarityRatingLoop);

  return Scheduler.Event.NEXT;
}


function SimilarityRatingTaskLoopEnd() {
  psychoJS.experiment.removeLoop(SimilarityRatingTask);

  return Scheduler.Event.NEXT;
}


var LabelingTask;
function LabelingTaskLoopBegin(LabelingTaskLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  LabelingTask = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'LabelingTask'
  });
  psychoJS.experiment.addLoop(LabelingTask); // add the loop to the experiment
  currentLoop = LabelingTask;  // we're now the current loop

  // Schedule all the trials in the trialList:
  LabelingTask.forEach(function() {
    const snapshot = LabelingTask.getSnapshot();

    LabelingTaskLoopScheduler.add(importConditions(snapshot));
    LabelingTaskLoopScheduler.add(Welcome4RoutineBegin(snapshot));
    LabelingTaskLoopScheduler.add(Welcome4RoutineEachFrame(snapshot));
    LabelingTaskLoopScheduler.add(Welcome4RoutineEnd(snapshot));
    const SoundLabelLoopLoopScheduler = new Scheduler(psychoJS);
    LabelingTaskLoopScheduler.add(SoundLabelLoopLoopBegin, SoundLabelLoopLoopScheduler);
    LabelingTaskLoopScheduler.add(SoundLabelLoopLoopScheduler);
    LabelingTaskLoopScheduler.add(SoundLabelLoopLoopEnd);
    LabelingTaskLoopScheduler.add(endLoopIteration(LabelingTaskLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var SoundLabelLoop;
function SoundLabelLoopLoopBegin(SoundLabelLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  SoundLabelLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Similarity_trials.xlsx', '83:171'),
    seed: undefined, name: 'SoundLabelLoop'
  });
  psychoJS.experiment.addLoop(SoundLabelLoop); // add the loop to the experiment
  currentLoop = SoundLabelLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  SoundLabelLoop.forEach(function() {
    const snapshot = SoundLabelLoop.getSnapshot();

    SoundLabelLoopLoopScheduler.add(importConditions(snapshot));
    SoundLabelLoopLoopScheduler.add(Count3RoutineBegin(snapshot));
    SoundLabelLoopLoopScheduler.add(Count3RoutineEachFrame(snapshot));
    SoundLabelLoopLoopScheduler.add(Count3RoutineEnd(snapshot));
    SoundLabelLoopLoopScheduler.add(SoundLabelingRoutineBegin(snapshot));
    SoundLabelLoopLoopScheduler.add(SoundLabelingRoutineEachFrame(snapshot));
    SoundLabelLoopLoopScheduler.add(SoundLabelingRoutineEnd(snapshot));
    SoundLabelLoopLoopScheduler.add(endLoopIteration(SoundLabelLoopLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function SoundLabelLoopLoopEnd() {
  psychoJS.experiment.removeLoop(SoundLabelLoop);

  return Scheduler.Event.NEXT;
}


function LabelingTaskLoopEnd() {
  psychoJS.experiment.removeLoop(LabelingTask);

  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
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
    counter += 1;
    checkcount = (counter.toString() + "/6");
    
    CheckTrial.setText(checkcount);
    CheckResp.keys = undefined;
    CheckResp.rt = undefined;
    _CheckResp_allKeys = [];
    // keep track of which components have finished
    HeadphonePlayComponents = [];
    HeadphonePlayComponents.push(CheckSound);
    HeadphonePlayComponents.push(QuestionTxt);
    HeadphonePlayComponents.push(CheckTrial);
    HeadphonePlayComponents.push(CrossHeadphone);
    HeadphonePlayComponents.push(CheckResp);
    
    HeadphonePlayComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    if (t >= 0.0 && CheckSound.status === PsychoJS.Status.NOT_STARTED) {
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
    
    // *QuestionTxt* updates
    if (t >= (CheckSound.getDuration() + 0.5) && QuestionTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      QuestionTxt.tStart = t;  // (not accounting for frame time here)
      QuestionTxt.frameNStart = frameN;  // exact frame index
      
      QuestionTxt.setAutoDraw(true);
    }

    
    // *CheckTrial* updates
    if (t >= 0.0 && CheckTrial.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CheckTrial.tStart = t;  // (not accounting for frame time here)
      CheckTrial.frameNStart = frameN;  // exact frame index
      
      CheckTrial.setAutoDraw(true);
    }

    frameRemains = 0.0 + (CheckSound.getDuration() + 0.5) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((CheckTrial.status === PsychoJS.Status.STARTED || CheckTrial.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      CheckTrial.setAutoDraw(false);
    }
    
    // *CrossHeadphone* updates
    if (t >= 0.0 && CrossHeadphone.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CrossHeadphone.tStart = t;  // (not accounting for frame time here)
      CrossHeadphone.frameNStart = frameN;  // exact frame index
      
      CrossHeadphone.setAutoDraw(true);
    }

    frameRemains = 0.0 + (CheckSound.getDuration() + 0.5) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((CrossHeadphone.status === PsychoJS.Status.STARTED || CrossHeadphone.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      CrossHeadphone.setAutoDraw(false);
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
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    HeadphonePlayComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    HeadphonePlayComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    CheckSound.stop();  // ensure sound has stopped at end of routine
    if ((CheckResp.corr === 1)) {
        message = "CORRECT";
    } else {
        message = "INCORRECT";
    }
    
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
    FeedbackTxt.setText(message);
    // keep track of which components have finished
    HeadphoneFeedbackComponents = [];
    HeadphoneFeedbackComponents.push(FeedbackTxt);
    
    HeadphoneFeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    // *FeedbackTxt* updates
    if (t >= 0.0 && FeedbackTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FeedbackTxt.tStart = t;  // (not accounting for frame time here)
      FeedbackTxt.frameNStart = frameN;  // exact frame index
      
      FeedbackTxt.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((FeedbackTxt.status === PsychoJS.Status.STARTED || FeedbackTxt.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      FeedbackTxt.setAutoDraw(false);
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
    HeadphoneFeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    HeadphoneFeedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _Welcome1Continue_allKeys;
var Welcome1Components;
function Welcome1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Welcome1'-------
    t = 0;
    Welcome1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Welcome1Continue.keys = undefined;
    Welcome1Continue.rt = undefined;
    _Welcome1Continue_allKeys = [];
    // keep track of which components have finished
    Welcome1Components = [];
    Welcome1Components.push(Welcome1Continue);
    Welcome1Components.push(Task1Slide);
    
    Welcome1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Welcome1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Welcome1'-------
    // get current time
    t = Welcome1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Welcome1Continue* updates
    if (t >= 0.0 && Welcome1Continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Welcome1Continue.tStart = t;  // (not accounting for frame time here)
      Welcome1Continue.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Welcome1Continue.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Welcome1Continue.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Welcome1Continue.clearEvents(); });
    }

    if (Welcome1Continue.status === PsychoJS.Status.STARTED) {
      let theseKeys = Welcome1Continue.getKeys({keyList: ['space'], waitRelease: false});
      _Welcome1Continue_allKeys = _Welcome1Continue_allKeys.concat(theseKeys);
      if (_Welcome1Continue_allKeys.length > 0) {
        Welcome1Continue.keys = _Welcome1Continue_allKeys[_Welcome1Continue_allKeys.length - 1].name;  // just the last key pressed
        Welcome1Continue.rt = _Welcome1Continue_allKeys[_Welcome1Continue_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Task1Slide* updates
    if (t >= 0.0 && Task1Slide.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Task1Slide.tStart = t;  // (not accounting for frame time here)
      Task1Slide.frameNStart = frameN;  // exact frame index
      
      Task1Slide.setAutoDraw(true);
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
    Welcome1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Welcome1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Welcome1'-------
    Welcome1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Welcome1Continue.keys', Welcome1Continue.keys);
    if (typeof Welcome1Continue.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Welcome1Continue.rt', Welcome1Continue.rt);
        routineTimer.reset();
        }
    
    Welcome1Continue.stop();
    // the Routine "Welcome1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _WelcomeContinueKey2_allKeys;
var PracticeBeginComponents;
function PracticeBeginRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'PracticeBegin'-------
    t = 0;
    PracticeBeginClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    WelcomeContinueKey2.keys = undefined;
    WelcomeContinueKey2.rt = undefined;
    _WelcomeContinueKey2_allKeys = [];
    // keep track of which components have finished
    PracticeBeginComponents = [];
    PracticeBeginComponents.push(WelcomeContinueKey2);
    PracticeBeginComponents.push(PracticeText2);
    
    PracticeBeginComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PracticeBeginRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'PracticeBegin'-------
    // get current time
    t = PracticeBeginClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *WelcomeContinueKey2* updates
    if (t >= 0.0 && WelcomeContinueKey2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WelcomeContinueKey2.tStart = t;  // (not accounting for frame time here)
      WelcomeContinueKey2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { WelcomeContinueKey2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { WelcomeContinueKey2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { WelcomeContinueKey2.clearEvents(); });
    }

    if (WelcomeContinueKey2.status === PsychoJS.Status.STARTED) {
      let theseKeys = WelcomeContinueKey2.getKeys({keyList: ['space'], waitRelease: false});
      _WelcomeContinueKey2_allKeys = _WelcomeContinueKey2_allKeys.concat(theseKeys);
      if (_WelcomeContinueKey2_allKeys.length > 0) {
        WelcomeContinueKey2.keys = _WelcomeContinueKey2_allKeys[_WelcomeContinueKey2_allKeys.length - 1].name;  // just the last key pressed
        WelcomeContinueKey2.rt = _WelcomeContinueKey2_allKeys[_WelcomeContinueKey2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *PracticeText2* updates
    if (t >= 0.0 && PracticeText2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeText2.tStart = t;  // (not accounting for frame time here)
      PracticeText2.frameNStart = frameN;  // exact frame index
      
      PracticeText2.setAutoDraw(true);
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
    PracticeBeginComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracticeBeginRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'PracticeBegin'-------
    PracticeBeginComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('WelcomeContinueKey2.keys', WelcomeContinueKey2.keys);
    if (typeof WelcomeContinueKey2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('WelcomeContinueKey2.rt', WelcomeContinueKey2.rt);
        routineTimer.reset();
        }
    
    WelcomeContinueKey2.stop();
    // the Routine "PracticeBegin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var WTrialCount;
var _PracticeRespKey2_allKeys;
var Practice1Components;
function Practice1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Practice1'-------
    t = 0;
    Practice1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    WTcount += 1;
    WTrialCount = ("Trial " + WTcount.toString());
    
    TrialNumber.setText(WTrialCount);
    PracticeSound = new sound.Sound({
    win: psychoJS.window,
    value: SoundFile,
    secs: -1,
    });
    PracticeSound.setVolume(1);
    PracticeRespKey2.keys = undefined;
    PracticeRespKey2.rt = undefined;
    _PracticeRespKey2_allKeys = [];
    // keep track of which components have finished
    Practice1Components = [];
    Practice1Components.push(TrialNumber);
    Practice1Components.push(PracticeSound);
    Practice1Components.push(PracticeCross);
    Practice1Components.push(PracticeRespKey2);
    
    Practice1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Practice1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Practice1'-------
    // get current time
    t = Practice1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *TrialNumber* updates
    if (t >= 0.0 && TrialNumber.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrialNumber.tStart = t;  // (not accounting for frame time here)
      TrialNumber.frameNStart = frameN;  // exact frame index
      
      TrialNumber.setAutoDraw(true);
    }

    // start/stop PracticeSound
    if (t >= 0.0 && PracticeSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeSound.tStart = t;  // (not accounting for frame time here)
      PracticeSound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ PracticeSound.play(); });  // screen flip
      PracticeSound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (PracticeSound.getDuration() + PracticeSound.tStart)     && PracticeSound.status === PsychoJS.Status.STARTED) {
      PracticeSound.stop();  // stop the sound (if longer than duration)
      PracticeSound.status = PsychoJS.Status.FINISHED;
    }
    
    // *PracticeCross* updates
    if (t >= 0.0 && PracticeCross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeCross.tStart = t;  // (not accounting for frame time here)
      PracticeCross.frameNStart = frameN;  // exact frame index
      
      PracticeCross.setAutoDraw(true);
    }

    
    // *PracticeRespKey2* updates
    if (t >= 0.0 && PracticeRespKey2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeRespKey2.tStart = t;  // (not accounting for frame time here)
      PracticeRespKey2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { PracticeRespKey2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { PracticeRespKey2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { PracticeRespKey2.clearEvents(); });
    }

    if (PracticeRespKey2.status === PsychoJS.Status.STARTED) {
      let theseKeys = PracticeRespKey2.getKeys({keyList: ['space'], waitRelease: false});
      _PracticeRespKey2_allKeys = _PracticeRespKey2_allKeys.concat(theseKeys);
      if (_PracticeRespKey2_allKeys.length > 0) {
        PracticeRespKey2.keys = _PracticeRespKey2_allKeys[_PracticeRespKey2_allKeys.length - 1].name;  // just the last key pressed
        PracticeRespKey2.rt = _PracticeRespKey2_allKeys[_PracticeRespKey2_allKeys.length - 1].rt;
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
    Practice1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Practice1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Practice1'-------
    Practice1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    PracticeSound.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('PracticeRespKey2.keys', PracticeRespKey2.keys);
    if (typeof PracticeRespKey2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('PracticeRespKey2.rt', PracticeRespKey2.rt);
        routineTimer.reset();
        }
    
    PracticeRespKey2.stop();
    // the Routine "Practice1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Practice_resp_allKeys;
var PracticeFeedbackComponents;
function PracticeFeedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'PracticeFeedback'-------
    t = 0;
    PracticeFeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    if ((Type === "NEW")) {
        message = "This is a NEW word. \nThis is your first time hearing this word.";
    } else {
        if ((Type === "SIMILAR")) {
            message = "This is a NEW word. \nNote that this one sounds similar to the previous word but is not exactly the same.";
        } else {
            if ((Type === "OLD")) {
                message = "This is an OLD word. \nThis word is exactly the same as the first word.";
            }
        }
    }
    
    Practice_resp.keys = undefined;
    Practice_resp.rt = undefined;
    _Practice_resp_allKeys = [];
    PracticeMssg.setText(message);
    // keep track of which components have finished
    PracticeFeedbackComponents = [];
    PracticeFeedbackComponents.push(Practice_resp);
    PracticeFeedbackComponents.push(PracticeMssg);
    PracticeFeedbackComponents.push(FeedbackCross);
    
    PracticeFeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PracticeFeedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'PracticeFeedback'-------
    // get current time
    t = PracticeFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Practice_resp* updates
    if (t >= 0.0 && Practice_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Practice_resp.tStart = t;  // (not accounting for frame time here)
      Practice_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Practice_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Practice_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Practice_resp.clearEvents(); });
    }

    if (Practice_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Practice_resp.getKeys({keyList: ['space'], waitRelease: false});
      _Practice_resp_allKeys = _Practice_resp_allKeys.concat(theseKeys);
      if (_Practice_resp_allKeys.length > 0) {
        Practice_resp.keys = _Practice_resp_allKeys[_Practice_resp_allKeys.length - 1].name;  // just the last key pressed
        Practice_resp.rt = _Practice_resp_allKeys[_Practice_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *PracticeMssg* updates
    if (t >= 0.0 && PracticeMssg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeMssg.tStart = t;  // (not accounting for frame time here)
      PracticeMssg.frameNStart = frameN;  // exact frame index
      
      PracticeMssg.setAutoDraw(true);
    }

    
    // *FeedbackCross* updates
    if (t >= 0.0 && FeedbackCross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FeedbackCross.tStart = t;  // (not accounting for frame time here)
      FeedbackCross.frameNStart = frameN;  // exact frame index
      
      FeedbackCross.setAutoDraw(true);
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
    PracticeFeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var feedback;
function PracticeFeedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'PracticeFeedback'-------
    PracticeFeedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if ((Practice_resp.corr === 1)) {
        feedback = "CORRECT";
    } else {
        feedback = "INCORRECT";
    }
    
    psychoJS.experiment.addData('Practice_resp.keys', Practice_resp.keys);
    if (typeof Practice_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Practice_resp.rt', Practice_resp.rt);
        routineTimer.reset();
        }
    
    Practice_resp.stop();
    // the Routine "PracticeFeedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _StartKey_allKeys;
var StartComponents;
function StartRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Start'-------
    t = 0;
    StartClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    StartKey.keys = undefined;
    StartKey.rt = undefined;
    _StartKey_allKeys = [];
    // keep track of which components have finished
    StartComponents = [];
    StartComponents.push(StartTxt);
    StartComponents.push(StartKey);
    
    StartComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function StartRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Start'-------
    // get current time
    t = StartClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *StartTxt* updates
    if (t >= 0.0 && StartTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StartTxt.tStart = t;  // (not accounting for frame time here)
      StartTxt.frameNStart = frameN;  // exact frame index
      
      StartTxt.setAutoDraw(true);
    }

    
    // *StartKey* updates
    if (t >= 0.0 && StartKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StartKey.tStart = t;  // (not accounting for frame time here)
      StartKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { StartKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { StartKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { StartKey.clearEvents(); });
    }

    if (StartKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = StartKey.getKeys({keyList: ['space'], waitRelease: false});
      _StartKey_allKeys = _StartKey_allKeys.concat(theseKeys);
      if (_StartKey_allKeys.length > 0) {
        StartKey.keys = _StartKey_allKeys[_StartKey_allKeys.length - 1].name;  // just the last key pressed
        StartKey.rt = _StartKey_allKeys[_StartKey_allKeys.length - 1].rt;
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
    StartComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var count;
var condition;
var c;
function StartRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Start'-------
    StartComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('StartKey.keys', StartKey.keys);
    if (typeof StartKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('StartKey.rt', StartKey.rt);
        routineTimer.reset();
        }
    
    StartKey.stop();
    count = 0
    condition = "0:100";
    c = Math.floor(Math.random() * 6);
    if ((c === 0)) {
        condition = "0:100";
    } else {
        if ((c === 1)) {
            condition = "100:200";
        } else {
            if ((c === 2)) {
                condition = "200:300";
            } else {
                if ((c === 3)) {
                    condition = "300:400";
                } else {
                    if ((c === 4)) {
                        condition = "400:500";
                    } else {
                        if ((c === 5)) {
                            condition = "500:600";
                        }
                    }
                }
            }
        }
    }
    
    // the Routine "Start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var CountdownComponents;
function CountdownRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Countdown'-------
    t = 0;
    CountdownClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    CountdownComponents = [];
    CountdownComponents.push(No3);
    CountdownComponents.push(No2);
    CountdownComponents.push(No1);
    
    CountdownComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function CountdownRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Countdown'-------
    // get current time
    t = CountdownClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *No3* updates
    if (t >= 0.0 && No3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      No3.tStart = t;  // (not accounting for frame time here)
      No3.frameNStart = frameN;  // exact frame index
      
      No3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((No3.status === PsychoJS.Status.STARTED || No3.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      No3.setAutoDraw(false);
    }
    
    // *No2* updates
    if (t >= 1 && No2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      No2.tStart = t;  // (not accounting for frame time here)
      No2.frameNStart = frameN;  // exact frame index
      
      No2.setAutoDraw(true);
    }

    frameRemains = 1 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((No2.status === PsychoJS.Status.STARTED || No2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      No2.setAutoDraw(false);
    }
    
    // *No1* updates
    if (t >= 2 && No1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      No1.tStart = t;  // (not accounting for frame time here)
      No1.frameNStart = frameN;  // exact frame index
      
      No1.setAutoDraw(true);
    }

    frameRemains = 2 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((No1.status === PsychoJS.Status.STARTED || No1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      No1.setAutoDraw(false);
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
    CountdownComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function CountdownRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Countdown'-------
    CountdownComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var number;
var Count1Components;
function Count1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Count1'-------
    t = 0;
    Count1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    count += 1;
    number = (count.toString() + "/100");
    
    // keep track of which components have finished
    Count1Components = [];
    Count1Components.push(no_3);
    
    Count1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Count1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Count1'-------
    // get current time
    t = Count1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *no_3* updates
    if (t >= 0.0 && no_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no_3.tStart = t;  // (not accounting for frame time here)
      no_3.frameNStart = frameN;  // exact frame index
      
      no_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((no_3.status === PsychoJS.Status.STARTED || no_3.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      no_3.setAutoDraw(false);
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
    Count1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Count1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Count1'-------
    Count1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _MST_resp_allKeys;
var MSTWordComponents;
function MSTWordRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'MSTWord'-------
    t = 0;
    MSTWordClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    TargetSound = new sound.Sound({
    win: psychoJS.window,
    value: File,
    secs: -1,
    });
    TargetSound.setVolume(1);
    ItemNumber.setText(number);
    MST_resp.keys = undefined;
    MST_resp.rt = undefined;
    _MST_resp_allKeys = [];
    // keep track of which components have finished
    MSTWordComponents = [];
    MSTWordComponents.push(TargetSound);
    MSTWordComponents.push(ItemNumber);
    MSTWordComponents.push(MST_resp);
    MSTWordComponents.push(Option2);
    
    MSTWordComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function MSTWordRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'MSTWord'-------
    // get current time
    t = MSTWordClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop TargetSound
    if (t >= 0.0 && TargetSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TargetSound.tStart = t;  // (not accounting for frame time here)
      TargetSound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ TargetSound.play(); });  // screen flip
      TargetSound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (TargetSound.getDuration() + TargetSound.tStart)     && TargetSound.status === PsychoJS.Status.STARTED) {
      TargetSound.stop();  // stop the sound (if longer than duration)
      TargetSound.status = PsychoJS.Status.FINISHED;
    }
    
    // *ItemNumber* updates
    if (t >= 0.0 && ItemNumber.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ItemNumber.tStart = t;  // (not accounting for frame time here)
      ItemNumber.frameNStart = frameN;  // exact frame index
      
      ItemNumber.setAutoDraw(true);
    }

    
    // *MST_resp* updates
    if (t >= 1 && MST_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MST_resp.tStart = t;  // (not accounting for frame time here)
      MST_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { MST_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { MST_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { MST_resp.clearEvents(); });
    }

    if (MST_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = MST_resp.getKeys({keyList: ['1', '2'], waitRelease: false});
      _MST_resp_allKeys = _MST_resp_allKeys.concat(theseKeys);
      if (_MST_resp_allKeys.length > 0) {
        MST_resp.keys = _MST_resp_allKeys[_MST_resp_allKeys.length - 1].name;  // just the last key pressed
        MST_resp.rt = _MST_resp_allKeys[_MST_resp_allKeys.length - 1].rt;
        // was this correct?
        if (MST_resp.keys == WordCorrect) {
            MST_resp.corr = 1;
        } else {
            MST_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Option2* updates
    if (t >= 0.0 && Option2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Option2.tStart = t;  // (not accounting for frame time here)
      Option2.frameNStart = frameN;  // exact frame index
      
      Option2.setAutoDraw(true);
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
    MSTWordComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function MSTWordRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'MSTWord'-------
    MSTWordComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    TargetSound.stop();  // ensure sound has stopped at end of routine
    // was no response the correct answer?!
    if (MST_resp.keys === undefined) {
      if (['None','none',undefined].includes(WordCorrect)) {
         MST_resp.corr = 1;  // correct non-response
      } else {
         MST_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('MST_resp.keys', MST_resp.keys);
    psychoJS.experiment.addData('MST_resp.corr', MST_resp.corr);
    if (typeof MST_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('MST_resp.rt', MST_resp.rt);
        routineTimer.reset();
        }
    
    MST_resp.stop();
    // the Routine "MSTWord" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _End1Cont_allKeys;
var End1Components;
function End1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'End1'-------
    t = 0;
    End1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    End1Cont.keys = undefined;
    End1Cont.rt = undefined;
    _End1Cont_allKeys = [];
    // keep track of which components have finished
    End1Components = [];
    End1Components.push(EndMssg);
    End1Components.push(End1Cont);
    
    End1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function End1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'End1'-------
    // get current time
    t = End1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *EndMssg* updates
    if (t >= 0.0 && EndMssg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EndMssg.tStart = t;  // (not accounting for frame time here)
      EndMssg.frameNStart = frameN;  // exact frame index
      
      EndMssg.setAutoDraw(true);
    }

    
    // *End1Cont* updates
    if (t >= 0.0 && End1Cont.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      End1Cont.tStart = t;  // (not accounting for frame time here)
      End1Cont.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { End1Cont.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { End1Cont.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { End1Cont.clearEvents(); });
    }

    if (End1Cont.status === PsychoJS.Status.STARTED) {
      let theseKeys = End1Cont.getKeys({keyList: ['space'], waitRelease: false});
      _End1Cont_allKeys = _End1Cont_allKeys.concat(theseKeys);
      if (_End1Cont_allKeys.length > 0) {
        End1Cont.keys = _End1Cont_allKeys[_End1Cont_allKeys.length - 1].name;  // just the last key pressed
        End1Cont.rt = _End1Cont_allKeys[_End1Cont_allKeys.length - 1].rt;
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
    End1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function End1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'End1'-------
    End1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('End1Cont.keys', End1Cont.keys);
    if (typeof End1Cont.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('End1Cont.rt', End1Cont.rt);
        routineTimer.reset();
        }
    
    End1Cont.stop();
    // the Routine "End1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Welcome2Continue_allKeys;
var Welcome2_2Components;
function Welcome2_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Welcome2_2'-------
    t = 0;
    Welcome2_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Welcome2Continue.keys = undefined;
    Welcome2Continue.rt = undefined;
    _Welcome2Continue_allKeys = [];
    // keep track of which components have finished
    Welcome2_2Components = [];
    Welcome2_2Components.push(Welcome2Continue);
    Welcome2_2Components.push(Task2Slide);
    
    Welcome2_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Welcome2_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Welcome2_2'-------
    // get current time
    t = Welcome2_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Welcome2Continue* updates
    if (t >= 0.0 && Welcome2Continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Welcome2Continue.tStart = t;  // (not accounting for frame time here)
      Welcome2Continue.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Welcome2Continue.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Welcome2Continue.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Welcome2Continue.clearEvents(); });
    }

    if (Welcome2Continue.status === PsychoJS.Status.STARTED) {
      let theseKeys = Welcome2Continue.getKeys({keyList: ['space'], waitRelease: false});
      _Welcome2Continue_allKeys = _Welcome2Continue_allKeys.concat(theseKeys);
      if (_Welcome2Continue_allKeys.length > 0) {
        Welcome2Continue.keys = _Welcome2Continue_allKeys[_Welcome2Continue_allKeys.length - 1].name;  // just the last key pressed
        Welcome2Continue.rt = _Welcome2Continue_allKeys[_Welcome2Continue_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Task2Slide* updates
    if (t >= 0.0 && Task2Slide.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Task2Slide.tStart = t;  // (not accounting for frame time here)
      Task2Slide.frameNStart = frameN;  // exact frame index
      
      Task2Slide.setAutoDraw(true);
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
    Welcome2_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Welcome2_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Welcome2_2'-------
    Welcome2_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Welcome2Continue.keys', Welcome2Continue.keys);
    if (typeof Welcome2Continue.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Welcome2Continue.rt', Welcome2Continue.rt);
        routineTimer.reset();
        }
    
    Welcome2Continue.stop();
    // the Routine "Welcome2_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var TrialCount;
var _PracticeRespKey2II_allKeys;
var SoundPracticeComponents;
function SoundPracticeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SoundPractice'-------
    t = 0;
    SoundPracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Tcount += 1;
    TrialCount = ("Trial " + Tcount.toString());
    
    PracticeSound2 = new sound.Sound({
    win: psychoJS.window,
    value: SoundMST_File,
    secs: -1,
    });
    PracticeSound2.setVolume(1);
    PracticeTrialNo.setText(TrialCount);
    PracticeRespKey2II.keys = undefined;
    PracticeRespKey2II.rt = undefined;
    _PracticeRespKey2II_allKeys = [];
    // keep track of which components have finished
    SoundPracticeComponents = [];
    SoundPracticeComponents.push(PracticeSound2);
    SoundPracticeComponents.push(PracticeCrossW);
    SoundPracticeComponents.push(PracticeTrialNo);
    SoundPracticeComponents.push(PracticeRespKey2II);
    
    SoundPracticeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SoundPracticeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SoundPractice'-------
    // get current time
    t = SoundPracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop PracticeSound2
    if (t >= 0.0 && PracticeSound2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeSound2.tStart = t;  // (not accounting for frame time here)
      PracticeSound2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ PracticeSound2.play(); });  // screen flip
      PracticeSound2.status = PsychoJS.Status.STARTED;
    }
    if (t >= (PracticeSound2.getDuration() + PracticeSound2.tStart)     && PracticeSound2.status === PsychoJS.Status.STARTED) {
      PracticeSound2.stop();  // stop the sound (if longer than duration)
      PracticeSound2.status = PsychoJS.Status.FINISHED;
    }
    
    // *PracticeCrossW* updates
    if (t >= 0.0 && PracticeCrossW.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeCrossW.tStart = t;  // (not accounting for frame time here)
      PracticeCrossW.frameNStart = frameN;  // exact frame index
      
      PracticeCrossW.setAutoDraw(true);
    }

    
    // *PracticeTrialNo* updates
    if (t >= 0.0 && PracticeTrialNo.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeTrialNo.tStart = t;  // (not accounting for frame time here)
      PracticeTrialNo.frameNStart = frameN;  // exact frame index
      
      PracticeTrialNo.setAutoDraw(true);
    }

    
    // *PracticeRespKey2II* updates
    if (t >= 0.0 && PracticeRespKey2II.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeRespKey2II.tStart = t;  // (not accounting for frame time here)
      PracticeRespKey2II.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { PracticeRespKey2II.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { PracticeRespKey2II.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { PracticeRespKey2II.clearEvents(); });
    }

    if (PracticeRespKey2II.status === PsychoJS.Status.STARTED) {
      let theseKeys = PracticeRespKey2II.getKeys({keyList: ['space'], waitRelease: false});
      _PracticeRespKey2II_allKeys = _PracticeRespKey2II_allKeys.concat(theseKeys);
      if (_PracticeRespKey2II_allKeys.length > 0) {
        PracticeRespKey2II.keys = _PracticeRespKey2II_allKeys[_PracticeRespKey2II_allKeys.length - 1].name;  // just the last key pressed
        PracticeRespKey2II.rt = _PracticeRespKey2II_allKeys[_PracticeRespKey2II_allKeys.length - 1].rt;
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
    SoundPracticeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SoundPracticeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SoundPractice'-------
    SoundPracticeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    PracticeSound2.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('PracticeRespKey2II.keys', PracticeRespKey2II.keys);
    if (typeof PracticeRespKey2II.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('PracticeRespKey2II.rt', PracticeRespKey2II.rt);
        routineTimer.reset();
        }
    
    PracticeRespKey2II.stop();
    // the Routine "SoundPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _PracticeSoundKey_allKeys;
var SoundPracticeFeedbackComponents;
function SoundPracticeFeedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SoundPracticeFeedback'-------
    t = 0;
    SoundPracticeFeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    if ((SoundType === "NEW")) {
        message = "This is a NEW sound. \nThis is your first time hearing this sound.";
    } else {
        if ((SoundType === "SIMILAR")) {
            message = "This is a NEW sound. \nNote that this one sounds similar to the previous sound but is not exactly the same.";
        } else {
            if ((SoundType === "OLD")) {
                message = "This is an OLD sound. \nThis sound is exactly the same as the first sound.";
            }
        }
    }
    
    Message.setText(message);
    PracticeSoundKey.keys = undefined;
    PracticeSoundKey.rt = undefined;
    _PracticeSoundKey_allKeys = [];
    // keep track of which components have finished
    SoundPracticeFeedbackComponents = [];
    SoundPracticeFeedbackComponents.push(Message);
    SoundPracticeFeedbackComponents.push(PracticeCrossW2);
    SoundPracticeFeedbackComponents.push(PracticeSoundKey);
    
    SoundPracticeFeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SoundPracticeFeedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SoundPracticeFeedback'-------
    // get current time
    t = SoundPracticeFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Message* updates
    if (t >= 0.0 && Message.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Message.tStart = t;  // (not accounting for frame time here)
      Message.frameNStart = frameN;  // exact frame index
      
      Message.setAutoDraw(true);
    }

    
    // *PracticeCrossW2* updates
    if (t >= 0.0 && PracticeCrossW2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeCrossW2.tStart = t;  // (not accounting for frame time here)
      PracticeCrossW2.frameNStart = frameN;  // exact frame index
      
      PracticeCrossW2.setAutoDraw(true);
    }

    
    // *PracticeSoundKey* updates
    if (t >= 0.0 && PracticeSoundKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeSoundKey.tStart = t;  // (not accounting for frame time here)
      PracticeSoundKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { PracticeSoundKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { PracticeSoundKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { PracticeSoundKey.clearEvents(); });
    }

    if (PracticeSoundKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = PracticeSoundKey.getKeys({keyList: ['space'], waitRelease: false});
      _PracticeSoundKey_allKeys = _PracticeSoundKey_allKeys.concat(theseKeys);
      if (_PracticeSoundKey_allKeys.length > 0) {
        PracticeSoundKey.keys = _PracticeSoundKey_allKeys[_PracticeSoundKey_allKeys.length - 1].name;  // just the last key pressed
        PracticeSoundKey.rt = _PracticeSoundKey_allKeys[_PracticeSoundKey_allKeys.length - 1].rt;
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
    SoundPracticeFeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SoundPracticeFeedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SoundPracticeFeedback'-------
    SoundPracticeFeedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if ((PracticeSoundKey.corr === 1)) {
        feedback = "CORRECT";
    } else {
        feedback = "INCORRECT";
    }
    
    psychoJS.experiment.addData('PracticeSoundKey.keys', PracticeSoundKey.keys);
    if (typeof PracticeSoundKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('PracticeSoundKey.rt', PracticeSoundKey.rt);
        routineTimer.reset();
        }
    
    PracticeSoundKey.stop();
    // the Routine "SoundPracticeFeedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _MSTSoundStrtKey_allKeys;
var MSTSoundStartComponents;
function MSTSoundStartRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'MSTSoundStart'-------
    t = 0;
    MSTSoundStartClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    MSTSoundStrtKey.keys = undefined;
    MSTSoundStrtKey.rt = undefined;
    _MSTSoundStrtKey_allKeys = [];
    // keep track of which components have finished
    MSTSoundStartComponents = [];
    MSTSoundStartComponents.push(MSTSoundStrtMssg);
    MSTSoundStartComponents.push(MSTSoundStrtKey);
    
    MSTSoundStartComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function MSTSoundStartRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'MSTSoundStart'-------
    // get current time
    t = MSTSoundStartClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *MSTSoundStrtMssg* updates
    if (t >= 0.0 && MSTSoundStrtMssg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MSTSoundStrtMssg.tStart = t;  // (not accounting for frame time here)
      MSTSoundStrtMssg.frameNStart = frameN;  // exact frame index
      
      MSTSoundStrtMssg.setAutoDraw(true);
    }

    
    // *MSTSoundStrtKey* updates
    if (t >= 0.0 && MSTSoundStrtKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MSTSoundStrtKey.tStart = t;  // (not accounting for frame time here)
      MSTSoundStrtKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { MSTSoundStrtKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { MSTSoundStrtKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { MSTSoundStrtKey.clearEvents(); });
    }

    if (MSTSoundStrtKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = MSTSoundStrtKey.getKeys({keyList: ['space'], waitRelease: false});
      _MSTSoundStrtKey_allKeys = _MSTSoundStrtKey_allKeys.concat(theseKeys);
      if (_MSTSoundStrtKey_allKeys.length > 0) {
        MSTSoundStrtKey.keys = _MSTSoundStrtKey_allKeys[_MSTSoundStrtKey_allKeys.length - 1].name;  // just the last key pressed
        MSTSoundStrtKey.rt = _MSTSoundStrtKey_allKeys[_MSTSoundStrtKey_allKeys.length - 1].rt;
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
    MSTSoundStartComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var rows;
var s;
function MSTSoundStartRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'MSTSoundStart'-------
    MSTSoundStartComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    count = 0
    rows = "5:133";
    s = Math.floor(Math.random() * 1);
    if ((s === 0)) {
        rows = "5:133";
    } else {
        if ((s === 1)) {
            rows = "133:261";
        } else {
            if ((s === 2)) {
                rows = "261:389";
            } else {
                if ((s === 3)) {
                    rows = "389:517";
                } else {
                    if ((s === 4)) {
                        rows = "517:645";
                    } else {
                        if ((s === 5)) {
                            rows = "645:773";
                        }
                    }
                }
            }
        }
    }
    
    psychoJS.experiment.addData('MSTSoundStrtKey.keys', MSTSoundStrtKey.keys);
    if (typeof MSTSoundStrtKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('MSTSoundStrtKey.rt', MSTSoundStrtKey.rt);
        routineTimer.reset();
        }
    
    MSTSoundStrtKey.stop();
    // the Routine "MSTSoundStart" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var NoSoundOn;
var Count2Components;
function Count2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Count2'-------
    t = 0;
    Count2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    count += 1;
    number = (count.toString() + "/128");
    NoSoundOn = 0;
    if (((count === 45) || (count === 82))) {
        NoSoundOn = 1;
    } else {
        NoSoundOn = 0;
    }
    
    // keep track of which components have finished
    Count2Components = [];
    Count2Components.push(no2);
    
    Count2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Count2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Count2'-------
    // get current time
    t = Count2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *no2* updates
    if (t >= 0.0 && no2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no2.tStart = t;  // (not accounting for frame time here)
      no2.frameNStart = frameN;  // exact frame index
      
      no2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((no2.status === PsychoJS.Status.STARTED || no2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      no2.setAutoDraw(false);
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
    Count2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Count2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Count2'-------
    Count2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var MSTSoundComponents;
function MSTSoundRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'MSTSound'-------
    t = 0;
    MSTSoundClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    MSTSoundCount.setText(number);
    MSTSoundPlay = new sound.Sound({
    win: psychoJS.window,
    value: SoundMST_File,
    secs: -1,
    });
    MSTSoundPlay.setVolume(1);
    // keep track of which components have finished
    MSTSoundComponents = [];
    MSTSoundComponents.push(MSTSoundCount);
    MSTSoundComponents.push(MSTSoundPlay);
    MSTSoundComponents.push(MSTSoundCross);
    
    MSTSoundComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function MSTSoundRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'MSTSound'-------
    // get current time
    t = MSTSoundClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *MSTSoundCount* updates
    if (t >= 0.0 && MSTSoundCount.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MSTSoundCount.tStart = t;  // (not accounting for frame time here)
      MSTSoundCount.frameNStart = frameN;  // exact frame index
      
      MSTSoundCount.setAutoDraw(true);
    }

    frameRemains = 0.0 + (MSTSoundPlay.getDuration() + 0.5) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((MSTSoundCount.status === PsychoJS.Status.STARTED || MSTSoundCount.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      MSTSoundCount.setAutoDraw(false);
    }
    // start/stop MSTSoundPlay
    if (t >= 0.0 && MSTSoundPlay.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MSTSoundPlay.tStart = t;  // (not accounting for frame time here)
      MSTSoundPlay.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ MSTSoundPlay.play(); });  // screen flip
      MSTSoundPlay.status = PsychoJS.Status.STARTED;
    }
    if (t >= (MSTSoundPlay.getDuration() + MSTSoundPlay.tStart)     && MSTSoundPlay.status === PsychoJS.Status.STARTED) {
      MSTSoundPlay.stop();  // stop the sound (if longer than duration)
      MSTSoundPlay.status = PsychoJS.Status.FINISHED;
    }
    
    // *MSTSoundCross* updates
    if (t >= 0.0 && MSTSoundCross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MSTSoundCross.tStart = t;  // (not accounting for frame time here)
      MSTSoundCross.frameNStart = frameN;  // exact frame index
      
      MSTSoundCross.setAutoDraw(true);
    }

    frameRemains = 0.0 + (MSTSoundPlay.getDuration() + 0.5) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((MSTSoundCross.status === PsychoJS.Status.STARTED || MSTSoundCross.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      MSTSoundCross.setAutoDraw(false);
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
    MSTSoundComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function MSTSoundRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'MSTSound'-------
    MSTSoundComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    MSTSoundPlay.stop();  // ensure sound has stopped at end of routine
    // the Routine "MSTSound" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _MSTSoundKey_allKeys;
var MSTSoundResponseComponents;
function MSTSoundResponseRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'MSTSoundResponse'-------
    t = 0;
    MSTSoundResponseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    MSTSoundKey.keys = undefined;
    MSTSoundKey.rt = undefined;
    _MSTSoundKey_allKeys = [];
    //MSTSoundOptions.setAlignHoriz('left');
    //MSTSoundNote.setAlignHoriz('left');
    // keep track of which components have finished
    MSTSoundResponseComponents = [];
    MSTSoundResponseComponents.push(MSTSoundKey);
    MSTSoundResponseComponents.push(Options2II);
    
    MSTSoundResponseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function MSTSoundResponseRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'MSTSoundResponse'-------
    // get current time
    t = MSTSoundResponseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *MSTSoundKey* updates
    if (t >= 0.0 && MSTSoundKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MSTSoundKey.tStart = t;  // (not accounting for frame time here)
      MSTSoundKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { MSTSoundKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { MSTSoundKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { MSTSoundKey.clearEvents(); });
    }

    if (MSTSoundKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = MSTSoundKey.getKeys({keyList: ['1', '2'], waitRelease: false});
      _MSTSoundKey_allKeys = _MSTSoundKey_allKeys.concat(theseKeys);
      if (_MSTSoundKey_allKeys.length > 0) {
        MSTSoundKey.keys = _MSTSoundKey_allKeys[_MSTSoundKey_allKeys.length - 1].name;  // just the last key pressed
        MSTSoundKey.rt = _MSTSoundKey_allKeys[_MSTSoundKey_allKeys.length - 1].rt;
        // was this correct?
        if (MSTSoundKey.keys == SoundCorrect) {
            MSTSoundKey.corr = 1;
        } else {
            MSTSoundKey.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Options2II* updates
    if (t >= 0.0 && Options2II.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Options2II.tStart = t;  // (not accounting for frame time here)
      Options2II.frameNStart = frameN;  // exact frame index
      
      Options2II.setAutoDraw(true);
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
    MSTSoundResponseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function MSTSoundResponseRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'MSTSoundResponse'-------
    MSTSoundResponseComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (MSTSoundKey.keys === undefined) {
      if (['None','none',undefined].includes(SoundCorrect)) {
         MSTSoundKey.corr = 1;  // correct non-response
      } else {
         MSTSoundKey.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('MSTSoundKey.keys', MSTSoundKey.keys);
    psychoJS.experiment.addData('MSTSoundKey.corr', MSTSoundKey.corr);
    if (typeof MSTSoundKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('MSTSoundKey.rt', MSTSoundKey.rt);
        routineTimer.reset();
        }
    
    MSTSoundKey.stop();
    // the Routine "MSTSoundResponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Welcome3Continue_allKeys;
var Welcome3Components;
function Welcome3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Welcome3'-------
    t = 0;
    Welcome3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Welcome3Continue.keys = undefined;
    Welcome3Continue.rt = undefined;
    _Welcome3Continue_allKeys = [];
    // keep track of which components have finished
    Welcome3Components = [];
    Welcome3Components.push(Task3Slide);
    Welcome3Components.push(Welcome3Continue);
    
    Welcome3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Welcome3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Welcome3'-------
    // get current time
    t = Welcome3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Task3Slide* updates
    if (t >= 0.0 && Task3Slide.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Task3Slide.tStart = t;  // (not accounting for frame time here)
      Task3Slide.frameNStart = frameN;  // exact frame index
      
      Task3Slide.setAutoDraw(true);
    }

    
    // *Welcome3Continue* updates
    if (t >= 0.0 && Welcome3Continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Welcome3Continue.tStart = t;  // (not accounting for frame time here)
      Welcome3Continue.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Welcome3Continue.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Welcome3Continue.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Welcome3Continue.clearEvents(); });
    }

    if (Welcome3Continue.status === PsychoJS.Status.STARTED) {
      let theseKeys = Welcome3Continue.getKeys({keyList: ['space'], waitRelease: false});
      _Welcome3Continue_allKeys = _Welcome3Continue_allKeys.concat(theseKeys);
      if (_Welcome3Continue_allKeys.length > 0) {
        Welcome3Continue.keys = _Welcome3Continue_allKeys[_Welcome3Continue_allKeys.length - 1].name;  // just the last key pressed
        Welcome3Continue.rt = _Welcome3Continue_allKeys[_Welcome3Continue_allKeys.length - 1].rt;
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
    Welcome3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Welcome3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Welcome3'-------
    Welcome3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Welcome3Continue.keys', Welcome3Continue.keys);
    if (typeof Welcome3Continue.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Welcome3Continue.rt', Welcome3Continue.rt);
        routineTimer.reset();
        }
    
    Welcome3Continue.stop();
    // the Routine "Welcome3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Count3Components;
function Count3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Count3'-------
    t = 0;
    Count3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    Count3Components = [];
    Count3Components.push(Cross1Sec);
    
    Count3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Count3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Count3'-------
    // get current time
    t = Count3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Cross1Sec* updates
    if (t >= 0 && Cross1Sec.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Cross1Sec.tStart = t;  // (not accounting for frame time here)
      Cross1Sec.frameNStart = frameN;  // exact frame index
      
      Cross1Sec.setAutoDraw(true);
    }

    frameRemains = 0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Cross1Sec.status === PsychoJS.Status.STARTED || Cross1Sec.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      Cross1Sec.setAutoDraw(false);
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
    Count3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Count3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Count3'-------
    Count3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var simcounter;
var SimilarityPresentationComponents;
function SimilarityPresentationRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SimilarityPresentation'-------
    t = 0;
    SimilarityPresentationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    simcount += 1;
    simcounter = (simcount.toString() + "/83");
    
    FirstSound = new sound.Sound({
    win: psychoJS.window,
    value: Sound1,
    secs: -1,
    });
    FirstSound.setVolume(1);
    SecondSound = new sound.Sound({
    win: psychoJS.window,
    value: Sound2,
    secs: -1,
    });
    SecondSound.setVolume(1);
    SimTrialNumber.setText(simcounter);
    // keep track of which components have finished
    SimilarityPresentationComponents = [];
    SimilarityPresentationComponents.push(FirstSound);
    SimilarityPresentationComponents.push(SecondSound);
    SimilarityPresentationComponents.push(Cross);
    SimilarityPresentationComponents.push(NumberOne);
    SimilarityPresentationComponents.push(NumberTwo);
    SimilarityPresentationComponents.push(SimTrialNumber);
    
    SimilarityPresentationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SimilarityPresentationRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SimilarityPresentation'-------
    // get current time
    t = SimilarityPresentationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop FirstSound
    if (t >= 0.0 && FirstSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FirstSound.tStart = t;  // (not accounting for frame time here)
      FirstSound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ FirstSound.play(); });  // screen flip
      FirstSound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (FirstSound.getDuration() + FirstSound.tStart)     && FirstSound.status === PsychoJS.Status.STARTED) {
      FirstSound.stop();  // stop the sound (if longer than duration)
      FirstSound.status = PsychoJS.Status.FINISHED;
    }
    // start/stop SecondSound
    if (t >= (FirstSound.getDuration() + 1.0) && SecondSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SecondSound.tStart = t;  // (not accounting for frame time here)
      SecondSound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ SecondSound.play(); });  // screen flip
      SecondSound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (SecondSound.getDuration() + SecondSound.tStart)     && SecondSound.status === PsychoJS.Status.STARTED) {
      SecondSound.stop();  // stop the sound (if longer than duration)
      SecondSound.status = PsychoJS.Status.FINISHED;
    }
    
    // *Cross* updates
    if (t >= FirstSound.getDuration() && Cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Cross.tStart = t;  // (not accounting for frame time here)
      Cross.frameNStart = frameN;  // exact frame index
      
      Cross.setAutoDraw(true);
    }

    frameRemains = FirstSound.getDuration() + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Cross.status === PsychoJS.Status.STARTED || Cross.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      Cross.setAutoDraw(false);
    }
    
    // *NumberOne* updates
    if (t >= 0.0 && NumberOne.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NumberOne.tStart = t;  // (not accounting for frame time here)
      NumberOne.frameNStart = frameN;  // exact frame index
      
      NumberOne.setAutoDraw(true);
    }

    frameRemains = 0.0 + FirstSound.getDuration() - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((NumberOne.status === PsychoJS.Status.STARTED || NumberOne.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      NumberOne.setAutoDraw(false);
    }
    
    // *NumberTwo* updates
    if (t >= (FirstSound.getDuration() + 1.0) && NumberTwo.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NumberTwo.tStart = t;  // (not accounting for frame time here)
      NumberTwo.frameNStart = frameN;  // exact frame index
      
      NumberTwo.setAutoDraw(true);
    }

    frameRemains = (FirstSound.getDuration() + 1.0) + SecondSound.getDuration() - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((NumberTwo.status === PsychoJS.Status.STARTED || NumberTwo.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      NumberTwo.setAutoDraw(false);
    }
    
    // *SimTrialNumber* updates
    if (t >= 0.0 && SimTrialNumber.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SimTrialNumber.tStart = t;  // (not accounting for frame time here)
      SimTrialNumber.frameNStart = frameN;  // exact frame index
      
      SimTrialNumber.setAutoDraw(true);
    }

    frameRemains = 0.0 + ((FirstSound.getDuration() + 1) + SecondSound.getDuration()) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((SimTrialNumber.status === PsychoJS.Status.STARTED || SimTrialNumber.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      SimTrialNumber.setAutoDraw(false);
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
    SimilarityPresentationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SimilarityPresentationRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SimilarityPresentation'-------
    SimilarityPresentationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    FirstSound.stop();  // ensure sound has stopped at end of routine
    SecondSound.stop();  // ensure sound has stopped at end of routine
    // the Routine "SimilarityPresentation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _SimilarityRatingKey_allKeys;
var SimlarityResponseComponents;
function SimlarityResponseRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SimlarityResponse'-------
    t = 0;
    SimlarityResponseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    SimilarityRatingKey.keys = undefined;
    SimilarityRatingKey.rt = undefined;
    _SimilarityRatingKey_allKeys = [];
    // keep track of which components have finished
    SimlarityResponseComponents = [];
    SimlarityResponseComponents.push(SimilarityRatingScale);
    SimlarityResponseComponents.push(SimilarityRatingKey);
    
    SimlarityResponseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SimlarityResponseRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SimlarityResponse'-------
    // get current time
    t = SimlarityResponseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *SimilarityRatingScale* updates
    if (t >= 0.0 && SimilarityRatingScale.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SimilarityRatingScale.tStart = t;  // (not accounting for frame time here)
      SimilarityRatingScale.frameNStart = frameN;  // exact frame index
      
      SimilarityRatingScale.setAutoDraw(true);
    }

    
    // *SimilarityRatingKey* updates
    if (t >= 0.0 && SimilarityRatingKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SimilarityRatingKey.tStart = t;  // (not accounting for frame time here)
      SimilarityRatingKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { SimilarityRatingKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { SimilarityRatingKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { SimilarityRatingKey.clearEvents(); });
    }

    if (SimilarityRatingKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = SimilarityRatingKey.getKeys({keyList: ['1', '2', '3', '4'], waitRelease: false});
      _SimilarityRatingKey_allKeys = _SimilarityRatingKey_allKeys.concat(theseKeys);
      if (_SimilarityRatingKey_allKeys.length > 0) {
        SimilarityRatingKey.keys = _SimilarityRatingKey_allKeys[_SimilarityRatingKey_allKeys.length - 1].name;  // just the last key pressed
        SimilarityRatingKey.rt = _SimilarityRatingKey_allKeys[_SimilarityRatingKey_allKeys.length - 1].rt;
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
    SimlarityResponseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SimlarityResponseRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SimlarityResponse'-------
    SimlarityResponseComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SimilarityRatingKey.keys', SimilarityRatingKey.keys);
    if (typeof SimilarityRatingKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('SimilarityRatingKey.rt', SimilarityRatingKey.rt);
        routineTimer.reset();
        }
    
    SimilarityRatingKey.stop();
    // the Routine "SimlarityResponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _Welcome4Continue_allKeys;
var Welcome4Components;
function Welcome4RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Welcome4'-------
    t = 0;
    Welcome4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Welcome4Continue.keys = undefined;
    Welcome4Continue.rt = undefined;
    _Welcome4Continue_allKeys = [];
    // keep track of which components have finished
    Welcome4Components = [];
    Welcome4Components.push(Task4Slide);
    Welcome4Components.push(Welcome4Continue);
    
    Welcome4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Welcome4RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Welcome4'-------
    // get current time
    t = Welcome4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Task4Slide* updates
    if (t >= 0.0 && Task4Slide.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Task4Slide.tStart = t;  // (not accounting for frame time here)
      Task4Slide.frameNStart = frameN;  // exact frame index
      
      Task4Slide.setAutoDraw(true);
    }

    
    // *Welcome4Continue* updates
    if (t >= 0.0 && Welcome4Continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Welcome4Continue.tStart = t;  // (not accounting for frame time here)
      Welcome4Continue.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Welcome4Continue.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Welcome4Continue.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Welcome4Continue.clearEvents(); });
    }

    if (Welcome4Continue.status === PsychoJS.Status.STARTED) {
      let theseKeys = Welcome4Continue.getKeys({keyList: ['space'], waitRelease: false});
      _Welcome4Continue_allKeys = _Welcome4Continue_allKeys.concat(theseKeys);
      if (_Welcome4Continue_allKeys.length > 0) {
        Welcome4Continue.keys = _Welcome4Continue_allKeys[_Welcome4Continue_allKeys.length - 1].name;  // just the last key pressed
        Welcome4Continue.rt = _Welcome4Continue_allKeys[_Welcome4Continue_allKeys.length - 1].rt;
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
    Welcome4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Welcome4RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Welcome4'-------
    Welcome4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Welcome4Continue.keys', Welcome4Continue.keys);
    if (typeof Welcome4Continue.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Welcome4Continue.rt', Welcome4Continue.rt);
        routineTimer.reset();
        }
    
    Welcome4Continue.stop();
    // the Routine "Welcome4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _LabelingKey_allKeys;
var SoundLabelingComponents;
function SoundLabelingRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SoundLabeling'-------
    t = 0;
    SoundLabelingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Sound = new sound.Sound({
    win: psychoJS.window,
    value: Sound1,
    secs: -1,
    });
    Sound.setVolume(1);
    LabelingKey.keys = undefined;
    LabelingKey.rt = undefined;
    _LabelingKey_allKeys = [];
    // keep track of which components have finished
    SoundLabelingComponents = [];
    SoundLabelingComponents.push(SoundLabelQuestion);
    SoundLabelingComponents.push(Sound);
    SoundLabelingComponents.push(LabelingKey);
    
    SoundLabelingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SoundLabelingRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SoundLabeling'-------
    // get current time
    t = SoundLabelingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *SoundLabelQuestion* updates
    if (t >= 0.0 && SoundLabelQuestion.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SoundLabelQuestion.tStart = t;  // (not accounting for frame time here)
      SoundLabelQuestion.frameNStart = frameN;  // exact frame index
      
      SoundLabelQuestion.setAutoDraw(true);
    }

    // start/stop Sound
    if (t >= 0.5 && Sound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Sound.tStart = t;  // (not accounting for frame time here)
      Sound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ Sound.play(); });  // screen flip
      Sound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (Sound.getDuration() + Sound.tStart)     && Sound.status === PsychoJS.Status.STARTED) {
      Sound.stop();  // stop the sound (if longer than duration)
      Sound.status = PsychoJS.Status.FINISHED;
    }
    
    // *LabelingKey* updates
    if (t >= 0.0 && LabelingKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LabelingKey.tStart = t;  // (not accounting for frame time here)
      LabelingKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { LabelingKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { LabelingKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { LabelingKey.clearEvents(); });
    }

    if (LabelingKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = LabelingKey.getKeys({keyList: ['space'], waitRelease: false});
      _LabelingKey_allKeys = _LabelingKey_allKeys.concat(theseKeys);
      if (_LabelingKey_allKeys.length > 0) {
        LabelingKey.keys = _LabelingKey_allKeys[_LabelingKey_allKeys.length - 1].name;  // just the last key pressed
        LabelingKey.rt = _LabelingKey_allKeys[_LabelingKey_allKeys.length - 1].rt;
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
    SoundLabelingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SoundLabelingRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SoundLabeling'-------
    SoundLabelingComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    Sound.stop();  // ensure sound has stopped at end of routine
    psychoJS.experiment.addData('LabelingKey.keys', LabelingKey.keys);
    if (typeof LabelingKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('LabelingKey.rt', LabelingKey.rt);
        routineTimer.reset();
        }
    
    LabelingKey.stop();
    // the Routine "SoundLabeling" was not non-slip safe, so reset the non-slip timer
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
