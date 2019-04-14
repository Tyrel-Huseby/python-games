import random

deck = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King'
] * 4

table = []
books = []

cpu_hand = []
player1_hand = []
player2_hand = []
player3_hand = []
player4_hand = []
player5_hand = []
player6_hand = []

players = [player1_hand]

cpu_choice_list = []

turn_counter = 0

player_dict = {
    1: cpu_hand,
    2: player2_hand,
    3: player3_hand,
    4: player4_hand,
    5: player5_hand,
    6: player6_hand
    }
   

def deal(xbooks , player_count):
    global players
    global deck
    random.shuffle(deck)
    
    if player_count == 1:
        counter = 7
        while counter > 0:
            for i in range(2):
                players[i].append(deck.pop())
                xbooks = [0 for i in range(2)]
            counter -= 1
       
        print('')
    elif player_count == (2 or 3):
        counter = 7
        while counter > 0:
            for i in range(player_count):
                players[i].append(deck.pop())
                xbooks = [0 for i in range(player_count)]
            counter -= 1
    elif player_count > 3:
        counter = 5
        while counter > 0:
            for i in range(player_count):
                players[i].append(deck.pop())
                xbooks = [0 for i in range(player_count)]
            counter -= 1        
    return xbooks

# AI functions -------------------------------------------------------------------#
def AI_reloop(hand_copy, used_list):
    global deck
    for used in used_list:
        while used in hand_copy:
            hand_copy.remove(used)
    
    if len(hand_copy) == 0 and len(deck) != 0:
        hand_copy.append(deck.pop())
        print(f"Computer draws a card\n")
        used_list.clear()
        AI_reloop(hand_copy, used_list)
    return AI_player(hand_copy)        
              

def AI_player(hand):#defines computer A.I; hand defined as players[1]
    global table
    global deck
    global books
    global cpu_choice_list
    global turn_counter
    
    choice = None
    
    if turn_counter % 3 == 0: 
        cpu_choice_list.clear()
    
    print('Computer has used: ', cpu_choice_list)
    print('')
    for i in range(1, len(hand)):
        book = 0
        for card in hand:
            if hand.count(card) == 4:
                book = 1
                rem = card 
        n = hand.count(hand[i-1])
        if book == 1 or n == 4:
            if rem == 'Six':
                print(f'The computer has a book of {rem}es')      
            else:
                print(f'The computer has a book of {rem}s')   
            
            for j in range(4):
                table.append(rem)
                hand.remove(rem)
            
            books[1] += 1
            
            if len(hand) == 0 and len(deck) != 0: #UnboundLocalError fix
                hand.append(deck.pop())
                print(f"Computer draws a card\n")
                cpu_choice_list.clear()
                choice = AI_player(hand)
                #end fix
            choice = AI_player(hand)
            break
        
        else:  
            if n == 3:
                choice = hand[hand.index(hand[i-1])]
                
                if choice in cpu_choice_list:
                    choice = AI_reloop(hand.copy(), cpu_choice_list)
                    break
                
                if choice == 'Six':
                    print(f'Do you have any {choice}es?')
                    cpu_choice_list.append(choice)
                    break                
                else:
                    print(f'Do you have any {choice}s?')
                    cpu_choice_list.append(choice)
                    break
                    
            elif n == 2:
                choice = hand[hand.index(hand[i-1])]
                if choice in cpu_choice_list:
                    choice = AI_reloop(hand.copy(), cpu_choice_list)
                    break

                if choice == 'Six':
                    print(f'Do you have any {choice}es?')
                    cpu_choice_list.append(choice)
                    break                
                else:
                    print(f'Do you have any {choice}s?')
                    cpu_choice_list.append(choice)
                    break
                    
            elif i == len(hand)-1:           
                choice = random.choice(hand)
                print('Random choice is', choice)
                if choice == 'Six':
                    print(f'Do you have any {choice}es?')
                    break
                               
                else:
                    print(f'Do you have any {choice}s?')
                    break    
            else:
                if len(hand) == 0 and len(deck) != 0: #UnboundLocalError fix
                    hand.append(deck.pop())
                    print(f"Computer draws a card\n")
                    cpu_choice_list.clear()
                    choice = AI_player(hand)
                    #end fix
                else:
                    continue
    
    return choice

# end AI functions -------------------------------------------------------------------#

def logic(card, turn):
    global players
    global deck
    if len(players) == 2 and cpu_hand in players:
        if turn == 0:
            if card in players[1]:
                for i in range(players[1].count(card)):
                    players[1].remove(card)
                    players[0].append(card)
            else:
                if len(deck) != 0:
                    print('Go Fish!\n')
                    players[0].append(deck.pop())
                else:
                    print('No more cards in deck\n')
        elif turn == 1:    
            if card in players[0]:
                for i in range(players[0].count(card)):
                    players[0].remove(card)
                    players[1].append(card)
            else:
                if len(deck) != 0:
                    print('Go Fish!\n')
                    players[1].append(deck.pop())
                else:
                    print('No more cards in deck\n')
    else:
        print('null')
       
    
def gameplay(xdeck, player_count):
    global books
    global table
    global players
    global turn_counter
    
    if player_count == 1:
        while len(table) != 52:
            turn_counter += 1
            print('Turn: ', turn_counter)
            print('Score: ', books)
            print('\n')
            for boo in range(2):
                if boo == 0:
                    for i in players[0]:
                        if players[0].count(i) == 4:
                            rem = i
                            for j in range(4):
                                table.append(rem)
                                players[0].remove(rem)
                            books[0] = books[0] + 1
                            if rem == 'Six':
                                print(f'Player 1 has a book of {rem}es')          
                            else:
                                print(f'Player 1 has a book of {rem}s')
                              
                    print('Player 1:\n', players[0])    
                    while True:
                        choice = input('What would you like to ask for?: ')
                        choice = choice.capitalize()
                        if choice in players[0]:
                            break
                        else:
                            print('You do not have that card')    
                    if choice == 'Six':
                        print(f'Do you have any {choice}es?')
                        logic(choice, boo)
                        continue
                            
                    else:
                        print(f'Do you have any {choice}s?')
                        logic(choice, boo)
                        continue
                                        
                else:# else following boo == 0 if statment
                    print('CPU\'s turn\n')
                    choice = AI_player(players[1])
                    logic(choice, boo)
            print('\n')
                       
    #else: #if players are 2 or more
def win(score, players):
    global players_dict
    idx = score.index(max(score))
    if cpu_hand in players:
        if idx == 0:
            print('The winner is The Player!')
        else:
            print('The Computer wins!')    
    else:
        print('Not ready') #future features
    
def run():
    global books
    global deck
    global table
    global players
    global player_dict
    
    
    player_selection = int(input('How many Players are there? (1 defaults to an A.I opponent; must be an integer): '))
        
    if 1 < player_selection <= 6:
        run()
        #for i in range(1, player_selection):
            #players.append(player_dict[i+1])
        #print(players)
        #deck = deal(deck, player_selection)
        #print('The table contains' ,table)
        #break
    elif player_selection == 1:
        players.append(player_dict[1])
        books = deal(books, player_selection)
        gameplay(deck, player_selection)
        win(books, players)
    else:
        print('That is not a valid selection!')
        run()
        
      
    
run()        
