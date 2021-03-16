rod_1 = [3, 2, 1]
rod_2 = []
rod_3 = []

complete_rod = [3, 2, 1]

rod_numbers = {'1': rod_1, '2': rod_2, '3': rod_3}

def move_disk(from_rod, to_rod):
    if not from_rod:
        print('There\'s no disks there. Choose another rod.')
    elif to_rod != [] and from_rod[-1] > to_rod[-1]:
        print('You cannot place a larger disk on top of a smaller one. Choose again.')
    else:
        to_rod.append(from_rod.pop())


while True:
    print('So far, your rods are:')
    print('1: ', rod_1)
    print('2: ', rod_2)
    print('3: ', rod_3)
    source = input('Choose a rod from which the disk will be taken: ')
    destination = input('Choose a rod to which the disk will be added: ')

    move_disk(rod_numbers.get(source), rod_numbers.get(destination))

    if rod_3 == complete_rod:
        print("Congratulations! You built your tower.")
        break
    else:
        continue
