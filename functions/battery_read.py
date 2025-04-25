
#import time
import math
import Adafruit_ADS1x15 #import ADS1115

def Get_bat(data):
    adc1 = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)
    GAIN = 2/3   
    adc_v_conv = 6.144 / pow(2,15) #one bit is for sign     #3.3/26380

    tmp = [0,0,0,0]
    tmp[0] = ((adc1.read_adc(0,GAIN)*adc_v_conv) - 2.507) * (50/2)
    tmp[1] = adc1.read_adc(1,GAIN)*adc_v_conv*(26.65/3.477)
    #data[2] = adc1.read_adc(2,GAIN)*adc_v_conv
    #data[3] = adc1.read_adc(3,GAIN)*adc_v_conv
    #print(str(data[0])+"  "+str(data[1])) #+"  "+str(data[2])+"  "+str(data[3]))
    #time.sleep(0.5)
    data[1] = tmp[1]
    data[2] = tmp[0] 
    return(data)





