import csv
import sys

train_input = sys.argv[1]
validation_input = sys.argv[2]
test_input = sys.argv[3]
dict_input = sys.argv[4]
formatted_train_out = sys.argv[5]
formatted_valid_out = sys.argv[6]
formatted_test_out = sys.argv[7]
feature_flag = int(sys.argv[8])


dict_word = {}
with open(dict_input,'r') as f:
    for row in f:
        (key,value) = row.split()
        dict_word[key] = int(value)
f.close
def findValue(word):
    if word in dict_word:
        return dict_word[word]
    else:
        return -10

def model1(train_input,formatted_train_out):
    wr = open(formatted_train_out,'w')
    with open(train_input,'r') as function:
        for row in function:
            newrow = []
            raw_data = row.split("\t")            
            label = raw_data[0]
            word = raw_data[1]
            wordlist = word.split()
            for i in range(len(wordlist)):
                temp = findValue(wordlist[i])
                if temp != -10:
                    if str(temp)+':1'+ '\t' not in newrow:
                        newrow.append(str(temp)+':1'+ '\t') 

            newrow[-1] = newrow[-1].strip('\t')
            
            wr.write(label+'\t')
            for index in newrow:
                wr.write(index)
            wr.write('\n')
    return
    
def model2(train_input,formatted_train_out):
    wr = open(formatted_train_out,'w')
    with open(train_input,'r') as function:
        for row in function:
            test = {}
            newrow = list()
            raw_data = row.split("\t")            
            label = raw_data[0]
            word = raw_data[1]
            wordlist = word.split()  
            
            for i in range(len(wordlist)):
                temp = findValue(wordlist[i])        
                if temp not in test:
                    test[temp] = 1
                else:
                    test[temp] += 1 
                      
            for i in range(len(wordlist)):
                temp = findValue(wordlist[i]) 
                if temp != -10 and test[temp] < 4:
                    if str(temp)+':1'+ '\t' not in newrow:
                        newrow.append(str(temp)+':1'+ '\t') 
                
            newrow[-1] = newrow[-1].strip('\t')
            
            wr.write(label+'\t')
            for index in newrow:
                wr.write(index)
            wr.write('\n')
    return             
    
if feature_flag == 1: 
    model1(train_input,formatted_train_out)
    model1(validation_input,formatted_valid_out)
    model1(test_input,formatted_test_out)    
else:
    model2(train_input,formatted_train_out)   
    model2(validation_input,formatted_valid_out)        
    model2(test_input,formatted_test_out)   