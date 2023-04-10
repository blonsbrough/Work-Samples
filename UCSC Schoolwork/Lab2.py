import numpy as np
import math 
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import csv 
  
# opening the CSV file 
AV1 = []
Adeg1 = []
AHZ1 = []
AV2 = []
Adeg2 = []
AZ2 = []
with open('BOX A.csv', mode ='r')as file: 
    
  # reading the CSV file 
  csvFile = csv.reader(file) 
  
  # displaying the contents of the CSV file 
  for lines in csvFile: 
        AV1.append(lines[0])
        Adeg1.append(lines[1])
        AHZ1.append(lines[2])
        AV2.append(lines[3])
        Adeg2.append(lines[4])
        AZ2.append(lines[5])
        print(lines)

CV1 = []
Cdeg1 = []
CHZ1 = []
CV2 = []
Cdeg2 = []
CZ2 = []
with open('BOX C.csv', mode ='r')as file: 
    
  # reading the CSV file 
  csvFile = csv.reader(file) 
  
  # displaying the contents of the CSV file 
  for lines in csvFile: 
        CV1.append(lines[0])
        Cdeg1.append(lines[1])
        CHZ1.append(lines[2])
        CV2.append(lines[3])
        Cdeg2.append(lines[4])
        CZ2.append(lines[5])
        print(lines)

FV1 = []
Fdeg1 = []
FHZ1 = []
FV2 = []
Fdeg2 = []
FZ2 = []

with open('BOX F.csv', mode ='r')as file: 
    
  # reading the CSV file 
  csvFile = csv.reader(file) 
  
  # displaying the contents of the CSV file 
  for lines in csvFile: 
        FV1.append(lines[0])
        Fdeg1.append(lines[1])
        FHZ1.append(lines[2])
        FV2.append(lines[3])
        Fdeg2.append(lines[4])
        FZ2.append(lines[5])
        print(lines)
Ax = []
Ay=[]
Cx=[]
Cy=[]
Fx=[]
Fy=[]
FxE=[]
AxE=[]
Dy=[]
Dx=[]
Sf = 10
Sw=2*math.pi*Sf
CxE = [] 
DxE = []





PhAx = []
PhAy = []

PhCx = []
PhCy = []

PhFx = []
PhFy = []






















for item in AZ2[2:]:
    term=float(item)**2
    Ay.append(term)
    
for item in AHZ1[2:]:
    term=1/((2*math.pi*float(item))**2)
    AxE.append(-4*math.pi*(1/(2*math.pi*float(item))**(3)))
    Ax.append(term)
    PhAx.append(2*math.pi*float(item))
for item in CZ2[2:]:
    Cy.append(1/(float(item)**2))
for item in CHZ1[2:]:
    Cx.append((2*math.pi*float(item))**2)
    CxE.append(Sw*2*float(item)*2*math.pi)
    PhCx.append(2*math.pi*float(item))
for item in CZ2[2:]:
    Dy.append(1/(float(item)**2))
for item in CHZ1[2:]:
    Dx.append(1/(2*math.pi*float(item))**2)
    DxE.append(-4*math.pi*(1/(2*math.pi*float(item))**(3)))

print(CZ2[4])

for item in FZ2[2:]:
    term=((float(item)**-2))
    Fy.append(term)
for item in FHZ1[2:]:
    term=((2*math.pi*float(item))**2)
    Fx.append(term)
    PhFx.append(2*math.pi*float(item))
    
    FxE.append(Sw*2*float(item)*2*math.pi)
  
    

PhAy = []


PhCy = []


PhFy = []
for item in Adeg2[2:]:
    PhAy.append(float(item))

for item in Cdeg2[2:]:
    PhCy.append(float(item))

for item in Fdeg2[2:]:
    PhFy.append(float(item))


fig, Ph1 = plt.subplots()
Ph1.plot(PhAx,PhAy,'+')

Ph1.axhline(y=90, xmin=0, xmax=10**12)
Ph1.set(ylabel='phi(degrees)', xlabel='angular frequency w=2pif(Ohms)', title='Box A phi plot')
Ph1.errorbar(PhAx, PhAy, yerr = 5, fmt ='o') 

fig, Ph2 = plt.subplots()

Ph2.plot(PhCx,PhCy,'+')
C = 7.1*10**-9
L = 0.0175
x = np.linspace(1,700000,100000)
y=[]
for item in x:
    y.append(math.degrees((math.atan(1000*((float(item)*C)-1/(float(item)*L))))))
Ph2.plot(x,y,)
Ph2.set(ylabel='phi(degrees)', xlabel='angular frequency w=2pif(Ohms)', title='Box C phi plot')
Ph2.errorbar(PhCx, PhCy, yerr = 5, fmt ='o') 

fig, Ph3 = plt.subplots()

Ph3.plot(PhFx,PhFy,'+')
x = np.linspace(1,700000,100000)
y=[]
for item in x:
    y.append(math.degrees(math.atan(float(item)*9.54*10**(-9)*1941)))
Ph3.plot(x,y)
Ph3.set(ylabel='phi(degrees)', xlabel='angular frequency w=2pif(Ohms)', title='Box F phi plot')
Ph3.errorbar(PhFx, PhFy, yerr = 5, fmt ='o') 

plt.show()
































"""
fig, P1 = plt.subplots()

P1.plot(Cx,Cy,'+')
z = np.polyfit(Cx,Cy,1)
p = np.poly1d(z)
xp = np.linspace(0,8*10**11,1000)
P1.plot(xp,p(xp),'-')
P1.set(ylabel='1/Impedence^2 1/|Z|^2', xlabel='angular frequency^2 w^2=(2pif)^2', title='Box C Relation(High frequency)')
P1.errorbar(Cx, Cy, xerr = CxE, fmt ='o') 
print("C(High Frequency)")
slope = (p(5)-p(0))/(5)
C = (slope)**(0.5)
Yint = p(0)
R = 1/(Yint)**(0.5)
print(f"C = {C}")
print(f"R = {R}")


fig, P4 = plt.subplots()
P4.plot(Dx,Dy,'+')
z = np.polyfit(Dx,Dy,1)
p = np.poly1d(z)
xp = np.linspace(0,1.4*10**-8,1000)
P4.plot(xp,p(xp),'-')
P4.set(ylabel='1/Impedence^2 1/|Z|^2', xlabel='1/angular frequency^2 1/w^2=1/(2pif)^2', title='Box C Relation(low frequency)')
#P1.plot(xp,0*xp+90000,'-')
P4.errorbar(Dx, Dy, xerr = DxE, fmt ='o') 
Yint = p(0)
slope = (p(5)-p(0))/(5)
L = 1/(slope)**(0.5)
R = 1/(Yint)**(0.5)
print("C Low Frequency")
print(f"L = {L}")
print(f"R = {R}")
fig, P2 = plt.subplots()

P2.plot(Ax,Ay,'+')
z = np.polyfit(Ax,Ay,1)
p = np.poly1d(z)
xp = np.linspace(0,4*10**-4,1000)
P2.plot(xp,p(xp),'-')
P2.set(ylabel='Impedance^2 |Z|^2', xlabel='1/Angular Frequency^2 1/w^2 = 1/(2pif)^2', title='Box A Relation')
P2.errorbar(Ax, Ay, xerr = AxE, fmt ='o') 
slope = (p(5)-p(0))/(5)
C = 1/(slope)**(0.5)
print("A")
print(C)
print(p(0))
fig, P3 = plt.subplots()

P3.plot(Fx,Fy,'+')
z = np.polyfit(Fx,Fy,1)
p = np.poly1d(z)
xp = np.linspace(0,5*10**11,1000)
P3.plot(xp,p(xp),'-')
P3.set(ylabel='1/Impedence^2 1/|Z|^2', xlabel='angular frequency^2 w^2=(2pif)^2', title='Box F Relation')
P3.errorbar(Fx, Fy, xerr = FxE, fmt ='o') 
slope = (p(5)-p(0))/(5)
C = (slope)**(0.5)
print("F")
print(C)
Yint=(p(0))
R = 1/(Yint)**(0.5)
print(R)





plt.show()
"""


























