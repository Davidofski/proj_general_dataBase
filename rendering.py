import pandas as pd
from datetime import datetime
import os
import sub

db_fileName = "DB_PW.csv"

# set taday_0 to today's raw date format
today_0 = datetime.now()

def readFile():
    print("INFO     readFile()")
    global db_loaded
    error_code = 0
    try:
        path = (r"C:\Users\david\OneDrive\Dokumenter\GitHub\DB_PW.csv")

        x = os.path.isfile(path)    # check if path and file existant
        path_exists = x

        if path_exists:
            db_loaded = pd.read_csv(path, sep=";", index_col=[0])
            print("existing db: ")
            print(db_loaded)
            error_code = 1
            error_message = "File existing, but CAN'T be read"

        else:
            error_code = 2
            error_message = "File or path not existant."

        error_code = 0

    except:
        db_fileExists = False
        db_loaded = {}
        error_code = 3
        error_message = "Failure at loading file."

    # return error_code, error_message
def formating(db_lastTimeChange):
    print("INFO     formating()")

    # formating of date
    newContainer = {}
    newContainer = db_lastTimeChange[0]
    
    print('DEBUG 0')
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

    # !! need for condition that 1st line won't be altered

    print("INFO     dslc()")
    readFile()
    global db_loaded
    print("[INFO]   dslc()")

    try:
        dslc_before = db_loaded['DSLC']
        print("DEBUG    days since last change before renderign: ", dslc_before)
        dslc_date = db_loaded['last time changed']
        print("DEBUG    date since last change: ", dslc_date)

        x = 0
        dslc_after = {}
        for i in dslc_before:
            print("DEBUG    i: ", i)
            print("DEBUG    dslc date: ", dslc_date[x])
            
            date = str(dslc_date[x])
            print("DEBUG    dslc(); date:", date)
            year = int(date[8:10])
            month = int(date[3:5])
            day = int(date[:2])
            print("DEBUG    day, month, year: ", day, month, year)

            diff_days = calc_dslc(year, month, day)

            if x > 0:
                db_loaded.loc[[x], ['DSLC']] = diff_days
                print("DEBUG    dscl()  dslc_after:", db_loaded)
                print("x= ", x)
            x = x + 1

        print('db_loaded:\n', db_loaded)
        db_loaded.to_csv('%s' %db_fileName, sep=";")

    except:
        text = 'UNEXPECTED ERROR - Failure formating: days since last change in %s' %db_fileName
        print(text)

def calc_dslc(past_year, past_month, past_day):
    print("INFO     calc_dslc")
    global today_0

    today_year = int(today_0.strftime("%y"))
    today_month = int(today_0.strftime("%m"))
    today_day = int(today_0.strftime("%d"))
    print("DEBUG    today_raw: [d,m,y] ", today_day, today_month, today_year)

    diff_year = today_year - past_year
    diff_month = today_month - past_month
    diff_day = today_day - past_day

    diff_days = str(diff_year*365 + diff_month*30 + diff_day)

    print("DEBUG    diff:   ", diff_days)
    return diff_days

# only for testing
# readFile()
# dslc()