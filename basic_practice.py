#1

"""message = "This is message"
print(message)
message = "This is new value assigned to the same variable"
print(message)"""

#2

"""#title method --> 
name = "mihir SOni"
print(name.title())
name = "Mihir soni"
print(name.title())
name = "mihir soNi"
print(name.title())
name = "Mihir Soni"
print(name.lower())
#lower method is typically used to store the data u won't trust the user for the capitalization"""

#3

"""#f string -->
first_name = "mihir"
last_name = "Soni"
full_name = f"{first_name} {last_name}"
print(f"Hello , {full_name.title()} !")"""

#4

"""#To use tabs and newline in output
print("\tHello\n\tMihir")"""

#5

"""#To compare string we must first keep in mind about whitespaces
name_1 = " mihir"
name_2 = "mihir "
name_3 = " mihir "
name_1 = name_1.lstrip()
name_2 = name_2.rstrip()
name_3 = name_3.strip()
#if i use print(name_1.lstrip()) it is only temporary 
print(f"\n\t{name_1}\n\t{name_2}\n\t{name_3}")"""

#6

"""#removeprefix() method -->
url_name = "https://noshud.com"
simple_url = url_name.removeprefix("https://")
print(simple_url)"""

#7

"""name = "Eric"
print(f"Hello {name}, would you like to learn some python today")"""

#8

"""name = "Mihir Soni"
print(name.lower())
print(name.upper())
print(name.title())"""

#9

"""print('Albert Einstein once said, "A person who never made a mistake had never tried something new"')"""

#10

"""famous_person = "Albert Einstein"
message = "A person who never made a mistake had never tried anything new"
print(f"{famous_person.title()} once said, {message}")"""

#11

"""filename = "python_notes.txt"
print(filename.removesuffix(".txt"))"""

#12

"""print(0.2+0.1)#it will print arbitrary number of decimals
universe_age = 14_000_000_000#to represent and understand numbers correctly
print(universe_age)
x , y ,z = 0,0,0#multiple assignments
print(f"{x},{y},{z}")
print(2+1.0)#u will see the result in float int+float = float and so on
MAX_CONNECTIONS = 5000"""

#13

"""favorite_number = 6
print(f"{favorite_number} is my favorite number")"""

#14

"""drinks = ['sprite','cocacola','pepsi',]
print(drinks)
print(drinks[0])"""

#14

"""#last item in the list or the second last item in the list --> list[-1]
drinks = ['sprite','pepsi','cocacola','limka','mountain dew']
print(drinks[-1].title())
print(drinks[-2].title())
print(drinks[-3].title())"""

#15

"""drinks = ['sprite','pepsi','cocacola','limka','mountain dew']
message = f"My favorite drink is {drinks[0].title()}"
print(message)"""

#16

"""#Modifying a list
drinks = ['sprite','pepsi','cocacola','limka','mountain dew']
print(drinks)
drinks[-1] = 'water'
print(drinks)"""

#17

"""#Adding elements to the list also known as appending the list
#Despite string methods being temporary and known to assign first and use after 
#the list methods are permanent the data inside the list is changed without assigning the values
drinks =[]
drinks.append('sprite')
drinks.append('cocacola')
drinks.append('pepsi')
drinks.append('limka')
drinks.append('mountain dew')
print(drinks)"""

#18

"""#Inserting elements to the list instead of appending
#this insert() method transfers every other value in the list to the right
drinks = ['sprite','pepsi','cocacola','limka','mountain dew']
drinks.insert(2,'string')
print(drinks)"""

#19

"""#deleting a element from the list --> del , pop and remove
drinks = ['sprite','pepsi','cocacola','limka','mountain dew']
drinks.insert(2,'string')
del drinks[2]
print(drinks)
#Here in list only pop is used to assign a value like in string but pop is also permanent
#while in string method simply calling the method won't change the string calling the pop method will change it
#so to simply assign a value pop is used
#default pop deletes the last value in the string when arguments are used
drinks.insert(2,'string')
dislike_drink = drinks.pop(2)
print(f"I don't like {dislike_drink.title()}")
#remove method is used when we don't know the index but only the value of the element
#not_like = drinks.remove('limka')
#print(f"I don't like {not_like}")
#to use remove method and also assign don't use it like pop as it will give none to the variable instead do this
not_like = 'limka'
drinks.remove(not_like)
print(f"I don't like {not_like}")
#The remove() method remove only first such element specified in the list to remove all such element use loop"""

#20

"""#Sorting a list permanently with changing the original list and temporarily without changing the original list
drinks = ['sprite','pepsi','cocacola','limka','mountain dew']
#sort is a method and sorted is a function 
#To sort/sorted first always assume list elements are in lowercase
print(sorted(drinks))#temporary method does not change the original list
print(drinks)#original order of the list
drinks.sort()
print(drinks)
drinks.sort(reverse = True)
print(drinks)
#reverse method --> To reverse the original order of the list
print(drinks)
drinks.reverse()#it is also permanent but we can find the original order by reversing again
#if u find yourself a index error use drinks[-1] for the last element"""

#21

"""family_members = ['father','mother','brother']
for member in family_members :
    print(f"Happy New Year {member.title()}")
#for prints in new line without even using \n 
#indentation mean that block is inside the for loop"""

#22

"""#Generating series of number using range function 
for number in range(1,6):#range doesn't end with the given number 
    print(number)
for number in range(6):#if no start is specified range generates number from zero
    print(number)"""

#23 

"""#Make a list of numbers that are the square of 1 to 10
squares = []
for number in range(1,11):
    squares.append(number**2)
print(squares)"""

#24

"""#range() function also accepts 3 arguments
for even_number in range(2,11,2):
    print(even_number)
#Once again , looping through a list in python doesn't require \n """

#25 

"""#few standard functions for list note here function are len(list) sum(list) min(list) max(list)
numbers =[]
for number in range(1,11):
    numbers.append(number)
list_length = len(numbers)
list_sum = sum(numbers)
list_min = min(numbers)
list_max = max(numbers)
print(f"{list_length} {list_sum} {list_min} {list_max}")"""

#26

"""#List comprehension for first 10 cubes
cubes = [natural_number**3 for natural_number in range(1,11)]"""

#27 

"""#To work with some specific items in the list --> slicing
natural_numbers =[number for number in range(1,11)] #To make a list
for number in natural_numbers[-5:]:
    print(number)#It will slice the list of natural numbers to print last five natural numbers
#If we have to work with something like last 5 or last 4 always use -number"""

#28 

#Copying a list(wrong method)
"""drinks = ['sprite','pepsi','cocacola','limka','mountain dew']
friends_drink = drinks # we can use this for assigning the same value means both lists are same if we change one other will also change
print(friends_drink)
print(drinks)
drinks.append('string')
print(friends_drink)
print(drinks)"""
#Copying a list(right method)
""""drinks = ['sprite','pepsi','cocacola','limka','mountain dew']
friends_drink = drinks[:]
drinks.append('string')
print(drinks)
print(friends_drink)"""

#29 

"""#Making a number list using range() and list() function
even_numbers = list(range(2,11,2))
print(even_numbers)"""

#30

"""#Immutable list or tuples in python
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
area = dimensions[0] * dimensions[1]
print(f"The are of the rectangle is : {area}")
#Looping over a tuple 
for dimension in dimensions:
    print(dimension)
#Although we can't modify a element in a tuple we could write over a tuple
#We can change the value assigned to a varible
dimensions = (400,20)
print(f"\n\tModified dimensions\n\t{dimensions[0]}\n\t{dimensions[1]}")"""

#31

"""age = 18
if age<=4 :
    price =0
elif age<=18:
    price = 50
else :
   price = 80
print(f"Admission fees is ${price}")"""

#32

"""required_toppings = []
available_toppings = ['mushroom','olives','green pepper','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushroom','french fries','extra cheese']
for requested_topping in requested_toppings :
    if requested_topping in available_toppings :
        print(f"Adding {requested_topping}")
    else :
        required_toppings.append(requested_topping)
if len(required_toppings) != 0:
    for required_topping in required_toppings:
         print(f"{required_topping} not available")
print("\nPizza is ready")"""

#33 

"""#Dictionaries Key - value pairs and syntax
alien_0 = {'color' : 'green' , 'health' : 5}
print(alien_0['color'])
print(alien_0['health'])"""

#33

"""#Adding new key value pairs to the dictionary
alien_0 = {'color': 'green' , 'hp' : 10 }
alien_0['points'] = 5
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#deleting a key value pair
del alien_0['hp']
print(alien_0)"""

#34

"""#Using key to access the value has one problem the key might not exist so you would get a error
#for eg: here points key does not exist in the dictionary
alien_0 = {'color': 'green', 'hp': 10 }
#print(alien_0['points']) It will give a keyerror
points = alien_0.get('points','Value does not exist')
print(points)"""

#35

"""#Looping through key-value pairs
user_data = {'name':'mihir soni','age':'17','birth date':'11/10/2007','status':'idle'}
for key,value in user_data.items():
    print(f"{key}:{value}")"""

#36

"""#Looping through key values
aliens_0 = {'color':'green','hp':10,'points':5,'x_position':0,'y_position':25}
for names in aliens_0:#OR   for names in aliens_0.keys():
    print(names)"""

#37

"""favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward':'rust',
    'phil':'python'
}
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name}")
    if name in friends:
        value = favorite_languages[name].title()
        print(f"I see your favorite language is {value}")
if 'erin' not in favorite_languages.keys():
    print("erin please take our poll")"""

#38

"""#Looping through in alphabetical order
favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward':'rust',
    'phil':'python'
}
for name in sorted(favorite_languages.keys()):
    print(name)"""

#39

"""#Looping through all values and sets
favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward':'rust',
    'phil':'python'
}
print("The most popular languages are :\n")
for value in favorite_languages.values():
    print(value)
#There is duplicate items in value so wrap set function around
for value in set(favorite_languages.values()):
    print(value)
#if we don't write key value pairs in dictionary format it is called set
#Unlike lists , tuples, dictionaries sets don't have particular order
#for eg:
names = {
    'jen','sarah','edward','phil','jen'
}
print(names)"""

#40

"""#Nested
alien_0 = {'color':'green','points':10}
alien_1 = {'color':'yellow','points':15}
alien_2 = {'color':'red','points':5}
alien = [alien_0 , alien_1 , alien_2]"""

#41

"""aliens = []
for alien_number in range(30):
    new_alien = {'color':'green', 'points':10}
    aliens.append(new_alien)
for alien_stats in aliens:
    print(alien_stats)"""

#42

"""#List in a dictionary
order = {
    'crust':'thick',
    'toppings':['cheese','pepper']
}
print(f"The order toppings are : {order['toppings']}")"""

#43

#Dictionary inside dictionary
"""users_gmail = {
    'ai.trekdrivemihir@gmail.com' : {
        'first_name':'mihir',
        'last_name':'soni',
        'location':'india'
    },
    'mihir123@gmail.com' :{
        'first_name' : 'alex',
         'last_name': 'pierra',
         'location' : 'UK'
    },
    'alexander_is_great@gmail.com' : {
        'first_name' : 'alexander',
        'last_name' : 'peru',
        'location' : 'greek'
    }
}
for gmail,data in users_gmail.items():
    print(gmail)
    print(f"{data} \n")"""

#44

"""message = input("Tell me something so that i can repeat ")
print(message)"""

#45

"""#Multi line prompt/string
prompt = "If you share your name we can personalize for you."
prompt += "\nWhat is your name? "
name = input(prompt)
print(f"Hello {name}")"""

#46

"""#int() in input() for numerical values
age = input("How old are you? ")
age = int(age)
if age >=18 :
    print("Adult")
else :
    print("Minor")"""

#47

"""#while loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
"""

#48

"""prompt = '\nTell me something u want me to repeat '
prompt += '\nType "quit" to quit '
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)"""

#49

"""#flag
flag = True
while flag:
    name = input('Enter your name: ')
    if name.lower() == 'mihir':
        flag = False
    else:
        print("Enter correct name")
    print("flag does not immediately exits the block")"""

#50

"""prompt = "\nEnter the city you want to visit "
prompt += "\nPlease enter 'quit' to quit "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else :
        print(f"I would love to visit {city.title()}")
    print("\nbreak immediately exits the block")"""

#51

"""#continue escapes only the current ongoing loop
#This program is used to print odd numbers
current_number = 1
while current_number < 10:
    if current_number % 2 == 0 :
        current_number += 1 
        continue
    else :
        print(current_number)
        current_number += 1 """

#52

"""unconfirmed_users = []
prompt = "\nEnter the names of new user :"
prompt+= "\nEnter 'quit' for further verification "
while True:
    new_user = input(prompt) 
    if new_user == 'quit':
        break
    else :
      unconfirmed_users.append(new_user)
confirmed_users = []
while unconfirmed_users :
    current_user = unconfirmed_users.pop()
    print(f"\nVerifying user : {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users has been verified :")
print(confirmed_users)"""

#53

"""#to delete multiple instances of same name in a list
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)"""

#54

"""#filling a dictionary with user input
unconfirmed_users = []
prompt = "\nEnter the names of new user :"
prompt+= "\nEnter 'quit' for further verification "
while True:
    new_user = input(prompt) 
    if new_user == 'quit':
        break
    else :
      unconfirmed_users.append(new_user)
confirmed_users = []
for current_user in unconfirmed_users :
    stats= {}
    age = input(f"\nEnter {current_user.title()} age :")
    dob = input(f"Enter {current_user.title()} dob :")
    gender = input(f"Enter {current_user.title()} gender :")
    email = input(f"Enter {current_user.title()} email :")
    stats['name'] = current_user.title()
    stats['age'] = age 
    stats['date of birth'] = dob
    stats['gender'] = gender
    stats['email'] = email
    confirmed_users.append(stats)
print("\n The confirmed users :")
for current_user in confirmed_users :
    print("\n")
    for key,value in current_user.items():
        print(f"{key.title()} : {value.title()}")"""

#55

"""def greet_user():
    print("Hello")
def greet_users(username):
    print(f"Hello {username.title()}")
greet_users('mihir soni')
def describe_pet(pet_species,pet_name):
    print(f"\nI have {pet_species.title()}")
    print(f"My {pet_species.title()}'s name is {pet_name.title()}")
describe_pet('dog','tom')
describe_pet('hamster','harry')
#order matters in positional arguments"""

#56

"""#keyword arguments so that u won't mix up the order even if u want to
def describe_pets(pet_species,pet_name):
    print(f"\nI have {pet_species.title()}")
    print(f"My {pet_species.title()}'s name is {pet_name.title()}")
describe_pets(pet_name = 'harry',pet_species = 'hamster')"""

#57

"""#default values
def describe_pets(pet_name,pet_type = 'dog'):
     print(f"\nI have {pet_type.title()}")
     print(f"My {pet_type.title()}'s name is {pet_name.title()}")
describe_pets('tom')"""

#58

"""def describe_city(city_name,country_name):
    print(f"{city_name.title()} is in {country_name.title()}")
for i in range(3):
    city_name = input("\nEnter a city :")
    country_name = input("Enter the name of the country in which the city is :")
    describe_city(city_name,country_name)"""

#59

"""def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
name = get_formatted_name(first_name = 'mihir', last_name = 'soni')
print(name)"""

#60

"""#Making a argument optional so we may or may not pass values
def get_formatted_name(first_name,last_name,middle_name=''):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
name = get_formatted_name('mihir','soni')
print(name)
name = get_formatted_name('aditya',middle_name = 'kumar' ,last_name = 'soni')
print(name)"""

#61

"""def build_person(first_name,last_name):
    person = {'first':first_name , 'last':last_name}
    return person
person = build_person('mihir','soni')
print(person)"""

#62

"""#optional argument in addition to dictionary
def build_person(first_name,last_name,age=None,middle_name = ''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    if middle_name :
        person['middle'] = middle_name
    return person
person_1 = build_person('mihir','soni',age = 18)
person_2 = build_person('aditya',middle_name = 'kumar',last_name = 'soni' , age = 19)
print(person_1)
print(person_2)"""

#63

"""def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nTell me your name")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print(f"Hello {formatted_name.title()}")"""

#64

"""def greet_users(names):
    for name in names :
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['Mihir','Adam','Eve']
greet_users(usernames)"""

#65

"""unprinted_designs = []
printed_designs =[]
def designs_input():
    prompt = "Enter designs: "
    prompt += "\n(Enter 'q' if you have finished inputting):  "
    print(prompt)
    while True:
        current_design = input()
        if current_design == 'q':
            break
        else:
            unprinted_designs.append(current_design)
def designs_process():
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model {current_design.title()}")
        printed_designs.append(current_design)

def designs_print():
    print("\nThe following designs have been printed :")
    for designs in printed_designs:
        print(designs)

designs_input()
designs_process()
designs_print()"""

#66

"""#Pass copy of list also known as slicing in case you don't want to change the original list
def designs_process(unprinted_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printed model {current_design.title()}")
        printed_designs.append(current_design)
def designs_print(printed_designs):
    print("\nThe following designs have been printed :")
    for designs in printed_designs:
        print(designs)
unprinted_designs = ['robot_chassis','robot_arms','robot_wheels','robot_legs']
printed_designs = []
designs_process(unprinted_designs[:])
designs_print(printed_designs)
print(f"\nOriginal List: {unprinted_designs}")"""

#67

"""#Passing an arbitrary number of arguments
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepproni')
make_pizza('mushrooms','green peppers','extra cheese')"""

#68

"""def make_pizza(*toppings):
    print("Making pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('extra cheese')
make_pizza('mushrooms','pepproni','green pepper','red pepper','extra cheese')"""

#69

"""#Always positional argument comes first then arbitrary argument
def make_pizza(size,*toppings):
    print(f"Making a {size}-inch pizza with the follwing toppings")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16 ,'pepproni','extra cheese')
make_pizza(12 ,'mushrooms','cheese burst', 'paneer')"""

#70 

"""#Passing arbitrary keyword arguments
def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    print(user_info)
build_profile('Mihir','Soni',location = 'Arunachal' ,field ='Engineering')"""

#71

"""def make_pizza(size,*toppings):
    print(f"Making a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")"""




















    


    
















    















