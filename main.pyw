import dearpygui.dearpygui as dpg
import sub
import settings as st
import rendering as rd
import os
import time

# create emtply list container
db_platform = []
db_email = []
db_pw = []
db_lastTimeChange = []
db_addInfo = []
db_fileStat = [False, False]    # [0]: file exists at start-up; [1]: file encrypted
dslc = []
db = {}
table_1stUpdate = False
table_updateClicked = False
timerStarted0 = False
timerStarted1 = False
startTime0 = 0
startTime1 = 0

# filename used to create and read file into dataframe
db_fileName = "DB_PW.csv"
currentDirectory = os.getcwd()
print("[INFO]  current directory: ", currentDirectory)
db_path = currentDirectory + r"\%s"%db_fileName
module_encryption = currentDirectory + r"\de_encrytpion.pyw"
module_errorLog = currentDirectory + r"\showErrorLog.pyw"
    
def saveClicked():
    global db, db_fileName

    # append new list item into container | in this proj always only one item per container
    # container will be cleared after use
    db_platform.append(dpg.get_value(iField_platform))
    db_email.append(dpg.get_value(iField_email))
    db_pw.append(dpg.get_value(iField_pw))
    db_lastTimeChange.append(dpg.get_value(iField_lastTimeChange))
    db_addInfo.append(dpg.get_value(iField_addInfo))

    # run subroutine to save data to frame and in .cvs file
    sub.saveClicked(db_platform, db_email, db_pw, db_lastTimeChange, db_addInfo)

    # clear containers after use in sub.saveClicked
    db_platform.clear()
    db_email.clear()
    db_pw.clear()
    db_lastTimeChange.clear()
    db_addInfo.clear()

    # update after save has been clicked to refresh table 1
    # tabke one will always show the complete frame from loaded csv file
    updateClicked(False)

    # clear entry fields
    dpg.set_value(iField_platform, "")
    dpg.set_value(iField_email, "")
    dpg.set_value(iField_pw, "")
    dpg.set_value(iField_addInfo, "")

def updateClicked(sortTable):
    global table_content, table_maxEntry, table_updateClicked, table_size
    table_content = sub.updateClicked(sortTable)
    table_maxEntry, table_size = sub.maxEntry()
    table_updateClicked = True

def sortClicked():
    updateClicked(True)


def exitClicked():
    dpg.stop_dearpygui()

def exitAndEncryptClicked():
    dpg.stop_dearpygui()
    os.startfile(module_encryption)

def openErorLog():
    # dpg.stop_dearpygui()
    os.startfile(module_errorLog)

def okClicked():
    dpg.delete_item("error message")

# try to read in existing file
# if file is not existant a new one will be created in safe_clicked()
def checkFileStat():
    db_fileStat = sub.checkFileStatus()
    return db_fileStat

# check wether file is encrypted at startup to prevent failure at start-up with building a table in window 2
# failure in maxEntrys would occur otherwise
db_fileStat = checkFileStat()

# load db into table_content the first time onl if file not encrypted
if not db_fileStat[1]:
    sub.readFile()
    db_maxEntry, table_size = sub.maxEntry()
    if db_fileStat[0]:
        if db_maxEntry > 0:
            rd.dslc()
    updateClicked(False)
else: os.startfile(module_encryption)

# GUI build up
dpg.create_context()
dpg.set_global_font_scale(1)

with dpg.window(label="'%s' MANIPULATION" %db_fileName, width=st.window1_width, height=st.window1_heigh, pos=(st.window1_xpos,st.window1_ypos)):
    dpg.add_text("In this UI you can read and manipulate the database: '%s'" %db_fileName, pos=(st.item1_xpos, st.item1_ypos))
    
    if db_fileStat[0] and not db_fileStat[1]:
        w1_text1 = dpg.add_text("Reading in of file was sucessfull!", pos=(st.item2_xpos, st.item2_ypos))
    else:
        w1_text3 = dpg.add_text("File not found or encrypted!!", color=[255,0,0], pos=(st.item3_xpos, st.item3_ypos))

    # Window 1 input fields
    iField_platform = dpg.add_input_text(label="platform [str]", hint='e.g. gmail or facebook', pos=(st.item4_xpos, st.item4_ypos), height=st.iField_heigh, width=st.iField_width)
    iField_email = dpg.add_input_text(label="email [str]", hint='max.musterman@gmail.com', pos=(st.item5_xpos, st.item5_ypos), height=st.iField_heigh, width=st.iField_width)
    iField_pw = dpg.add_input_text(label="password [str; no spaces allowed]", hint='1234', no_spaces=True, pos=(st.item6_xpos, st.item6_ypos), height=st.iField_heigh, width=st.iField_width)
    iField_lastTimeChange = dpg.add_date_picker(label="last time changed [int]", default_value={'month_day': 1, 'year': 122, 'month': 0}, pos=(st.item7_xpos, st.item7_ypos))
    iField_addInfo = dpg.add_input_text(label="additional Information [str]", hint='additional infrmaion which might be important', pos=(st.item8_xpos, st.item8_ypos), height=st.iField_heigh, width=st.iField_width)

    # Window 1 buttons
    # #b_update = dpg.add_button(label="update output", callback=updateClicked)
    b_saveChanges = dpg.add_button(label="SAVE changes to '%s'" %db_fileName, callback=saveClicked, pos=(st.item9_xpos, st.item9_ypos))
    b_exitClicked = dpg.add_button(label="EXIT", callback=exitClicked, pos=(st.item10_xpos, st.item10_ypos))
    b_exitNencrypt = dpg.add_button(label="EXIT and goto encrypter", callback=exitAndEncryptClicked, pos=(st.item16_xpos, st.item16_ypos))
    b_openErrorLog = dpg.add_button(label="OPEN error log", callback=openErorLog, pos=(st.item22_xpos, st.item22_ypos))
    b_sortEntrys = dpg.add_button(label="Sort after DSLC or platform", callback=sortClicked, pos=(st.item23_xpos, st.item23_ypos))

    # Window 1 output fields
    oField_today = dpg.add_text("Today's date: %s" %sub.today, pos=(st.item11_xpos,st.item11_ypos))
    oField_fileSize = dpg.add_text("File size: %s" %table_size, pos=(st.item13_xpos,st.item13_ypos))
    oField_dateDifference = dpg.add_text("Not changed since: ?? days", pos=(st.item12_xpos,st.item12_ypos))

def updateWindow():
    with dpg.window(label="'%s' CONTENT" %db_fileName, width=st.window2_width, height=st.window2_heigh, pos=(st.window2_xpos,st.window2_ypos), tag="content"):
        with dpg.table(label='DatasetTable', tag="table1", borders_innerV=True, resizable=True, policy=dpg.mvTable_SizingFixedFit, reorderable=True, sortable=True, row_background=True):
            for i in range(table_content.shape[1]):                    # Generates the correct amount of columns
                dpg.add_table_column(label=table_content.columns[i])   # Adds the headers
            for i in range(table_maxEntry):
                with dpg.table_row():
                    for j in range(table_content.shape[1]):
                        if j == 5:
                            if int(table_content.iloc[i,j]) > st.table_maxDiff:     # check if the date is in the allowed range
                                dpg.add_text(f"{table_content.iloc[i,j]}", color=[255,0,0])     # Displays the value of each row/column combination
                            elif int(table_content.iloc[i,j]) > st.table_intDiff and int(table_content.iloc[i,j]) < st.table_maxDiff:
                                dpg.add_text(f"{table_content.iloc[i,j]}", color=[255,255,0])
                            else:
                                dpg.add_text(f"{table_content.iloc[i,j]}")
                        else:
                            dpg.add_text(f"{table_content.iloc[i,j]}", color=[200,155,200])

dpg.create_viewport(title='Data Base Manipulation 2.0', width=st.ui_width + 10, height=st.ui_heigh, x_pos=1500, y_pos=0)
dpg.setup_dearpygui()
dpg.show_viewport()

startTime1 = time.time()

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():
    # space for all running operations

    # display the choosen difference in days since the last time changed
    if time.time() - startTime1 > 1:
        db_lastTimeChange.append(dpg.get_value(iField_lastTimeChange))
        db_lastTimeChange_f, diff_days = rd.formating(db_lastTimeChange)
        dpg.set_value(oField_dateDifference, 'Not changed since: %s days' %diff_days)
        db_lastTimeChange.clear()
        startTime1 = time.time()

    if db_fileStat[1] and not timerStarted0:
        timerStarted0 = True
        startTime0 = time.time()

    if db_fileStat[1] and timerStarted0 and time.time() - startTime0 > 5:
        db_fileStat = sub.checkFileStatus()
        if not db_fileStat[1]:
            updateClicked(False)
            table_updateClicked = True
            not timerStarted0
            dpg.set_value(w1_text3, 'File encrypted.')

        else: startTime0 = time.time()

    if table_updateClicked:
        dpg.delete_item("content")
        updateWindow()
        dpg.set_value(oField_fileSize, "File size: %s" %table_size)
        table_updateClicked = False

    dpg.render_dearpygui_frame()

dpg.destroy_context()

# OPEN POINTS:
# [ADD]:    Main window where you can choose which program to open. ??
# [ToDo]:   rename programs to modules
# [ToDo]:   make it possible to change values in DB by choosing a cell [change button in menue to activate change mode]