import time


from functions.getGMTTime                           import getDateTime
from functions.sensor_simulate_discharge_non_lin    import getNewDataUNPWR
#from functions.sensor_getRNGData                    import getRNGData
from functions.nonlinearVoltageToBatPercent         import getBatEstamate
from functions.modified_ADS1115_sensor_read	    import getSensorData


while 1: # the big main loop
    
    try: #initialize the bool for if their is mains
        if init:
            #why wont it let me put an empty if
            #im trying to get it to discover its NULL
            1+1
    except:
        init = True
        powered = True
        data = [0,0,0,30,0,0,0,0,0,0]
        hist = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
        point = 0
    
    
    
    try: #create new log file each 10 min and init if the program has just started or errored
        if time.time() >= ctime+600:
            ctime = time.time()
            datalog.close()
            datalog = open("/var/www/html/logs/" + getDateTime(1) + ".csv",'a')
    except:
        datalog = open("/var/www/html/logs/" + getDateTime(1) + ".csv",'a')
        ctime = time.time()
    
    
    
    
    
    #data[] = bat%,vb,ib,rb,vo,io,vi,ii,vrec,irec
    #data = getData() # get sim data 
    #data = getNewDataUNPWR(data , 1) # updata sim data
    try:
        data = getSensorData()
    except:
        print("-----------sensor error----------------")
        data = [0,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        time.sleep(2)


    #----the getting data script should be replaced with the finalized version of ADS1115_sensor_read.py
    


    data = getBatEstamate(data)
    #----get battery percentage using battery_prediction_model.py  when it gets finalized
    #----put that variable somewhere
    # i think that we should run the battery prediction model on a separate thread and have it
    # update the main program when it can so we can not be time constrained by it and log more data
    
    print(data)# output for testing purposes this is not needed on the final program
    
    
    
    #----this is currently working on voltage and should be swaped to bat%
    if data[1] <= 23: #shuts down the sytem 
        print("battery undervoltage")
        print("shuting down")
        exit()
        #---- push that the system is shutting down to clients 
        #----i know im forgetting something that needs to be done here
        
    if (data[6] < 112) & powered: #mains failure 
        print("input undervoltage")
        print("moving to battery")
        powered = False
        #----turn off battery charger
        #the rest is passively switched
        
    if (data[6] > 125) & powered: #over voltage protection
        print("input overvoltage")
        print("moving to battery")
        powered = False
        #----turn off battery charger
        #nothing can be done for the power supply currently
        
        
    if (data[6] >= 112) & (data[6] <= 120) & (not powered):
        print("input restored")
        print("tranfering to mains")
        powered = True
        #----turn charger back on 
        
    
            
        
        
    
    #log files
    datalog.write(getDateTime(1)) #log the time
    datalog.write(", ") #buffer
    datalog.write(str(data).strip("[]")) #log the data
    #---- add the bat%
    datalog.write("\n") #seperate data logs
    

    # take the running average of the data to output to the active file
    #this will make the first few data points wilding innacurate
    hist[point] = data[0]
    point = point + 1
    if point > 9:
        point = 0
    sum = 0
    for x in range(0,10):
        sum = sum + hist[x]
    data[0] = sum/10
    #print(str(hist).strip("[]"))

    while 1:#wright current data to file
        try:# since this file will be opened by another program it might error so it will wait a little if it fails
            currentdata = open("/var/www/html/data.csv",'w')
            currentdata.write(str(data).strip("[]"))
            currentdata.close()
            break
        except:
            time.sleep(0.25)
            print("currentstate output error")    
        
    #time.sleep(1.5) #delay for testing purposes to not swamp the logs
    # i belive that once all the code is running together the 
    # time it takes to run the code can replace this

    
