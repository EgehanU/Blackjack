from random import randint

class Card:
    suit = None
    value = None
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def returnValue(self):
        return self.value
    def returnSuit(self):
        return self.suit
    def __repr__(self):
        return self.returnSuit()

class Deck:
    cards = []
    l = []
    
    def shuffle(self):
        for i in range(1, 14):
            self.cards.append(Card(i, "Club"))
        for i in range(1, 14):
            self.cards.append(Card(i, "Diamond"))
        for i in range(1, 14):
            self.cards.append(Card(i, "Heart"))
        for i in range(1, 14):
            self.cards.append(Card(i, "Spade"))
    
    def returnLength(self):
        return len(self.cards)

    def deduct(self, randomNumber):
        self.randomNumber = randomNumber
        self.cards.pop(self.randomNumber)

    def showCards(self):
        for i in self.cards:
            self.l.append(i.suit)
        return self.l

class Player:
    def __init__(self, amountOfMoney):
        self.amountOfMoney = amountOfMoney
    # If the game is lost, then changedAmountOfMoney will be negative
    def updateMoney(self, changedAmountOfMoney):
        self.amountOfMoney = changedAmountOfMoney



class Blackjack:

    deck = Deck()
    deck.shuffle()
    numberOfOrders = 51
    def __init__(self):
        pass

    def randomGenerator(self):
        r = randint(0, self.numberOfOrders)
        self.numberOfOrders -= 1
        self.deck.deduct(r)
        return r

    def cardPrinter(self, cardsEntered):
        self.cardsEntered = cardsEntered
        printedCards = []
        
        for i in range(len(cardsEntered)):
            if self.cardsEntered[i] / 13 > 1:
                self.cardsEntered[i] = 1 + (self.cardsEntered[i] % 13)
   
            if self.cardsEntered[i] == 10:
                printedCards.append("J")
            elif self.cardsEntered[i] == 11:
                printedCards.append("Q")
            elif self.cardsEntered[i] == 12:
                printedCards.append("K")
            elif self.cardsEntered[i] == 13:
                printedCards.append("A")
            else:
                if self.cardsEntered[i] == 0:
                    self.cardsEntered[i] = 1
                printedCards.append(self.cardsEntered[i])
        return printedCards

    def valueAssigner(self, cardsEntered):
        self.cardsEntered = cardsEntered
        value = 0
        for i in range(len(self.cardsEntered)):
            if self.cardsEntered[i] / 13 > 1:
                self.cardsEntered[i] = 1 + (self.cardsEntered[i] % 13)
            if self.cardsEntered[i] == 10:
                value += 10
            elif self.cardsEntered[i] == 11:
                value += 10
            elif self.cardsEntered[i] == 12:
                value += 10
            elif self.cardsEntered[i] == 13:
                value += 10
            else:
                value += self.cardsEntered[i]
        if value == 20:
            value = 21 # blackjack
        return value

def main():
    game = Blackjack()
    orderCardsOfPlayer = []
    orderCardsOfDealer = []
    orderCardsOfPlayer.append(game.randomGenerator())
    orderCardsOfPlayer.append(game.randomGenerator())
    orderCardsOfDealer.append(game.randomGenerator())
    orderCardsOfDealer.append(game.randomGenerator())
    totalAmount = input ("\nPlease enter total amount of money you will be playing with")

    def value(orderCards):
        return game.valueAssigner(orderCards)

    gameCont = True

    while(gameCont):
        #turnAmount = input("\nEnter the amount of money you will be betting in this turn")
        cardsOfPlayer = game.cardPrinter(orderCardsOfPlayer)
        cardsOfDealer = game.cardPrinter(orderCardsOfDealer)
        print("\nCards of dealer: {} and {}".format(cardsOfDealer[0], cardsOfDealer[1]))
        print("Your cards: {} and {}".format(cardsOfPlayer[0], cardsOfPlayer[1]))
        possibleResults = ["win", "loss", "tie"]# to see the result of the turn
        result = None
        hitOrStand = input("Hit or stand (h for hit and s for stand)\n")

        if(hitOrStand.lower() == 'h' or hitOrStand.lower() == "hit"):
            orderCardsOfPlayer.append(game.randomGenerator())
            cardsOfPlayer = game.cardPrinter(orderCardsOfPlayer)
            print("\nYour cards are: ")
            for i in cardsOfPlayer: 
                print(i, " ")
        else:
            if value(orderCardsOfPlayer) > 21:
                result = possibleResults[1]
            elif value(orderCardsOfPlayer) == 21 and value(orderCardsOfDealer) != 21:
                result = possibleResults[0]
            elif value(orderCardsOfPlayer) == 21 and value(orderCardsOfDealer) == 21:
                result = possibleResults[2]
            elif value(orderCardsOfPlayer) > value(orderCardsOfDealer):
                result = possibleResults[0]
            elif value(orderCardsOfPlayer) == value(orderCardsOfDealer):
                result == possibleResults[2]
        checker = True
        if(hitOrStand.lower() == 's' or hitOrStand.lower() == "stand") and (result == possibleResults[0] or (result == possibleResults[2] and value(orderCardsOfDealer) <= 16)):
            while((result == possibleResults[0] or result == possibleResults[2]) and checker == True):
                orderCardsOfDealer.append(game.randomGenerator())
                orderCardsOfDealer = game.cardPrinter(orderCardsOfDealer)
                print("\nThe cards of dealer are: ")
                for i in cardsOfDealer: 
                    print(i, " ")

                if value(orderCardsOfDealer) > 21:
                    result = possibleResults[0]
                    checker = False
                elif value(orderCardsOfDealer) > value(orderCardsOfPlayer):
                    result = possibleResults[0]
                    checker = False
        print(result)

if __name__ == '__main__':
    main()








 


