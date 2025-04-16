import random
#this function generates a random unpowered state for the system
#this assumes that the inverter is working properly but has fluctuations
# the battery percentage is canulated as if it were a lead acid 

#data[] = bat%,vb,ib,rb,vo,io,vi,ii,vrec,irec

def getRNGData(): 
    data = [0,0,0,0,0,0,0,0,0,0]
    
    vbr = random.random() * 5.2 + 24
    ib = random.random() * 50
    
    data[0] = (vbr-24) / 5.1
    data[1] = vbr-ib*0.02
    data[2] = ib
    data[3] = 20
    data[4] = 110 + random.random()*10
    data[5] = random.random() * 8
    data[6] = 0
    data[7] = 0
    data[8] = 0
    data[9] = 0
    return(data)