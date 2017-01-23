#get three matrix
from trainparam import priormatrix #get the prior matrix
from trainparam import hiddentrans #get the hidden transfer matrix
from trainparam import confusematrix #get the confuse matrix
from trainparam import allsum # get the number of all the nominals
from trainparam import getmax 
#viterbi algorithm
line=['恢复','高度','自治','的','方针'] #input 
nominal=[] #all the nominals for words in corpus
nominal=list(priormatrix.keys())
#print(nominal)
lastprob={} #probability of all the nominal for the word before current word
newprob={} #probability of all the nominals for current word 
for i in range(len(line)): #use viterbi algorithm tag the words 
    for j in range(len(nominal)):
        if i==0:
            if line[i] in confusematrix[nominal[j]]:
                newprob[nominal[j]]=confusematrix[nominal[j]][line[i]]/allsum
            else:
                newprob[nominal[j]]=0
        else:
            newprob[nominal[j]]=0
            if line[i] in confusematrix[nominal[j]]:
                for k in range(len(nominal)):
                    if nominal[j] in hiddentrans[nominal[k]]:
                        newprob[nominal[j]]=newprob[nominal[j]]+lastprob[nominal[k]]*(hiddentrans[nominal[k]][nominal[j]]/priormatrix[nominal[k]])*(confusematrix[nominal[j]][line[i]]/priormatrix[nominal[j]])
    print(line[i]+'/'+getmax(newprob)+' ',end='')
    #print(newprob)
    lastprob=newprob
    newprob={}

                                    
    

