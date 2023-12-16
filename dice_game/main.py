# Write your solution to exercise 1 here
import random


class Dice:

    def __init__(self, numberOfSides: int = 6):
        self._sides = numberOfSides

    def roll_dice(self, numberOfRolls: int):
        self.results = []
        for _ in range(numberOfRolls):
            self.results.append(random.randint(1, self._sides))
        return self.results

    def __str__(self):
        return f"{self._sides}-sided dice"
    

class DiceGame(Dice):
    
    def __init__(self, dice: Dice):
        self._dice = dice
        self._numberOfDices = 5
        
    def roll_once(self):
        values = self._dice.roll_dice(self._numberOfDices)
        values.sort()
        if all(value == values[0] for value in values):
            print("Yatzy!")
        
        else:
            listOfNumbers = map(str, values)
            print(f"Rolled {self._numberOfDices} dice and got {", ".join(listOfNumbers)}")
            
    def roll_five_of_a_kind(self):
        NumberOfRolls = 0
        while True:
            NumberOfRolls += 1
            values = self._dice.roll_dice(self._numberOfDices)
            if all(value == values[0] for value in values):
                print(f"It took {NumberOfRolls} rolls to get five of a kind.")
                break
    
    def __str__(self):
        return f"The goal of the game is to roll the dice and get 5 of the same number. Using {self._dice}-sided dice."
       

if __name__ == "__main__":

    # six_sided_dice = Dice()
    # eight_sided_dice = Dice(8)
    # print(six_sided_dice)
    # print(eight_sided_dice)
    # dice_roll = six_sided_dice.roll_dice(5)
    # print(dice_roll)
    # second_dice_roll = eight_sided_dice.roll_dice(2)
    # print(second_dice_roll)

    six_sided_dice = Dice()
    game = DiceGame(six_sided_dice)
    print(game)
    game.roll_once()
    game.roll_once()
    game.roll_once()
    game.roll_once()
    game.roll_five_of_a_kind()
    difficult_game = DiceGame(Dice(10))
    difficult_game.roll_five_of_a_kind()
    easy_game = DiceGame(Dice(1))
    easy_game.roll_once()
    easy_game.roll_once()
    easy_game.roll_once()
    easy_game.roll_once()