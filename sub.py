import os
import pandas as pd

def saveClicked(db_fName, db_lName, db_age, db_addInfo, db_ID, db_fileExists, db_loaded, db_fileName):
    
    # only for debuging
    print("Hand over after save clicked:")
    print("First Name: '%s'" %db_fName)
    print("Last Name: '%s'" %db_lName)
    print("Age: %s" %db_age)
    print("Additional information: %s" %db_addInfo)

    try:
        f = {"DB ID" : db_ID, "first name" : db_fName, "last name" : db_lName, "age" : db_age, "additional information" : db_addInfo}
        print(f)
        db_new = pd.DataFrame(f)
        print(db_new)

        if db_fileExists == False:
            db_new.to_csv('%s' %db_fileName, sep=";")
            print(db_new)
        else:
            db = pd.concat([db_loaded, db_new])
            db.to_csv('%s' %db_fileName, sep=";")
            print(db)

        text = "saving was successfull"

    except:
        text = "saving was NOT successfull"

    return text

