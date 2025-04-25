####
##### bash: pip install adafruit-ads1x15
####

import time
import math
import Adafruit_ADS1x15 #import ADS1115

 
adc1 = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1) #(0x48)  # Default I2C address 
adc2 = Adafruit_ADS1x15.ADS1115(address=0x49, busnum=1)
#adc3 = ADS1115(address=0x4A)
#adc4 = ADS1115(address=0x4B)
GAIN = 2/3   
adc_v_conv = 6.144 / pow(2,15) #one bit is for sign     #3.3/26380
hist = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
point = 0

print("1 for acd 1 and not1 for adc 2")
select = (input())
print(select)

while(1):
    data = [0,0,0,0]
    if select == '1':
        print("adc 1")
        data[0] = adc1.read_adc(0,GAIN)*adc_v_conv
        data[1] = adc1.read_adc(1,GAIN)*adc_v_conv
        data[2] = adc1.read_adc(2,GAIN)*adc_v_conv
        data[3] = adc1.read_adc(3,GAIN)*adc_v_conv
    else:
        print("adc 2")
        data[0] = adc2.read_adc(0,GAIN)*adc_v_conv
        data[1] = adc2.read_adc(1,GAIN)*adc_v_conv
        data[2] = adc2.read_adc(2,GAIN)*adc_v_conv
        data[3] = adc2.read_adc(3,GAIN)*adc_v_conv





    hist[0][point] = data[0]
    hist[1][point] = data[1]
    hist[2][point] = data[2]
    hist[3][point] = data[3]

    point = point +1
    if point >=10:
        point = 0
    sum = [0,0,0,0]
    for x in range (0,10):
        sum[0] = sum[0] + hist[0][x]
        sum[1] = sum[1] + hist[1][x]
        sum[2] = sum[2] + hist[2][x]
        sum[3] = sum[3] + hist[3][x]

    #print(hist)
    print(str(round(data[0],3))+"  "+str(round(data[1],3))+"  "+str(round(data[2],3))+"  "+str(round(data[3],3)))
    print(str(round(sum[0]/10,3))+"  "+str(round(sum[1]/10,3))+"  "+str(round(sum[2]/10,3))+"  "+str(round(sum[3]/10,3))+"\n")
    time.sleep(0.5)
