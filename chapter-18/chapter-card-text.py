#!/usr/bin/env python
# encoding: utf-8
"""
chapter-card-text.py

Created by Terry Bates on 2014-08-02.
Copyright (c) 2014 http://the-awesome-python-blog.posterous.com. All rights reserved.
"""

import sys
import os


class Card(object):
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', 
        '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    """Represents a standard playing card."""
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)

class Deck(object):
    # Alternative with nasty list comprehension
    # self.cards = [Card(suit,rank) for suit in range(4)
    #         for rank in range(1, 14)]
    self.cards = []
    for suit in range(4):
        for rank in range(1, 14):
            card = Card(suit, rank)
            self.cards.append(card)

    def __str__(self):
        # Or use a list comprehension
        # res = [str(card) for card in self.cards]
        res=[]
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)


def main():
	pass


if __name__ == '__main__':
	main()

