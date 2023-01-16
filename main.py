import os
import pandas as pd
import dearpygui.dearpygui as dpg
import sub

db_fName = []
db_lName = []
db_age = []
db_addInfo = []
db_ID = []
db = {}

db_fileExists = False
db_fileName = "DB_General.csv"
window_width = 1000
window_height = 1000

def saveClicked():
    global db

    db_fName.append(dpg.get_value(iField_fName))
    db_lName.append(dpg.get_value(iField_lName))
    db_age.append(dpg.get_value(iField_age))
    db_ID.append(int(db_ID_max) + 1)
    print("Database's highes ID is: %s" %db_ID)
    db_addInfo.append(dpg.get_value(iField_addInfo))

    # run subroutine to save data to frame and in .cvs file
    sC_return, db = sub.saveClicked(db_fName, db_lName, db_age, db_addInfo, db_ID, db_fileExists, db_loaded, db_fileName)
    print(sC_return)

def updateClicked():
    x = 1

def exitClicked():
    dpg.stop_dearpygui()

# try to read in existing file
# if file is not existant a new one will be created in safe_clicked()
try:
    path = (r"C:\Users\david\OneDrive\Dokumenter\GitHub\DB_General.csv")
    db_loaded = pd.read_csv(path, sep=";")
    # get the number of entries 
    db_ID_max = db_loaded['db_ID'].max()
    db_fileExists = True
except:
    db_fileExists = False
    db_loaded = {}
    db_ID_max = 0

    print("File status '%s'" %db_fileExists)

dpg.create_context()

with dpg.window(label="'%s' MANIPULATION" %db_fileName, width=window_width, height=260, pos=(0,0)):
    dpg.add_text("In this UI you can read and manipulate the database: '%s'" %db_fileName)
    
    if db_fileExists == True:
        w1_text1 = dpg.add_text("Reading in of file was sucessfull!")
    else:
        w1_text2 = dpg.add_text("!!Reading in of file was NOT sucessfull, probably file not existant!!", color=[255,0,0])
    
    # Window 1 input fields
    iField_ID = dpg.add_input_text(label="database ID [str]")
    iField_fName = dpg.add_input_text(label="first name [str]")
    iField_lName = dpg.add_input_text(label="last name [str]")
    iField_age = dpg.add_slider_int(label="age [int]", default_value=30, max_value=100)
    iField_addInfo = dpg.add_input_text(label="additional Information [str]")

    # Window 1 buttons
    b_update = dpg.add_button(label="update output", callback=updateClicked)
    b_saveChanges = dpg.add_button(label="save changes to '%s'" %db_fileName, callback=saveClicked)
    b_exitClicked = dpg.add_button(label="EXIT", callback=exitClicked)

with dpg.window(label="'%s' CONTENT" %db_fileName, width=window_width, height=680, pos=(0,260), tag="content"):
    with dpg.table(header_row=True, resizable=True, policy=dpg.mvTable_SizingStretchProp,
                   borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True):

        column_id = dpg.add_table_column(label="DB ID")
        column_fName = dpg.add_table_column(label="DB First Name")
        column_lName = dpg.add_table_column(label="DB Last Name")
        column_age = dpg.add_table_column(label="DB Age")
        column_addInfo = dpg.add_table_column(label="DB Additional Information")

dpg.create_viewport(title='Data Base Manipulation 2.0', width=window_width + 10, height=window_height, x_pos=1500, y_pos=0)
dpg.setup_dearpygui()
dpg.show_viewport()

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():
    # space for all running operations
    
    dpg.render_dearpygui_frame()

dpg.destroy_context()