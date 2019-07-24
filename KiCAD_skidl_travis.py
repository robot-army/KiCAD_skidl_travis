from skidl import *
resistor = Part('Device', 'R', value='500', footprint='R_0805_2012Metric')
resistor.value = '1K'
ERC()
generate_netlist()
