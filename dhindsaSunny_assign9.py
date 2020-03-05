'''Dhindsa Sunny CSCI-0002.004 Assignment 10'''

#create program that runs through movie_reviews.txt file
openFile = open('movie_reviews.txt', 'r')

#read in the data using .read() 
readReviews = openFile.read()
#.split doesn't exist for text files, have to read it in first

#now split the function
splitReviews = readReviews.split("\n")

#prompt user for word
word = input("Enter a word to test ")

#create counter variables
count = 0
avg = 0
score = 0 

#iterate through list
for x in splitReviews:
    if word in x: 
        score += int(x[0])
        count+=1
try:
    avg = score/count
except:
    print("This word does not exist in our reviews")
    print("Cannot determine if this word is positive or negative")

else:
    print(word, "appears", count, "times")
    print("the avg score for reviews containing the word 'happy' is", avg)
    if avg>2:
        print("This is a positive word")
    elif avg<2:
        print("this is a negative word")
    elif avg == 2:
        print("This is a neutral word")




        
        

