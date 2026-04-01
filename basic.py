#%%
'''### Syntax 
- Single line Comments and multiline comments 
- Syntax and Semantics'''

#this is my first Code start
'''bfjfinef 1+2'''

#%%
#syntax
## Basic Syntax Rules In Python
## Case sensitivity- Python is case sensitive

name_="sp"
name="sp"

print(name_)
print(Name)
print(name_==name)

#%%
'''Indentation
Indentation in Python is used to define the structure and hierarchy of the code. Unlike many other programming languages that use braces {} to delimit blocks of code, Python uses indentation to determine the grouping of statements. This means that all the statements within a block must be indented at the same level.'''
## Indentation
## Python uses indentation to define blocks of code. Consistent use of spaces (commonly 4) or a tab is required.

age= 3.4
print(type(age))
#%%
if age>30:
    
    print(age)
    
print(age)

if age>38:
    print("age is more")



#%%
## This is a single line comment
print("Hello World")

#%%
## Line Continuation
##Use a backslash (\) to continue a statement to the next line

total=1+2+3+4+5+6+7+\
4+5+6

print(total)

#%%
## Multiple Statements on a single line
x=5;y=10;z=x+y
print(z)

#%%
##Understand  Semnatics In Python
# variable assignment
age=55 ##age is an integer
name="sp" ##name is a string

#%%
type(age)
type(name)

#%%
## Type Inference
variable=10
print(type(variable))
variable="sp"
print(type(variable))

#%%
age=55
if age>25:
    print(age)

#%%
## Name Error
a=34
b=22
print(a)
a=b
b
print(a)
#%%
## Code exmaples of indentation
if True:
    print("Correct Indentation")
    if False:
        print("This ont print")
    print("This will print")
print("Outside the if block")


#%%
'''Variables'''

#%%
print("trial run")
# %%
