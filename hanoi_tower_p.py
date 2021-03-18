from os import system, name

rod_1 = []
rod_2 = []
rod_3 = []

first_starting_message = """
╔══════════════════════════════════════════════════════════════════════════╗
║                 ╔═════════════════════════════════════╗                  ║
║                 ║                                     ║                  ║
║                 ║  █   █   ███   █   █  █████  █████  ║                  ║
║                 ║  █   █  █   █  ██  █  █   █    █    ║                  ║
║                 ║  █████  █████  █ █ █  █   █    █    ║                  ║
║                 ║  █   █  █   █  █  ██  █   █    █    ║                  ║
║                 ║  █   █  █   █  █   █  █████  █████  ║                  ║
║                 ╠═════════════════════════════════════╣                  ║
║                 ║       |          |          |       ║                  ║
║                 ║      ▓|▓         |          |       ║                  ║
║                 ║     ▓▓|▓▓        |          |       ║                  ║
║                 ║    ▓▓▓|▓▓▓       |          |       ║                  ║
║                 ║   ▓▓▓▓|▓▓▓▓      |          |       ║                  ║
║                 ║‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾║                  ║
║                 ╚═════════════════════════════════════╝                  ║
╚══════════════════════════════════════════════════════════════════════════╝
"""
starting_message = {'en': """
╔══════════════════════════════════════════════════════════════════════════╗
║                 ╔═════════════════════════════════════╗                  ║
║                 ║                                     ║                  ║
║                 ║  █   █   ███   █   █  █████  █████  ║                  ║
║                 ║  █   █  █   █  ██  █  █   █    █    ║                  ║
║                 ║  █████  █████  █ █ █  █   █    █    ║                  ║
║                 ║  █   █  █   █  █  ██  █   █    █    ║                  ║
║                 ║  █   █  █   █  █   █  █████  █████  ║                  ║
║                 ╠═════════════════════════════════════╣                  ║
║                 ║       |          |          |       ║                  ║
║                 ║      ▓|▓         |          |       ║                  ║
║                 ║     ▓▓|▓▓        |          |       ║                  ║
║                 ║    ▓▓▓|▓▓▓       |          |       ║                  ║
║                 ║   ▓▓▓▓|▓▓▓▓      |          |       ║                  ║
║                 ║‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾║                  ║
║                 ╚═════════════════════════════════════╝                  ║
║                                                                          ║
║                          Hello, future builder.                          ║
║     In this game you will be able to solve the Hanoi Tower Challenge.    ║
║     Your objective is to move all disks from one rod to another.         ║
║                       The rules are pretty simple:                       ║
║       - Only one disk can be moved at each time                          ║
║       - Only the the top disk can be moved                               ║
║       - Only smaller disks can rest on the top of the bigger ones        ║
║     See? That's everything you need to start building your own tower!    ║
║                               Good luck!                                 ║
╚══════════════════════════════════════════════════════════════════════════╝
        """,
        'pt': """
╔══════════════════════════════════════════════════════════════════════════╗
║                 ╔═════════════════════════════════════╗                  ║
║                 ║                                     ║                  ║
║                 ║  █   █   ███   █   █  █████  █████  ║                  ║
║                 ║  █   █  █   █  ██  █  █   █    █    ║                  ║
║                 ║  █████  █████  █ █ █  █   █    █    ║                  ║
║                 ║  █   █  █   █  █  ██  █   █    █    ║                  ║
║                 ║  █   █  █   █  █   █  █████  █████  ║                  ║
║                 ╠═════════════════════════════════════╣                  ║
║                 ║       |          |          |       ║                  ║
║                 ║      ▓|▓         |          |       ║                  ║
║                 ║     ▓▓|▓▓        |          |       ║                  ║
║                 ║    ▓▓▓|▓▓▓       |          |       ║                  ║
║                 ║   ▓▓▓▓|▓▓▓▓      |          |       ║                  ║
║                 ║‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾║                  ║
║                 ╚═════════════════════════════════════╝                  ║
║                                                                          ║
║                          Olá, futuro construtor.                         ║
║    Nesse jogo você será capaz de resolver o Desafio da Torre de Hanoi.   ║
║    Seu objetivo é mover todos os discos de uma estrutura para a outra.   ║
║                        As regras são bem simples:                        ║
║       - Apenas um disco pode ser movido por vez;                         ║
║       - Apenas o disco no topo pode ser movido;                          ║
║       - Apenas discos menores podem ser colocados sobre discos maiores.  ║
║    Viu? Isso é tudo que precisa saber para construir a sua torre!        ║
║                                 Boa sorte!                               ║
╚══════════════════════════════════════════════════════════════════════════╝
        """}
hanoi_logo = """
╔══════════════════════════════════════════════════════════════════════════╗
║                 ╔═════════════════════════════════════╗                  ║
║                 ║                                     ║                  ║
║                 ║  █   █   ███   █   █  █████  █████  ║                  ║
║                 ║  █   █  █   █  ██  █  █   █    █    ║                  ║
║                 ║  █████  █████  █ █ █  █   █    █    ║                  ║
║                 ║  █   █  █   █  █  ██  █   █    █    ║                  ║
║                 ║  █   █  █   █  █   █  █████  █████  ║                  ║
║                 ╚═════════════════════════════════════╝                  ║
╚══════════════════════════════════════════════════════════════════════════╝
"""
starting_input = {'en': 'How many disks will your tower have? Choose between 2 and 9: ',
                  'pt': 'Quantos discos sua torre terá? Escolha entre 2 e 9: '}
checkup_message = {'en': 'So far, your building site is:',
                   'pt': 'Até agora, essa é a sua área de construção:'}
value_error = {'en': 'But that\'s not math! Try again using numbers this time!',
               'pt': 'Mas isso não é matemática! Tente de novo usando números dessa vez.'}
size_too_small = {'en': 'Too small, have you tried to play Hanoi House instead? Try again.',
                  'pt': 'Pequena demais, já tentou jogar Casa Hanoi em vez disso? Tente de novo'}
too_many_moves = {'en': """
That number is just too big. 
Our calculators said that they\'re done with math and are gonna study philosophy now, 
so you better start calculating your own numbers.""",
                  'pt': """
Esse número é grande demais. 
Nossas calculadoras disseram que desistiram da matemática e vão estudar filosofia agora,
então é melhor começar a fazer as suas próprias contas."""}
size_too_big = {'en': 'But that would take {n} movements to solve! Try again, don\'t be so greedy.',
                'pt': 'Mas isso levaria {n} movimentos para resolver! Tente de novo, não seja tão gananciose.'}
size_really_too_big = {'en': 'But that would take {:.2e} movements to solve! Try again, don\'t be so greedy.',
                       'pt': 'Mas isso levaria {:.2e} movimentos para resolver! Tente de novo, não seja tão gananciose.'}
source_input = {'en': 'Choose a rod (1, 2 or 3) from which the disk will be taken: ',
                'pt': 'Escolha uma estrutura (1, 2 ou 3) para retirar o disco: '}
destination_input = {'en': 'Choose a rod (1, 2 or 3) to which the disk will be added: ',
                     'pt': 'Escolha uma estrutura (1, 2 ou 3) para adicionar o disco: '}
input_not_in_dict = {'en': 'Are you sure this tower is located here, friend? '
                           'Choose one of the rods that you see.',
                     'pt': 'Você tem certeza de que essa estrutura existe aqui, companheire? '
                           'Escolha uma das estruturas que você pode ver.'}
empty_rod = {'en': 'Are you seeing any disks there? Choose another rod.',
             'pt': 'Você está vendo algum disco nessa estrutura? Escolha outra.'}
what_goes_where = {'en': 'You cannot place a larger disk on top of a smaller one. Choose again.',
                   'pt': 'Você não pode colocar um disco maior em cima de um menor. Escolha de novo.'}
victory_message = {'en': 'Congratulations! You built your tower.',
                   'pt': 'Parabéns! Você construiu a sua torre.'}


def cls():
    system('cls' if name == 'nt' else 'clear')
    return

cls()
print(first_starting_message)

while True:
    print("""Please choose a language/Escolha a lingua:
            1. English
            2. Português""")
    try:
        lang = int(input('Select a number/Selecione um número: '))
    except ValueError:
        cls()
        print(first_starting_message)
        print('Answer with 1 or 2. Try again.\nAs respostas só podem ser 1 ou 2. Tente de novo.')
        continue

    if lang == 1:
        lang = 'en'
        cls()
        break
    elif lang == 2:
        lang = 'pt'
        cls()
        break
    else:
        cls()
        print(first_starting_message)
        print('Answer with 1 or 2. Try again.\nAs respostas só podem ser 1 ou 2. Tente de novo.')
        continue


print(starting_message[lang])

while True:  # loop to generate the starting tower size accordingly to the user input
    try:
        starting_size = int(input(starting_input[lang]))
    except ValueError:  # makes sure the input is a number
        cls()
        print(starting_message[lang])
        print(value_error[lang])
        continue

    if 2 > starting_size:
        cls()
        print(starting_message[lang])
        print(size_too_small[lang])
        continue
    elif starting_size > 100:
        cls()
        print(starting_message[lang])
        print(too_many_moves[lang])
        continue
    elif starting_size > 9:
        cls()
        print(starting_message[lang])
        min_number = 2 ** starting_size - 1
        if min_number > 1_000_000:
            print(size_really_too_big[lang].format(min_number))
            continue
        else:
            print(size_too_big[lang].format(n=min_number))
            continue
    else:  # if the input has satisfied all the conditions to be a valid tower size
        break

rod_1 = list(reversed(range(1, starting_size + 1)))  # generate the amount of disks in the starting tower
complete_rod = list(reversed(range(1, starting_size + 1)))  # generate the solution acc to chosen disks amount

rod_numbers = {'1': rod_1, '2': rod_2, '3': rod_3}  # associate rod numbers with their contents


def tower_art():
    spaces_header = ' ' * (1 + starting_size)
    under_dash = '‾' * ((6 * starting_size) + 17)

    visual_rod_1 = rod_1[:]
    visual_rod_2 = rod_2[:]
    visual_rod_3 = rod_3[:]

    while len(visual_rod_1) < len(complete_rod):
        visual_rod_1.append(0)
    while len(visual_rod_2) < len(complete_rod):
        visual_rod_2.append(0)
    while len(visual_rod_3) < len(complete_rod):
        visual_rod_3.append(0)

    print(spaces_header, '|', spaces_header,  # first row of the rods where there are no disks
          spaces_header, '|', spaces_header,
          spaces_header, '|', spaces_header)

    for i in complete_rod:
        spaces_rod_1 = ' ' * (1 + starting_size - visual_rod_1[i - 1])
        blocks_rod_1 = '▓' * visual_rod_1[i - 1]
        spaces_rod_2 = ' ' * (1 + starting_size - visual_rod_2[i - 1])
        blocks_rod_2 = '▓' * visual_rod_2[i - 1]
        spaces_rod_3 = ' ' * (1 + starting_size - visual_rod_3[i - 1])
        blocks_rod_3 = '▓' * visual_rod_3[i - 1]

        print(spaces_rod_1, blocks_rod_1 + '|' + blocks_rod_1, spaces_rod_1,
              spaces_rod_2, blocks_rod_2 + '|' + blocks_rod_2, spaces_rod_2,
              spaces_rod_3, blocks_rod_3 + '|' + blocks_rod_3, spaces_rod_3)

    print(under_dash) # line underneath the rods


while True:
    cls()
    print(hanoi_logo)
    print(checkup_message[lang])
    tower_art()

    while True:
        source = input(source_input[lang])  # receives a single number as input
        destination = input(destination_input[lang])  # either 1, 2 or 3
        from_rod = rod_numbers.get(source)
        to_rod = rod_numbers.get(destination)
        if source not in rod_numbers or destination not in rod_numbers:
            cls()
            print(hanoi_logo)
            print(checkup_message[lang])
            tower_art()
            print(input_not_in_dict[lang])
        elif not from_rod:  # checks if the rod is empty
            cls()
            print(hanoi_logo)
            print(checkup_message[lang])
            tower_art()
            print(empty_rod[lang])
            continue
        elif to_rod != [] and from_rod[-1] > to_rod[-1]:  # checks if the disks respect the size rule
            cls()
            print(hanoi_logo)
            print(checkup_message[lang])
            tower_art()
            print(what_goes_where[lang])
            continue
        else:
            cls()
            to_rod.append(from_rod.pop())  # takes off the disk from one rod and add to another
            break

    if rod_3 == complete_rod:  # checks if the game is won and breaks the loop
        print(hanoi_logo)
        print(victory_message[lang])
        tower_art()
        break
    else:
        continue
