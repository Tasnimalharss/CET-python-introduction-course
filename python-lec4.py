''' while example '''
i =0
while i < 5:
    print(i)
    i+=1
else:
    print('end')
     
'''
Appened and extend
Use a loop to display elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]'''

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(1,len(my_list),2):
    print(my_list[i])

'''Write a program that will allow someone to guess a four digit pin exactly 4 times. If the user guesses the number correctly.
 It prints “That was Correct!”  Otherwise it will print “Sorry that was wrong.” Program stops after the 4th attempt of if they got it right.
For ex :pin = 0704'''
pin=0704
for i in range(4):
    e_pin=int(input('Enter your pin'))
    if e_pin ==pin:
        print('That was Correct!')
        break
    else:
        print("Sorry that was wrong.")
else:
    print("You failed")


'''Write a program to use the loop to find the factorial of a given number
For example: calculate the factorial of 5
5! = 5 × 4 × 3 × 2 × 1 = 120.'''

num=int(input('Enter the number'))
fact=1
for i in range(1,num+1):
    fact*=i
    #fact=fact*i
print("The factorial is" , fact)

'''Using a for loop and .append() method append each item with a Dr. prefix to the lst.
lst1=["Phil", "Oz", "Seuss", "Dre"]
lst2=[]'''

lst1=["Phil", "Oz", "Seuss", "Dre"]
lst2=[]
for name in lst1:
    lst2.append('Dr '+name)
else:
    print(lst2)
    
'''Using for loop and if statement, append the value minus 1000 for each key to the new list
if the value is above 1000. i.e.: if the value is 1500, 500 should be added to the new list.
dict={"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst=[]
'''
d={"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst=[]

for key in d:
    if d[key] > 1000:
       lst.append(d[key]-1000)     
print(lst)


'''printing every char in string using for'''

txt='askjdkas'
for i in txt:
    print(i)

    
'''Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]'''

list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)):
    print(list1.pop(-1))

rev = reversed(list1)
for item in rev:
    print(item)

    
    
