### For preprocessing data files from BL study Sessions 1 and 2 (Aug 11, 2021) ###
import csv
import BL_functions as BL_functions
import pandas as pd

### Use the below line if running multiple subjects at a time
subjectlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
### Get a list of files that need to be analyzed from the 'data' folder
# filelist = [BL_functions.create_filelist(1, i) for i in subjectlist] # Enter session number (1, 2) and subject ID (or subject list)
subj = 34
filelist = BL_functions.create_filelist(2, subj)
print(subj)
for file in filelist:
    if file.session == 1:
        # sound, type, corr = file.smst_process()
        word, type, corr, trialn = file.wmst_process()
        #word = word[6:]
        sim_type = ["na"]*len(word)
        occurrence = ["na"]*len(word)
        tai = 1
        na = 1
        mo = 1
        rai = 1
        li = 1

        for i in range(len(sim_type)):
            if type[i] == "SIMILAR":
                if "TAI" in word[i]:
                    sim_type[i] = "taigisa"
                    occurrence[i] = tai
                    tai += 1
                elif "WAI" in word[i]:
                    sim_type[i] = "nawaivu"
                    occurrence[i] = na
                    na += 1
                elif "DAY" in word[i]:
                    sim_type[i] = "mopuday"
                    occurrence[i] = mo
                    mo += 1
                elif "RAI" in word[i]:
                    sim_type[i] = "raizofu"
                    occurrence[i] = rai
                    rai += 1
                elif "KAY" in word[i]:
                    sim_type[i] = "likayba"
                    occurrence[i] = li
                    li += 1

        corr.insert(0, file.subject)
        sim_type.insert(0, file.subject)
        occurrence.insert(0, file.subject)

        
        with open ('Analysis/wmst_responses.csv', 'a', newline="") as f:
            writer = csv.writer(f)
            # writer.writerow(sim_type)
            # writer.writerow(occurrence)
            writer.writerow(word)
        # wmst = file.wmst_process()
        # smst = file.smst_process()
        # wmst += smst
        # wmst.insert(0, file.subject)
        # with open('Analysis/mstdata.csv', 'a', newline="") as f:
        #     writer = csv.writer(f)
        #     writer.writerow(wmst)
        # sound1, sound2, similarity = file.get_similarity()
        # similarity.insert(0, file.subject)
        # with open('Analysis/similaritydata.csv', 'a', newline="") as f:
        #     writer = csv.writer(f)
        #     writer.writerow(similarity)
        # soundnames, labels = file.get_labels()
        # labels.insert(0, file.subject)
        # with open('Analysis/labels.csv', 'a', newline="") as f:
        #     writer = csv.writer(f)
        #     #writer.writerow(soundnames)
        #     writer.writerow(labels)
        pass
    elif file.session == 2:
        # sl = file.sl_process()
        # with open('Analysis/sldata.csv', 'a', newline="") as f:
        #     writer = csv.writer(f)
        #     writer.writerow(sl)
        rt = file.sl_RT()
        rt.to_csv('Analysis/RTs_test2.csv', mode='a', header=False, index=False) # Write raw RT
        #L_functions.get_positionwise(pd.read_csv('Analysis/rawRT.csv')) # Average RT per position
        pass

# Get false alarm rate
# df = pd.read_csv('Analysis/sldata.csv')
# df = df[20:21]
# BL_functions.get_falsealarm(df)


