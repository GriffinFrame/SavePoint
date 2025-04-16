import random
# this function is used to update a state of the system using previous data and a delta time in seconds
# this assumes that the inverter is functioning properly
# this function depletes the battery in a linear fission in a lead acid battery stile

#data[] = bat%,vb,ib,rb,vo,io,vi,ii,vrec,irec

def getNewDataUNPWR(data , time): 
    ib_old = data[2] 
    vb_old = data[1]
    rb = data[3] / 1000
    vbr_old = vb_old + ib_old*rb
    
    work = ib_old * vbr_old * time
    # new voltage is the old voltage nimus the percentage of the delta v linear to the AHr used and its max of 50 AHr
    vbr_new = vbr_old - 5.2*((ib_old*(time / 3600))/50)
    ib_new = random.random() * 50
    
    data[0] = (vbr_new-24) / 5.2
    data[1] = vbr_new-ib_new*0.02
    data[2] = ib_new
    data[3] = rb * 1000
    data[4] = 110 + random.random()*10
    data[5] = (data[1]*data[2])/data[4]
    data[6] = 0
    data[7] = 0
    data[8] = 0
    data[9] = 0
    return(data)