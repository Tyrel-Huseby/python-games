import random
#import pokerBot as AI

#declare lists
face = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King'
]

suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

deck = []
hand = []
cpu_hand = []
xface =[]
xsuit = []

#--------------------------------------------------------------------------------#
#declare dictonaries
card_num_dictionary = {
    'Ace': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13
}

pairings = {
    2: 'One Pair of Cards',
    3: 'a Three of a kind',
    4: 'a Four of a kind',
}

winning_hands = {
    'None': 0,
    'One Pair of Cards': 1,
    'Two Pairs of Cards': 2,
    'a Three of a kind': 3,
    'Straight': 4,
    'Flush': 5,
    'a Full house': 6,
    'a Four of a kind': 7,
    'Straight Flush': 8,
    'Royal Flush': 9
    }

#--------------------------------------------------------------------------------#
#define functions
def build_deck(xface, xsuits):
    
    global deck
    
    for i in range(len(xface)):
        for j in range(len(xsuits)):
            deck.append(f'{xface[i]} of {xsuits[j]}')

def deal_hand(xdeck):
    random.shuffle(xdeck)
    
    global hand
    global cpu_hand
    
    for i in range(10):
        if i % 2 == 1:
            hand.append(xdeck.pop())
        else:
            cpu_hand.append(xdeck.pop())
                    
    print(f'Your hand:\n {hand}')
    #print(f"Computer's hand:\n {cpu_hand}")
    return xdeck
    

def player_discard(xhand):
    global deck
    queue = []
    times = int(input('How many cards do you want to discard?: '))
    if times == 5:
        queue = [0, 1, 2, 3, 4]       
        for rem in queue:
            deck.insert(0, xhand.pop(rem))
            xhand.insert(rem, deck.pop())
        return xhand
    elif 1 <= times < 5:
        for t in range(times):
            discard = int(input('What card do you want to discard?: #'))-1
            queue.append(discard)    
        for rem in queue:
            deck.insert(0, xhand.pop(rem))
            xhand.insert(rem, deck.pop())
        return xhand        
    elif times == 0:        
        return xhand   
    else:
        print('Invalid Choice!')
        player_discard(xhand)
            
#begin processing for cases ---------------------------------------------------------------------------------------------------#

def hand_processing(xhand): #copy the hand and split the string in the list element
    global xface
    global xsuit
    global card_num_dictionary
    
    shand = [xhand[i].split() for i in range(5)] 
    for i in range(5):
        shand[i].remove('of')
        shand[i][0] = card_num_dictionary[shand[i][0]]
    xface = sorted([shand[i][0] for i in range(5)])
    xsuit = [shand[i][1] for i in range(5)]
    #print(xface)
    
def pairs(face):
    global pairings
    face_copy = face.copy()
    tally = []
    for i in range(5):
        tally.append(face.count(face_copy[0]))
        face_copy.pop(0)
        face_copy.append(0)   
    
    if max(tally) == 3 and 2 in tally:
        return 'a Full house' #got this once 3 7s and 2 11s
    
    elif tally.count(2) == 4:
        return 'Two Pairs of Cards' 
    
    elif max(tally) != (1 or 0):   
        return pairings[max(tally)]
    
    else:
        return False                
       
def straight(face):
    total = 0
    special_case = [1, 10, 11, 12, 13]
    for i in range(4):
        total += face[i] - face[(i + 1)]
    if total == -4:
        return True
    elif total == -12:
        if face == special_case:
            return True
        else:
            return False 
    
def flush(suits):
    if suits[0] == suits[1] and suits[1] == suits[2] and suits[2] == suits[3] and suits[3] == suits[4]:
        return True
    else:
        return False
    
def straight_flush(x, y):
    
    if x and y == True:
        return True
    else:
        return False
    
def royal_flush(boo, face):
    special_case = [1, 10, 11, 12, 13]
    if special_case == face and boo == True:
        return True
    else:
        return False    
    
def logic(output, boolean1, boolean2, boolean3, boolean4, num):
    if num == 1:
        if output != False:
            print('You have ' + output)
            return output
        elif boolean4 == True:   
            print('You have a Royal Flush!')
            return 'Royal Flush'
        elif boolean3 == True:
            print('You have a Straight Flush')
            return 'Straight Flush'
        elif boolean2 == True:
            print('You have a Flush')
            return 'Flush'
        elif boolean1 == True:    
            print('You have a Straight')
            return 'Straight'
        else:
            print('Nothing of interest was found')
            return 'None'
        
    else:
        if output != False:
            return output
        elif boolean4 == True: 
            return 'Royal Flush'
        elif boolean3 == True:
            return 'Straight Flush'
        elif boolean2 == True:
            return 'Flush'
        elif boolean1 == True: 
            return 'Straight'
        else:
            return 'None'
            

def poker_logic(xhand, num):
    global deck
    hand_processing(xhand)
    
    output = pairs(xface) 
    boolean1 = straight(xface) 
    boolean2 = flush(xsuit)
    boolean3 = straight_flush(boolean1, boolean2) 
    boolean4 = royal_flush(boolean2, xface)
    
    logic(output, boolean1, boolean2, boolean3, boolean4, num)          
    
    if num == 1:
        xhand = player_discard(xhand)
    else:
        AI.discard_logic(deck, xhand, xface, xsuit, output, boolean1, boolean2, boolean3, boolean4, num)    
    
    hand_processing(xhand)
    print('')
    print(xhand)
    print('')
    output = pairs(xface) 
    boolean1 = straight(xface) 
    boolean2 = flush(xsuit)
    boolean3 = straight_flush(boolean1, boolean2) 
    boolean4 = royal_flush(boolean2, xface) 
    
    logic(output, boolean1, boolean2, boolean3, boolean4, num) 
#--------------------------------------------------------------------------------#
def run():
    global face
    global suits
    global deck
    global hand
    global cpu_hand
        
    build_deck(face, suits)

    deck = deal_hand(deck)

    best_hand1 = poker_logic(hand, 1)
    #best_hand2 = poker_logic(cpu_hand, 2)
    #compare(best_hand1, best_hand2)
    redeal = str(input('Deal again? y/n: '))
    if redeal != 'n':
        deck = []
        hand = []
        cpu_hand = []
        run()           
            
run()            
