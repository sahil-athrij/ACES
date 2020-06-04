
max = int(input())
fizz = int(input())
buzz = int(input())
for fizzbuzz in range(100):  
    string = ''
   
    if fizzbuzz % fizz == 0:      
        string+='Fizz'
 
    if fizzbuzz % buzz == 0:       
        string+='Buzz'
        print(string)                                      
        continue
  
    print(fizzbuzz) 
