num = int(input("Enter number:"))
if num<=1:
    print("Number is not prime")
    
else:
    for i in range(2,num):
     if (num%i) == 0:
         print(num,"is not prime")
         break
        
     else:
         print(num,"is a prime number")
         break
           
