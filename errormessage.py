import dearpygui.dearpygui as dpg
import settings as st
import main

db_fileName = "DB_PW.csv"

# messages
em1 = "ERROR:[1]   File could not be found!"
em2 = "ERROR:[2]   Could not safe dataframe to csv!"
em3 = "ERROR:[3]   Path could not be found or has been changed!"
em4 = "ERROR:[4]   Updating 'days since last change' in csv file not possible"

def exitClicked():
    dpg.stop_dearpygui()

def errorMessage():
    main.handOverErrorCode(error_code, error_code_rd)

    # error_code, error_code_rd = main.handOverErrorCode()
        # GUI
    dpg.create_context()

    with dpg.window(label="Failure in handling: '%s'" %db_fileName, width=st.uifm_width, height=st.uifm_heigh):

        if error_code == 1:
            text1 = dpg.add_text(em2, color=[255,0,0])        
        if error_code == 2:
            text2 = dpg.add_text(em2, color=[255,0,0])
        if error_code_rd == 3:
            text3 = dpg.add_text(em3, color=[255,0,0])
        if error_code_rd == 4:
            text4 = dpg.add_text(em3, color=[255,0,0])

        button1 = dpg.add_button(label="OK", callback=exitClicked)
            
    dpg.create_viewport(title='ERROR MESSAGE', width=st.uifm_width + 10, height=st.uifm_heigh, x_pos=1000, y_pos=0)
    dpg.setup_dearpygui()
    dpg.show_viewport()

    # below replaces, start_dearpygui()
    while dpg.is_dearpygui_running():
        # space for all running operations

        dpg.render_dearpygui_frame()

    dpg.destroy_context()