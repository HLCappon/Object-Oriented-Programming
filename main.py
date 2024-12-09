#### let op als p1 geactiveerd wordt word k3 juist gedeactiveerd ipv geactiveerd

import numpy as np


class enzymes: #creating parent class enzyme
    def __init__(self,threshold):
        self.threshold=threshold
         
    def function(self): #so it is obvious every child has a function
        pass
    

class k1(enzymes): #create child class of enzymes and defining enzyme k1
    def __init__(self,threshold):
        super().__init__(threshold)
    
    def activation_function_k1(self,input): #define the activation function of k1 with list as to make it possible to increase complexity
        value=sum(input)
        if value> self.threshold:
            output=value
        else:
            output=0
        return output

class k2(enzymes): #create child class of enzymes and defining enzyme k2
    def __init__(self,threshold):
        super().__init__(threshold)

    def activation_function_k2(self,input): #define the activation function of k2
        input=[input]
        x=sum(input)/len(input)
        if x > self.threshold:
            value = x+self.threshold
            output=value
        else:
            output=0
        return output

class k3(enzymes): #create child class of enzymes and defining enzyme k3
    def __init__(self,threshold):
        super().__init__(threshold)
    
    def activation_function_k3(self,input): #define the activation function of k3
        input=[input]
        x=sum(input)/len(input)
        if x > self.threshold:
            value = x-self.threshold
            output=value
        else:
            output=0
        return output
    
class p1(enzymes): #create child class of enzymes and defining enzyme p1
    def __init__(self,threshold):
        super().__init__(threshold)

    def activation_function_p1(self,input): #define the activation function of p1
        input=[input]
        x=sum(input)/len(input)
        if x > self.threshold:
            value = 1/(1+np.exp(x-self.threshold))
            output = value
        else:
            output = 0
        return output

class c(enzymes): #create child class of enzymes and defining enzyme c
    def __init__(self,threshold):
        super().__init__(threshold)

    def activation_function_c(self,input): #define the activation function of c
        x=min(input)
        if x >self.threshold:
            output=x
        else:
            output=0
        return output

class a(enzymes): #create child class of enzymes and defining apoptose decision
    def __init__(self,threshold):
        super().__init__(threshold)

    def activation_function_a(self,input): #define the decision function if apoptose occurs or not
        input=[input]
        x=sum(input)/len(input)
        if x > self.threshold:
            output= 1
        else:
            output = 0      
        return bool(output)

def simulation(r1,r2): #defining function to run the simulation using all different enzymes

    enzyme_K1=k1(1) #creating all enzyme objects with corresponding activation thresholds
    enzyme_K2=k2(0.2)
    enzyme_K3=k3(0.01)
    enzyme_P1=p1(0.1)
    enzyme_C=c(0.15)
    apoptose=a(0.1)

    input=[r1,r2] #turning input into a list to be used as input
    output_k1=enzyme_K1.activation_function_k1(input) #passing the input trough the different enzymes
    output_p1=enzyme_P1.activation_function_p1(output_k1)
    output_k2=enzyme_K2.activation_function_k2(output_k1)
    output_k3=enzyme_K3.activation_function_k3(output_p1)
    input_k2_k3=[output_k2,output_k3]
    output_C=enzyme_C.activation_function_c(input_k2_k3)
    apoptose_decision=apoptose.activation_function_a(output_C)
    print(apoptose_decision)
    return apoptose_decision

#simulation(0.7,0.8)
    


