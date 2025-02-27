####
##### bash: pip install adafruit-ads1x15
####




import time
import math
from Adafruit_ADS1x15 import ADS1115

 
adc = ADS1115(address=0x48)  # Default I2C address 
GAIN = 1   
 
R1 = 4000000   
R2 = 1000000   
divider_factor = R2 / (R1 + R2)  # The scaling factor for voltage divider

#constants for scaling
VREF = 6.0  # Max ADC input voltage 
MAX_VOLTAGE = 29.2  # Full battery voltage  

# SCT-013-000 current sensor constants
V_CURRENT_MIN = 2.0  # Minimum voltage from the current sensor (0A)
V_CURRENT_MAX = 5.5  # Maximum voltage from the current sensor (e.g., 100A)
CURRENT_MAX = 100.0  # Maximum current corresponding to 5.5V (in Amperes)

# Function to read voltage from the ADC 
def read_voltage(): 
    raw_value = adc.read_adc(0, gain=GAIN)
    voltage = (raw_value / 32767.0) * VREF
    actual_voltage = voltage / divider_factor
    
    return actual_voltage

# Function to read current from SCT-013-000 sensor 
# The sensor uses 2 analog pins but every example ive found only use 1
def read_current():
    raw_value = adc.read_adc(1, gain=GAIN)   
    voltage = (raw_value / 32767.0) * VREF   
    
    # Current = (V_sensor - 2.0V) / (3.5V) * 100A
    current = ((voltage - V_CURRENT_MIN) / (V_CURRENT_MAX - V_CURRENT_MIN)) * CURRENT_MAX
    
    return current

# Function to estimate battery charge and runtime
def estimate_battery_state(voltage, current):
    # linear approximation
    SOC = (voltage - 23) / (29.2 - 23) * 100  # State of Charge (%)

    battery_capacity = 50  # in Ah 
    remaining_capacity = (SOC / 100) * battery_capacity
    
    # Estimate runtime in hours
    if current != 0:  # had to put this shit in cuz it shit out during testing
        runtime = remaining_capacity / current
    else:
        runtime = 0  # No current, no runtime
    
    return SOC, remaining_capacity, runtime




while True:
 
    voltage = read_voltage()
    current = read_current()
     
    SOC, remaining_capacity, runtime = estimate_battery_state(voltage, current)
     
    print(f"Voltage: {voltage:.2f} V")
    print(f"Current: {current:.2f} A")
    print(f"State of Charge (SOC): {SOC:.2f}%")
    print(f"Remaining Capacity: {remaining_capacity:.2f} Ah")
    print(f"Estimated Runtime: {runtime:.2f} hours")
     
    time.sleep(2) # was 1 but it was pulling too much memory when running the svm


