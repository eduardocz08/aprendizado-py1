import math
def verificar_primo (n):        
    if n<=1:
        return False    
  
    if n == 2 or n==3:
        return True 
    
    for i in range(2,math.isqrt(n) +1):
        if n%i ==0:
            return False
    return True


print (verificar_primo (10))



