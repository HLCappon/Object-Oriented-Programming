#### let op als p1 geactiveerd wordt word k3 juist gedeactiveerd ipv geactiveerd

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class enzymes:
    def __init__(self,type,threshold):
        self.threshold=threshold
        if type == 'k1':
            self.function=self.function_k1
        elif type == 'k2':
            self.function=self.function_k2
        elif type == 'k3':
            self.function=self.function_k3
        elif type == 'p1':
            self.function=self.function_p1
        elif type == 'C':
            self.function=self.function_C
        elif type == 'A':
            self.function=self.function_apoptosis
        else:
            print('error', type ,'not an option')


    def function_k1(self,input):
        value=sum(input)
        if value> self.threshold:
            output=value
        else:
            output=0
        return output
    
    def function_k2(self,input):
        input=[input]
        x=sum(input)/len(input)
        if x > self.threshold:
            value = x+self.threshold
            output=value
        else:
            output=0
        return output
    
    def function_k3(self,input):
        input=[input]
        x=sum(input)/len(input)
        if x > self.threshold:
            value = x-self.threshold
            output=value
            print(output)
        else:
            output=0
        return output
    
    def function_p1(self,input):
        input=[input]
        x=sum(input)/len(input)
        if x > self.threshold:
            value = 1/(1+np.exp(x-self.threshold))
            output = value
        else:
            output = 0
        return output
    
    def function_C(self,input):
        x=min(input)
        if x >self.threshold:
            output=x
        else:
            output=0
        return output
    
    def function_apoptosis(self,input):
        input=[input]
        x=sum(input)/len(input)
        if x > self.threshold:
            output= 1
        else:
            output = 0       
        return bool(output)
    
    def run_function(self,input):
        output=self.function(input)
        return output
    

def simulation(r1,r2):
    k1=enzymes('k11',1)
    k2=enzymes('k2',0.2)
    k3=enzymes('k3',0.01)
    p1=enzymes('p1',0.1)
    C=enzymes('C',0.15)
    A=enzymes('A',0.1)
    input=[r1,r2]
    a=k1.run_function(input)
    b=p1.run_function(a)
    c=k2.run_function(a)
    d=k3.run_function(b)
    cd=[c,d]
    e=C.run_function(cd)
    f=A.run_function(e)
    return f

#output = simulation(0.4,0.6) #onze false  ook false
#output = simulation(0.7,0.8) #onze true   ook true
output = simulation(0.9,0.9) #onze false   ook false
print(output)


            


        
    
    