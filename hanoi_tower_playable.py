rod_1 = []
rod_2 = []
rod_3 = []

print("""
Hello, future builder. 
In this game you will be able to solve the Hanoi Tower Challenge. 
Your objective is to move all disks from the first rod to the third one.
The rules are pretty simple:
- Only one disk can be moved at each time
- Only the the top disk can be moved
- Only smaller disks can rest on the top of the bigger ones
See? That's everything you need to start building your own tower!
Good luck!

""")

while True:  # loop to generate the starting tower size accordingly to the user input
    try:
        starting_size = int(input('How many disks will your tower have? Choose between 2 and 11: '))
    except ValueError:  # makes sure the input is a number
        print('But that\'s not a tower! Try again, using numbers this time.')
        continue

    if 2 > starting_size:
        print('Too small, have you tried to play Hanoi House instead? Try again.')
        continue
    elif starting_size > 11:
        print('They don\'t make towers that big! Try again.')
        continue
    else:  # if the input has satisfied all the conditions to be a valid tower size
        break

rod_1 = list(reversed(range(1, starting_size + 1)))  # generate the amount of disks in the starting tower
complete_rod = list(reversed(range(1, starting_size + 1)))  # generate the solution acc to chosen disks amount

rod_numbers = {'1': rod_1, '2': rod_2, '3': rod_3}  # associate rod numbers with their contents


def move_disk(from_rod, to_rod):
    if not from_rod:  # checks if the rod is empty
        print('There\'s no disks there. Choose another rod.')
    elif to_rod != [] and from_rod[-1] > to_rod[-1]:  # checks if the disks respect the size rule
        print('You cannot place a larger disk on top of a smaller one. Choose again.')
    else:
        to_rod.append(from_rod.pop())  # takes off the disk from one rod and add to another


while True:
    print('So far, your building site is:')
    print('1: ', rod_1)
    print('2: ', rod_2)
    print('3: ', rod_3)
    source = input('Choose a rod from which the disk will be taken: ')  # receives a single number as input
    destination = input('Choose a rod to which the disk will be added: ')  # either 1, 2 or 3

    move_disk(rod_numbers.get(source), rod_numbers.get(destination))  # function call

    if rod_3 == complete_rod:  # checks if the game is won and breaks the loop
        print("Congratulations! You built your tower.")
        break
    else:
        continue
