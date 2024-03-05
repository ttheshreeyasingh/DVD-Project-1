import os

template_netlist = 'nmos_template_off.net'
netlist_dir = 'netlists'
output_dir = 'simulation_results'

# transistor widths (W)
widths = ['45n', '90n', '135n', '180n', '270n', '360n']

# Create output directories if they don't exist
os.makedirs(netlist_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

for width in widths:
    # Generate modified netlist filename
    output_netlist = os.path.join(netlist_dir, f'netlist_width_{width}.net')
    
    # Read template netlist
    with open(template_netlist, 'r') as f:
        template_content = f.read()
    
    # Replace placeholders with parameter values
    modified_content = template_content.replace('{W}', width)
    
    # Write modified netlist to file
    with open(output_netlist, 'w') as f:
        f.write(modified_content)
    
    # Run Ngspice simulation
    os.system(f'ngspice {output_netlist} > {output_dir}/output_width_{width}.txt')
