import os
import pandas as pd
import dearpygui.dearpygui as dpg

x = 0
y = 1

dpg.create_context()

with dpg.window(label="Main Window"):
    dpg.add_text("Test one")
    dpg.add_button(label="Update")
    field1 = dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    print("this will run every frame")

    z = dpg.get_value(field1)
    print(z)
    dpg.render_dearpygui_frame()

dpg.destroy_context()