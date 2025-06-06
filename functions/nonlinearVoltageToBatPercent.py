# this is a program that will estimate the bat% using the real voltage
# this program is based on a non linear vb bat% curve


#data[] = bat%,vb,ib,rb,vo,io,vi,ii,vrec,irec

def getBatEstamate(data): 
    vb = data[1]
    ib = data[2]
    rb = data[3]
    vb_real = vb + (ib*(rb/1000))
    
    if vb_real <= 20:
        bat = 0
    elif vb_real < 24:
        bat = (vb_real-20)*(5/2)+0
    elif vb_real < 25.6:
        bat = (vb_real-24)*(25/4)+10
    elif vb_real < 25.8:
        bat = (vb_real-25.6)*(50)+20
    elif vb_real < 26.0:
        bat = (vb_real-25.8)*(50)+30
    elif vb_real < 26.1:
        bat = (vb_real-26.0)*(100)+40
    elif vb_real < 26.2:
        bat = (vb_real-26.1)*(100)+50
    elif vb_real < 26.4:
        bat = (vb_real-26.2)*(50)+60
    elif vb_real < 26.6:
        bat = (vb_real-26.4)*(50)+70
    elif vb_real < 26.8:
        bat = (vb_real-26.6)*(50)+80
    elif vb_real < 27.2:
        bat = (vb_real-26.8)*(25)+90
    else: 
        bat = 100
    data[0] = bat/100
    return(data)
