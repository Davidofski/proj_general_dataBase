import pandas as pd
import os
from datetime import datetime
import errormessage as erm

# get current location and merge with file name
cD = os.getcwd()
db_fileName = "DB_PW.csv"
db_path = cD + r"\%s"%db_fileName

def readFile():
    print("[FUNCTION]   sub.readFile()")

    try:
        db_fileExists = os.path.isfile(db_path)        
        db_loaded = pd.read_csv(db_path, sep=";", index_col=[0])
        print("[INFO]   Loaded dataframe:\n", db_loaded)

    except ImportError:
        pass

    return db_loaded