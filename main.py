class Time:
    def __init__(self, h, m, s):
        self.hour = h
        self.min = m
        self.sec = s

    def myhour(self):
        return self.hour
    def mymin(self):
        return self.min
    def mysec(self):
        return self.sec


    def __str__(self):
        return(str(self.hour) + ":" + str(self.min) + ":" + str(self.sec))

    #multiplies each hour min sec value by the correct minutage in order to convert each to seconds
    def timeinseconds(self):
        ts = 0
        ts += self.hour * 3600
        ts += self.min * 60
        ts += self.sec
        return ts
    #swaps the implicit parameters time values with the ones entered
    def changethetime(self, h, m, s):
        self.hour = h
        self.min = m
        self.sec = s
    #based upon the hourage, a string describing the time of day shall be returned
    def whattimeisit(self):
        #if hours is 6 or above but under 12
        if 6 <= self.hour < 12:
            return "Morning"
        #if hours is 12 or above but under 17
        elif 12 <= self.hour < 17:
            return "afternoon"
        # #if hours is 17 or above but under 22
        elif 17 <= self.hour < 22:
            return "evening"
        #if one of the above are true it must be nighttime
        else:
            return "nighttime"

    #converts the 24 hour oclockage into the time in terms of 12 hour oclockage
    def twelvehourclock(self):
        #if hour is 12 than its the pm 12
        if self.hour == 12:
            return (str(self.hour) + ":" + str(self.min) + ":" + str(self.sec) + "pm")
        #if hours is greater than 12
        elif self.hour > 12:
            hrs = self.hour - 12
            return (str(hrs) + ":" + str(self.min) + ":" + str(self.sec) + "pm")
        #if hour in 24 time is 0 than its must be the am 12
        elif self.hour == 0:
            hrs = 12
            return (str(hrs) + ":" + str(self.min) + ":" + str(self.sec) + "am")
        #if the hour is neither 24, 0 , or greater than 12:the number can just be returned as an am time
        else:
            return (str(self.hour) + ":" + str(self.min) + ":" + str(self.sec) + "am")

    #compares two time objects by converting each into seconds and then subtracting. returns the difference
    def compareto(self, obj):
        x = self.timeinseconds()
        y = obj.timeinseconds()
        return x - y

    #takes two time objects. returns a time object that is the difference in time between the implicit parameter and explicit parameter
    def timetill(self, obj):
        dhour = obj.hour - self.hour
        dmin = obj.min - self.min
        dsec = obj.sec - self.sec
        #checks if the difference is negative
        if (dhour < 0):
            dhour += 24
        # checks if the difference is negative
        if (dmin < 0):
            dmin += 60
        # checks if the difference is negative
        if (dsec < 0):
            dsec += 60
        ntime = Time(dhour, dmin, dsec)
        return ntime



t1 = Time(5, 50, 30)
print(t1)
print(t1.timeinseconds())
print(t1.twelvehourclock())
print( t1.whattimeisit() )
t1.changethetime(7, 10 , 9)
print( t1 )

print("myhhr:" + str( t1.myhour()) )
print("mymin:" + str( t1.mymin() ) )
print("mymin:", str( t1.mysec()) )


t2 = Time(24, 12, 13)
t1 = Time(0, 12, 13)
t3 = Time(13, 12, 13)

nt1 = Time(17, 50 , 30)
nt2 = Time(12, 49, 29)
nt3 = Time(18, 51, 31)

print(t2.compareto(t3))
print(t2.twelvehourclock())
print(t3.twelvehourclock())
print( t2.whattimeisit() )
print( t3.whattimeisit() )

print( (nt2.timetill(nt1)) )
print((nt3.timetill(nt1))  )

