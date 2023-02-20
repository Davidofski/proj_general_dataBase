import dearpygui.dearpygui as dpg
import pandas as pd
import sub

x = False
y = False

ds = {'Age':[1, 2, 3, 4, 5, 6], 'Name':['Hubert', 'David', 'Susie', 'Hermann', 'Petra', 'Manuela'], 'add info':[2,2,2,2,2,2]}

df = pd.DataFrame(ds)

print(df)

for i in df.items():
    print(i)

coloums = 3

while False:

    cell = int(input())
    row = cell//coloums
    y = cell/coloums
    coloumn = int(round(coloums*(y-row), 0))
    print('row:     ', row)
    print('coloumn: ', coloumn)

cell = '3_cell_11'
newValue = '01-01-1000'


sub.readFile()
sub.changeItem(cell, newValue)

newValue = 30 if cell == '3_cell_11' else 10