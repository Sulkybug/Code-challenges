'''
You are playing poker with your friends and need to evaluate your hand. 
A hand consists of five cards and is ranked, from lowest to highest, in the following way:
High Card: Highest value card (from 2 to Ace).
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: 10, Jack, Queen, King, Ace, in same suit. 

Task:
Output the rank of the give poker hand. 

Input Format: 
A string, representing five cards, each indicating the value and suite of the card, separated by spaces. 
Possible card values are: 2 3 4 5 6 7 8 9 10 J Q K A
Suites:  H (Hearts), D (Diamonds), C (Clubs), S (Spades)
For example, JD indicates Jack of Diamonds. 

Output Format:
A string, indicating the rank of the hand (in the format of the above description). 

Sample Input:
JS 2H JC AC 2D

Sample Output: 
Two Pairs
'''

hand = input().split(" ") 

cardsValues = []
suit=[] 
for i in hand:
 if '10' in i:
  cardsValues.append('10')
  suit.append(i[2])
 else:
  cardsValues.append(i[0])
  suit.append(i[1])

values = sorted(list(set(cardsValues)))
suitValues = list(set(suit))

convertNum = []
for i in values:
    if i.isdigit():
        x = int(i)
    elif i == 'A':
        x = 1
    else:
        x = {'J': 11, 'Q': 12, 'K': 13}[i]
    convertNum.append(x)

v= -20
status = False
for i in sorted(convertNum):
 x = i
 if x == v + 1:
  status= True
 else:
  status = False
 v = x
 
game = []
suitGame = []
for i in values:
 game.append(cardsValues.count(i))

for i in suitValues:
 suitGame.append(suit.count(i))

if '10' in values and 'J' in values and 'Q' in values and 'K' in values and  'A' in values and 5 in suitGame :
 print("Royal Flush")

elif 5 in suitGame and status == True:
 print("Straight Flush")

elif status == True:  
 print("Straight")
 
elif 5 in suitGame:
 print("Flush")

elif 2 in game and 3 in game:
 print("Full House")

elif game.count(2) == 2:
 print("Two Pairs")

elif 2 in game:
 print("One Pair")

elif 3 in game:
 print("Three of a Kind")

elif 4 in game:
 print("Four of a Kind")

else:
 print("High Card")
