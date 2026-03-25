import glob
import time

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '10-*')[0]
device_file = device_folder + '/w1_slave'

def read_temp():
    with open(device_file, 'r') as f:
        lines = f.readlines()
        
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        with open(device_file, 'r') as f:
            lines = f.readlines()
            
    temp_pos = lines[1].find('t=');
    temp_string = lines[1][temp_pos+2:]
    temp_c = float(temp_string) / 1000.0
    
    return temp_c

while True:
    print(f"Temperature: {read_temp():.2f} C")
    time.sleep(1)
    
    