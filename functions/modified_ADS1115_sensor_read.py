#sudo apt-get update
#sudo apt-get install build-essential python-pip python-dev python-smbus git
#git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
#cd Adafruit_Python_GPIO
#sudo python3 setup.py install
#cd ..
#git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
#cd Adafruit_Python_ADS1x15
#sudo python setup.py install



#   adc     addr-pin     address     chael0      chanel1     chanel2     chanel3        
#   1       ground       0x48        Vi          Vo	     ---         ---
#   2       vdd          0x49        Vpsu        Vbat        ---         Isys
#   3       sda          0x4A        Ii          Io          Io1         Io2
#   4       scl          0x4B        ---         ---         ---         ---
#

import Adafruit_ADS1x15 #import ADS1115

adc1 = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)  # Default I2C address
adc2 = Adafruit_ADS1x15.ADS1115(address=0x49, busnum=1)
adc3 = Adafruit_ADS1x15.ADS1115(address=0x4A, busnum=1)
#adc4 = Adafruit_ADS1x15.ADS1115(address=0x4B, busnum=1)
GAIN = 2/3 #this is to make th input voltage able to hadle 6 volts
count_gain = 6.144 / pow(2,15) #conversion from count ot volts with one bit is for sign
dc_gain = 26.4/4.46 #27/4	#gain from op amp adapter
ac_gain = 121.85/4.15 #177/5	#gain from op amp adapter

def getSensorData():
#           0    1  2  3  4  5  6  7  8    9    10   11   12   13   14  15  16  17 
    #data = bat%,Vb,Ib,Rb,Vo,Io,Vi,Ii,Vbuk,Ibuk,Vpsu,Ipsu,Vinv,Iinv,Vo1,Io1,Vo2,Io2
    data = [0   ,0 ,0 ,30,0 ,0 ,0 ,0 ,0   ,0   ,0   ,0   ,0   ,0   ,0  ,0  ,0  ,0]
	
	
    	
    #get ac charaterisics
    #AC voltage
    data[6] = adc1.read_adc(0,GAIN) * count_gain * ac_gain	#vi
    data[4] = adc1.read_adc(2,GAIN) * count_gain * ac_gain	#vo
    data[14] = data[4] #adc1.read_adc(2,GAIN) * count_gain * ac_gain	#vo1
    data[16] = data[4] #adc1.read_adc(3,GAIN) * count_gain * ac_gain	#vo2
    
    #print("adc1")

    #AC current
    sum = [0,0,0,0]
    count = 20
    for x in range(0,count):
        sum[0] = sum[0] + abs((adc3.read_adc(0,GAIN) * count_gain)-2.5) 	#ii
        sum[1] = sum[1] + abs((adc3.read_adc(1,GAIN) * count_gain)-2.5)	#io
        sum[2] = sum[2] + abs((adc3.read_adc(2,GAIN) * count_gain)-2.5)	#io1
        sum[3] = sum[3] + abs((adc3.read_adc(3,GAIN) * count_gain)-2.5)	#io2
        time.sleep(0.01)

    data[7]  = (sum[0]/count) *(50/2.5)	#ii
    data[5]  = (sum[1]/count) *(50/2.5)	#io
    data[15] = (sum[2]/count) *(50/2.5) 	#io1
    data[17] = (sum[3]/count) *(50/2.5) 	#io2

    #print("adc3")

    #get dc charaterisics
    #DC voltage
    data[10] = adc2.read_adc(0,GAIN) * count_gain * dc_gain	#vpsu
    data[1] = adc2.read_adc(1,GAIN) * count_gain * dc_gain	#vbat
    #data[8] = adc2.read_adc(2,GAIN) * count_gain * dc_gain	#vbuck
    #data[12] = adc2.read_adc(3,GAIN) * count_gain * dc_gain	#vinv
	

    #print("adc2")
    
    #DC current
    #data[11] = adc3.read_adc(0,GAIN) * count_gain * 	#i psu
    #data[2] = adc3.read_adc(1,GAIN) * count_gain * 	#i bat
    #data[9] = adc3.read_adc(2,GAIN) * count_gain * 	#i buck
    #data[13] = adc3.read_adc(3,GAIN) * count_gain * 	#i inv
    if (data[10] >=25) and (data[7] >= 0.3) and (data[6] >= 100):
        data[11] = ((adc2.read_adc(3,GAIN) * count_gain)-2.5) * (100/2.5)	#i psu
    else:
        data[2]  = ((adc2.read_adc(3,GAIN) * count_gain)-2.5) * (100/2.5)	#i bat


    return(data)
