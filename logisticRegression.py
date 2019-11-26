import sys
import csv
import math
import numpy as np

formatted_train_input = sys.argv[1]
formatted_validation_input = sys.argv[2]
formatted_test_input = sys.argv[3]
dict_input = sys.argv[4]
train_out = sys.argv[5]
test_out = sys.argv[6]
metrics_out = sys.argv[7]
num_epoch = int(sys.argv[8])

dict_word = {}
with open(dict_input,'r') as f:
    for row in f:
        (key,value) = row.split()
        dict_word[key] = int(value)
f.close

def sigmoid(dotProduct):
    return math.exp(dotProduct)/(1+math.exp(dotProduct))

def dealFeature(features):
    output = np.zeros(len(dict_word)+1)
    output[0] = 1.0
    for key in features:
        output[int(key)+1] = 1.0
    return output  #x
    

    
def computeDP(parameters,features):
    DP = parameters[0]
    for key in features:
        DP += float(parameters[int(key)+1])
    return DP
    
    
def oneSGD(label,features,parameters):
    learning_rate = 0.1
    DP = computeDP(parameters,features)
    temp = learning_rate*(float(label) - Sigmoid(DP))
    gradient = np.multiply(temp,dealFeature(features))
    parameters = np.add(parameters, gradientJi)
    return parameters
    

def SGD(path,num_epoch):
    count = 0
    parameters = np.zeros(len(dict_word) + 1)
    while count < num_epoch:
        with open(path,'r') as f:
            for row in f:
                features = {}
                raw_data = row.split("\t")
                label = float(raw_data[0])   ##try 1.0*
                feats_list = raw_data[1:]
                for i in feats_list:
                    (key1,value1) = i.split(sep = ":")
                    features[key1] = int(value1) 
                parameters = oneSGD(parameters, label, features)
            count += 1
    return parameters
    
def predictLabel(parameters,features):
    DP = computeDP(parameters,features)
    if sigmoid(DP) > 0.5:
        return 1
    else:
        return 0

def predictError(input, train_out, num_epoch):
    count = {1:0,0:0} #1 for ture, 0 for false 
    with open(input,'r') as f:
    output = open(train_out,'w')
        for row in f:
            features = {}
            raw_data = row.split("\t")
            label = float(raw_data[0])   ##try 1.0*
            feats_list = raw_data[1:]
            for i in feats_list:
                (key1,value1) = i.split(sep = ":")
                features[key1] = int(value1) 
            parameters = SGD(input,num_epoch)
            labelPredict = predictLabel(parameters,features)

            if label == labelPredict:
                count[1] +=1
            else:
                count[0] +=1  
                              
            output.write(str(labelPredict))
            output.write('\n')
    num_true = float(count[1])
    num_false = float(count[0])
    return num_false/(num_true + num_false)

trainError = predictError(formatted_train_input, train_out, num_epoch)
testError = predictError(formatted_test_input, test_out, num_epoch)

error = "error (train): " + str(trainError) + "\n" + "error (test): " + str(testError) + "\n"

with open(metrics_out, 'w') as metrics:
    metrics.write(error)
          


