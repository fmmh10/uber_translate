#-*- coding: utf-8 -*-

# 2016-2017 Programacao 1 (LTI)
# Grupo 070
# 49990 Francisco Henriques
# 49994 Mykhaylo Levytskyy





def readTranslatorsFile(file_name):
    """Reads a file with a list of translators into a collection.

    Requires:
    file_name is str with the name of a .txt file containing
    a list of translators organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    dict where each item corresponds to a translator listed in
    file with name file_name, a key is the string with the name of a translator,
    and a value is the list with the other elements belonging to that
    translator, in the order provided in the lines of the file.
    """
    trans = removeHeader(file_name)
    translators = {}

    for line in trans:
        translatorsData = line.rstrip().split(", ")
        if len(translatorsData) == 9:
			translatorsData[4] = float(translatorsData[4])
			translatorsData[5] = int(translatorsData[5])
			translatorsData[6] = int(translatorsData[6])
			translatorsData[7] = int(translatorsData[7])
			translators[translatorsData[0]] = translatorsData[1:]
    
    return translators
    
    
def removeHeader(file):
    """ This function removes the header, so that way only reads the text we want
    to use further in the program
    Requires:
    a file .txt
    Ensures:
    The lines we want to use ( in this case the tasks)
    """
    lines = open(file, "r").readlines()[7:]
    return lines


def readTasksFile(file_name):
    """Reads a file with a list of translation tasks into a collection.
    Requires:
    file_name is a str with name of a .txt file containing a list of tasks
    to the translators.
    Ensures:
    The list of all tasks contained in separated lists

    """

    inFile = removeHeader(file_name)

    tasksList = []
    for line in inFile:
        taskData = line.rstrip().split(", ")
        if len(taskData) == 7:
			taskData[4] = int(taskData[4])
			tasksList.append(taskData)

    return tasksList

def obtain_date(file_name):
	"""Obtains the date from file_name"""
	date = open(file_name, "r").readlines()[3]
	return date

def transform_date(date):
	"""Change the date to something that could be operaded for example 
	increment days on the given date"""
	update = []
	day = int(date[0:2])
	update.append(day)
	month = int(date[3:5])
	update.append(month)
	year = int(date[6:10])
	update.append(year)
	return update

