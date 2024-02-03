# 1.3 Journal

## Learning Goals

Implement conditional statements in Python to determine program flow

Use loops to reduce time and effort in Python programming

Write functions to organize Python code

### 1. In this Exercise, you learned how to use if-elif-else statements to run different tasks based on conditions that you define. Now practice that skill by writing a script for a simple travel app using an if-elif-else statement for the following situation:

The script should ask the user where they want to travel. 
The user’s input should be checked for 3 different travel destinations that you define. 
If the user’s input is one of those 3 destinations, the following statement should be printed: “Enjoy your stay in ______!”
If the user’s input is something other than the defined destinations, the following statement should be printed: “Oops, that destination is not currently available.”

```
    destinations = ["Iowa", "North Carolina", "Florida"]

    a = input("enter your travel destination: ")

    destination_found = False

    for place in destinations:
        if place.lower() == a.lower():
            destination_found = True
            break
    if destination_found:
        print("Enjoy your stay in " + a + "!")
    else:
        print("Oops, that destination is not currently available.")
```


### 2 Imagine you’re at a job interview for a Python developer role. The interviewer says “Explain logical operators in Python”. Draft how you would respond.

Logical operators in python deal with truth and false statements. They are constructed using ```> < >= <=``` to be able to determing find if the statement is truthful or false. These can be combined with ```or``` and ```and``` statements to be able to compare many logical expressions to determin what outcome should come from them. 

### 3 What are functions in Python? When and why are they useful?

Functions in python are used to manipulate data and to look through data. They can grab or find specific things you are looking for and change this or work with them. An example of this would be a for loop looking through a whole set of data to see if it matches something that was input, then it could pass this along or work with it to do calculations or any number of changes. 

### 4 In the section for Exercise 1 in this Learning Journal, you were asked in question 3 to set some goals for yourself while you complete this course.  In preparation for your next mentor call, make some notes on how you’ve progressed towards your goals so far.

I have gotten a better handling of what python can do and how to manipulate the functions within. 

I still want to learn more about the larger scope of big projects or tasks that can be done with python. I understand the simple data entry and manipulation however I still want to know how it can be used to do larger things and how it can be implimented to work with the user front of the site. 

I would also like to learn how scripts in a local environment gets put out into the world and how it interacts with the rest of the applications out in the world. It works great for messing with data and getting statistics and calculations but I do not currently see it usefulness in larger scope applications. 