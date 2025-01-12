

#		python code
#		script_name: Summer Song
#
#		author: Michael Delgado
#		description: Summer Song - Three Minutes
#

from earsketch import *
from random import *
init()
setTempo(120)

beatcollection = []
sectionCrandom1 = []
sectionCrandom2 = []
sectionCrandom3 = []
question = readInput("What type of BEATS do you want? Choose: Electro or Rock").lower()
question2 = readInput("What type of RANDOM MUSIC do you want? Choose: Electro or Rock").lower()
print("Loading [" +question+ "] beats and [" + question2 + "] random music... This may take a little while!")

# QUESTION_1
if question == "electro":
    beatcollection.extend([RD_ELECTRO_MAINBEAT_1,RD_EDM_MAINBEAT_4,RD_ELECTRO_MAINBEAT_10,RD_EDM_DRUMBEATPART_2])
    clap = OS_CLAP01
elif question == "rock":
    beatcollection.extend([RD_ROCK_POPRHYTHM_MAINDRUMS_1,RD_ROCK_POPRHYTHM_DRUM_PART_22,RD_ROCK_POPRHYTHM_DRUM_PART_21,RD_ROCK_POPRHYTHM_DRUM_PART_4])
    clap = OS_CLAP04
else:
    print("I don't know what [" +question+ "] is, we'll give you the funny. (It sounds bad...)")
    beatcollection.extend([OS_CLAP01,OS_CLAP04,OS_COWBELL01,OS_OPENHAT02])
    clap = OS_CLAP02
  
# QUESTION_2  
if question2 == "electro":
    sectionCrandom1.extend([ELECTRO_ANALOGUE_SPACELEAD_004,ELECTRO_ANALOGUE_SPACELEAD_001,ELECTRO_ANALOGUE_SPACELEAD_003])
    sectionCrandom2.extend([ELECTRO_DRUM_MAIN_BEAT_003,ELECTRO_DRUM_MAIN_BEAT_011,ELECTRO_DRUM_MAIN_BEAT_005,ELECTRO_DRUM_MAIN_BEAT_007])
    sectionCrandom3.extend([ELECTRO_ANALOGUE_BASS_005,ELECTRO_ANALOGUE_BASS_010,ELECTRO_ANALOGUE_BASS_001,ELECTRO_ANALOGUE_BASS_012])
elif question2 == "rock":
    sectionCrandom1.extend([RD_ROCK_POPELECTRICLEAD_1,RD_ROCK_POPELECTRICLEAD_3,RD_ROCK_POPELECTRICLEAD_2,RD_ROCK_POPELECTRICLEAD_4])
    sectionCrandom2.extend([RD_ROCK_POPRHYTHM_MAINDRUMS_1,RD_ROCK_POPRHYTHM_MAINDRUMS_4,RD_ROCK_POPRHYTHM_MAINDRUMS_11,RD_ROCK_POPRHYTHM_MAINDRUMS_12])
    sectionCrandom3.extend([RD_ROCK_POPELECTRICBASS_2,RD_ROCK_POPELECTRICBASS_3,RD_ROCK_POPELECTRICBASS_11,RD_ROCK_POPELECTRICBASS_16])
else:
    print("I don't know what " +question2+ " is... We'll give you hiphop instead.")
    sectionCrandom1.extend([HIPHOP_FUNKLEAD_001,HIPHOP_SOLOMOOGLEAD_001,HIPHOP_SYNTHPLUCKLEAD_005,HIPHOP_SYNTH_LEAD_002])
    sectionCrandom2.extend([HIPHOP_STOMP_BEAT_002,HIPHOP_STOMP_BEAT_004,HIPHOP_STOMP_BEAT_006,HIPHOP_STOMP_BEAT_010])
    sectionCrandom3.extend([HIPHOP_BASSSUB_002,HIPHOP_SYNTHBASS_004,HIPHOP_BASSSUB_007,HIPHOP_BASSSUB_003])

introbeat = "0+--0+--0+--0+--0+--0+"
firstbeat = "021+-20+12-1+122+--11+0+2++2+-"
wooh = "0++-0++-"
sectionA2_1beat = "0++000+0++000-"
sectionBrise = "0+++++++"
sectionCbeat1 = "013+12+03-"
sectionCbeat2 = "132+212+013+-"
sectionCbeatotal = sectionCbeat1 + sectionCbeat2
sectionDbeat1 = "1+313+0+2+21-"
sectionDbeat2 = "021+323+123-"
sectionDbeattotal = sectionDbeat1 + sectionDbeat2
clapsectionD = "-00-000-00-"
sectionEbeat = "0+12+312+00+111"
secondrandombeat = "01+000+1121+310"

#workspace
def volume():
    setEffect(1,VOLUME,GAIN,-60,1,3,5)
    setEffect(2,VOLUME,GAIN,-60,1,3,5)
    setEffect(3,VOLUME,GAIN,-60,1,3,5)
    setEffect(4,VOLUME,GAIN,-60,1,3,5)
    setEffect(3,VOLUME,GAIN,0,30,-60,32)
    setEffect(2,VOLUME,GAIN,0,30,-60,32)
    setEffect(4,VOLUME,GAIN,0,30,-60,32)
    setEffect(1,VOLUME,GAIN,0,30,-60,32)
    setEffect(3,VOLUME,GAIN,-60,32.5,-7.5,33)
    setEffect(2,VOLUME,GAIN,-60,32.5,-7.5,33)
    setEffect(4,VOLUME,GAIN,-60,32.5,-7.5,33)
    setEffect(1,VOLUME,GAIN,0,32,-7.5,32.5)
    setEffect(1,VOLUME,GAIN,-60,32.5,-7.5,33)
    setEffect(1,VOLUME,GAIN,-7.5,55,-60,56)
    setEffect(2,VOLUME,GAIN,-7.5,55,-60,56)
    setEffect(5,VOLUME,GAIN,-7.5,55,-60,56)
    setEffect(1,VOLUME,GAIN,-60,57,-5,57)
    setEffect(2,VOLUME,GAIN,-60,57,-7.5,57)
    setEffect(5,VOLUME,GAIN,-60,57,-7.5,57)
    setEffect(1,VOLUME,GAIN,-7.5,79,-60,80)
    setEffect(1,VOLUME,GAIN,-60,80,-7.5,80)
    setEffect(2,VOLUME,GAIN,-7.5,79,-60,80)
    setEffect(2,VOLUME,GAIN,-60,80,-7.5,80)
    setEffect(3,VOLUME,GAIN,-7.5,79,-60,80)
    setEffect(3,VOLUME,GAIN,-60,80,-7.5,80)
    setEffect(4,VOLUME,GAIN,-7.5,79,-60,80)
    setEffect(4,VOLUME,GAIN,-60,80,-7.5,80)
volume()

def intro(startMeasure,endMeasure,smloop,emloop,countby,risestart,riseend,dropstart,dropend):
    fitMedia(ELECTRO_ANALOGUE_LEAD_001,2,startMeasure,endMeasure)
    fitMedia(ELECTRO_DRUM_MAIN_BEAT_002,3,startMeasure,endMeasure + 2)
    fitMedia(ELECTRO_STARLEAD_003,4,startMeasure,endMeasure + 3)
    for measure in range(smloop,emloop,countby):
        makeBeat(OS_CLAP04,1,measure,introbeat)
    fitMedia(RD_ELECTRO_SFX_SYNTHRISE_1,1,risestart,riseend)
    fitMedia(ELECTRO_ANALOGUE_BASS_006,2,dropstart,dropend)

def sectionA(startMeasure,endMeasure,smloop,emloop):
    fitMedia(RD_ELECTRO_EDGYLEAD_1,2,startMeasure,endMeasure + 4)
    for measure in range(smloop,emloop,2):
        makeBeat(beatcollection,1,measure,firstbeat)

def sectionA2(startMeasure,endMeasure,vocalsmloop,vocalemloop,vocalcbloop):
    fitMedia(ELECTRO_DRUM_MAIN_BEAT_012,3,startMeasure,endMeasure + 12)
    fitMedia(YG_GOSPEL_CYMBAL_1,5,startMeasure + 4,endMeasure + 0.8)
    fitMedia(RD_ROCK_POPLEADSTRUM_GUITAR_5,4,startMeasure + 5,endMeasure + 4)
    for measure in range(vocalsmloop,vocalemloop):
        makeBeat(HIPHOP_VOCALHIT_002,1,measure,wooh)
    for measure2 in range(vocalsmloop + 4, vocalemloop + 8):
        makeBeat(clap,1,measure2,sectionA2_1beat)

def sectionB(startMeasure,endMeasure,smloop,emloop,cbloop):
    fitMedia(ELECTRO_ANALOGUE_LEAD_003,4,startMeasure,endMeasure)
    fitMedia(RD_ELECTRO_MAINBEAT_2,2,startMeasure,endMeasure + 4)
    fitMedia(ELECTRO_ANALOGUE_BASS_006,5,startMeasure + 7,endMeasure + 4)
    fitMedia(Y05_CYMBAL_SWELL_1,1,startMeasure + 8,endMeasure + 4.5)
    for measure in range(smloop,emloop,cbloop):
        makeBeat(ELECTRO_ANALOGUE_LEAD_003,1,measure,sectionBrise)

#sectionC
for measure in range(33,45):
    fitMedia(sectionCrandom1[randint(0,len(sectionCrandom1)-1)],1,measure,measure + 1)
    fitMedia(sectionCrandom2[randint(0,len(sectionCrandom2)-1)],2,measure,measure + 1)
    fitMedia(sectionCrandom3[randint(0,len(sectionCrandom3)-1)],3,measure,measure + 1)
for beats in range(33,46,2):
    makeBeat(beatcollection,4,beats,sectionCbeatotal)
    
def sectionD(startMeasure,endMeasure):
    fitMedia(CIARA_MELANIN_DRUMBEAT_1,1,startMeasure,endMeasure)
    fitMedia(CIARA_MELANIN_THEME_TUBA_1,2,startMeasure,endMeasure)
    fitMedia(ELECTRO_SFX_WHITENOISE_SCATTER_001,3,startMeasure + 10, endMeasure + 0.55)
    for measure in range(46,55,2):
        makeBeat(beatcollection,5,measure,sectionDbeattotal)
        makeBeat(clap,3,measure,clapsectionD)
        
def sectionE(startMeasure,endMeasure):
    fitMedia(HIPHOP_VOCALHIT_002,1,startMeasure + 1,endMeasure - 10.75)
    fitMedia(HIPHOP_VOCALHIT_002,1,startMeasure + 12,endMeasure  + 0.25)
    fitMedia(HIPHOP_VOCALHIT_003,1,startMeasure + 1.5,endMeasure)
    fitMedia(COMMON_LOVE_DRUMBEAT_1,2,startMeasure + 1.5,endMeasure)
    fitMedia(RD_ROCK_POPLEADSTRUM_GUITAR_5,3,startMeasure + 1.5,endMeasure)
    for measure in range(startMeasure + 1,endMeasure):
        makeBeat(beatcollection,4,measure,sectionEbeat)
        
for measure in range(69,80):
    fitMedia(sectionCrandom1[randint(0,len(sectionCrandom1)-1)],1,measure,measure + 1)
    fitMedia(sectionCrandom2[randint(0,len(sectionCrandom2)-1)],2,measure,measure + 1)
    fitMedia(sectionCrandom3[randint(0,len(sectionCrandom3)-1)],3,measure,measure + 1)
for beats in range(69,80):
    makeBeat(beatcollection,4,beats,secondrandombeat)
fitMedia(ELECTRO_SFX_WHITENOISE_SCATTER_002,5,79,80)
    
intro(1,9,1,8,2,8.5,10.5,10,11)
sectionA(12,20,12,16)
sectionA2(16,20,16,20,2)
sectionB(24,28,28,32,1)
sectionD(45,56)
sectionE(56,68)
intro(80,88,80,87,2,88,90,89,90)
finish()
