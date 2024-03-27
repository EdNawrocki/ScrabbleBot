from Board import GameBoard
from TileBag import TileBag
import random
import pickle
from string import ascii_uppercase
import heapq

PLAYS_CONSIDERED = 10

class Player():
    def __init__(self, board: GameBoard, tilebag: TileBag) -> None:
        self.rack = []
        self.score = 0
        self.board = board
        self.tilebag = tilebag
        self.turns = 0

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
        self.turns += 1
        while len(self.rack) != 0:
            ret = self.rack.pop()
            self.tilebag.AvailableLetters.append(ret)
        self.DrawTiles()

    def Move(self) -> bool:
        self.turns += 1
        plays = self.board.FindPlays(self.rack)
        while len(plays) == 0:
            self.Exchange()
            plays = self.board.FindPlays(self.rack)

        best_index = 0
        for i in range(len(plays)):
            if plays[best_index].score <= plays[i].score:
                best_index = i
        mvs = self.GetTopMoves(plays)
        for m in mvs:
            print(m)
        print()
        best_play = plays[best_index]
        self.board.MakePlay(best_play)
        self.rack = best_play.leave
        self.score += best_play.score

    def MoveAI(self, play):
        self.board.MakePlay(play)
        self.rack = play.leave
        self.DrawTiles()

    def GetTopMoves(self, plays) -> list:
        items = []
        for p in plays:
            node = PlayNode(-p.score, p)
            items.append(node)
        heapq.heapify(items)
        data_result = []
        play_result = []
        while len(data_result) != PLAYS_CONSIDERED:
            if not items:
                break
            item = heapq.heappop(items)
            data = [item.val, *[ord(letter) for letter in item.play.leave]]
            while len(data) != 7:
                data.append(0)
            if len(data_result) == 0 or data != data_result[-1]:
                data_result.append(data)
                play_result.append(item.play)
        return data_result, play_result

class PlayNode(object):
    def __init__(self, val: int, play):
        self.val = val
        self.play = play

    def __lt__(self, other):
        return self.val < other.val