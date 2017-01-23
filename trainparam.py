corpus=open('corpus.txt','r')
test=open('test.txt','w')
count=0
for line in corpus: #delete half of the data from the corpus to make training faster
    if count<12044:
        test.write(line)
    count=count+1
corpus.close()
test.close()
start=0 #flag
nominal=''
priormatrix={} #prior matrix
text=open('test.txt','r') #open file
for line in text: #get prior matrix 
    for i in range(len(line)):
        if start==1:
            nominal=nominal+line[i]
        if line[i]=='/':
            start=1
        if line[i]==' ':
            start=0
            if nominal!='':
                if nominal in priormatrix:
                    priormatrix[nominal]=priormatrix[nominal]+1
                else:
                    priormatrix[nominal]=1
                nominal=''
#print(priormatrix)
x=list(priormatrix.keys())
allsum=0
for i in range(len(x)):
    allsum=allsum+priormatrix[x[i]]
#print(allsum)


hiddentrans={} #hidden transfer matrix
first=0 #flag
start=0
nominal1=''
nominal2=''
text=open('test.txt','r') #open file
for line in text: #get hidden transfer matrix
    for i in range(len(line)):
        if start==1:
            nominal2=nominal2+line[i]
        if line[i]=='/':
            start=1
        if line[i]==' ':
            start=0
            if first==0:
                if nominal2!='':
                    nominal1=nominal2
                    nominal2=''
                    first=1
            else:
                #print(1)
                if nominal2!='':
                    if nominal1 in hiddentrans:
                        if nominal2 in hiddentrans[nominal1]:
                            #print(2)
                            hiddentrans[nominal1][nominal2]=hiddentrans[nominal1][nominal2]+1
                        else:
                            #print(3)
                            hiddentrans[nominal1][nominal2]=1
                    else:
                        #print(4)
                        hiddentrans[nominal1]={}
                        hiddentrans[nominal1][nominal2]=1
                    nominal1=nominal2
                nominal2=''
#print(hiddentrans)

confusematrix={} #confuse matrix
divide=0 #flag
word=''
nominal=''
text=open('test.txt','r') #open file
for line in text: #get the confuse matrix
    for i in range(len(line)):
        if divide==0 and line[i]!='/':
            word=word+line[i]
        if divide==1:
            nominal=nominal+line[i]
        if line[i]==' ':
            #print(1)
            divide=0
            if nominal in confusematrix:
                if word in confusematrix[nominal]:
                    confusematrix[nominal][word]= confusematrix[nominal][word]+1
                else:
                    confusematrix[nominal][word]=1
            else:
                 confusematrix[nominal]={}
                 confusematrix[nominal][word]=1
            nominal=''
            word=''
        if line[i]=='/':
            divide=1
#print(confusematrix)


def getmax(dictx): #return the key of the max value
    k=list(dictx.keys())
    v=list(dictx.values())
    m=0
    for i in range(len(k)):
        if v[i]>=m:
            m=v[i]
            key=k[i]
    return key
        


            
        
            
            
    
