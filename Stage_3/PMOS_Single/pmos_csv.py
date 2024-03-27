import pandas as pd

with open(r'pmos_off.txt', 'r') as file:
    pmos_off = file.read()

    pmos_off=pmos_off.replace('  ',' ')

with open(r'pmos_off.txt', 'w') as file:    
    file.write(pmos_off)

with open (r'pmos_on.txt', 'r') as file:
    pmos_on = file.read()

    pmos_on=pmos_on.replace('  ',' ')

with open(r'pmos_on.txt', 'w') as file:
    file.write(pmos_on)

pmos_off_data=pd.read_table('pmos_off.txt', header=None, sep=' ')
pmos_off_data=pmos_off_data.dropna(axis=1)
pmos_off_data.columns=['Temperature', 'Vdd', 'Vdrain', 'Vgate', 'Vsource', 'Vbody', 'Idrain', 'Igate', 'Isource', 'Ibody']
pmos_off_data.to_csv('pmos_off.csv',index = None)

pmos_on_data=pd.read_table('pmos_on.txt', header=None, sep=' ')
pmos_on_data=pmos_on_data.dropna(axis=1)
pmos_on_data.columns=['Temperature', 'Vdd', 'Vdrain', 'Vgate', 'Vsource', 'Vbody', 'Idrain', 'Igate', 'Isource', 'Ibody']
pmos_on_data.to_csv('pmos_on.csv',index = None)