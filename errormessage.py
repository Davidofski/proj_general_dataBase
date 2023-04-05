import pandas as pd
from datetime import datetime
import os

db_fileName = "DB_PW.csv"
errorLogName = "errorLog.csv"
fileExists = False
log_content = {}
currentDirectory = os.getcwd()
print("[INFO]  current directory: ", currentDirectory)
db_path = currentDirectory + r"\%s"%db_fileName
module_encryption = currentDirectory + r"\de_encrytpion.pyw"
module_errorLog = currentDirectory + r"\showErrorLog.pyw"
rec_path = currentDirectory + r"\%s" %errorLogName

# messages
em1 = "ERROR:[1]   File could not be found!"
em2 = "ERROR:[2]   Could not safe dataframe to csv!"
em3 = "ERROR:[3]   Path could not be found or has been changed!"
em4 = "ERROR:[4]   Updating 'days since last change' in csv file not possible"
em5 = "ERROR:[5]   Error-log could not be opened."
em6 = "ERROR:[6]   File encrypted; main can not be started; decrypt file before!"
em7 = "ERROR:[7]   Neither encrypted nor decrypted file found."
em8 = """ERROR:[8]   Variable could not be changed
            It is either not changeable or format incorrect"""

def alterlog():
    # try to read in file
    print("[FUNKTION]   erm.alterlog()")
    global fileExists
    fileExists = False
    log_content = {}
    try:
        path = (rec_path)
        # path_exists = os.path.isfile(path)    # check if path and file existant
        df = pd.read_csv(path, sep=";", index_col=[0])
        log_content = df
        fileExists = True
        log_maxEntry = len(log_content.axes[0])

    except:
        print("[INFO]   csv file coldn't be read or found!")
        fileExists = False

    # add error messages to loaded dataframe for display in window error message
    errorLog = []

    if fileExists:
        for errorCode in log_content["error code"]:
            match errorCode:
                case 1:
                    errorLog.append(em1)
                case 2:
                    errorLog.append(em2)
                case 3:
                    errorLog.append(em3)
                case 4:
                    errorLog.append(em4)
                case 5:
                    errorLog.append(em5)
                case 6:
                    errorLog.append(em6)
                case 7:
                    errorLog.append(em7)
                case 8:
                    errorLog.append(em8)
                case other:
                    errorLog.append("...")

        log_content["message"] = errorLog
        log_content = log_content.drop(columns=['error code'], axis=0)

    print("[Error LOG]:\n", log_content)
    return log_content, log_maxEntry

def saveErrorLog(errorCode):
    print("[Function]   erm.saveErrorLog with error code ", errorCode)

    errorEntry = []
    entryTimeStamp = []
    errorEntry.append(errorCode)
    entryTimeStamp.append(datetime.now().replace(microsecond=0))

    try:
        path = (rec_path)
        em_loaded = pd.read_csv(path, sep=";", index_col=[0])
        fileExists = True

    except:
        em_loaded = {}
        fileExists = False

    f = {"time stamp":entryTimeStamp, "error code":errorEntry}
    em_new = pd.DataFrame(f)

    if fileExists:
        df = pd.concat([em_loaded, em_new])
        df = pd.DataFrame(df)
        df.to_csv("errorLog.csv", sep=";", index=True)

    else:
        df = pd.DataFrame(em_new)
        df.to_csv(rec_path, sep=";", index=True)