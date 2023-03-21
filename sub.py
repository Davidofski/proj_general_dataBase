import os
import pandas as pd
from datetime import datetime
import rendering as rd
import errormessage as erm
import filehandling as fh

db_entryTimeStamp = []
sortUnsort = False
error_code = 0
db_cryptExists = False
db_fileStat = [False, False]

# get current location and merge with file name
cD = os.getcwd()
db_fileName = "DB_PW.csv"
db_path = cD + r"\%s"%db_fileName

today_0 = datetime.now()
today_raw = str(today_0.replace(microsecond=0))
today = today_raw[:-9]

# date for main date picker
today_year = datetime.now().year
today_month = datetime.now().month
today_day = datetime.now().day

def checkFileStatus():
    print("[FUNCTION]     sub.checkFileStatus()")

    fh.readFile()

    fileExists = fh.fileExists.status
    fileEncrypted = fh.fileEncrypted.status
    db_fileStat[0] = fileExists
    db_fileStat[1] = fileEncrypted

    return db_fileStat

def updateClicked(sort):
    print("[FUNCTION]   sub.updateClicked()")
    global db_loaded

    rd.dslc()
    db_loaded = fh.readFile()

    if sort: table_content = sortTable()
    else: table_content = db_loaded
    return table_content

def sortTable():
    global db_loaded, sortUnsort
    if sortUnsort:
        sortedTable = db_loaded.sort_values(by=['email'],
                                            ascending=True)
        print("[INFO]       table sorted after 'email'")
        sortUnsort = False
    else:
        sortedTable = db_loaded.sort_values(by=['DSLC'],
                                            ascending=False)
        print("[INFO]       table sorted after 'DSLC'")
        sortUnsort = True
    return sortedTable

def maxEntry():
    # returns the number of entries and the size of the loaded DF
    print("[FUNCTION]   sub.maxEntry()")

    table_maxEntry = fh.maxEntry.status
    table_size = fh.tableSize.status

    return table_maxEntry, table_size

def changeItem(cell, newValue, save):
    global db_loaded
    accepted = False
    print("[FUNCTION]   sub.changeItem()")

    print('[INFO]       cell:', cell)
    print('[INFO]       newValue', newValue)

    if not save:
        # Method to determine the row and the coloumn of the cell
        # position to change the corresponding item in the dataframe.
        coloumn = int(cell[:1])
        try:
            row = int(cell[-2:])
        except:
            row = int(cell[-1:])

        print('[BUILD]  coloumn: ', coloumn)
        print('[BUILD]  row: ', row)

        # Testing procedure to determine wether the changes are allowed
        # or not
        # Check date since last time changed
        if coloumn == 3:
            try:
                int(newValue[:2])
                int(newValue[3:5]),
                int(newValue[6:10])
                dashCount = str(newValue).find('-')
                if (dashCount > 1
                    and dashCount < 3
                    and len(newValue)== 10): accepted = True
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

def saveClicked(db_platform, db_email, db_pw, db_lastTimeChange,
                db_addInfo):
    print("[FUNCTION]   sub.saveClicked()")
    global db_loaded

    db_fileExists = fh.fileExists.status

    # only alter variables when database already existant
    # if not, first line shall not be alterd
    '''if db_fileExists:'''
    db_lastTimeChange_f,dslc = rd.formating(db_lastTimeChange)
    dslc = int(dslc)
    db_dslc = []
    db_dslc.append(dslc)
    table_maxEntry, table_size = maxEntry()
    db_id = table_maxEntry
    '''else:
        db_id = []
        db_id.append(0)
        db_lastTimeChange_f = db_lastTimeChange
        db_dslc = []
        db_dslc.append('0')'''

    try:
        f = {"platform" : db_platform,
             "email" : db_email,
             "password" : db_pw,
             "last time changed" : db_lastTimeChange_f,
             "additional information" : db_addInfo,
             "DSLC" : db_dslc}
        
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