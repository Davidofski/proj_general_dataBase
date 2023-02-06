# settings for context in main.py

# user interface dimentions
ui_width = 1000
ui_heigh = 1000

# window 1 [input] dimentions
window1_heigh = 300
window1_width = ui_width - 6
window1_xpos = 0
window1_ypos = 0

# window 2 [output] dimentions
window2_heigh = 700
window2_width = ui_width - 6
window2_xpos = 0
window2_ypos = 300

# item locations
item_xpos_offset = 50
item_ypos_offset = 30
item1_xpos = item_xpos_offset + 250         # item 1 = header
item1_ypos = item_ypos_offset * 1
item2_xpos = item_xpos_offset + 250         # item 2 = file read status successfull
item2_ypos = item_ypos_offset * 1.8
item3_xpos = item_xpos_offset + 250         # item 3 = error message
item3_ypos = item_ypos_offset * 1.8
item4_xpos = item_xpos_offset               # item 4 = input platform
item4_ypos = item_ypos_offset * 4
item5_xpos = item_xpos_offset               # item 5 = input email
item5_ypos = item_ypos_offset * 5
item6_xpos = item_xpos_offset               # item 6 = input password
item6_ypos = item_ypos_offset * 6
item7_xpos = item_xpos_offset + 480         # item 7 = input date picker
item7_ypos = item_ypos_offset * 4
item8_xpos = item_xpos_offset               # item 8 = input additional information
item8_ypos = item_ypos_offset * 7
item9_xpos = item_xpos_offset + 700         # item 9 = button save
item9_ypos = item_ypos_offset * 4
item10_xpos = item_xpos_offset + 700        # item 10 = button exit
item10_ypos = item_ypos_offset * 5

item16_xpos = item_xpos_offset + 700        # If file found path
item16_ypos = item_ypos_offset * 6

item11_xpos = item_xpos_offset              # item 11 = output today's date
item11_ypos = item_ypos_offset * 8
item12_xpos = item_xpos_offset              # item 12 = output date difference
item12_ypos = item_ypos_offset
item13_xpos = item_xpos_offset + 160        # item 13 = spare
item13_ypos = item_ypos_offset * 2.3

iField_width = 200
iField_heigh = 10

# colour setting for max day difference
table_maxDiff = 180
table_intDiff = 150

# de- and encryption
enc_width = 500
enc_heigh = 500

item14_xpos = item_xpos_offset         # header
item14_ypos = item_ypos_offset
item15_xpos = item_xpos_offset         # File found [True, Flase]
item15_ypos = item_ypos_offset * 2

item17_xpos = item_xpos_offset         # item 17 = input path of file to encrypt
item17_ypos = item_ypos_offset * 4
item18_xpos = item_xpos_offset         # item 18 = input password for encryption
item18_ypos = item_ypos_offset * 5
item19_xpos = item_xpos_offset         # item 19 = button encrypt file
item19_ypos = item_ypos_offset * 6
item20_xpos = item_xpos_offset + 100   # item 20 = button decrypt file
item20_ypos = item_ypos_offset * 6
item21_xpos = item_xpos_offset         # item 21 = button exit clicked
item21_ypos = item_ypos_offset * 7