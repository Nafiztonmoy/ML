#variables and data_type
int="Nafiz"
print (int)

#Data type casting:

print ("#-1")
b=float(1)
print(b)

#0 User Input and Data Type Casting
print ("#0") 
A=input("Whats her name?")
print("Your crushs name is "+ A)


#String Formatting in Python
'''A="hello world"
      012345678910 <--(0 based indexing) + space counts as a index as well'''
#1.Accessing an index
print ("#1") 
A="hello world"
print(A[0])

#2.lenth
print ("#2") 
A="hello world"
print(len(A))

#3.check 
print ("#3") 
A="hello world"
print("hello "in A)

#4.slicing
print ("#4") 
A="hello world"
print(A[1:4])

#5.upper and lower
print ("#5") 
A="hello world"
print(A.lower()) 
''' 'upper' on other case'''

#6.String addition
print ("#6") 
a="hello"
b="world"
c=  a +" "+b
print(c)

#7.F-String
print ("#7") 
A="hello"
print(f"world{A}")

#Operator
'''Compasion operator(>,<,==,<=,>=,!=)
   Bitwise opeartor(&,or |,Not ~,Xor ^)
   logical operator(if,else,elif)
   Arithmatic(addition,subtraction,multiplication,division,floor division,Modulus)
'''
#Floor division(//):{4.5-->4]+Reminder(%)
print("#8")
f=9
g=2
h1=f//g
h2=f%g
print(h1)
print(h2)

#Logical operator:TASK 2 & 3
#Task 2
print("#9")
x=input("The value of X:")
y=input("The value of y:") 
z=input("The value of z:")  
if x>y and x>z:
    print("x is the largest number" )
elif y>x and y>z:
    print("y is the largest number")
else:
    print("z is the largest number")

#Task 3 (FLoat kore nite hobe otherwise string detected hoy as input() always returns a string.)
print("#10")
Cg1=float(input("First guy cg:"))
Cg2=float(input("Second guy cg:"))
Cg3=float(input("Third guy cg:"))
if Cg1<Cg2 and Cg1<Cg3:
    print("First guy has lowest Cg")
elif Cg2<Cg1 and Cg2<Cg3:
    print("Second guy has lowest Cg")
else:
    print("Third guy has lower cg")
x=Cg1+Cg2+Cg3
avg_cg=x/3
print("The avg Cg is",avg_cg)

#List/for loop/while loop:

#for loop:
print("#11")
fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)

#nested for loop
print("#12")
for x in range(11): #0-10 print korbe
    print(x)

'''#doing a matrix using c++
1 2 3
4 5 6 
7 8 9    
(outer loop for rows and inner loop for columns)
int number=1
for(int i=0;i<3;i++)//outer loop{
   for (int j=0;j<3;j++)//inner loop{
   cout<<number<<""
   number++;
   }
   }


'''
print("#13")
number=1
#outer loop
for i in range(3):
    #for inner loop
    for j in range(3):
        print(number,end=" ")
        number += 1
    print()    

#CHAPTER ! TOPIC 10:Loops in python
print("#14")#Task 4
i=1
while i<=9:
    print(i,end=" ")
    i+=1
  
print("#15")
i=1
while i<=4:
    print("**",end=" ")
    i+=1 

print("#16")
i=1
while i<=1:
    print("** * **",end=" ")
    i+=1
print("#17")#PRINT 1 22 333 4444 (logic is “Number of iterations = number of digits printed.
            #means outer loop goes (1-4) 4 times and inner loop goes i times as Number of iterations = number of digits printed)
            #first find out how many times the iteration will go,then print
i = 1
while i <= 4:
    j = 1
    while j <= i:
        print(i, end="")
        j += 1
    print(" ", end="")  # space between groups
    i += 1
print("#18")#print 1 13 135 1357 

i = 1
while i <= 4:
    j = 1
    num=1
    while j <= i:
        print(num, end="")
        num +=2
        j += 1
    print(" ", end="")  # space between groups
    i += 1

print("#19")#print 1 12 123 1234
i = 1
while i <= 4:
    j = 1
    num=1
    while j <= i:
        print(num, end="")
        num +=1
        j += 1
    print(" ", end="")  # space between groups
    i += 1

print("#20")#print 2 24 246 2468    
i = 1
while i <= 4:
    j = 1
    num=2
    while j <= i:
        print(num, end="")
        num +=2
        j += 1
    print(" ", end="")  # space between groups
    i += 1
print("#21")#1357 135 13 1

i = 4
while i >= 1:
    j = 1
    num = 1
    while j <= i:
        print(num, end="")
        num += 2
        j += 1
    print(" ", end="")  # space between groups
    i -= 1    






        




    
    
    




















