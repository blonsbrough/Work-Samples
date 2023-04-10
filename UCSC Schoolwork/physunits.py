
import numpy as np


unitlist = ('m','kg','s','k','','','')

class preal:
    """class preal gives values 2 characteristics, a units array corresponding
    to various powers of dimensional units, and a value, corresponding the 
    numerical value of that unit combination.
    ---------------------------------------------------------------------
    value = numerical value of the units (#)
    units = array value of the units (7 term array)
    first = first term in combination
    second = second term in combination
    __init__ runs on creating a term with dimensional
    __repr__ runs when object is displayed
    __add__,__radd__ run when adding, the first when the first term is a preal, the second when the second term is preal
    __sub__,__rsub__ run when subtracting, the first when the first term is a preal, the second when the second term is preal
    __mul__,__rmul__ run when ,multiplying, the first when the first term is a preal, the second when the second term is preal
    __truediv__,__rtruediv__ run when dividing, the first when the first term is a preal, the second when the second term is preal
    """

    def __init__(self, value, units): #defines preal term given a value and a unit matrix. (premade units below)
        
        self.value = float(value) #makes sure value is a float
        self.units = np.array(units,int) #makes sure array values are integer

    def __repr__(first): #formats how to express a preal value when called without changing internal information
        message = f"{first.value}" #start message to return
        Um = '('
        Lm = '('
        for i in range(7): #loop to check each unit and add its name and power to the message
            if first.units[i] > 0.5: #arranges positive powers of dimension
                Um += f"{unitlist[i]}^{first.units[i]}"
            elif first.units[i] <-0.5: #arranges negative powers of dimension
                Lm += f"{unitlist[i]}^{-first.units[i]}"
            else:
                message += '' #if there is no unit power, it is not important to show it to the 0 power
        Um += ')'
        Lm += ')'
        message += Um   #compose and cap message
        message += '/'
        message += Lm
        return message
        
            
    def __add__(first, second): #adds preal values if they are the same units
        for i in range(7):  #checks each unit to assure they are equal values in the array
            if first.units[i] != second.units[i]:
                print("cannot add unequal units")
                equalunits = False
                break
            else:
                equalunits = True
        if equalunits == True:
            
            return preal(first.value+second.value, first.units)  #returns a number with added values, and same units
    
    def __radd__(second, first):  #a bit redundant but does the same as above except checks the second term first
        for i in range(7): #checks each unit to assure they are equal values in the array
            if second.units[i] != first.units[i]:
                print("cannot add unequal units")
                equalunits = False
                break
            else:
                equalunits = True
        if equalunits == True:
            
            return preal(second.value+first.value, second.units) #returns a number with added values, and same units
            
    def __sub__(first, second): #similar to addition, but subtracts the values instead of adding them, still keeps same units
        for i in range(7):
            if first.units[i] != second.units[i]: #unit check
                print("cannot subtract unequal units")
                equalunits = False
                break
            else:
                equalunits = True
        if equalunits == True:
            
            return preal(first.value-second.value, first.units) #subtracts values, keeps units of first
    
    def __rsub__(second, first): #again, a bit redundant but checks second term first
        for i in range(7): # checks each unit to assure equality
            if first.units[i] != second.units[i]:
                print("cannot subtract unequal units")
                equalunits = False
                break
            else:
                equalunits = True
        if equalunits == True:
            
            return preal(first.value-second.value, second.units) #subtract value, keep units of second

    def __mul__(first, second): #multiplies 2 values if the first is a preal value, multiplies the value, adds the unit arrays, unit array for integers or floats is all 0
        if type(second) == int or type(second) == float: #check to see if term is an integer or a float, to determine whether to look for a unit array
            
            return preal(first.value*second, first.units) #Keep units as int or float has none, multiply values
        else:
            
            return preal(first.value*second.value, first.units+second.units) #add unit array if both are preal values
    
    def __rmul__(second, first): #multiplies 2 values if the second is a preal value, multiplies values together, adds unit arrays.
        if type(first) == int or type(first) == float: #check to see if second term is an integer

            return preal(first*second.value, second.units) #does not add unit arrays if the value doesnt have one
        else:
            
            return preal(first.value*second.value, first.units+second.units) #add unit arrays, multiply values
    
    def __pow__(first, second): #defines powers, a simplified multiplication function
        
        return preal(first.value**second, second*first.units) #raises value to power, multiplies unit array by power.
    
    def __truediv__(first, second): #division, similar to multiplication, except reduce unit array if divided by, add if on top, divide values, works if value on top is preal
        if type(second) == int or type(second) == float: #check for float or integer value input
            
            return preal(first.value/second, first.units) #unit array remains the same because lower value is an integer or float with no dimension
        else:
            
            return preal(first.value/second.value, first.units-second.units) #divide values, subtract second units from first in the array
    
    def __rtruediv__(second, first): #similar to regular division, but this works if the value on top is not preal and the value below is preal
        if type(first) == int or type(first) == float: #type check for int or float
            
            return preal(first/second.value, -1*second.units) # as bottom will be preal value, make negative the unit array to represent negative powers of dimension
        else:
            
            return preal(first.value/second.value, first.units-second.units) #divide values, subtract second unit array from first
        




m = preal(1,[1,0,0,0,0,0,0]) #define meters
kg = preal(1,[0,1,0,0,0,0,0]) #define kilograms
s = preal(1,[0,0,1,0,0,0,0]) #define seconds
k = preal(1,[0,0,0,1,0,0,0]) #define kelvin
mm = preal(0.001,[1,0,0,0,0,0,0]) #define milimeters
cm = preal(0.01,[1,0,0,0,0,0,0]) #define centimeters
erg = preal(10**-7,[2,1,-2,0,0,0,0]) #define special unit erg
    