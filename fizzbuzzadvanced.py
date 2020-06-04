d = {}
max = int(input())
fizz = int(input())
a = input()
d[fizz] = a

while a.lower()!='buzz':
  tezz = int(input())
  a = input()
  d[tezz] = a

for fizzbuzz in range(max):  
    string = ''
    for i in d:
        if  fizzbuzz%i==0:
            string+= d[i]
     
    if not string: 
        print(fizzbuzz) 
    else:
        print(string)
