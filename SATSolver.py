import random
import pysat
from pysat.formula import CNF
from pysat.solvers import Solver



class person:

    def __init__(self,cnf,list3):
        
        self.cnf=cnf
        self.list1=list3
        
        

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
    societyList=[]
    for j in range(0,100):
        listPerson=[]
        for i in range(1, 101):
                var = (random.randint(0, 1))
                if var == 1:
                    listPerson.append(i)
                else:
                    listPerson.append(-i)
        societyList.append(person(0,listPerson))
    
    while(True):
        for i in range(0,100):

            societyList[i].cnf=TRUEnumber(societyList[i].list1)
        for i in range(len(societyList)):
            for j in range(i + 1, len(societyList)):

                if societyList[i].cnf > societyList[j].cnf:
                    societyList[i], societyList[j] = societyList[j], societyList[i]

        parentsList=[]
        for i in range(59,100):
            parentsList.append(societyList[i])
        for i in range(0,40):
            mom=random.randrange(0,40)
            father=random.randrange(0,40)
            while (father==mom):
                father=random.randrange(0,40)
            index=random.randrange(0,100)
            childList=[]
            for i in range(0,index):
                childList.append(parentsList[mom].list1[i])
            for i in range(index,100):
                childList.append(parentsList[father].list1[i])
            jahesh=random.randrange(0,100)
            childList[jahesh]=-1*childList[jahesh]
            societyList.append(person(0,childList))
        for i in range(100,140):
            societyList[i].cnf=TRUEnumber(societyList[i].list1)
        for i in range(len(societyList)):
            for j in range(i + 1, len(societyList)):

                if societyList[i].cnf > societyList[j].cnf:
                    societyList[i], societyList[j] = societyList[j], societyList[i]

        for i in range(0,40):
            societyList.pop(0)
        max=425
        flag=True
        answer=0
        for i in range(0,100):
            x=TRUEnumber(societyList[i].list1)
            if x==max:
                flag=False
                answer=i

        if flag==False :
            print("solution found")
            print(societyList[answer].list1)
            break

function()