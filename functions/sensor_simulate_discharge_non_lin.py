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
    
    
    # calulate new voltage via non linear relationship
    # asumes a 50 AH battery with a high of 27.2(resting) and a low of 20
    amphr = data[0]*50 
    amphr_new = amphr - data[2]*(time/3600)
    bat_new = amphr_new/50
    if bat_new >= 0.90:
        vbr_new = 26.8 + (bat_new-0.9)*(1/25)
    elif bat_new >= 0.80:
        vbr_new = 26.6 + (bat_new-0.8)*(1/50)
    elif bat_new >= 0.70:
        vbr_new = 26.4 + (bat_new-0.7)*(1/50)
    elif bat_new >= 0.60:
        vbr_new = 26.2 + (bat_new-0.6)*(1/50)
    elif bat_new >= 0.50:
        vbr_new = 26.1 + (bat_new-0.5)*(1/100)
    elif bat_new >= 0.40:
        vbr_new = 26.0 + (bat_new-0.4)*(1/100)
    elif bat_new >= 0.30:
        vbr_new = 25.8 + (bat_new-0.3)*(1/50)
    elif bat_new >= 0.20:
        vbr_new = 25.6 + (bat_new-0.2)*(1/50)
    elif bat_new >= 0.10:
        vbr_new = 24 + (bat_new-0.1)*(1/25)
    else: 
        vbr_new = 20 + (bat_new)*(1/5)    
    
    ib_new = random.random() * 50
    
    data[0] = bat_new
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