import dearpygui.dearpygui as dpg
import settings as st
import errormessage as erm

db_fileName = "DB_PW.csv"
errorLogName = "errorLog.csv"

def exitClicked():
    dpg.stop_dearpygui()

# altering error code numbers to understandable text
log_content, log_maxEntry = erm.alterlog()

# resorting table to descending that newest logs are on top
sortedTabe = log_content.sort_values(by=['time stamp'],
                                     ascending=False)

dpg.create_context()

# window with exit button and descernding error log
with dpg.window(label="'%s' CONTENT" %errorLogName,
                width=st.eL_width,
                height=st.eL_height,
                pos=(0,0),
                tag="error log"):
    b_exit = dpg.add_button(label='EXIT',
                            callback=exitClicked)
    with dpg.table(label='Error Log',
                   tag="table1",
                   context_menu_in_body=True,
                   borders_innerV=True,
                   resizable=True,
                   policy=dpg.mvTable_SizingFixedFit):
        for i in range(sortedTabe.shape[1]):
            dpg.add_table_column(label=sortedTabe.columns[i])
        for i in range(log_maxEntry):
            with dpg.table_row():
                for j in range(sortedTabe.shape[1]):
                    if j == 1:
                        dpg.add_text(f"{sortedTabe.iloc[i,j]}",
                                     color=[255,0,100])
                    else:
                        dpg.add_text(f"{sortedTabe.iloc[i,j]}",
                                     color=[0,255,100])

dpg.create_viewport(title='Error Log',
                    width=st.eL_width+13,
                    height=st.eL_height+38,
                    x_pos=1000,
                    y_pos=100)
dpg.setup_dearpygui()
dpg.show_viewport()

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():

    dpg.render_dearpygui_frame()
dpg.destroy_context()