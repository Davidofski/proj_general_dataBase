import pandas as pd
import cryptpandas as crp
import dearpygui.dearpygui as dpg
import settings as st
import os
import errormessage as erm

db_fileName = "DB_PW.csv"
currentDirectory = os.getcwd()
db_path = currentDirectory + r"\%s"%db_fileName
main_path = currentDirectory + r"\main.exe"
encrypted = False
decrypted = False
stateChange = False

dongel = b'\xbf\xb9=\xb9\x140\xb1\xe1\x19\xd5CP\tR\x89\xa9n\xec\x16\x12,\xdcF\xe8/\xfd;\xb5\xb7\xbbo\x80'

def exitClicked():
    dpg.stop_dearpygui()

def updateClicked():
    currentDirectory = os.getcwd()
    db_path = currentDirectory + r"\%s"%db_fileName
    if len(db_path) > 60:
        path = db_path[:20] + '......' + db_path[-30:]
    dpg.set_value(t_path, 'Path: %s' %path)
    dpg.set_value(t_message, '')
    readFile()

def readFile():
    global encrypted, decrypted, fileExists, stateChange
    fileExists = os.path.isfile(db_path)

    if fileExists:
        try:
            db_loaded = pd.read_csv(db_path, sep=";",
                                    index_col=[0])
            if db_loaded.empty:
                encrypted = True
                stateChange = True
            else:
                decrypted = True
                stateChange = True
                return db_loaded
        except:
            print('[DEBUG]  Error occured during reading file')
    else:
        errorCode = 7
        erm.saveErrorLog(errorCode)

def saveFile(db_decrypted):
    db_toSave = pd.DataFrame(db_decrypted)
    db_toSave.to_csv('%s' %db_fileName, sep=';')

def errorMessage(message):
    print(f'[INFO]  errorMessage with {message} as message.')

    if message == 'youShallNotPass':
        dpg.set_value(t_message,
                      'Password does not fit requirements!')

    if message == 'negative':
        dpg.set_value(t_message, 'DE- or En-cryption failed!')

def encryptFile():
    global decrypted, encrypted, stateChange

    if decrypted:
        try:
            db_loaded = readFile()
            print('[DEBUG]  file read')
            pw = password()
            print(f'[DEBUG]  pw handled and returned {pw}')
            if pw != 'youShallNotPass':
                crp.to_encrypted(db_loaded,
                                 password=pw,
                                 path=db_path,
                                 salt=dongel)
                encrypted = True
                decrypted = False
                stateChange = True
                dpg.set_value(iF_pw, '')
                dpg.set_value(iF_cpw, '')
                dpg.set_value(t_message, '')
            else:
                errorMessage('youShallNotPass')
        except: errorMessage('negative')

def decryptFile():
    global encrypted, decrypted, stateChange

    if encrypted:
        try:
            pw = password()
            if pw != 'youShallNotPass':
                db_decrypted = crp.read_encrypted(path=db_path,
                                                  password=pw,
                                                  salt=dongel)
                saveFile(db_decrypted)
                decrypted = True
                encrypted = False
                stateChange = True
                dpg.set_value(iF_pw, '')
                dpg.set_value(iF_cpw, '')
                dpg.set_value(t_message, '')
            else:
                errorMessage('youShallNotPass')
        except: errorMessage('negative')
    
    
def password():
    allowed = False
    number = ['1','2','3','4','5','6','7','8','9','0']
    character = ['!','-','_']
    pw = str(dpg.get_value(iF_pw))
    cpw = str(dpg.get_value(iF_cpw))

    if len(pw) > 8:
        allowed = True

    for i in number:
        x = pw.find(i)    
        if x > -1:
            for i in character:
                x = pw.find(i)
                if x > -1:
                    allowed = True

    if allowed == True and pw == cpw:
        return pw
    else:
        return 'youShallNotPass'

readFile()

dpg.create_context()
with dpg.window(label="De- and Encrypting %s" %db_fileName,
                width=st.enc_width,
                height=st.enc_heigh,
                pos=(0,0),
                tag='mainwindow'):
    dpg.add_text("Progam to de- and encrypt database.\nAttention!! Dongle of this program used, file can't be encrypted without!",
                 pos=(st.item14_xpos,
                      st.item14_ypos))
    t_fileStatus = dpg.add_text("No file found",
                                pos=(st.item15_xpos,
                                     st.item15_ypos),
                                     tag='fileStatus')
    if len(db_path) > 60:
        # shorten the displayed path so it doesn't exceed the window size
        path = db_path[:20] + '......' + db_path[-30:]    
    t_path = dpg.add_text("Path: %s" %path,
                          pos=(st.item17_xpos,
                               st.item17_ypos))
    t_message = dpg.add_text("",
                             pos=(st.item27_xpos, st.item27_ypos),
                             color=(255,0,0))
    
    iF_pw = dpg.add_input_text(label='password',
                               hint='some password; [no spaces allowed]',
                               no_spaces=True,
                               pos=(st.item18_xpos,
                                    st.item18_ypos),
                                    height=st.iField_heigh,
                                    width=st.iField_width + 140)
    iF_cpw = dpg.add_input_text(label='confirm password',
                                hint='same as above',
                                no_spaces=True,
                                pos=(st.item26_xpos, st.item26_ypos),
                                height=st.iField_heigh,
                                width=st.iField_width + 140)
    
    b_encrypt = dpg.add_button(label='Encrypt',
                               callback=encryptFile,
                               pos=(st.item19_xpos,
                                    st.item19_ypos))
    b_decrypt = dpg.add_button(label='Decrypt',
                               callback=decryptFile,
                               pos=(st.item20_xpos, st.item20_ypos))
    b_exit = dpg.add_button(label='Exit', callback=exitClicked,
                            pos=(st.item21_xpos, st.item21_ypos))
    b_update = dpg.add_button(label='Update', callback=updateClicked,
                              pos=(st.item24_xpos, st.item24_ypos))

dpg.create_viewport(title='Data Base de- and encryption',
                    width=st.enc_width,
                    height=st.enc_heigh,
                    x_pos=1000, y_pos=100)
dpg.setup_dearpygui()
dpg.show_viewport()

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():

    if encrypted and fileExists and stateChange:
        dpg.delete_item('fileStatus')
        t_fileStatus = dpg.add_text("File EN-crypted",
                                    pos=(st.item15_xpos,
                                         st.item15_ypos),
                                         color=[255,0,0],
                                         tag='fileStatus',
                                         parent='mainwindow')
        dpg.configure_item(b_encrypt, show=False, enabled=False)
        dpg.configure_item(b_decrypt, show=True, enabled=True)
        stateChange = False

    if decrypted and fileExists and stateChange:
        dpg.delete_item('fileStatus')
        t_fileStatus = dpg.add_text("File DE-crypted",
                                    pos=(st.item15_xpos,
                                         st.item15_ypos),
                                         color=[0,255,100],
                                         tag='fileStatus',
                                         parent='mainwindow')
        dpg.configure_item(b_decrypt, show=False, enabled=False)
        dpg.configure_item(b_encrypt, show=True, enabled=True)
        stateChange = False

    if stateChange:
        print(f'[DEBUG] decrypted: {decrypted}')
        print(f'[DEBUG] encrypted: {encrypted}')
        print(f'[DEBUG] stateChange: {stateChange}')

    dpg.render_dearpygui_frame()
dpg.destroy_context()