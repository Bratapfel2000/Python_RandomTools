'''
takes subjects and places them randomly in a schedule for 5 days
'''

import random

#create subjects
a = "subject 1"
b = "subject 2"
c = "subject 3" 
d = "subject 4" 
e = "subject 5" 
f = "subject 6" 
g = "subject 7" 
h = "subject 8" 

i = "subject a" 
j = "subject b" 
k = "subject c" 
l = "subject d" 

#creates a list with subjects
subject_list = 2*[a,b,c,d,e,f,g,h]+[i,j,k,l]
    
#checks if subject is still in list after assigning to schedule, if it is there, it will be deleted
def check_if_subject_left(word):
    for i in range(len(subject_list)+1):
        if subject_list[i] == word:
            del subject_list[i]
            return subject_list


#create schedule fields for subjects
field = {}
def fields():
    global field
    for i in range(len(subject_list)):
        field[i] = [i+1,0]
        field[i] = [0]
fields()

#draws schedule
def schedule_():
    print('%-20s%-20s%-20s%-20s%-20s' %("day 1","day 2","day 3","day 4","day 5"))
    print('%-20s%-20s%-20s%-20s%-20s' %(18*"-",18*"-",18*"-",18*"-",18*"-"))
    for i in range(4):
        print('%-20s%-20s%-20s%-20s%-20s' %(field[i],
                                            field[i+4],
                                            field[i+8],
                                            field[i+12],
                                            field[i+16]))

#assigns randomly subjects from subject_list, multiple times
def dict_asign():
    while len(subject_list)>0:
        for i in range(len(subject_list)):
            z = random.choice(subject_list)
            field[i]= z
            check_if_subject_left(z)
dict_asign()

schedule_()
