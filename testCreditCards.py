# Tests Credit Cards

import random
from random import randint
import copy


def cardType():
  cardTypeList = ["AMEX", "DISCOVER", "MASTERCARD", "VISA"]
  return random.choice(cardTypeList)


def cardNumber():
  cardNum = ""
  for _i in range(16):
    cardNum = cardNum + str(randint(0, 9))
  return cardNum


class Money:

  def __init__(self, dollars: int, cents: int):
    self.dollars = dollars
    self.cents = cents
    self.total = float(str(self.dollars) + "." + str(self.cents))

  def getDollars(self):
    return self.dollars
  
  def getCents(self):
    return self.cents
  
  def getAmount(self):
    return self.total



class CreditCard:

  def __init__(self, card_number, card_type, balance_dollars, balance_cents):
    self.card_number = card_number
    self.card_type = card_type
    self.balance = Money(balance_dollars, balance_cents)
    self.balanceDollars = self.balance.dollars
    self.balanceCents = self.balance.cents
    self.balanceTotal = self.balance.total
  
  def getCardNumber(self):
    return self.card_number
  
  def getCardType(self):
    return str(self.card_type)
  
  def getBalance(self):
    return self.balanceTotal
  
  def payBalance(self, amount):
    self.payAmount = amount
    self.balanceTotal -= self.payAmount
    
  
  def chargeBalance(self, amount):
    self.chargeAmount = amount
    self.balanceTotal += self.chargeAmount



def testCreditCard():

  cc1 = CreditCard("0000000000000000", "AMEX", 0, 0)
  cc2 = CreditCard(cardNumber(), cardType(), 110, 45)
  cc3 = CreditCard(cardNumber(), cardType(), 1678, 16)
  cc4 = CreditCard(cardNumber(), cardType(), 45, 45)

  def printCards():
    
    cc = []
    c1 = copy.deepcopy(cc1)
    c2 = copy.deepcopy(cc2)
    c3 = copy.deepcopy(cc3)
    c4 = copy.deepcopy(cc4)
    cc.append(c1)
    cc.append(c2)
    cc.append(c3)
    cc.append(c4)

    for i in range(len(cc)):
      print(f"Credit Card {i+1}")
      print(f"Card Number is {cc[i].getCardNumber()}")
      print(f"Card Type is {cc[i].getCardType()}")
      print(f"Balance is ${cc[i].getBalance():.2f}\n")

  printCards()

  cc2charge = 45.75
  cc2.chargeBalance(cc2charge)
  print(f"Amount to be charged to Credit Card 2 is ${cc2charge}\n")
  print(f"The new balance of Credit Card 2 is ${cc2.getBalance():.2f}\n")

  cc3charge = 100.00
  cc3.chargeBalance(cc3charge)
  print(f"Amount to be charged to Credit Card 3 is ${cc3charge:.2f}\n")
  print(f"The new balance of Credit Card 3 is ${cc3.getBalance():.2f}\n")

  cc4pay = 35.90
  cc4.payBalance(cc4pay)
  print(f"Amount to be paid to Credit Card 4 is ${cc4pay:.2f}\n")
  print(f"The new balance of Credit Card 4 is ${cc4.getBalance():.2f}\n")


testCreditCard()


