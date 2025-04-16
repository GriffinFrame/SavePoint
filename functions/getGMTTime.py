import time
# this function gets the current GMT time and convertis it into a string in the YYYYMMDD/HHMMSS format with the seconds being optional
def getDateTime(sec):
    ctime = time.gmtime(time.time())
    timestr =str(ctime.tm_year)
    if ctime.tm_mon < 10:
        timestr = timestr + "0" + str(ctime.tm_mon)
    else:
        timestr = timestr + str(ctime.tm_mon)
    
    if ctime.tm_mday < 10:
        timestr = timestr + "0" + str(ctime.tm_mday)
    else:
        timestr = timestr + str(ctime.tm_mday)
    
    if ctime.tm_hour < 10:
        timestr = timestr + "0" + str(ctime.tm_hour)
    else:
        timestr = timestr + str(ctime.tm_hour)
    
    if ctime.tm_min < 10:
        timestr = timestr + "0" + str(ctime.tm_min)
    else:
        timestr = timestr + str(ctime.tm_min)
        
    if sec:
        if ctime.tm_sec < 10:
            timestr = timestr + "0" + str(ctime.tm_sec)
        else:
            timestr = timestr + str(ctime.tm_sec)
    
    return(timestr)