# String are the datatype which are used to store charectors and even long paragraphs.

# String are written in single or double qutation 

# Writing string in single qutaion and double qutation.

print('In the name of Allah Almighty.')# String in single qutation.
print(" In the name of Allah Almighty.")# String in the double qutation.

# storing a string value in variable.
myword=" In the name of Allah Almighty."

#print value 
print(myword)

# String values on multiple line 

print('''
      this is first line.
      this is second line.
      this is third line.
      this is fourth line.''')

# Storing multiple line string value in variable.

thisstr='''
        this is also first line.
        this is also second line.
        this is also third line.
        this is also fourth lin.'''
#Printing value.
print(thisstr)



#=======================================================================#

##########################Using Different Modification mathods in String in Python.####################

#Uppercase Function.
# This function is used by using "upper()" function.
upperstr=thisstr.upper()
print(upperstr) # It will convert all charactors in uppercase.



# Lowecase Function.
# This function is used by using "lowe()" for the string values.
lowestr=thisstr.lower()
print(lowestr)# This function will convert all the charactors into lowercase values.

thisvar=" This is the value of the python language in the artificial intelligence"
print(thisvar.upper())
print(upperstr)


# Strip Funtion. 
# This function is used to remore white spaces before and after text.

stripstr="  this is the test.  This is also test.  Again I am taking test."
print(stripstr)
print(stripstr.strip()) # Strip function will remove first and last spaces in strings.

## Replace Function.
# This function is used to replace any particular word or charactor with any other. 
# This is done by using e.g replace("Text","Other text")

replacestr="My name is Kamran Shahid. I am studen of AI."
print(replacestr)
print(replacestr.replace("Kamran","Usman"))


# Capitalize Function
# This function is used to capatilize fisrt charactor of words in strings.

capstr="this is the test text, and i am using the test to check capatilization."
print(capstr)
print(capstr.capitalize())

#Casefold Function

# This function is used to convert string into lower case.
casestr="THIS IS ALSO TEST TEXT."
print(casestr)
print(casestr.casefold())
# This function coverts all the charactors into lower case.

#Count Function
# This function is used to count the occurance of word in string. For instance if the string has three time simialar work it will give count as tree.
countstr=" Why you are not doing good work? You are doing the work that should be improved."
print(countstr)
print(countstr.count("work"))




