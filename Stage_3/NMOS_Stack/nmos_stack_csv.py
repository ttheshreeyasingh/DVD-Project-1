import pandas as pd

with open(r'nstack.txt', 'r') as file:
    nmos_stack = file.read()

    nmos_stack=nmos_stack.replace('  ',' ')

with open(r'nstack.txt', 'w') as file:    
    file.write(nmos_stack)

nmos_stack_data=pd.read_table('nstack.txt', header=None, sep=' ')
nmos_stack_data=nmos_stack_data.dropna(axis=1)
nmos_stack_data.columns=['Temperature', 'Vdd', 'Va', 'Vb', 'Vx', 'LeakagePower']
nmos_stack_data.to_csv('nmos_stack.csv',index = None)