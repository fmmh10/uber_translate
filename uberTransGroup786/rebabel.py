#-*- coding: utf-8 -*-

# 2016-2017 Programacao 1 (LTI)
# Grupo 070
# 49990 Francisco Henriques
# 49994 Mykhaylo Levytskyy
import sys
from scheduling import *
from dateTime import *
from readingFromFiles import *
from writingToFiles import *


def assign(translatorsFileName, tasksFileName):
    """Obtains the assignment of translation tasks to translators.

    Requires:
    translatorsFileName is a str with the name of a .txt file containing a list
    of translators, organized as in the examples provided;
    tasksFileName is a str with the name of a .txt file containing a list
    of translation tasks requested in the 10 minute period right after the update
    time of translatorsFileName, organized as in the examples provided;
    both these input files concern the same company, date and time.
    Ensures:
    writing of two .txt files containing the list of translation tasks assigned
    to translators and the updated list of translators, according to
    the requirements in the general specifications provided (omitted here for
    the sake of readability);
    these two output files are named, respectively, scheduleXXhYY.txt and
    translatorsXXhYY.txt, where XXhYY represents the time and date 10 minutes
    after the time and date indicated in the files translatorsFileName and
    tasksFileName, and are written in the same directory of the latter.
    """
    h = retrieve_hour(translatorsFileName)
    h1 = retrieve_hour(tasksFileName)
    writeScheduleFile(scheduleTasks(readTranslatorsFile(str(translatorsFileName)), readTasksFile(str(tasksFileName))), timeupdate(h), translatorsFileName)
    writeTranslatorsFile(readTranslatorsFile(translatorsFileName),timeupdate(h),translatorsFileName)

try:
    assign(sys.argv[1],sys.argv[2])    # calls the function assign and uses the sys.argv[1] and sys.argv[2] as parameters of the function, these two are given the commandline
    
    
    
except:
	print "Input file error: scope or time inconsistency between name and header in file <name of file>."
