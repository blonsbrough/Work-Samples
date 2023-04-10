from random import *
import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

Alist = []; ##creates blank list for the averages
AO = 40 ##AO is the number of numbers that are averages
for j in range(100):  ##run 100 average loops.
    numberset = [] ##remake blank list of numbers to average
    for i in range(AO):  ##run random number generator AO times and append to the numberset array
       x = random()
       numberset.append(x);
        
    settotal=0 ##add the numbers all up using settotal, resetting to 0 each loop
    for x in numberset: ##for each randomly generated number, add it to the total
        settotal += x
    setaverage = settotal/AO  ##after adding all the numbers together, divide them by the number of numbers
    print(setaverage) ##print the average to verify it is what I want
    
    Alist.append(setaverage) ##put the average in a list of averages
    
y=0 ##y will be the sum of the averages
mean=0 ##mean will be the average of the averages
for x in Alist: ##for each number in that average list, add them together
    y += x
mean = y/100  ##mean is the sum divided by the number of trials

mean=round(mean,4) ##round the number so it is easier to display
 
Asum=0  ##Asum is the sum used in the standard deviation summation equation
for x in Alist: ##for all of those numbers in the list of averages, plug them into that standard deviation formula.
    Asum += (x-mean)**2
SD = math.sqrt(Asum/99) ##divide by the trials-1 to get the Standard Deviation

SD=round(SD,4)  ##round for graph clarity

x = np.linspace(0,1,1000) ##create a set of x values between 0 and 1, with 1000 increments to graph a line
num_bins = 20  ##set bins to 20, gives the chance to see big changes, without being too restrictive
n, bins, patches = plt.hist(Alist, num_bins,range=[0,1], facecolor='blue', density=True)  ##plot the histogram, place the numbers in their bins
plt.plot(x, ((1/(SD*math.sqrt(2*math.pi)))*(math.e**((-1*((x-mean)**2))/(2*(SD**2))))))  ##plot the line of best fit given the gaussian probability distribution
plt.xlabel('distance (m)')   ##labels
plt.ylabel('#of instances per bin subdivision ')
plt.title(f'Histogram of 40set averages: mean={mean}  Standard Deviation={SD}')

plt.show()  ##display the plot
print(bins)  ##print the bin divisions for quality assurance
text = "the mean value is {}, and the standard deviation of the averages is {}"  ##display the average and standard deviation in the command line to check
print(text.format(mean,SD))  ##print the mean and SD
