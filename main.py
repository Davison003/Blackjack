############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random;

user_cards = [];
dealer_cards = [];
still_play = True;


def hit():
    user_cards.append(random.choice(cards));


def inicial_hand():
    for i in range(2):
        user_cards.append(random.choice(cards));
        dealer_cards.append(random.choice(cards));

def clear_hand():
    user_cards.clear();
    dealer_cards.clear();

def stand(): #makes dealer hit until 17
    while sum(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards));
        check_ace();


    user_lose();


def check_ace(): #if ace in hand with > 21, ace becomes 1
    if 11 in user_cards and sum(user_cards) > 21: 
        user_cards.remove(11);
        user_cards.append(1);

    if 11 in dealer_cards and sum(dealer_cards) > 21:
        dealer_cards.remove(11);
        dealer_cards.append(1);

def lose_msg():
        print(f"\nYour Final Hand: {user_cards}, final score: {sum(user_cards)}");
        print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}");
        print("You Lose! ;-;");

def win_msg():
        print(f"\nYour Final Hand: {user_cards}, final score: {sum(user_cards)}");
        print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}");
        print("You Win! :D");

def auto_lose_win():

    if sum(user_cards) == 21 and sum(dealer_cards) == 21:
        print(f"Your Final Hand: {user_cards}, final score: {sum(user_cards)}");
        print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}");
        print("You Draw! :/");
        return False;
        
    elif sum(dealer_cards) == 21:
        lose_msg();
        return False;

    elif sum(user_cards) == 21:
        win_msg();
        return False;
    else: 
        return True;


def user_win():
    
    if sum(dealer_cards) > 21 or (sum(user_cards) > sum(dealer_cards) and sum(user_cards) <= 21): 
        win_msg()
    else:
        user_draw();

def user_lose(): 
    if sum(user_cards) > 21: #se user estourar
        lose_msg()

    elif (sum(dealer_cards) > sum(user_cards) and sum(dealer_cards) <= 21):
        lose_msg()
    else:
        user_win()

def user_draw():
    if sum(user_cards) == sum(dealer_cards): #draw
        print(f"Your Final Hand: {user_cards}, final score: {sum(user_cards)}");
        print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}");
        print("You Draw! :/");

def check_state(): #checks state of the game, also checks if ace in > 21 hand
        
    check_ace();

    if sum(user_cards) == 21:
        user_win();
        return True;
    
    if sum(user_cards) > 21:
        user_lose();
        return True;
    else:
        print(f"Your Cards: {user_cards}, current score: {sum(user_cards)}");
        print(f"Computer's first card: {dealer_cards[0]}");


def continue_play():
    op = input("Type 'y' to get another card, type 'n' to pass: ").lower();

    if op == 'y':
        hit();
        gameOver = check_state(); 
        if not gameOver:
            still_play = continue_play();
    else:
        return stand();
        #check_state();
        #return False;


def blackjack():
    option = input("\nWanna play BlackJack? Y/N: ").lower();
    if option =='y':
        print("\033[H\033[J");
        inicial_hand()
        still_play = auto_lose_win();
        if still_play:
            check_state()
        
        while still_play:
            still_play = continue_play();
    elif option == 'n':
        return;
        
    clear_hand();
    blackjack();


blackjack();
