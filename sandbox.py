import dearpygui.dearpygui as dpg

x = False
y = False

def toggleState():
    global x,y
    if x:
        x = False
        y = True
    elif y:
        y = False
        x = True
    else:
        y = True
    print('x:   ', x)
    print('y:   ', y)
    print('\n')

dpg.create_context()

# window one with exit button
with dpg.window(label='ui', width=300, height=300, pos=(0,0), tag='buttons'):
    b_exit = dpg.add_button(label='Toggle State', callback=toggleState, tag='button', enabled=True)


dpg.create_viewport(title='Sandbox', width=300, height=300, x_pos=1000, y_pos=100)
dpg.setup_dearpygui()
dpg.show_viewport()

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():

    if x:
        dpg.configure_item(b_exit, enabled= False, show=False)

    dpg.render_dearpygui_frame()
dpg.destroy_context()