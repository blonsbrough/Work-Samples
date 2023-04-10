import numpy as np
import math 
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import csv 
import scipy
from scipy.optimize import curve_fit
e=2.71828


PHV = [] #Preliminary high voltage
PPA = [] #preliminary pulse amplitude
PC = [] #premilinary count
PT = [] #preliminary time
PCR = [] #preliminary count rate
PPCR = [] #preliminary poisson rates
C = []
T = []
LX = []
LY = []
LM = []
with open('Preliminary Experiments Data.csv', mode ='r')as file: 
    
  # reading the CSV file 
  csvFile = csv.reader(file) 
  
  # displaying the contents of the CSV file 
  for lines in csvFile: 
        PHV.append(lines[0])
        PPA.append(lines[1])
        PC.append(lines[2])
        PT.append(lines[3])
        PPCR.append(lines[11])

with open('Gamma Absorption Data.csv', mode ='r')as file: 
    
  # reading the CSV file 
  csvFile = csv.reader(file) 
  
  # displaying the contents of the CSV file 
  for lines in csvFile: 
        C.append(lines[12])
        T.append(lines[13])
        LX.append(lines[4])
        LY.append(lines[5])
        LM.append(lines[6])
LX = LX[3:8]
LY = LY[3:8]
LM = LM[3:8]
H = []

for i in range(len(LX)):
    H.append(float(LM[i])/(float(LX[i])*float(LY[i])))
print(H)
print(LX)
print(LY)
print(LM)
h=0
LH = []
for i in range(5):
    h += H[i]
    LH.append(h)



C = C[5:10]
T = T[5:10]

BCR = 2004/3992
SBCR = (2004**(0.5))/3992
CR = []
CRa = []
for i in range(len(C)):
    CR.append((float(C[i])/float(T[i]))-BCR)
    CRa.append((float(C[i])/float(T[i])))
print(CR)


PHV = PHV[3:17]
PPA = PPA[3:17]
PC = PC[3:17] 
PT = PT[11:17] 
SPCR = []
PPCR = PPCR[4:]
for i in range(len(PPCR)):
    PPCR[i] = int(PPCR[i])

PPCR.sort()
PPCR.remove(20)
Xsum=0
for item in PPCR:
    Xsum += item
L = Xsum/(len(PPCR))

for i in range(len(PPA)):
    PPA[i] = float(PPA[i])
for i in range(8):
    PCR.append(0)
    SPCR.append(0)
for i in range(len(PC[8:14])):
    term = float(PC[i+8])/float(PT[i])
    PCR.append(term)
    SPCR.append(float(PC[i+8])**(1/2)/float(PT[i]))



x = np.linspace(0,20,21)
print(x)
P=[]
for i in x:
    P.append(101*e**(-L)*L**i/math.factorial(i))
    
#Uncertainty in height of lead
##uncertainty in each plate
SP = []
Sx = 0.05
Sy = 0.05
Sg = 0.5
a = 0
b = 0
c = 0

for i in range(5):
    lg = float(LM[i])
    lx = float(LX[i])
    ly = float(LY[i])
    a = ((lg)/(lx*ly**2))*Sy
    b = ((lg)/(lx**2*ly))*Sx
    c = ((1)/(lx*ly))*Sg
    SP.append((a**2+b**2+c**2)**(0.5))
SH = []
SP2 = []
for i in range(5):
    SP2.append(float(SP[i])**2)
a1=0
a2=0
a3=0
a4=0
a5=0
HPE = 0
for i in range(5):
    if i >= 0:
        a1=1
    if i >= 1:
        a2=1
    if i >= 2:
        a3=1
    if i >= 3:
        a4=1
    if i >= 4:
        a5=1
    E = a1*SP2[0]+a2*SP2[1]+a3*SP2[2]+a4*SP2[3]+a5*SP2[4]
    HPE = E**(0.5)
    SH.append(HPE)

STCR = []
SCR = []
for i in range(5):
    STCR.append((SBCR**2+(float(C[i])/(float(T[i])**2))**(0.5))/float(CR[i]))
    SCR.append(((float(C[i])/(float(T[i])**2))**(0.5)))
print(SCR)
CR2 = []
for i in range(len(CR)):
    CR2.append(np.log(CR[i]))

##Preliminary Experiments
#Plateau
fig, P1 = plt.subplots()

P1.plot(PHV,PCR,'.')
P1.errorbar(PHV, PCR, yerr = SPCR)
P1.set(ylabel='Count Rate [#/s]', xlabel='Voltage Amplitude [V]', title='Count rate vs High Voltage')
fig, P2 = plt.subplots()

P2.plot(PHV,PPA,'.')
P2.errorbar(PHV, PPA, yerr = 0.05)
P2.set(ylabel='Pulse Amplitude [V]', xlabel='Voltage Amplitude [V]', title='Pulse Amplitude vs High Voltage')
#
fig, P3 = plt.subplots()
bins = np.linspace(0,20,21)

counts, edges, plot = P3.hist(PPCR,bins)
P3.plot(x,P)
P3.set(ylabel='# of Events', xlabel='# of Counts', title='Distribution of Counts per second')
print(counts[5])
CHI2=0
for i in range(14):
    CHI2 += (101*e**(-L)*L**(i+3)/math.factorial(i+3)-counts[i+3])**2/(101*e**(-L)*L**(i+3)/math.factorial(i+3))
print(CHI2)


fig, P4 = plt.subplots()

P4.plot(LH,CR2,'+')
P4.plot(LH,CRa,'.')
P4.errorbar(LH,CR2, xerr = SH)
#P4.errorbar(LH,CR2, yerr = STCR)
P4.errorbar(LH,CRa, xerr = SH)
P4.errorbar(LH,CRa, yerr = SCR)
P4.set(ylabel='Count Rate [#/s]', xlabel='Rho*x [g/m^2]', title='Count Rate vs Rho x, exponential fit')
def func(i, k, o, j):
    return k*np.exp(-o*i)+j
popt, pcov = curve_fit(func, LH, CRa, sigma=SCR)
print(popt)
xFit = np.arange(1.0,14.0,0.01)
plt.plot(xFit, func(xFit, *popt), 'g--',
        label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

perr = np.sqrt(np.diag(pcov))
print(perr)
print('hello world')
SI = []
for i in range(len(LH)):
    t1 = np.exp(-0.138*float(LH[i]))*(0.612)
    t2 = 11.847*float(LH[i])*np.exp(-0.138*float(LH[i]))*0.039
    t3 = 0.832
    term = (t1**2+t2**2+t3**2)
    term = term**(0.5)
    SI.append(term)
aCHI2 = 0
for i in range(len(CRa)):
    topterm = (float(CRa[i])-float(func(LH[i],*popt)))**2
    aCHI2 += (topterm/(2*float(SI[i])**2))
    
    
print(SI)
print(aCHI2)
print(BCR)
print(SBCR)

plt.show()
