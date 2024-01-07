#Note: Below the coding, each datatype is explained very well.

# Using int value and checking datatype for varification of the datatype by type() function.
thisint=32
print(thisint)
print(type(thisint))

# Using float value and checking datatype for the validation of datatype by using "type()" function.
thisfloat=32.9300
print(thisfloat)
print(type(thisfloat))

#Using Complex value and checking datatype.
# thiscomplex=3+2i


# Using Text datatype and checking its datatype .

thistext="This is the code of python language."
print(thistext)
print(type(thistext))

# Using String in multiple lines

thisstr='''

            In the name Of Allah Almighty,
            Write your code of multiple lines.
            '''
            
print(thisstr)
print(type(thisstr))

# For char datatype
thischar="A"
print(thischar)
print(type(thischar))

#Using Boolean datatype and valifing this datype by using type() function.

thisboltrue=True
print(thisboltrue)
print(type(thisboltrue))
# Using Boolean false datatype
thisbolfalse=False
print(thisbolfalse)
print(type(thisbolfalse))

# Using List for storing values in single variable and printing values by indexing.

thislist=['this','is','list','items',32,3.3]
print(thislist)
print(thislist[0])# Print first list item by using index value.
print(thislist[1:4])# Printing list item from second to fourth value.

thislist2=thislist[2]=4 # Changing the value of list item as list are changeable and ordered.


# Printing values of Tuple as tuple are represented by small brackets.

thistuple=('apple','banana','strawbarry',3,2.2)
print(thistuple)
print(type(thistuple))

#Using tuple having just a single value. We have to place comma after value
thistuplesingle=(3,)
print(thistuplesingle)
print(type(thistuplesingle))




#Using set and chekcing datatype of the set.
'''
As the set is unordered, do not allow duplicates, and 
reprensented by curly brackets.'''
thisset=('apple','banana','strawbarry',3.3,'apple')# As set do not allow duplicate value, it will print apple just once.
print(thisset)
print(type(thisset))

# Using none type
thisnonevalue=None
print(thisnonevalue)
print(type(thisnonevalue))

# Using dictionary to store keys and values. 
thisdic={
    "Name":"Usman Shahid",
    "Age":22,
    "Year":2024,
    "Nationality":"Pakistani"
}

#Printint dictionary keys and values
print(thisdic)
print(type(thisdic))

#Printing specific key values 
print(thisdic['Nationality'])

# Changing value of dictionary , as dictionary datatype is mutable and values can be edit.
thisdic["Year"]=2023
print(thisdic)



'''
Datatype:-
    Datatype are the type of assigned values to the variable. This datatype some the nature and type of assigned values that either it is, int, float, boolean, string, or any other. 
        Python language can detect datatype of variable without even nominating by programmer. Python has ability to decect datatype ,
    so even if we don't declare datatype, python will automatically detect and assign datatype to variable for assigned values'''
#  To check datatype of values or the variable, we use type() function.
print(type(34.22)) 
'''    
There are different type of dataype used in python language. Following are datatype used in python

1. Number datatype: There are mainly three types of number datatype used in python
  
    a. int datatype: This datatype is used for integer values without any decimal point value. e.g 23, 42,-422
    b. float datatype: This datatype is used for floating point values, means the numaric values having decimal points. It can be either positive or negative. e.g 22.002,-442.23,-
    c. complex datatype: This datatype is used for complex number. example of complex number can be as "2+ai" and similar to that.
    


2. Text type: This datatype is used for text values.
  
    a. string datatype: Denoted as " str " and used to store string values. String values means charecters or alphabets. 
        Example. a="AI, is the brach of Computer science."
    b. char: char is sometime used for single charector value in python 
        Example. b="A"
 
    
3. Boolean Dataype: This dataype is used for just two output that are may be "0,1" or "ture, false".
    a.true: This is used for the representation of "1" values or any presented values as correct or true output.
    b.false: The numaric value of this boolean value is"0" and showes false for undesired out put or empty values
    

4. Sequence dataype: This datatype is used to store different values at same time in a single variable. It has two main types.

    a. list: List is the ordered collection of items, it is mutable means if you want to change the values of list item in future you can do it easily.
            Represention of the list is done by using square bracket" [] " and the values of the list are sepereated by commas.
            example. list_of_fruits=["apple, banana, mangoes, strawbarry",2,42.4].
            We can include all datatype in a single list 
    
    b. tuple: Tuple of also the set of ordered collection of the items, the main difference between list and tuple is that the list is mutable means that we can 
                easily change the values of the list item in future, but the tuple is immutable: means the items of the tuple cannot be changes once it is declared .
                
                Representation of the tuple is done by usinge small braket " () " and all the values are seperated by using commas.
                We can also include all datatypes values in single tuple.
                    example: tuple_of_values=("apple, mangoes", 23,2.2)
                    
                    
5. Set type: This type is used to assign multiple values by using curly bracket " {} ", set are unordered and repeated values are not allowed in set.

        a.set: Unordered collection of items, repeatation not allowed, immutable.
            example: set_value={3,2,4,"val"}
        
        b.frozenset: Immutable version of set is known as frozenset. Means we can't change the values of set once it has been declared.
        

6. Mapping type: This datatype is used to store keys and values
        a.dic: Dictionary is used to store keys and values. Its representation is done by using curly bracket and the values of key and values are seperated by colon
            example: my_dic={
                country:"Pakistan"
                age: 33
                year" 2024
                
            }
            First value before colon is known as keys and values after colon is known as "value"
        
        
7. Binary type: This type is used for the repersentation of the values in bytes and data values.
    a. bytes: Immutable sequance of the bytes, often used for the raw data e.g (b'Hello')
    b.bytearray: Mutable sequence of bytes is called as bytearray
    c. memoryview: efficiant way to access and share memory block.
    

8. None dataype: This datatype is used to represent empty value of any declared variable.
        example: my_book=None;

'''





