import pandas as pd
import cryptpandas as crp
import dearpygui.dearpygui as dpg
import settings as st
import os
import errormessage as erm

db_fileName = "DB_PW.csv"
db_path = r"C:\Users\David\OneDrive\Dokumenter\GitHub\proj_general_dataBase\DB_PW.csv"
crypt_path = r"C:\Users\David\OneDrive\Dokumenter\GitHub\proj_general_dataBase\DB_PW.crypt"
main_path = r"C:\Users\David\OneDrive\Dokumenter\GitHub\proj_general_dataBase\main.py"
encrypted = False
decrypted = False

token = b'\xbf\xb9=\xb9\x140\xb1\xe1\x19\xd5CP\tR\x89\xa9n\xec\x16\x12,\xdcF\xe8/\xfd;\xb5\xb7\xbbo\x80'

def exitClicked():
    dpg.stop_dearpygui()
    if decrypted:
        os.startfile(main_path)

def readFile():
    global encrypted, decrypted
    encrypted = os.path.isfile(crypt_path)
    decrypted = os.path.isfile(db_path)

    if encrypted == False and decrypted == False:
        errorCode = 7
        erm.saveErrorLog(errorCode)

    if decrypted: 
        db_loaded = pd.read_csv(db_path, sep=";", index_col=[0])
        return db_loaded

def saveFile(db_decrypted):
    db_toSave = pd.DataFrame(db_decrypted)
    db_toSave.to_csv('%s' %db_fileName, sep=';')

def encryptFile():
    global decrypted, encrypted
    if decrypted:
        db_loaded = readFile()
        pw = password()
        crp.to_encrypted(db_loaded, password=pw, path=crypt_path, salt=token)
        os.remove(db_path)
        encrypted = True
        decrypted = False

def decryptFile():
    global encrypted, decrypted
    if encrypted:
        pw = password()
        db_decrypted = crp.read_encrypted(path=crypt_path, password=pw, salt=token)
        saveFile(db_decrypted)
        os.remove(crypt_path)
        decrypted = True
        encrypted = False
    
def password():
    allowed = False
    number = ['1','2','3','4','5','6','7','8','9','0']
    character = ['!','-','_']
    pw = str(dpg.get_value(iF_pw))

    if len(pw) > 8:
        allowed = True

    for i in number:
        x = pw.find(i)    
        if x > -1:
            for i in character:
                x = pw.find(i)
                if x > -1:
                    allowed = True

    if allowed == True:
        return pw
    else:
        exit()

readFile()

dpg.create_context()
with dpg.window(label="De- and Encrypting %s" %db_fileName, width=st.enc_width, height=st.enc_heigh, pos=(0,0)):
    dpg.add_text("Progam to de- and encrypt database.", pos=(st.item14_xpos, st.item14_ypos))

    if decrypted:
        dpg.add_text("Uncrypted file found.", pos=(st.item15_xpos, st.item15_ypos))
    elif encrypted:
        dpg.add_text("Encrypted file found.", pos=(st.item15_xpos, st.item15_ypos))
    else:
        dpg.add_text("File NOT found! -> Check file location or path!", pos=(st.item15_xpos, st.item15_ypos))

    iF_path = dpg.add_input_text(label='path', hint='C:\somewhere\inFolder', pos=(st.item17_xpos, st.item17_ypos), height=st.iField_heigh, width=st.iField_width + 150)
    iF_pw = dpg.add_input_text(label='password', hint='some password; [no spaces allowed]', no_spaces=True, pos=(st.item18_xpos, st.item18_ypos), height=st.iField_heigh, width=st.iField_width + 100)
    
    b_encrypt = dpg.add_button(label='Encrypt', callback=encryptFile, pos=(st.item19_xpos, st.item19_ypos))
    b_decrypt = dpg.add_button(label='Decrypt', callback=decryptFile, pos=(st.item20_xpos, st.item20_ypos))
    b_exit = dpg.add_button(label='Exit', callback=exitClicked, pos=(st.item21_xpos, st.item21_ypos))

dpg.create_viewport(title='Data Base de- and encryption', width=st.enc_width, height=st.enc_heigh, x_pos=1000, y_pos=100)
dpg.setup_dearpygui()
dpg.show_viewport()

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():

    dpg.render_dearpygui_frame()
dpg.destroy_context()