import random

rules = { #Key beats value
    'Rock': ('Lizard', 'Scissors'),#correct
    'Paper': ('Rock', 'Spock'), #correct
    'Scissors': ('Paper', 'Lizard'), #correct
    'Lizard': ('Spock', 'Paper'), #correct
    'Spock': ('Rock', 'Scissors') #correct
}   

phrases = {
    'Rock': ('Rock crushes Lizard', 'Rock crushes Scissors'),
    'Paper': ('Paper covers Rock', 'Paper disproves Spock'),
    'Scissors': ('Scissors cut Paper', 'Scissors decapitates Lizard'),
    'Lizard': ('Lizard poisons Spock', 'Lizard eats Paper'),
    'Spock': ('Spock vaporizes Rock', 'Spock Smashes Scissors' )
}

cpu = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

def run():
    global rules
    global phrases
    global cpu
    choice = str(input('Choose from Rock, Paper, Scissors, Lizard, Spock: '))
    choice = choice.capitalize()
    cpu_choice = random.choice(cpu)
    print(f'Computer chose {cpu_choice}')
    player = rules[choice]
    computer = rules[cpu_choice] 
    for i in range(2):
        if player[i] == cpu_choice:
            print('You win')
            print(phrases[choice][i])
            break
        elif computer[i] == choice:
            print('The Computer wins')
            print(phrases[cpu_choice][i])
            break
        elif choice == cpu_choice:
            print("It's a tie!")
            break
        else:
            continue
run()            
