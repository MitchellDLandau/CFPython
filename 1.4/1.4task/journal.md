# 1.4 Journal File Handling in Python

Goal: Use files to store and retrieve data in Python

## Reflections Questions

## Why is file storage important when you’re using Python? What would happen if you didn’t store local files?

Each instance of python is only active and storing data while it is open and none of the data persists into other times you run something in python. Once you exit out all data is gone unless you have stored it with some other means. This is why local file storage is so important so that projects can continue to have the data they were working with before. This would also be how other large data sets could be accessed by python to run larger and more complex data analysis. 

## In this Exercise you learned about the pickling process with the ```pickle.dump()``` method. What are pickles? In which situations would you choose to use pickles and why? 

pickling is the act of converting a python object into a file format to be saved to the machine, the machine can then destructure the byte of information that was pickled so that python can use the data again. Pickles would be useful if you need information to persist in multiple python instances or projects.

## In Python, what function do you use to find out which directory you’re currently in? What if you wanted to change your current working directory?

```os.getcwd()``` would tell you which directory you are currently working on in python. You will also have to import the OS module using ```import os``` before you are able to use this. You can also do a ton of very useful things using this like changing your directory with ```os.chdir("<Path of directory wanted>")```. This would be useful if you need to grab data or functions from different places in your projects while working in python. 

## Imagine you’re working on a Python script and are worried there may be an error in a block of code. How would you approach the situation to prevent the entire script from terminating due to an error?

I would impliment ```try```, ```except``` blocks so that if we were to run into errors in some of our code we can tell it what to do and have it continue on. This also allows us to see where the code ran into an error to help us troubleshoot later on. You can even add the ```finally``` part to these blocks to make sure that no matter what you get to the last part of the ccode and it gets run. 

## You’re now more than halfway through Achievement 1! Take a moment to reflect on your learning in the course so far. How is it going? What’s something you’re proud of so far? Is there something 

With python being a whole new language for me it is not surprising that the start felt like reviewing things I already know how to do just in a different way. Now that we have been dealing with data handling and storage means it has made python seem a lot more useful. I still am having some trouble seeing how it can be helpful with large scale projects and I am quite confused as to how it can make the front end of a website seeing as all we have done so far is data entry and return in the most basic of ways. 
I do think that I need to practice a bit more with knowing how to grab specific data that I am trying to get when it is nested within objects. 