#run in python shell i terminal...


from datetime import datetime 
from datetime import date 
from datetime import timedelta

datetime.today()
#prints out current date and time
#therefore

today = datetime.today()
leo = datetime.today()
kawuono = datetime.today()

today = leo = kawuono
#leo ni leo

tpye(today)
# class of datetime.datetime

#moving forward

todaydate = date.today()

type(todaydate)
# class of datetime.date

todaydate
#prints date only



todaydate.month
#prints month
todaydate.day
#prints day
todaydate.year
#prints year


#assigning a date
birthdate = date(1992, 12, 26)
christmas = date(2021, 12, 25)

birthdate
#prints day I was born as defined
christmas
#prints christmas date defined

today date - birthdate
#prints days passed since I was born
christmas - todaydate
#prints out days remining to christmas

(christmas - todaydate).days
#prints out days only
(todaydate - birthdate).years
#prints out current age

#conditional statements
 if christmas != todaydate:
    print ("not so merry is it? " + str((christmas - todaydate).days) + " days to it though")
else:
    print ("whats so merry after all..?")
    
#if not christmas will print message with an indication of how many days remain to christmas.
#if chrismas will print "whats so merry after all..?"

#datetime timedelta (gap in time measured out)
# time between specific events ot certain periods 

t = timedelta (days=7, hours=23)
#time period of 7 days 23 hours
type(t)
# class of datetime.timedelta

t.days
#prints days
t.seconds
#prints time in seconds
t.hours
# error... deals in seconds

#solution to get time in hours
t.seconds/60/60
#prints time in hours
t.seconds/3600


eta = timedelta (hours=6)

today = datetime.today()

#add
today + eta
#prints out time after defined time in the eta assigned

str(today + eta)
#prints out formated date and time.




