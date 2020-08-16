
# this is a comment-  it can be used to document and explain code
# each line of a comment starts with a '#' and doesn't execute at runtime

print('\nthis is a print statement:\nit shows up in the console\n')
# '/n' is a newline character

# python is super smart so you don't need to specify data types-
# it will automatically detect it on its own
name = 'Kevin' # strings are in single or double quotes
is_awesome = True # boolean is True or False
age = 22

# if/else using boolean
if(is_awesome):
    print('u r awesome sauce')
else:
    print('u r a loser')

print('\n')

# if / elif / else using number ranges
if(age < 18):
    print('haha u cant vote')
elif(age < 21):
    print('welcome to the disillusionment of democracy too bad u cant drink ur feelings')
elif(age == 21):
    print('twenty FUN')
elif(age == 22):
    print('i dont know about u but im feeling 22')
else:
    print('every birthday is another year closer to death')

print('\n')

# this is a list
friends = ['heidi', 'blake', 'jo ann', 'justin', 'ashtin', 'dylan']

# you can loop through a list
for friend in friends:
    print(friend + " is pretty alright")
print('\n')

# or you can use 'range' to specify how many times you want to loop
for i in range(10):
    print(i)
