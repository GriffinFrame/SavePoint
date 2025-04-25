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
#   1       ground       0x48        Vi          Vo	     Vo1         Vo2
#   2       vdd          0x49        Vpsu        Vbat        Vbuck       Vinverter
#   3       sda          0x4A        Ipsu        Ibat        Ibuck       Iinverter
#   4       scl          0x4B        Ii          Io          Io1         Io2
#

import Adafruit_ADS1x15 #import ADS1115

adc1 = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)  # Default I2C address
adc2 = Adafruit_ADS1x15.ADS1115(address=0x49, busnum=1)
adc3 = Adafruit_ADS1x15.ADS1115(address=0x4A, busnum=1)
adc4 = Adafruit_ADS1x15.ADS1115(address=0x4B, busnum=1)
GAIN = 2/3 #this is to make th input voltage able to hadle 6 volts
count_gain = 6.144 / pow(2,15) #conversion from count ot volts with one bit is for sign
dc_gain = 27/4	#gain from op amp adapter
ac_gain = 177/5	#gain from op amp adapter

def getSensorData():
    #data = bat%,Vb,Ib,Rb,Vo,Io,Vi,Ii,Vbuk,Ibuk,Vpsu,Ipsu,Vinv,Iinv,Vo1,Io1,Vo2,Io2
    data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	
	
    #get dc charaterisics
    #voltage
    data[10] = adc2.read_adc(0,GAIN) * count_gain * dc_gain	#vpsu
    data[1] = adc2.read_adc(1,GAIN) * count_gain * dc_gain	#vbat
    data[8] = adc2.read_adc(2,GAIN) * count_gain * dc_gain	#vbuck
    data[12] = adc2.read_adc(3,GAIN) * count_gain * dc_gain	#vinv
	
    #current
    #data[11] = adc3.read_adc(0,GAIN) * count_gain * 	#i psu
    #data[2] = adc3.read_adc(1,GAIN) * count_gain * 	#i bat
    #data[9] = adc3.read_adc(2,GAIN) * count_gain * 	#i buck
    #data[13] = adc3.read_adc(3,GAIN) * count_gain * 	#i inv
	
    #get ac charaterisics
    #voltage
    data[6] = adc1.read_adc(0,GAIN) * count_gain * ac_gain	#vi
    data[4] = adc1.read_adc(1,GAIN) * count_gain * ac_gain	#vo
    data[14] = adc1.read_adc(2,GAIN) * count_gain * ac_gain	#vo1
    data[16] = adc1.read_adc(3,GAIN) * count_gain * ac_gain	#vo2
	
    #current
    #data[7] = adc4.read_adc(0,GAIN) * count_gain * 	#ii
    #data[5] = adc4.read_adc(1,GAIN) * count_gain * 	#io
    #data[15] = adc4.read_adc(2,GAIN) * count_gain * 	#io1
    #data[17] = adc4.read_adc(3,GAIN) * count_gain * 	#io2
	return(data)
