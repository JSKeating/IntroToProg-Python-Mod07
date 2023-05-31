**Jordan Keating**

**May 31, 2023**

**Foundations of Programming: Python**

**Assignment 07**

**[GitHub Page](https://github.com/JSKeating/IntroToProg-Python)**
# Pickling and Error Handling
## Introduction
This assignment was a bit more open-ended - our task was to create a program that demonstrates both pickling and error handling. I will start out by talking a little bit about the differences between pickled files and the text files we’ve been working with previously and then move into my idea for a program, a Home Buying/Selling calculator. The program will require quite a bit more time and attention later on to be really show ready for an interview situation, but it was a fun stretch to see what I could come up with while exhibiting these two techniques. 
## Text files vs. Binary files
So far in this course, we’ve been reading, writing and appending text files. Binary files work in much the same way, but with a couple of key differences. Binary files save data in bytes while a text file saves data as characters. A text file is easily manipulated from outside of a program (it’s easy to read and understand from the NotePad for example), while a binary file would be difficult to change outside of the intended program. 

By using pickling, as we’ll see later, you can add an additional level of security to the data you intend to store. When opened by a human, these binary files will look almost like complete gibberish. Only when the file is “un-pickled” can one understand what the data means. 
