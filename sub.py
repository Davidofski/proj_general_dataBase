import os
import pandas as pd
from datetime import datetime
import rendering as rd
import errormessage as erm

db_fileName = "DB_PW.csv"
db_entryTimeStamp = []
db_fileExists_atStartUp = False
sortUnsort = False
error_code = 0
db_cryptExists = False
db_fileStat = [False, False]
db_path = r"C:\Users\David\OneDrive\Dokumenter\GitHub\proj_general_dataBase\DB_PW.csv"
crypt_path = r"C:\Users\David\OneDrive\Dokumenter\GitHub\proj_general_dataBase\DB_PW.crypt"
modul_encryption = r"C:\Users\David\OneDrive\Dokumenter\GitHub\proj_general_dataBase\de_encrytpion.pyw"

today_0 = datetime.now()
today_raw = str(today_0.replace(microsecond=0))
today = today_raw[:-9]

def readFile():
    print("[FUNCTION]   sub.readFile()")
    global db_loaded, db_fileExists

    try:
        db_fileExists = os.path.isfile(db_path)
        db_fileExists_atStartUp = db_fileExists
        
        db_loaded = pd.read_csv(db_path, sep=";", index_col=[0])
        print("[INFO]   Loaded dataframe:\n", db_loaded)

    except:
        print("[EXEPTION]   sub.readFile()")
        db_fileExists_atStartUp = False
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

        # Error 1
        errorCode = 1
        erm.saveErrorLog(errorCode)

    return db_fileExists_atStartUp

def checkFileStatus():
    readFile()
    if db_fileExists and db_loaded.empty:
        encrypted = True
        errorCode = 6
        erm.saveErrorLog(errorCode)
    if db_fileExists and not db_loaded.empty:
        encrypted = False
    
    db_fileStat[0] = db_fileExists
    db_fileStat[1] = encrypted

    return db_fileStat

def updateClicked(sort):
    print("[FUNCTION]   sub.updateClicked()")
    global db_loaded

    rd.dslc()
    readFile()
    
    if sort:
        table_content = sortTable()
        pass
    else:
        table_content = db_loaded
    return table_content

def sortTable():
    global db_loaded, sortUnsort
    if sortUnsort:
        '''sortedTable = db_loaded.sort_index(inplace=False)
        sortUnsort = False
        '''
        sortedTable = db_loaded.sort_values(by=['platform'], ascending=True)
        sortUnsort = False
    else:
        sortedTable = db_loaded.sort_values(by=['DSLC'], ascending=False)
        sortUnsort = True
    return sortedTable

def maxEntry():                 # checks the number of entries in the loaded dataframe //used in creating the table window 2
    print("[FUNCTION]   sub.maxEntry()")
    global db_loaded, db_fileExists
    if db_fileExists:
        table_maxEntry = len(db_loaded.axes[0])
        table_size = db_loaded.size
    else:
        table_maxEntry = 0
        table_size = 0
    return table_maxEntry, table_size

def changeItem(cell, newValue, save):
    global db_loaded
    accepted = False
    print("[FUNCTION]   sub.changeItem()")

    print('[INFO]       cell:', cell)
    print('[INFO]       newValue', newValue)

    if not save:
        # Method to determine the row and the coloumn of the cell position to change the corresponding item in the dataframe.
        coloumn = int(cell[:1])
        try:
            row = int(cell[-2:])
        except:
            row = int(cell[-1:])

        print('[BUILD]  coloumn: ', coloumn)
        print('[BUILD]  row: ', row)

        """
        Testing procedure to determine wether the changes are allowed or not
        """
        # check date since last time changed
        if coloumn == 3:
            try:
                int(newValue[:2])
                int(newValue[3:5]),
                int(newValue[6:10])
                dashCount = str(newValue).find('-')
                if dashCount > 1 and dashCount < 3 and len(newValue) == 10: accepted = True
            except: accepted = False
        else: accepted = True

        if accepted and coloumn != 5:
            db_loaded.iloc[[row], [coloumn]] = str(newValue)
            return False
        else:
            erm.saveErrorLog(8)
            return True
    else:
        db_loaded.to_csv('%s' %db_fileName, sep=";", index=True)

    print("[BUILD]  db_loaded:\n", db_loaded)


    

def saveClicked(db_platform, db_email, db_pw, db_lastTimeChange, db_addInfo):
    print("[FUNCTION]   sub.saveClicked()")
    global db_loaded, db_fileExists

    # only alter variables when database already existant
    # in not, first line shall not be alterd
    if db_fileExists:
        db_lastTimeChange_f,dslc = rd.formating(db_lastTimeChange)
        dslc = int(dslc)
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
        print("[EXEPTION]   sub.saveClicked()")
        # Error 2
        errorCode = 2
        erm.saveErrorLog(errorCode)