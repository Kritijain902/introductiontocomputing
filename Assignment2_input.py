#Assignment 2
#Name = KRITI Jain
#SID = 21102078(CIVIL)



#question 1

#given- take input as 'Python is a case sensitive language'
#(a)
string = str("Python is a case sensitive language")
print("INPUT STRING = ",string)
print("(Answer of a)")
length=len(string)
print(length)
print

#(b)
print("(Answer of b)")
reverse_string=string[length::-1]
print(reverse_string)

#(c)
print("(Answer of c)")
new_string=string[10:26]
print(new_string)

#(d)
print("(Answer of d)")
#replace 'a case sensitive' with 'oject oriented'
replaced_string=string[0:10]+'object oriented'+string[26:35]
print(replaced_string)

#(e)
print("(Answer of e)")
index_a=string.find('a')
print(index_a)

#(f) first check the index of white spaces and then write the new string by not using those index
print("(Answer of f)")
remove_whitespaces=string.replace(" ","")
print(remove_whitespaces)




#question 2
name='Kriti Jain'
SID=21102078
department_name="Civil"
CGPA='9.0'

print("Hey,%s Here!"%(name))
print("My SID is %d"%(SID))
print("I am from %s department and my CGPA is %s"%(department_name,CGPA))




# question 3
a = 56
b = 10
#A
print("Answer of A")
print(a & b)
#B
print("Answer of B")
print(a | b)
#C
print("Answer of C")
print(a ^ b)
# D
print("Answer of D")
print(a << 2)
print(b << 2)
# E
print("Answer of E")
print(a >> 2)
print(b >> 4)




# question 4
#check whether word name is in the string given by user or not 
string = str(input("Enter the string: "))
if("name" in string):
    print("Yes\n")
else:
    print("No\n")




#question 5
#to check whether the given input lengths can form a triangle or not
side_1_of_triangle=int(input("Give a number:"))
side_2_of_triangle=int(input("Give a number:"))
side_3_of_triangle=int(input("Give a number:"))

if(side_1_of_triangle+side_2_of_triangle>side_3_of_triangle and side_2_of_triangle+side_3_of_triangle>side_1_of_triangle and side_1_of_triangle+side_3_of_triangle>side_2_of_triangle):
    print("The triangle is possible")
else:
    print("The triangle is not possible")




#question 6
def countSetBits( n ):
    count = 0
    while n:
        count += 1
        n &= (n-1)
    return count
     

def FlippedCount(a , b):
 
    return countSetBits(a^b)
    
a=int(input("First no:\n"))
b=int(input("second no:\n"))
print(FlippedCount(a,b))





