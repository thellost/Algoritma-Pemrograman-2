# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:29:28 2021

@author: ASUS
"""

# Python3 implementation of the approach
#this set the modulo
m = 23

  
# Function to return the GCD 
# of given numbers
def gcd(a, b):
  
    if (a == 0):
        return b
    return gcd(b % a, a)
  
# Recursive function to return (x ^ n) % m
def modexp(x, n):
  
    if (n == 0) :
        return 1
      
    elif (n % 2 == 0) :
        return modexp((x * x) % m, n // 2)
      
    else :
        return (x * modexp((x * x) % m, 
                           (n - 1) / 2) % m)
  
  
# Function to return the fraction modulo mod
def getFractionModulo(a, b):
  
    c = gcd(a, b)
  
    a = a // c
    b = b // c
  
    # (b ^ m-2) % m
    d = modexp(b, m - 2)
  
    # Final answer
    ans = ((a % m) * (d % m)) % m
  
    return ans

#return lambda function from eliptic curve if p equals q
def elipticCurveLambdaFunctionPequalsQ(xp,yp,a):
    
    print("\nThis is the lambda numerator")
    
    numerator =  (3*xp*xp + a)
    print("Numerator :", numerator)
    
    denominator = (2 * yp)
    print("Denominator :", denominator)
    
    lambdaFunction = getFractionModulo(numerator, denominator)
    print("lambda value after mod",m,":", lambdaFunction)
    
    return lambdaFunction


#return lambda function from eliptic curve if p NOT equals q
def elipticCurveLambdaFunctionPnotequalsQ(xp,yp,xq,yq):
    print("\nThis is the lambda numerator")
    numerator =  (yq - yp)
    print("Numerator :", numerator)
    denominator = (xq - xp)
    print("Denominator :", denominator)
    lambdaFunction = getFractionModulo(numerator, denominator)
    print("lambda value after mod",m,":", lambdaFunction)
    return lambdaFunction
    

def getYrandXr(lambdaNum , Xp, Xq, Yp):
    Xr = (lambdaNum*lambdaNum - Xp - Xq) % m
    print("result inside Xr =",(lambdaNum*lambdaNum - Xp - Xq) )
    Yr = (lambdaNum *(Xp - Xr) - Yp) % m
    print("result inside Yr =",(lambdaNum *(Xp - Xr) - Yp) )
    print("Xr with this itteration of lambda value :", Xr)
    print("Yr with this itteration of lambda value:", Yr)
    return [Xr,Yr]
  
# Driver code
if __name__ == "__main__":
  
    a = 1
    b = 1
    Pfunc = [1,7]
    Qfunc = [1,7]
    
    lambdaNum = elipticCurveLambdaFunctionPequalsQ(Pfunc[0], Pfunc[1], a)
    Pfunc = getYrandXr(lambdaNum, Pfunc[0], Qfunc[0], Pfunc[1])
    
  
