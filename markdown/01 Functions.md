# Functions in Python 3
---

- In Python 3, we are able to create custom functions that are much similar to the built-in functions we have encountered
- These functions are callable and can output results to our liking
- This allows us to organize our code when our projects become more complex
- In this unit we will only cover introductory level content for functions (returning values, predetermined arguments, and nested functions).

## What is a Function?

__Function:__ a block of organized, reusable code that is usually used to perform single and related action.

_Similar concepts: methods, subroutines and procedures_

#### Mathematical Functions vs Programming Functions

__Mathematical Function:__ Functions we learn in math classes, such as Grade 11 Functions, are by in nature following the laws of mathematics. These functions (Quadratic, Rational, Trignometric and Logarithmic to name a few) are all about relating an input to an output. They also must follow the these rules:
1. One input must have only one output
2. Multiple inputs are allowed to have same output

__Programming Function:__ In computer science, a function is a self contained module of code. It is not restricted to the rules of mathematical function _unless you want it do be_.

------

## Mindset for writing Functions in Python

1. __Clean Code:__ We want organize a solution to problem or a part of a problem into a single function
2. __Algorithms:__ Without functions, we cannot express algorithms properly
3. __Resuablility:__ Functions prevent us from repeating code you've written before
4. __Single Serving:__ Functions prevent overloaded programs that look like spaghetti

## Python Function Syntax


```python
def functionName(arg1, arg2, arg3):
    ''' function docString: state purpose here
    
    arguments:
    -- arg1 : explanation
    -- arg2 : explanation
    -- arg3 : explanation
    
    return:
    -- value : explanation
    '''
    
    # write code inside the function here
    
    return value
# end of functionName()
```

- ```def``` is the keyword designated to help us __define__ a custom function
- a function must have a callable name ... it is recommended to use name that is not [built-in function](https://docs.python.org/3/library/functions.html) or [keywords](https://www.tutorialspoint.com/What-are-Reserved-Keywords-in-Python) for Python.
- ```(arg1, arg2, arg3):``` This is state our function inputs. The number of inputs a function require is up to you. A proper definition for function inputs are called __arguments__.
- We can also write a descriptor for our function by using triple single(') or double(") quotation marks
- ```return``` is a keyword designed for functions. When a function is done executing its code, we can use __return__ to help us grab the result of our function

__Let's create an example function for the area of a circle.__


```python
def areaCircle(radius, pi):
    ''' areaCirlce() is a function that calculates the area of a circle
    
    arguments:
    -- radius : floating point value
    -- pi : floating point value
    
    return:
    -- area : the resulting area from the given arguments
    '''
    
    area = pi * (radius ** 2)
    
    return area
# end of areaCircle

my_radius = 6
pi = 3.14159

my_circle_area = areaCircle(my_radius, pi)
my_circle_area2 = areaCircle(my_radius, 3.14)
 
print('The area of my circle is %.4f units squared.' % my_circle_area)
print('The area of my circle with pi of 3.14 is %.4f units squared.' % my_circle_area2)
```

    The area of my circle is 113.0972 units squared.
    The area of my circle with pi of 3.14 is 113.0400 units squared.


## Explanation

1. We defined a function called _areaCircle_
2. There are 2 arguments
    - radius
    - pi
3. There is a docstring trapped inside triple single quotation marks
4. Variable area inside the function is calculated by using the argument variables for the function
5. We use the __return__ keyword to help us grab the resulting variable called: _area_
6. After the function has been defined we created our new variables of __my_radius__ and __pi__
    - please note that the new variable pi = 3.14159 does not conflict with the function's argument variable
    - We can use these new variables to be the explicit arguments for when we call the function
7. We calculated the result for two variables: __my_circle_area__ and __my_circle_area2__ by assigning it to the result of us calling our defined function
    - When the function __areaCircle__ is called, it will take the given arguments to calculate the function's area variable
    - Once the calculation is finished, it will be __returned__ back to the variable and assigned with the result
