#/usr/bin/python
# -*- coding: utf-8 -*-

import random

class Card(object):  
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        card_f = "{} of {}"
        rank = self.rank
        
        if rank == 'A':
            rank = 'Ace'
        elif rank == 'J':
            rank = 'Jack'
        elif rank == 'Q':
            rank = 'Queen'
        elif rank == 'K':
            rank = 'King'
            
        return card_f.format(rank, self.suit)

    def value(self, total):
        if self.rank in (2,3,4,5,6,7,8,9):
            value = self.rank
        elif self.rank in ('J','Q','K'):
            value = 10
        else:
            if total + 11 > 21:
                value = 1
            else:
                value = 11
        return value


def make_deck():
    deck = []
    suits = ['♠','♣','♦','♥']
    ranks = [2,3,4,5,6,7,8,9,'A','J','Q','K']
    
    for s in suits:
        for r in ranks:
            c = Card(s,r)
            deck.append(c)

    random.shuffle(deck)
    return deck


def main():
    deck = make_deck()
    p_score = 0 
    d_score = 0
    game_over = False
    
    print("~~~\nWelcome to Virtual Blackjack!\n~~~\n")
    
    draw_card = deck[0]
    print("You drew:", str(draw_card))
    
    p_score += draw_card.value(p_score)
    print('Your total:', str(p_score))
    del deck[0]
    choice = input('Do you want to draw another card? (y/n)\n')
    
    while choice == 'y':
        draw_card = deck[0]
        print("You drew:", str(draw_card))
    
        p_score += draw_card.value(p_score)
        print("Your total:", p_score)
        del deck[0]
        
        if p_score == 21:
            print("You win! Great job!")
            choice = 'n'
            game_over = True
        elif p_score > 21:
            print("You lose! Better luck next time.")
            choice = 'n'
            game_over = True
            
        if game_over == False:    
            choice = input('Do you want to draw another card? (y/n)\n')
            
    if game_over == False:
        print("\nOkay, it's my turn to play.")
        while d_score < 17:
            draw_card = deck[0]
            print("I drew:", str(draw_card))
            
            d_score += draw_card.value(d_score)
            print("My total:", d_score, '\n')
            del deck[0]
            
            if d_score == 21:
                print("I win! Better luck next time.")
                game_over = True
            elif d_score > 21:
                print("I lose!")
                game_over = True
                
        if game_over == False:
            print("My score is", d_score, "and your score is", p_score)
            decision = "That means that {}"
            
            if d_score == p_score:
                print(decision.format("the game is a push. Let's call it a tie."))
            elif d_score > p_score:
                print(decision.format("I win! Better luck next time."))
            else:
                print(decision.format("you win! Great job!"))

if __name__ == "__main__":
    main()
