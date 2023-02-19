import dearpygui.dearpygui as dpg
import settings as st
import errormessage as erm

db_fileName = "DB_PW.csv"
errorLogName = "errorLog.csv"

def exitClicked():
    dpg.stop_dearpygui()

log_content, log_maxEntry = erm.alterlog()

# resorting table to descending that newest logs are on top
sortedTabe = log_content.sort_values(by=['time stamp'], ascending=False)

dpg.create_context()

# window one with exit button
with dpg.window(label='ui', width=st.eL_width, height=50, pos=(0,0), tag='buttons'):
    b_exit = dpg.add_button(label='EXIT', callback=exitClicked)

# window 2 with descernding error log
with dpg.window(label="'%s' CONTENT" %errorLogName, width=st.eL_width, height=st.eL_height, pos=(0,50), tag="error log"):
    with dpg.table(label='Error Log', tag="table1", context_menu_in_body=True, borders_innerV=True, resizable=True, policy=dpg.mvTable_SizingFixedFit):
        for i in range(sortedTabe.shape[1]):                    # Generates the correct amount of columns
            dpg.add_table_column(label=sortedTabe.columns[i])   # Adds the headers
        for i in range(log_maxEntry):                            # shows all rows of the table
            with dpg.table_row():
                for j in range(sortedTabe.shape[1]):
                    if j == 1:
                        dpg.add_text(f"{sortedTabe.iloc[i,j]}", color=[255,0,100])
                    else:
                        dpg.add_text(f"{sortedTabe.iloc[i,j]}", color=[0,255,100])

dpg.create_viewport(title='Error Log', width=st.eL_width+13, height=st.eL_height+90, x_pos=1000, y_pos=100)
dpg.setup_dearpygui()
dpg.show_viewport()

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():

    dpg.render_dearpygui_frame()
dpg.destroy_context()