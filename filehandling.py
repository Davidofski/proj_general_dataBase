# loading and writing of file for other modules

import os
import pandas as pd
import errormessage as erm

# get the current location of the directory
cD = os.getcwd()
fileName = "DB_PW.csv"
path = cD + r"\%s" %fileName

# check if file existant
# returs boolean
def checkFile():
    print("""[INFO]       Module:   filehandling;
           Funktion:   checkFile()""")
    fileExists = os.path.isfile(path)
    return fileExists

def readFile():
    print("""[INFO]     Modul:  filehandling
           Function:   readFile()""")
    fileExists = checkFile()

    if fileExists:
        try: db_loaded = pd.read_csv(path, sep=";", index_col=[0])
        except: print("[Exception]      in readFile()")
    else:
        _id = []
        platform = []
        email = []
        pw = []
        lastTimeChange = []
        addInfo = []
        dslc = []
        _id.append('0')
        platform.append('x')
        email.append('xx')
        pw.append('xxx')
        lastTimeChange.append('01-01-2000')
        addInfo.append('4321')
        dslc.append('0')
        df = {"platform" : platform, "email" : email,
             "password" : pw,
             "last time changed" : lastTimeChange,
             "additional information" : addInfo,
             "DSLC" : dslc}
        db_loaded = pd.DataFrame(df, index=[_id])
        erm.saveErrorLog(1)

    return db_loaded

def saveFile(db_toSave):
    print("""[INFO]     Modul:  filehandling
           Function:   saveFile()""")
    try:
        db = pd.DataFrame(db_toSave)
        db.to_csv(fileName, sep=";", index=True)
    except:
        print("[Exception]      in saveFile()")
        erm.saveErrorLog(2)