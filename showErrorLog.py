import dearpygui.dearpygui as dpg
import settings as st
import os
import errormessage as erm

db_fileName = "DB_PW.csv"
errorLogName = "errorLog.csv"

def exitClicked():
    dpg.stop_dearpygui()
    os.startfile(r"C:\Users\David\OneDrive\Dokumenter\GitHub\proj_general_dataBase\main.py")

def getMaxEntry():
    pass

log_content, log_maxEntry = erm.alterlog()

dpg.create_context()
with dpg.window(label='ui', width=st.eL_width, height=50, pos=(0,0), tag='buttons'):
    b_exit = dpg.add_button(label='EXIT', callback=exitClicked)
with dpg.window(label="'%s' CONTENT" %errorLogName, width=st.eL_width, height=st.eL_height, pos=(0,50), tag="error log"):
    with dpg.table(label='Error Log', tag="table1", context_menu_in_body=True, precise_widths=True, inner_width=10, borders_innerH=True):
        for i in range(log_content.shape[1]):                    # Generates the correct amount of columns
            dpg.add_table_column(label=log_content.columns[i])   # Adds the headers
        for i in range(log_maxEntry):                            # shows all rows of the table
            with dpg.table_row():
                for j in range(log_content.shape[1]):
                    if j == 5:
                        if int(log_content.iloc[i,j]) > st.table_maxDiff:     # check if the date is in the allowed range
                            dpg.add_text(f"{log_content.iloc[i,j]}", color=[255,0,0])     # Displays the value of each row/column combination
                        elif int(log_content.iloc[i,j]) > st.table_intDiff and int(log_content.iloc[i,j]) < st.table_maxDiff:
                            dpg.add_text(f"{log_content.iloc[i,j]}", color=[255,255,0])
                        else:
                            dpg.add_text(f"{log_content.iloc[i,j]}")
                    else:
                        dpg.add_text(f"{log_content.iloc[i,j]}", color=[0,255,100])

dpg.create_viewport(title='Error Log', width=st.eL_width+20, height=st.eL_height+100, x_pos=1000, y_pos=100)
dpg.setup_dearpygui()
dpg.show_viewport()

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():

    dpg.render_dearpygui_frame()
dpg.destroy_context()