# 1. Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# a. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
print(x)
print(x[1][0])
x[1][0] = 15 
print(x)
print(x[1][0])
# b. Change the last_name of the first student from 'Jordan' to 'Bryant'
print(students)
print(students[0]['last_name'])
students[0]['last_name'] = "Bryant"
print(students)
print(students[0]['last_name'])
# c. In the sports_directory, change 'Messi' to 'Andres'
print(sports_directory)
print(sports_directory['soccer'][0])
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
print(sports_directory['soccer'][0])
# d. Change the value 20 in z to 30
print(z)
print(z[0]['y'])
z[0]['y'] = 30
print(z)
print(z[0]['y'])

# 2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the associated value. 
# For example, given the following list:

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterate_dictionary(list):
    for i in range(0, len(list)):
        output = ""
        for key,val in list[i].items():
            output += f" {key} - {val},"
        print(output)


iterate_dictionary(students)

# 3. Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary.

def iterate_dictionary2(key_name, some_list):
    for i in range(0, len(some_list)):
        for key,val in some_list[i].items():
            if key == key_name:
                print(val)

iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)


# 4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, and then prints the associated values within each key's list.   

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print(dojo)

def print_info(dict):
    for key in dict:
        val = dict[key]
        print("--------------------")
        print(f"{len(val)} {key.upper()}")
        for name in val:
            print(name)

print_info(dojo)

# alternative solution

# def print_info(dict):
#     for key,val in dict.items():
#         print("--------------")
#         print(f"{len(val)} {key.upper()}")
#         for i in range(0, len(val)):
#             print(val[i])