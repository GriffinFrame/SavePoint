
import time
#import math
import Adafruit_ADS1x15 #import ADS1115

 
adc1 = Adafruit_ADS1x15.ADS1115(address=0x4A, busnum=1) #(0x48)  # Default I2C address 
adc2 = Adafruit_ADS1x15.ADS1115(address=0x49, busnum=1)
#adc3 = ADS1115(address=0x4A)
#adc4 = ADS1115(address=0x4B)
GAIN = 2/3   
adc_v_conv = 6.144 / pow(2,15) #one bit is for sign
#hist = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
#point = 0


while(1):
    #data = [0,0,0,0]

    #data[0] = abs((adc1.read_adc(0,GAIN)*adc_v_conv)-2.5)
    #data[1] = abs((adc1.read_adc(1,GAIN)*adc_v_conv)-2.5)
    #data[2] = abs((adc1.read_adc(2,GAIN)*adc_v_conv)-2.5)
    #data[3] = abs((adc1.read_adc(3,GAIN)*adc_v_conv)-2.5)


    #hist[0][point] = data[0]
    #hist[1][point] = data[0]
    #hist[2][point] = data[0]
    #hist[3][point] = data[0]

    #point = point +1
    #if point >=10:
    #    point = 0
    stime = time.time()
    sum = [0,0,0,0]
    for x in range (0,20):
        sum[0] = sum[0] + abs((adc1.read_adc(0,GAIN)*adc_v_conv)-2.5)    #hist[0][x]
        sum[1] = sum[1] + abs((adc1.read_adc(1,GAIN)*adc_v_conv)-2.5)    #hist[1][x]
        sum[2] = sum[2] + abs((adc1.read_adc(2,GAIN)*adc_v_conv)-2.5)    #hist[2][x]
        sum[3] = sum[3] + abs((adc1.read_adc(3,GAIN)*adc_v_conv)-2.5)    #hist[3][x]
        #time.sleep(0.01)
    etime = time.time()

    #print(hist)
    #print(str(round(data[0],3))+"  "+str(round(data[1],3))+"  "+str(round(data[2],3))+"  "+str(round(data[3],3)))
    print(stime-etime)
    print(str(round(sum[0]/20,3))+"  "+str(round(sum[1]/20,3))+"  "+str(round(sum[2]/20,3))+"  "+str(round(sum[3]/20,3))+"\n")
    #time.sleep(0.2)
