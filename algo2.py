import random
import pysat
import math
from pysat.formula import CNF
from pysat.solvers import Solver

def TRUEnumber(PList):
    f = CNF(from_file="Input.cnf")
    clauses = f.clauses 
    count = 0 
    for i in range(len(clauses)):
        for j in range(3):
            if (clauses[i][j] > 0 and PList[clauses[i][j]-1] > 0) or (clauses[i][j] < 0 and PList[-clauses[i][j]-1] < 0):
                count += 1
                break
    return count

def function():
    listPerson=[]
    for i in range(1, 101):
        var = (random.randint(0, 1))
        if var == 1:
            listPerson.append(i)
        else:
            listPerson.append(-i)
    counter=5000
    while(True):
        currentStep=TRUEnumber(listPerson)
        index=random.randrange(0,100)
        new_Person_List=[]
        new_Person_List=listPerson

        new_Person_List[index]=-1*new_Person_List[index]
        nextStep=TRUEnumber(new_Person_List)
        move=nextStep-currentStep
        p=move/counter
        negativeRange=math.exp(p)
        randVar=(random.random())
        if move>0 :
            listPerson[index]=-1*listPerson[index]
        elif negativeRange>randVar:
            listPerson[index]=-1*listPerson[index]
        
        
        max=400
        answer=TRUEnumber(listPerson)
        if answer==max:
            print(listPerson)
            break
        counter=counter-0.1
        if counter<0:
            break

function()
