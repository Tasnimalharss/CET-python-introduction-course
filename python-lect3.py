#Answer of the first Q 
grade = int(input('Please enter your grade'))
if grade> 80:
   print('A')
elif grade<80 and grade>60:
   print('B')
elif grade<60 and grade>50:
   print('C')
elif grade<50 and grade>45:
   print('D')
elif grade<45 and grade>25:
   print('E')
else :
   print('F')
   
#Answer of the second Q 
c = input('Please enter the char')
arr = ['e' ,'a','i','u','o']

if c in arr:
    print('vowel')
else:
    print('constant')

#Answers of the third Q
x = int(input('First number'))
y = int(input('Second number'))
z = int(input('Third number'))
    
#First answer:    
if x >= y and x>=z:
    print(x)
elif y >= x and y>=z:
    print(y)
else:
    print(z)
#***************
#Second answer:        
if x >= y:
   if x >= z:
      print(x)
   else:
      print(z)
else:
    if y >=z:
        print(y)
    else:
        print(z)
#Third answer:        
print(max(x,max(z,y)))
#Forth answer:
temp= z
if x >= temp:
   temp=x
if y >= temp:
   temp=y
print(temp)

#Quiz game progarmm    
score=0
a=input('Enter the capital of libya')
if a == 'tripoli':
   score= score+25
   
a=int(input('Enter the number of countries in africa'))
if a == 54:
   score= score+25
   
a=input('Enter the name of larggest country')
if a == 'russia':
   score= score+25
   
a=input('Enter the name of smallest continent')
if a == 'austrilia':
   score= score+25
print('Your score is', score)


#Loop basics
arr=[5,8,1,4]

for item in arr:
    print(item)
    
for i in range(len(arr)):
    print(item[i])
    
#triming text
var= " txt "
#removes right spaces
print(var.rstrip())
#removes left spaces
print(var.lstrip())
#removes left and right spaces
print(var.lstrip())    
        
    

