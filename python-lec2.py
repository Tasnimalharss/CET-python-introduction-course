
emp={}
emp['age'] =int(input('Enter your age'))
emp['exp'] = int(input('Enter your expierence'))
emp['grade']=int(input('Enter your grade'))

if (emp['age'] > 18 and emp['age'] <30):
    if((emp['exp'] > 5) or (emp['grade']>=85 and emp['grade']<100)):
        print('You can work here')
else:
    print('You can\'t')

    
