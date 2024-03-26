from Board import GameBoard
from TileBag import TileBag
import random
import pickle
from string import ascii_uppercase

class Player():
    def __init__(self, board: GameBoard, tilebag: TileBag) -> None:
        self.rack = []
        self.score = 0
        self.board = board
        self.tilebag = tilebag
        self.NextPlay = []
        with open('Tree.pickle', 'rb') as handle:
            self.tree = pickle.load(handle)

    def DrawTiles(self)-> bool:
        if len(self.tilebag.AvailableLetters) == 0:
            return False
        num = 7 - len(self.rack)
        for i in range(num):
            r1 = random.randint(0, len(self.tilebag.AvailableLetters)-1)
            letter = self.tilebag.AvailableLetters[r1]
            self.rack.append(letter)
            self.tilebag.AvailableLetters.remove(letter)
            if len(self.tilebag.AvailableLetters) == 0:
                self.rack = sorted(self.rack)
                return False
        self.rack = sorted(self.rack)
        return True
    
    def Exchange(self):
        pass

    def Move(self) -> bool:
        plays = self.board.FindPlays(self.rack)
        best_index = 0
        for i in range(len(plays)):
            if plays[best_index].score <= plays[i].score:
                best_index = i

        best_play = plays[best_index]
        self.board.MakePlay(best_play)
        self.rack = best_play.leave
        self.score += best_play.score
    
    def DisplayTiles(self) -> None:
        for tile in self.rack:
            print(tile, end=" ")
        print()
    def DisplayScore(self) -> None:
        print(self.score)