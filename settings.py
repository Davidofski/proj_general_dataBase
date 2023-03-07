# settings for context in main.py

# user interface dimentions
ui_width = 1000
ui_heigh = 1000

# window 1 [input] dimentions
window1_heigh = 350
window1_width = ui_width - 6
window1_xpos = 0
window1_ypos = 0

# window 2 [output] dimentions
window2_heigh = 700
window2_width = ui_width - 6
window2_xpos = 0
window2_ypos = window1_heigh

# item locations
item_xpos_offset = 50
item_ypos_offset = 30
item1_xpos = item_xpos_offset + 250         # item 1 = header
item1_ypos = item_ypos_offset * 1
item2_xpos = item_xpos_offset + 260         # item 2 = file read status successfull
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
item9_xpos = item_xpos_offset + 0         # item 9 = button save new clicked
item9_ypos = item_ypos_offset * 3
item10_xpos = item_xpos_offset + 700        # item 10 = button exit
item10_ypos = item_ypos_offset * 8

item11_xpos = item_xpos_offset              # item 11 = output today's date
item11_ypos = item_ypos_offset * 8
item12_xpos = item_xpos_offset + 200        # item 12 = output date difference
item12_ypos = item_ypos_offset * 9
item13_xpos = item_xpos_offset              # item 13 = fils status
item13_ypos = item_ypos_offset * 9

item16_xpos = item_xpos_offset + 700        # item 16 = exit and open encryption
item16_ypos = item_ypos_offset * 6

item22_xpos = item_xpos_offset + 700        # item 22 = exit and open show error log
item22_ypos = item_ypos_offset * 7
item23_xpos = item_xpos_offset + 700        # item 23 = sort entrys in table after DSLC
item23_ypos = item_ypos_offset * 4

item25_xpos = item_xpos_offset + 700        # item 25 = save changes clicked
item25_ypos = item_ypos_offset * 5

iField_width = 200
iField_heigh = 10

# colour setting for max day difference
table_maxDiff = 180
table_intDiff = 150

# de- and encryption
enc_width = 640
enc_heigh = 350

item14_xpos = item_xpos_offset         # header
item14_ypos = item_ypos_offset
item15_xpos = item_xpos_offset         # File status [True, Flase]
item15_ypos = item_ypos_offset * 3

item17_xpos = item_xpos_offset         # item 17 = input path of file to encrypt
item17_ypos = item_ypos_offset * 4
item18_xpos = item_xpos_offset         # item 18 = input password for encryption
item18_ypos = item_ypos_offset * 5
item19_xpos = item_xpos_offset         # item 19 = button encrypt file
item19_ypos = item_ypos_offset * 7
item20_xpos = item_xpos_offset + 155   # item 20 = button decrypt file
item20_ypos = item_ypos_offset * 7
item21_xpos = item_xpos_offset         # item 21 = button exit clicked
item21_ypos = item_ypos_offset * 8.5

item24_xpos = item_xpos_offset + 180   # item 24 = button update
item24_ypos = item_ypos_offset * 3

item26_xpos = item_xpos_offset         # item 26 = input confirm password
item26_ypos = item_ypos_offset * 6
item27_xpos = item_xpos_offset + 300   # item 27 = message pw not possible or incorrect
item27_ypos = item_ypos_offset * 3


# error log window
eL_width = 680
eL_height = 1000