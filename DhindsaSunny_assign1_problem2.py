#ask the user for an input of names; store each as a string
name1 = input("Please enter name #1: ")
name2 = input("Please enter name #2: ")
name3 =input("Please enter name #3: ")
#print line break
print("")
print("Here are your names in every possible order:")
#44 dashes
print("--------------------------------------------")
#have line breaks between every different combination
#print combo1 after empty string
print("")
print("1.", name1,", " ,name2,", ", name3,sep="")
#print combo2 after empty string
print("")
print("2.", name1,", ", name3,", ", name2,sep="")
#print combo 3 after empty string
print("")
print("3.", name2,", ", name1,", ", name3,sep="")
#print combo 4 after empty string, but have each on different lines (no commas)
print("")
print("4.", name2)
print(name3)
print(name1)
#print combo 5 after empty string, different lines with no comma seperators
print("")
print("5.", name3)
print(name2)
print(name1)
#print combo 6 after empty string, different lines with no comma seperators
print("")
print("6.", name3)
print(name1)
print(name2)
