#-*- coding: utf-8

# 2016-2017 Programacao 1 (LTI)
# Grupo 070
# 49990 Francisco Henriques
# 49994 Mykhaylo Levytskyy
from readingFromFiles import *


def hourToInt(time):
    """ Takes the part of the hour in time and transforms it to an integer
    Requires: time is a string (Ex: 14:30)
    Ensures: Uses the hours of the parameter, and ensures
    the transformation from a string to an integer, in  the way it can be changed
    further in the program.
    """
    t = time.split(":")
    return int(t[0])


def minutesToInt(time):
    """Takes the part of the minutes in time and transforms it to an integer
    Requires: time is a string (Ex: 14:30)
    Ensures: Uses the minutes of the parameter, and ensures
    the transformation from a string to an integer, in  the way it can be changed
    further in the program.
    """
    t1 = time.split(":")
    return int(t1[1])


def intToTime(hour, minutes):
    """It uses the functions hourToInt and minutesToInt to make an update on the hour
    Requires: two parameters(hour and minutes) and they both must be an integer,
    from the result of the used functions
    Ensures: The updated hours and minutes if they're less then 10, it'll be added a
    zero(0) behind the value of that variable.
    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + ":" + m


def timeupdate(time):
    """ Uses hour and minutes to update the time, so that would be, add 10 minutes
    Requires: time is string
    Ensures: The updated time(time+10)
    """
    hour = hourToInt(time)
    minutes = minutesToInt(time)
    m = minutes + 10
    if m >= 60:
        mu = m - 60
        hour = hour + 1
        if hour == 24:
            hour = 0
    else:
        mu = m

    return intToTime(hour, mu)
 
def retrieve_hour(file_name):
	"""Retrive the hour from file_name"""
	f = str(file_name)
	d = f[-9:-4]
	final = d.replace("h", ":")
	return final


def upDate(date, days): 
	""" 
	Updates the date, by increasing the number of days needed to finish 
	the given task
	""" 
	data=transform_date(date) 
	data[0]=data[0]+days 
	if data[1] in [1,3,5,7,8,10,12]: 
		l=31 

	elif data[1] in [4,6,9,11]: 
		l=30 

	elif data[1]==2: 
		l=28 

	while data[0]>l: 
		if data[1] in [1,3,5,7,8,10,12]: 
			data[0]=(data[0]-31) 
			data[1]+=1 
		
		elif data[1] in [4,6,9,11]: 
			data[0]=(data[0]-30) 
			data[1]+=1 

		elif data[1]==2: 
			data[0]=(data[0]-28) 
			data[1]+=1 
	
	if data[1]>12: 
		data[1]=1 
		data[2]+=1 
	 
	data = str(data).strip("[]")
	data = data.replace(",",":")
	return data.replace(" ","")
