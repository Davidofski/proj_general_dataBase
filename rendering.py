import pandas as pd
from datetime import datetime
import errormessage as erm

db_fileName = "DB_PW.csv"
entryTimeStamp = []
errorMessage = []

# set taday_0 to today's raw date format
today_0 = datetime.now()

def readFile():
    print("[FUNCTION]   rd.readFile()")
    global db_loaded
    try:
        path = (r"C:\Users\david\OneDrive\Dokumenter\GitHub\DB_PW.csv")
        # path_exists = os.path.isfile(path)    # check if path and file existant
        db_loaded = pd.read_csv(path, sep=";", index_col=[0])

    except:
        db_loaded = {}
        # Error 3
        errorCode = 3
        erm.saveErrorLog(errorCode)

    # return error_code, error_message
def formating(db_lastTimeChange):
    print("[FUNCTION]   rd.formating()")

    # formating of date
    newContainer = {}
    newContainer = db_lastTimeChange[0]
    
    # compenasate lybrary error
    year = newContainer['year'] - 100   # -100: BUG which you need to compensate
    month = newContainer['month'] + 1   # +1 as return for Jan is 0
    day = newContainer['month_day']

    # calculate days since last change
    year = int(year)
    month = int(month)
    day = int(day)
    diff_days = calc_dslc(year, month, day) # calculation

    if month < 10:                  # add a 0 in fron in if < 10
        month = '0' + str(month)
    if day < 10:                    # add a 0 in fron in if < 10
        day = '0' + str(day)

    # convert objects to strings
    year = '20' + str(year)
    month = str(month)
    day = str(day)
    
    db_lastTimeChange_f = day + '-' + month + '-' + year
    # new_datetime = datetime.strptime(new_string, '%m/%d/%y %H:%M:%S')
    # db_lastTimeChange_f = new_datetime

    return db_lastTimeChange_f, diff_days

def dslc():
    print("[FUNCTION]   rd.dslc()")
    # !! need for condition that 1st line won't be altered
    readFile()
    global db_loaded

    try:
        dslc_date = db_loaded['last time changed']

        x = 0
        for i in dslc_date:       
            date = str(dslc_date[x])
            year = int(date[8:10])
            month = int(date[3:5])
            day = int(date[:2])

            diff_days = calc_dslc(year, month, day)

            if x > 0:
                db_loaded.loc[[x], ['DSLC']] = diff_days
            x = x + 1

        db_loaded.to_csv('%s' %db_fileName, sep=";")

    except:
        print("[EXPETION]   rd.dslc()")
        # Error 4
        errorCode = 4
        erm.saveErrorLog(errorCode)

def calc_dslc(past_year, past_month, past_day):
    print("[FUNCTION]   rd.calc_dslc")
    global today_0

    # very simple approximation of days difference
    today_year = int(today_0.strftime("%y"))
    today_month = int(today_0.strftime("%m")) 
    today_day = int(today_0.strftime("%d"))

    diff_year = today_year - past_year
    diff_month = today_month - past_month
    diff_day = today_day - past_day

    diff_days = str(diff_year*365 + diff_month*30 + diff_day)

    return diff_days

