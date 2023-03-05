import csv
import glob
import os
import pandas as pd
from pandas.io.parsers import read_csv
### Import functions to analyze the MST tasks
import sys
sys.path.append('c:\\Users\\wangs\\OneDrive - The University of Western Ontario\\Desktop\\ProjectBL\\Archive\\CombinedMST\\Analysis\\')
import cMST_analysis as mst
### Import functions needed to analyze RT, false alarm rate, familiarity, and AFC accuracy rate
sys.path.append('c:\\Users\\wangs\\OneDrive - The University of Western Ontario\\Desktop\\ProjectBL\\Archive\\SL alone_ver2\\Analysis\\')
import modifiedSLanalysis as sl
### Import functions for getting similarity ratings (currently only getting ratings for similar sounds) and sound labels 
sys.path.append('c:\\Users\\wangs\\OneDrive - The University of Western Ontario\\Desktop\\ProjectBL\\Archive\\SoundSimilarity\\Analysis\\')
import SoundSimilarity_analysis as similarity

#####################################
### Prepare classes and functions ###
#####################################
class File:
    def __init__(self, subject, session, condition):
        self.subject = subject
        self.session = session
        self.condition = condition
    
    def wmst_process(self):
        path = os.getcwd()
        df = glob.glob(os.path.join(path, f"Session{self.session}/data/", f"{self.subject}_*")) # Look for the file that starts with the subject ID
        df = pd.read_csv(df[0])
        acc_rate, alldata = mst.mst_accuracy(df, self.subject)
        alldata += acc_rate
        word, type, corr, trialn = mst.get_wmst_responses(df)
        return word, type, corr, trialn
        # return alldata # Return a list of z-scores, d-primes, LDI, subject ID and accuracy rate

    def smst_process(self):
        path = os.getcwd()
        df = glob.glob(os.path.join(path, f"Session{self.session}/data/", f"{self.subject}_*")) # Look for the file that starts with the subject ID
        df = pd.read_csv(df[0])
        alldata = mst.sound_accuracy(df, self.subject)
        sound, type, corr = mst.get_smst_responses(df)
        return sound, type, corr
        # return alldata

    def get_similarity(self):
        path = os.getcwd()
        df = glob.glob(os.path.join(path, f"Session{self.session}/data/", f"{self.subject}_*")) # Look for the file that starts with the subject ID
        df = pd.read_csv(df[0])
        sound1, sound2, ratings = similarity.similarity(df)
        return sound1, sound2, ratings

    def get_labels(self):
        path = os.getcwd()
        df = glob.glob(os.path.join(path, f"Session{self.session}/data/", f"{self.subject}_*")) # Look for the file that starts with the subject ID
        df = pd.read_csv(df[0])
        labels = similarity.labeling(df)
        return labels

    def sl_process(self):
        allSLdata = []
        path = os.getcwd()
        df = glob.glob(os.path.join(path, f"Session{self.session}/data/", f"{self.subject}_*")) # Look for the file that starts with the subject ID
        df = pd.read_csv(df[0])
         # Get familiarity rating
        old, part, word = sl.get_familiarity_rating(df)
        # Get AFC accuracy
        afc_accuracy = sl.get_afc_accuracy(df)
        # Check attentions
        attention = sl.check_pass(df) 
        allSLdata.extend([self.subject, old, part, word, afc_accuracy])
        allSLdata += attention
        allSLdata.append(self.session)
        return allSLdata # Return a list

    def sl_RT(self):
        path = os.getcwd()
        sldf = glob.glob(os.path.join(path, f"Session{self.session}/data/", f"{self.subject}_*")) # Look for the file that starts with the subject ID
        sldf = pd.read_csv(sldf[0])
        rt_df = sl.get_individual_RT(sldf, self.subject)
        return rt_df # Return a dataframe

def create_filelist(session, subjectlist):
    allfiles = []
    path = os.getcwd()
    df_list = glob.glob(os.path.join(path, f"Session{session}/data/", f"{subjectlist}_*")) # Directory to get files
    for i in df_list:
            df = pd.read_csv(i)
            subject = int(df["participant"][0])
            condition = [j for j in df["Condition"] if pd.isnull(j) == False]
            condition = str(condition[0])
            file = File(subject, session, condition)
            allfiles.append(file)
    return allfiles

def get_falsealarm(df):
    subject_list = df['Subject']
    for subject in subject_list:
        path = os.getcwd()
        df_direct = glob.glob(os.path.join(path, f"Session2/data/", f"{int(subject)}_*"))
        ind_df = pd.read_csv(df_direct[0])
        FAs = sl.get_fas(ind_df, subject)
        pd.DataFrame(FAs).to_csv('Analysis/FAs.csv', mode='a', header=False, index=False) 
        #header=['Total', 'FalseAlarm', 'HitRate', 'Syllable', 'Subject', 'Block', 'Condition'])
            

def get_positionwise(df):
    grouped_df = df.groupby(['Subject','Position']).mean()
    wider_df = grouped_df.pivot_table(index=['Subject'], columns='Position', values='RT')
    wider_df.to_csv('Analysis/byposition.csv')
    return wider_df
