### Data Type

## String 
#method,slicing,format
# print("hello world")
# print("The resutl of {0} and {1} is \n{2}".format(1,2,1+2))

# import math
# print(f'The value of pi is approximately {math.pi:.3f}.')

# bugs = 'roaches'
# count = 13
# area = 'living room'
# print(f'Debugging {bugs=} {count=} {area=}')
#_________________________________________________________________

##Number 
#int,float,complex
#_________________________________________________________________

##Boolean
#True,#False
#_________________________________________________________________

##Array
#Methods,Slicing(start:end:step),index,changeable
# lis1=['abb',2,1.23,1+5j,True,False] *****Ordered,Changeable,Allow Duplicates,The list() Constructor
# print(lis1[::-1])                        ####note the double round-brackets

# Tup1=('aa','bb','cc')               *****Ordered,Unchangeable,Allow Duplicates,The tuple() Constructor
# print(Tup1.index('aa'))                  ####note the double round-brackets
# (AA,BB,CC)=Tup1  ##Using Asterisk
# print(AA)

#Set items are unordered, unchangeable, and do not allow duplicate values.
# set1={1,2,3,4,5}                    *****Unordered,Unchangeable,Duplicates Not Allowed,The set() Constructor
# set2={3,4,5,6,7,8}                        ####note the double round-brackets
# print(set1-set2)#| , & , set1 - set2 , set2 - set1 , set1^set2

# Dic1={'abc':1,1:'abc',True:"haha","mylist":lis1[::-1]}
#                                     *****Ordered or Unordered?,Changeable,Duplicates Not Allowed,
# print(Dic1["mylist"])                      ####note the double round-brackets


## Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
#____________________________________________________________________________________________________________________

###Operators
##Arithmetic Operators
# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division
#________________________________

##Assignment Operators
# =	x = 5	
# +=	x += 3	
# -=	x -= 3	
# *=	x *= 3	
# /=	x /= 3	
# %=	x %= 3	
# //=	x //= 3	
# **=	x **= 3	
# &=	x &= 3	
# |=	x |= 3	
# ^=	x ^= 3	
# >>=	x >>= 3	
# <<=	x <<= 3	
#__________________________________

##Comparison Operators

# ==	Equal		
# !=	Not equal		
# >	Greater than		
# <	Less than		
# >=	Greater than or equal to		
# <=	Less than or equal to	
#___________________________________

##Logical Operator
#and
#or
#not
#___________________________________

##Identify Operator
#is
#is not
#___________________________________

##Membership Operator
#in
#not in
#____________________________________________________________

##Bitwise Operator
# & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	NOT	Inverts all the bits	~x	
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
#____________________________________________________________________________________________________________________________________________

###Control Structure     (that is use for decision making)
##if
##elif
##else
##Nested If
#______________________________________________________

###Looping 
##for loop 
##while loop
##Nested Loops

# **break**  Statement
#(the break statement we can stop the loop even if the while condition is true)

# **continue** Statement
#( the continue statement we can stop the current iteration, and continue with the next:)

# ** else **  Statemen
#(else statement we can run a block of code once when the condition no longer is true:)

# ** pass ** Statement
#( put in the pass statement to avoid getting an error.)




print("hello world")










