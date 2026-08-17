#This entire module practice is based on Program no. 71 in basic_practice.py
#Open both program 71 documentation there and the specific block here

"""#Importing Entire module
import basic_practice
basic_practice.make_pizza(16,'pepproni','extra cheese','mushrooms','green pepper')
basic_practice.make_pizza(12,'red pepper')"""

"""#Importing specific functions instead of entire module
from basic_practice import make_pizza
make_pizza(16,'mushrooms','extra cheese','green pepper')
make_pizza(12,'red_pepper','pepproni')"""

"""#Using as to give a function as alias
from basic_practice import make_pizza as mp
mp(16,'pepproni','mushrooms','extra cheese')
mp(12,'green pepper')"""

"""#Using as to give a module as alias
import basic_practice as bp
bp.make_pizza(16,'pepproni','red_pepper','extra cheese')
bp.make_pizza(12,'green pepper')"""

"""#Module is a file with the extension .py and contains the code which you will import in your program
#It helps us in the sense we don't actually need to see the code inside the module . We just need to understand the higher level logic
#Importing a module and entire functions contained in it
#Importing a specific function -> from module_name import function_0 , function_1 , function_2
#Importing a module with a alias -> import module_name as mp -> mp.function_name(args)
#Importing a function as an alias -> from module_name import function_name as fn  -> fn(args)
#Importing all functions in a module using asterisk -> from module_name import * -> function_name(args)
#We generally don't use this asterisk statement incase we importing a large module that you didn't write
#If the module contains an existing function that matches the name of the function in your program we get unexpected results
#One more thing that we actually need to remember that the module and your program being in the same directory is the simplest way for python to find your module"""










