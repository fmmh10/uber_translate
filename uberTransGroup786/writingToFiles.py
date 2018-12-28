#-*- coding: utf-8 -*-

# 2016-2017 Programacao 1 (LTI)
# Grupo 070
# 49990 Francisco Henriques
# 49994 Mykhaylo Levytskyy
import sys
from scheduling import *
from dateTime import *
from readingFromFiles import *


def writeScheduleFile(schedule, hour, file_name):
    """Writes a collection of services into a file.
    Requires:
    schedule is a list with the structure as in the output of
    scheduling.scheduleTasks representing the translation tasks assigned;
    file_name is a str with the name of a .txt file;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability).
    Ensures:
    writing of file named file_name representing the list of
    translation tasks in tasksAssigned prefixed by header and 
    organized as in the examples provided  in the general specification 
    (omitted here for the sake of readability);
    the listing in this file keeps the ordering top to bottom of 
    the translations tasks as ordered head to tail in schedule.
    """
    f = open("schedule"+ hour[:2]+"h"+hour[3:5]+".txt", "w")
    f.write("Company:\nReBaBel\nDay:\n"+obtain_date(file_name)+"Time:\n"+hour)
    f.write("\nSchedule:\n")
    for i in schedule:
		done = str(i).strip("[]")
		d = done.strip("''")
		f.write(d+"\n")
    f.close()

	

def writeTranslatorsFile(translatorsUpdate, hour, file_name):
	"""Write the updated translators into a file
	Requires:
	translatorsUpdate is a dictionary
	Ensures:
	the writing into a file, of the updated translators
	"""
	f = open("translators"+ hour[:2]+"h"+hour[3:5]+".txt", "w")
	f.write("Company:\nReBaBel\nDay:\n"+obtain_date(file_name)+"Time:\n"+hour)
	f.write("\nTranslators:\n")
	for name in translatorsUpdate:
		d = [name]+ translatorsUpdate[name]
		final = str(d).strip("[]")
		fi = final.strip("''")
		f.write(fi+"\n")
	f.close()




