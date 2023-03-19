# loading and writing of file for other modules

import os
import pandas as pd
import errormessage as erm

# get the current location of the directory
cD = os.getcwd()
fileName = "DB_PW.csv"
path = cD + r"\%s" %fileName

class fileStatus:

    def __init__(self) -> None:
        pass

    def setStatus(self, status):
        self.status = status

fileExists = fileStatus()
fileEncrypted = fileStatus()
maxEntry = fileStatus()
tableSize = fileStatus()

fileExists.setStatus(None)
fileEncrypted.setStatus(None)

# check if file existant
# returs boolean

def readFile():
    global db_loaded

    print("""[INFO]     Modul:  filehandling
             Function:   readFile()""")
    
    fileExists.setStatus(os.path.isfile(path))

    if fileExists.status:

        # reading file and create dataframe id possible.
        # if not possible, then file is encrypted
        try:
            db_loaded = pd.read_csv(path, sep=";", index_col=[0])

            if db_loaded.empty: fileEncrypted.status(True)
            maxEntry.setStatus(len(db_loaded.axes[0]))
            tableSize.setStatus(db_loaded.size)
        except:
            print("[Exception]      in readFile()")
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

readFile()