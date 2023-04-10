#This program is used to generate  various random passwords.
#can be run off of the command line with arguments, or can be run as a module.
import numpy as np
import string
import sys
import argparse






Lowercase_Letters = list(string.ascii_lowercase)
Uppercase_Letters = list(string.ascii_uppercase)  #Lists of Password Components to be used later
Digit_List = list(string.digits)
Punctuation_List = list(string.punctuation)


def passme(Lmin=16,Lmax=24, N=1, Lowercase=True, Uppercase=True, Digits=True, Punctuation=True):

    """Generate N Random Passwords with the given arguments.
        Parameters:
        -----------------------------------------------------------------------------
        Lmin: Int
          Minimum length of Password. Default is 16
        Lmax: Int
          Maximum length of Password. Default is 24
        N: Int
          Number of Passwords to generate. Default is 1
        Lowercase: True/False
          Determines if Lowercase Latin Alphabet Letters are included. Defualt is True.
        Uppercase: True/False
          Determines if Uppercase Latin Alphabet Letters are included. Default is True.
        Digits: True/false
          Determines if Arabic Digits are included. Default is True
        Punctuation: True/False
          Determines if Punctuation is included. Default is True
        Special: True/False
          Determines if Special characters are used
    """
    
    assert(Lmin >= 0), "cannot have negative password length"
    assert(Lmin <= Lmax), "Minimum Password Length must be less than maximum"
    assert(Lmax >=0), "Maximum Password Length Must be greater than 0"
    assert(N >= 0), "Cannot Generate a negative number of Passwords"
    
    options = []
    x = 0
    
    if Lowercase == True:          #Specifies which character lists are being used in the module
        options.append(1)  #If there are any False labeled lists they will not be included in options
        x = x+1                  #x variable determines how many character lists are included
    if Uppercase == True:        #x used to determine how long the list needs to be after the initial characters
        options.append(2)
        x = x+1
    if Digits == True:
        options.append(3)
        x = x+1
    if Punctuation == True:
        options.append(4)
        x = x+1
        
    assert(Lmin >= x), "Password must contain at least as many characters as 1 of each type"
    
    for n in range(N): #Creates N passwords
        password = ''   #create new password variable string for each new password
        if Lowercase == True: #append random element of each list to beggining of password to assure at least 1 of each
            password += np.random.choice(Lowercase_Letters)
        if Uppercase == True:
            password += np.random.choice(Uppercase_Letters)
        if Digits == True:
            password += np.random.choice(Digit_List)
        if Punctuation == True:
            password += np.random.choice(Punctuation_List)
        Length=np.random.randint(int(Lmin),int(Lmax+1))-x #generates random length of password between the minimum and maximum values
        for i in range(Length): #adds a random element to password up to the length of the password
            c = np.random.choice(options) #randomly choose element to include
            if c == 1: 
                password += np.random.choice(Lowercase_Letters) #append element to password
            if c == 2:
                password += np.random.choice(Uppercase_Letters)
            if c == 3:
                password += np.random.choice(Digit_List)
            if c == 4:
                password += np.random.choice(Punctuation_List)
                
        print(password)
        
def _pcl():  
        """Parse Command Line and generate a list of parameters for passme()"""
        parser = argparse.ArgumentParser(description='Create Random Passwords, All options are default True')
        parser.add_argument('-Lmin', help="Minimum Length of Password (default 16)",default=16, type=int)
        #Define minimum length of passwords
        parser.add_argument('-Lmax', help="Maximum Length of Password (default 24)",default=24, type=int)
        #Define Maximum length of passwords
        parser.add_argument('-N', help="number of passwords to generate (default 1)",default=1, type=int)
        #Define number of passwords
        parser.add_argument('-Lowercase', help="Disable Lowercase Letters(any input will disable)",default=True)
        #Determine which characters are used in the passwords
        parser.add_argument('-Uppercase', help="Disable Uppercase Letters(any input will disable)",default=True)
        
        
        
        parser.add_argument('-Digits', help="Disable Digits (any input will disable)",default=True)
        
        parser.add_argument('-Punctuation', help="Disable Punctuation (any input will disable)", default=True)
        
        args = parser.parse_args()
        return args
        
def _main():
    """runs passme() with command line inputs using _pcl() to generate passwords from the command line"""
    args = _pcl()
    passme(int(args.Lmin), int(args.Lmax), int(args.N), args.Lowercase, args.Uppercase, args.Digits, args.Punctuation)
    
if __name__ == '__main__':
    _main()