import pandas as pd
import datetime
import errormessage as erm
import os
import filehandling as fh

db_fileName = "DB_PW.csv"
entryTimeStamp = []
errorMessage = []
currentDirectory = os.getcwd()
print("[INFO]  current directory: ", currentDirectory)
db_path = currentDirectory + r"\%s"%db_fileName

# set taday_0 to today's raw date format
today_0 = datetime.date.today()

def readFile():
    print("[FUNCTION]   rd.readFile()")
    global db_loaded

    db_loaded = fh.readFile()

def formating(db_lastTimeChange):
    print("[FUNCTION]   rd.formating()")

    # formating of date
    newContainer = {}
    newContainer = db_lastTimeChange[0]
    
    # compenasate lybrary error
    year = newContainer['year'] - 100   # -100: compensate BUG
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

    return db_lastTimeChange_f, diff_days

def dslc():
    print("[FUNCTION]   rd.dslc()")
    readFile()
    global db_loaded

    try:
        dslc_date = db_loaded['last time changed']
        x = 0
        for i in dslc_date:   
            date = str(i)
            year = int(date[8:10])
            month = int(date[3:5])
            day = int(date[:2])
            diff_days = calc_dslc(year, month, day)
            db_loaded.loc[[x], ['DSLC']] = diff_days
            x = x + 1
        db_loaded.to_csv(db_path, sep=";")

    except:
        print("[EXPETION]   rd.dslc()")
        # Error 4
        errorCode = 4
        erm.saveErrorLog(errorCode)

def calc_dslc(past_year, past_month, past_day):
    print("[FUNCTION]   rd.calc_dslc")
    global today_0

    past = datetime.date(past_year + 2000, past_month, past_day)
    delta = today_0 - past
    diff_days = delta.days

    return diff_days