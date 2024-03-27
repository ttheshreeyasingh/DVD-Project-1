import pandas as pd

with open(r'nmos_off.txt', 'r') as file:
    nmos_off = file.read()

    nmos_off=nmos_off.replace('  ',' ')

with open(r'nmos_off.txt', 'w') as file:    
    file.write(nmos_off)

with open (r'nmos_on.txt', 'r') as file:
    nmos_on = file.read()

    nmos_on=nmos_on.replace('  ',' ')

with open(r'nmos_on.txt', 'w') as file:
    file.write(nmos_on)

nmos_off_data=pd.read_table('nmos_off.txt', header=None, sep=' ')
nmos_off_data=nmos_off_data.dropna(axis=1)
nmos_off_data.columns=['Temperature', 'Vdd', 'Vdrain', 'Vgate', 'Vsource', 'Vbody', 'Idrain', 'Igate', 'Isource', 'Ibody']
nmos_off_data.to_csv('nmos_off.csv',index = None)

nmos_on_data=pd.read_table('nmos_on.txt', header=None, sep=' ')
nmos_on_data=nmos_on_data.dropna(axis=1)
nmos_on_data.columns=['Temperature', 'Vdd', 'Vdrain', 'Vgate', 'Vsource', 'Vbody', 'Idrain', 'Igate', 'Isource', 'Ibody']
nmos_on_data.to_csv('nmos_on.csv',index = None)