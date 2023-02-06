import pandas as pd
from datetime import datetime

db_fileName = "DB_PW.csv"
errorLogName = "errorLog.csv"
fileExists = False
log_content = {}

# messages
em1 = "ERROR:[1]   File could not be found!"
em2 = "ERROR:[2]   Could not safe dataframe to csv!"
em3 = "ERROR:[3]   Path could not be found or has been changed!"
em4 = "ERROR:[4]   Updating 'days since last change' in csv file not possible"
em5 = "ERROR:[5]   Error-log could not be opened."
em6 = "ERROR:[6]   File encrypted; main can not be started."
em7 = "ERROR:[7]   Neither encrypted nor decrypted file found."

def alterlog():
    # try to read in file
    print("[FUNKTION]   erm.alterlog()")
    global log_content, fileExists
    fileExists = False
    log_content = {}
    try:
        path = (r"C:\Users\david\OneDrive\Dokumenter\GitHub\proj_general_dataBase\errorLog.csv")
        # path_exists = os.path.isfile(path)    # check if path and file existant
        df = pd.read_csv(path, sep=";", index_col=[0])
        log_content = df
        fileExists = True

    except:
        print("[INFO]   csv file coldn't be read or found!")
        fileExists = False

    # add error messages to loaded dataframe for display in window error message
    errorLog = []

    if fileExists:
        for errorCode in log_content["error code"]:
            if errorCode == 1:
                errorLog.append(em1)
            elif errorCode == 2:
                errorLog.append(em2)
            elif errorCode == 3:
                errorLog.append(em3)
            elif errorCode == 4:
                errorLog.append(em4)
            elif errorCode == 5:
                errorLog.append(em5)
            elif errorCode == 6:
                errorLog.append(em6)
            elif errorCode == 7:
                errorLog.append(em7)
            else:
                errorLog.append("...")

        log_content["message"] = errorLog

    print("[Error LOG]:\n", log_content)

def saveErrorLog(errorCode):
    print("[Function]   erm.saveErrorLog")

    errorEntry = []
    entryTimeStamp = []
    errorEntry.append(errorCode)
    entryTimeStamp.append(datetime.now().replace(microsecond=0))

    try:
        path = (r"C:\Users\david\OneDrive\Dokumenter\GitHub\proj_general_dataBase\errorLog.csv")
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
        df.to_csv("errorLog.csv", sep=";", index=True)

    alterlog()