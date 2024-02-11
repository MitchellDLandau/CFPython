# Exercise 1.5: Object-Oriented Programming in Python

## Goal: 

Apply object-oriented programming concepts to your Recipe app

## Reflection Questions

## In your own words, what is object-oriented programming? What are the benefits of OOP?

Object-oriented programming is when information and data is treated as a single thing that can be added to or changed. Each single object can then be manipulated using functions as it is passed between parts of the application. 

Object_oriented programming allows more freedom with the data that you are working with. Not every aspect that is able to be a part of the object is needed at all times so you can create and update objects as you go without their functions breaking down. 

## What are objects and classes in Python? Come up with a real-world example to illustrate how objects and classes work.

objects in python is a means of storing and passing around information. These can then be passed as props to other parts of the application. classes are a means of handling and creating objects as they allow you to dictate how getting information from an object or changing it can take place. 

Imagine a class named clothing. Clothing can be made up of many materials, have different colors, and be for different parts of the body. You could create a class that helps describe different kinds of clothing and the object that you create using this would hold its different charachteristics. A single objects by be named shirt, color: red, fabric: cotton, body part: chest. This would be one object but using the class that we set up earlier you could describe all sorts of clothing.

## In your own words, write brief explanations of the following OOP concepts; 100 to 200 words per method is fine. 

### Inheritance 

Inheritance is when an object can inherit methods used in another class into their own. They can only inherit methods from a partent class ie. one step larger than themselves and the parents cannot inherit their methods. This allows you to nest similar classes under one larger class so they can all have the parts that would be the same amongst themselves. 

### Polymorphism

Polymorphism is where a given atribute has the same name accross multiple classes. With our earlier example about clothing you could have one atribute named where that describes where you would wear a piece of clothing, depending on the class you are in this same polymorphic name could give you different body parts. 

### Operator Overloading

Operator overloading is used when you want to use pythons operators with custom classess. To do so you would have to specify that you are doing so by using ```__add__()``` for ```+``` and ```__sub__()``` for ```-```. The regular built in python methods would not work and would give a TypeError so this is why you would have to be more specific as to what is happening with working with these classes. 