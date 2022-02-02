#Basic Marks Counting codes!!
#Maded By HYPER!!
#gitHub https://github.com/HYPER-AD17 OR https://github.com/DEV-AD13
#Tg @HYPER_AD17 !! @CODER_DEV13

a = int(input("\nEnter Your Mark's In 1st Subject :\n\n"))

b = int(input("\nEnter Your Mark's In 2nd Subject :\n\n"))

c = int(input("\nEnter Your Mark's In 3rd Subject :\n\n"))

d = int(input("\nEnter Your Mark's In 4th Subject :\n\n"))

z = str((a+b+c+d)/4)

#Now We start if, elif , and else modules

if(a>=90 or b>=90 or c>=90 or d>=90 and z>=90):
 print("\n\nWell done!! You Are passed the Exam with Great Marks.\n")
 print('\nYour Total percentage is ' + z)
 print('''\nYour Grade is 'A'.\n ''')
elif(a>=80 or b>=80 or c>=80 or d>=80 and z>=80):
 print('\nCongo!! You are passed in the Exam.\n')
 print('\nYour Total percentage is ' + z)
 print('''\nYour Grade is 'B'.\n ''')
elif(a>=70 or b>=70 or c>=70 or d>=70 and z>=70):
 print('\nNyc!! You Passed the exam.\n')
 print('\nYour Total percentage is ' + z)
 print('''\nYour Grade is 'C'.\n ''')
elif(a>=50 or b>=50 or c>=50 or d>=50 and z>=50):
 print('\nGood! You Are pass!.\n')
 print('\nYour Total percentage is ' + z)
 print('''\nYour Grade is 'D'.\n ''')
else:
 print('\nSad!! You Are Fail.!\n')
 print('\nYour Total percentage is ' + z)
 print('''\nYour Grade is 'E'.\n ''')
 
#Code Finished!!
#The End!!
