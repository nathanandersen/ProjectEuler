#Problem 54
from itertools import combinations

global rounds_won_p1
rounds_won_p1 = 0
suits = ['C','S','D','H']
values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
poker = ['HC','1P','2P','3K','S','F','FH','4K','SF','RF']

class Round(object):
    p1 = object
    p2 = object
    def __init__(self):
        self.p1 = Hand()
        self.p2 = Hand()
    def p(self):
        string = "P1: "
        for card in self.p1.cards:
            string += card.p() + " "
        string += "\n"
        string += "P2: "
        for card in self.p2.cards:
            string += card.p() + " "
        return string

class Hand(object):
    cards = []
    poker_score = ""
    high_card = ""
    high_card2 = ""
    def __init__(self):
        self.cards = []
    def score(self):
        if royal_flush(self.cards):
            self.poker_score = 'RF'
            self.high_card = 'A'
            return self
        if straight_flush(self.cards):
            self.poker_score = 'SF'
            self.high_card = high_card(self.cards)
            return self
        if full_house(self.cards):
            self.poker_score = 'FH'
            self.high_card = full_house(self.cards)[0]
            self.high_card2 = full_house(self.cards)[1]
            return self
        if flush(self.cards):
            self.poker_score = 'F'
            self.high_card = high_card(self.cards)
            return self
        if straight(self.cards):
            self.poker_score = 'S'
            self.high_card = high_card(self.cards)
            return self
        if three_of_a_kind(self.cards):
            self.poker_score = '3K'
            self.high_card = three_of_a_kind(self.cards)
            return self
        if two_pairs(self.cards):
            self.poker_score = '2P'
            self.high_card = two_pairs(self.cards)[0]
            self.high_card2 = two_pairs(self.cards)[1]
            return self
        if one_pair(self.cards):
            self.poker_score = '1P'
            self.high_card = one_pair(self.cards)
            self.high_card2 = high_card(self.cards)[0]
            return self
        else:
            self.poker_score = 'HC'
            self.high_card = high_card(self.cards)[0]
            self.high_card2 = high_card(self.cards)[1]
            return self

class Card(object):
    suit = ""
    value = ""
    def __init__(self):
        suit = ""
        value = ""
    def p(self):
        return(self.suit + self.value)

# these methods all return the highest card in the
# set, if it exists.
# they must be called in this order.
def royal_flush(cards):
    suit = cards[0].suit
    for card in cards:
        if (not card.suit == suit) or values.index(card.value) < 8:
            return 0
    return 1
def straight_flush(cards):
    suit = cards[0].suit
    return (flush(cards) and straight(cards))
def four_of_a_kind(cards):
    for quad in combinations(cards,4):
        card_values = {values.index(card.value) for card in quad}
        if len(card_values) == 1:
            return(values[max(card_values)])
    return None
def full_house(cards):
    card_values = {values.index(card.value) for card in cards}
    if not len(card_values) == 2:
        return 0
    return(values[max(card_values)],values[min(card_values)])
def flush(cards):
    suit_set = {suits.index(card.suit) for card in cards}
    return high_card(cards) if len(suit_set) == 1 else None
def straight(cards):
    card_values = {values.index(card.value) for card in cards}
    min_index = min(card_values)
    if not len(card_values) == 5:
        return 0
    return sum(card_values) == (5*min_index + 10)
def three_of_a_kind(cards):
    for triple in combinations(cards,3):
        if (triple[0].value == triple[1].value and
            triple[1].value == triple[2].value):
            return triple[0].value
    return None
def two_pairs(cards):
    for quad in combinations(cards,4):
        card_values = {values.index(card.value) for card in quad}
        if len(card_values) == 2:
            return(values[max(card_values)],values[min(card_values)])
    return None
def one_pair(cards):
    for pair in combinations(cards,2):
        if (pair[0].value == pair[1].value):
            return pair[0].value
    return None
def high_card(cards):
    max_card = cards[0]
    for card in cards:
        if values.index(card.value) > values.index(max_card.value):
            max_card = card
    second_max_value = '2'
    for card in cards:
        if (values.index(card.value) > values.index(second_max_value) and
            card is not max_card):
            second_max_card = card
    return (max_card.value,second_max_card.value)

def score_round_p1(round):
    round.p1 = round.p1.score()
    round.p2 = round.p2.score()
    p1_score = round.p1.score().poker_score
    p2_score = round.p2.score().poker_score
    print(round.p())
    print(p1_score,p2_score)
    if poker.index(p1_score) > poker.index(p2_score):
        return 1
    elif poker.index(p1_score) == poker.index(p2_score):
        return (values.index(round.p1.high_card) >
                values.index(round.p2.high_card))
    return 0


def parse_round(round):
    cur_round = Round()
    for i in range(5):
        card = Card()
        card.value = round[3*i]
        card.suit = round[3*i+1]
        cur_round.p1.cards.append(card)
    for i in range(5,10):
        card = Card()
        card.value = round[3*i]
        card.suit = round[3*i+1]
        cur_round.p2.cards.append(card)
    return cur_round


with open("p054_poker.txt","r") as f:
    for round in f:
        rounds_won_p1 += score_round_p1(parse_round(round))

print(rounds_won_p1)
