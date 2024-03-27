import pandas as pd

with open(r'pstack.txt', 'r') as file:
    pmos_stack = file.read()

    pmos_stack=pmos_stack.replace('  ',' ')

with open(r'pstack.txt', 'w') as file:    
    file.write(pmos_stack)

pmos_stack_data=pd.read_table('pstack.txt', header=None, sep=' ')
pmos_stack_data=pmos_stack_data.dropna(axis=1)
pmos_stack_data.columns=['Temperature', 'Vdd', 'Va', 'Vb', 'Vx', 'LeakagePower']
pmos_stack_data.to_csv('pmos_stack.csv',index = None)