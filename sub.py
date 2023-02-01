import os
import pandas as pd
from datetime import datetime
import rendering as rd

db_fileName = "DB_PW.csv"
db_entryTimeStamp = []

today_0 = datetime.now()
today_raw = str(today_0.replace(microsecond=0))
today = today_raw[:-9]

def readFile():
    print("[FUNCTION]   sub.readFile()")
    global db_loaded, db_fileExists, error_code

    try:
        path = (r"C:\Users\david\OneDrive\Dokumenter\GitHub\DB_PW.csv")

        db_fileExists = os.path.isfile(path)
        
        db_loaded = pd.read_csv(path, sep=";", index_col=[0])
        print("Loaded dataframe:\n", db_loaded)

        error_code = 0

    except:
        db_fileExists = False
        db_platform = []
        db_email = []
        db_pw = []
        db_lastTimeChange = []
        db_addInfo = []
        db_platform.append('x')
        db_email.append('xx')
        db_pw.append('xxx')
        db_lastTimeChange.append('01-01-2000')
        db_addInfo.append('4321')
        saveClicked(db_platform, db_email, db_pw, db_lastTimeChange, db_addInfo)
        error_code = 1

    return db_fileExists, error_code

def updateClicked():
    print("[FUNCTION]   sub.updateClicked()")
    global db_fileExists, db_loaded, error_code
    table_content = db_loaded
    return table_content

def maxEntry():                 # checks the number of entries in the loaded dataframe //used in creating the table window 2
    print("[FUNCTION]   sub.maxEntry()")
    global db_loaded, db_fileExists
    if db_fileExists:
        table_maxEntry = len(db_loaded.axes[0])
    else:
        table_maxEntry = 0

    return table_maxEntry

def saveClicked(db_platform, db_email, db_pw, db_lastTimeChange, db_addInfo):
    print("[FUNCTION]   sub.saveClicked()")
    global db_loaded, db_fileExists, error_code

    # only alter variables when database already existant
    # in not, first line shall not be alterd
    if db_fileExists:
        db_lastTimeChange_f,dslc = rd.formating(db_lastTimeChange)
        db_dslc = []
        db_dslc.append(dslc)
        table_maxEntry = maxEntry()
        db_id = table_maxEntry
    else:
        db_id = []
        db_id.append(0)
        db_lastTimeChange_f = db_lastTimeChange
        db_dslc = []
        db_dslc.append('0')

    try:
        f = {"platform" : db_platform, "email" : db_email, "password" : db_pw, "last time changed" : db_lastTimeChange_f, "additional information" : db_addInfo, "DSLC" : db_dslc}
        db_new = pd.DataFrame(f, index=[db_id])

        if db_fileExists:
            db = pd.concat([db_loaded, db_new])
            db = pd.DataFrame(db)
            db.to_csv('%s' %db_fileName, sep=";", index=True)
            db_loaded = db
        else:
            db_new.to_csv('%s' %db_fileName, sep=";", index=True)
            db_loaded = db_new
            db_fileExists = True

    except:
        error_code = 2