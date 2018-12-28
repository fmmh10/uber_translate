#-*- coding: utf-8 -*-

# 2016-2017 Programacao 1 (LTI)
# Grupo 070
# 49990 Francisco Henriques
# 49994 Mykhaylo Levytskyy

from readingFromFiles import *
from dateTime import *
from operator import itemgetter
from constants import *
import math

def scheduleTasks(translators, tasks):


        """Assigns translation tasks to translators.

        Requires:
        translators is a dict with a structure as in the output of
        readingFromFiles.readTranslatorsFile concerning the update time;
        tasks is a list with the structure as in the output of
        readingFromFiles.readTasksFile concerning the period of
        periodAfter minutes immediately after the update time of translators;
        date is string in format DD:MM:YYYY with the update time;
        periodAfter is a int with the number of minutes of a period
        of time elapsed.
        Ensures:
        a list of translation tasks assigned according to the conditions
        indicated in the general specification (omitted here for
        the sake of readability).
        """
        
        sched = []
	for task in tasks:
		l = filter_lang(translators, task[1], task[2])
		
		m = filter_tamanho(translators, int(task[4]))
		
		trad= [] 
		for i in range(len(l)):
			for j in range(len(m)):
				if m[j] == l[i]:
					trad.append(l[i])   # find those available to translate by language and by the size of the task
			        
	 		
		if len(trad) > 0:				# if there is a tie in the translators
			val = []
			for name in trad:
				val.append([name] + translators[name])          

			if task[5] == 'quality':
				l2 = sorted(val, key= itemgetter(3),reverse=True)
				l2 = sorted(val, key= itemgetter(8,0))
			
			if task[5] == 'price':
				l2 = sorted(val, key= itemgetter(4,3,0))
								
			if task[5] == 'speed':
				l2 = sorted(val, key= itemgetter(8,3,4,0))
			
			
			price = int(task[4]) * float(l2[0][4])
			update_volume = int(l2[0][7]) + int(task[4])
			l2[0][7] = update_volume   
			    
			days = task[4] // l2[0][5]      # updates the date
			data = upDate(l2[0][8],days+1)
			l2[0][8] = data
			sched.append([data, l2[0][0],int(round(price)), task[0]]) # makes the append of the elements from schedule updated
			
		else:
			
			sched.append([NOTAssigned,NOTApplicable, task[0]])
	translators[l2[0][0]] = l2[0]	
	return sched
	   
def filter_tamanho(translators, tamanho):
	"""Filters the translators that are able to the task, taking into 
	account the size of the variable tamanho"""
	lis = []
	for j in translators:
		values = translators[j] # dictionary values
		volume = int(values[6])
		limit = int(values[5])
		if volume + tamanho < limit:
			lis.append(j)
	
	return lis

def filter_lang(translators, fro, to): 
    """fro is the from language and to is the language that you want 
    your translation result
    Filters the translators that are able to translate by the given parameters
    (fro and to)"""
    lis = []
    for k in translators:
        values = translators[k]
        langfrom = values[0]
        langto = values[1]
        if fro in langfrom and to in langto:
            lis.append(k)
    return lis



def updateTranslators(translators, schedule):
	"""Updates the list of translators"""
	values = []
	
	
	for name in translators:
		val.append([name] + translators[name])
	return val
