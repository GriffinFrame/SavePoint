import time
import random

def getData(): #this function is a placeholder that genreates a random state of data assuming its not on mains
    data = [0,0,0,0,0,0,0,0,0,0]
    
    vbr = random.random() * 5.2 + 24
    ib = random.random() * 50
    
    data[0] = (vbr-24) / 5.1
    data[1] = vbr-ib*0.02
    data[2] = ib
    data[3] = 20
    data[4] = 105 + random.random()*20
    data[5] = random.random() * 8
    data[6] = 0
    data[7] = 0
    data[8] = 0
    data[9] = 0
    return(data)
    
    
    

while 1: # the big main loop
    
    try: #initialize the bool for if their is mains
        if powered:
            #why wont it let me put an empty if
            #im trying to get it to discover its NULL
            1+1
    except:
        powered = True
    
    
    
    try: #create new log file each 10 min and init if the program has just started or errored
        if time.time() >= ctime+600:
            datalog.close()
            ctime = time.time()
            tmpstring = "data_"
            tmpstring = tmpstring + str(int(ctime - ctime%1))
            tmpstring = tmpstring + ".csv"
            datalog = open(tmpstring,'a')
    except:
        ctime = time.time()
        tmpstring = "data_"
        tmpstring = tmpstring + str(int(ctime - ctime%1))
        tmpstring = tmpstring + ".csv"
        datalog = open(tmpstring,'a')
    
    
    
    
    
    
    
    #data[] = bat%,vb,ib,rb,vo,io,vi,ii,vrec,irec
    data = getData() # get data 
    #----the getting data script should be replaced with the finalized version of ADS1115_sensor_read.py
    
    print(data)# output for testing purposes this is not needed on the final program
    
    #----get battery percentage using battery_prediction_model.py  when it gets finalized
    #----put that variable somewhere 
    # i think that we should run the battery prediction model on a separate thread and have it
    # updte the main program when it can so we can not be time constrained by it and log more data
    
    
    
    #----this is currently working on voltage and should be swaped to bat%
    if data[1] <= 23: #shuts down the sytem 
        print("battery undervoltage")
        Pring("shuting down")
        #---- push that the system is shutting down to clients 
        #----i know im forgetting something that needs to be done here
        
    if (data[6] < 112) & powered: #mains failure 
        print("input undervoltage")
        print("moving to battery")
        powered = False
        #----turn off battery charger
        #to my knowledge the rest is passively switched
        
    if (data[6] > 120) & powered: #over voltage protection
        print("input overvoltage")
        print("moving to battery")
        powered = False
        #----turn off battery charger
        
        
    if (data[6] >= 112) & (data[6] <= 120) & (not powered):
        print("input restored")
        print("tranfering to mains")
        powered = True
        #----turn charger back on 
        
    
            
        
        
    
    #log files
    datalog.write(str(time.time())) #log the time
    datalog.write("    ") #buffer
    datalog.write(str(data)) #log the data
    #---- add the bat%
    datalog.write("\n") #seperate data logs
        
    time.sleep(2.5) #delay for testing purposes to not swamp the logs
    # i belive that once all the code is running together the 
    # time it takes to run the code can replace this

    