from Player import Player
from TileBag import TileBag
from Board import GameBoard, Play
import torch

class Env:
    def __init__(self) -> None:
        self.tile_bag = TileBag()
        self.game_board = GameBoard()
        self.player = Player(self.game_board, self.tile_bag)
        self.action_space_size = 11
        self.score_sum = 0.0
        self.steps = 0.0
        self.plays = []
        self.last_state = []

    def step(self, action):
        self.steps += 1.0
        done = True if self.tile_bag.isempty() else False
        if len(self.tile_bag.AvailableLetters) < 7:
            action = 0
        if self.last_state[action][0] == 0:
            self.player.Exchange()
        else:
            move = self.plays[action]
            self.score_sum += -1 * move.score
            self.player.MoveAI(move)
        state, plays = self.player.GetTopMoves(self.game_board.FindPlays(self.player.rack))
        while len(state) != 11:
            state.append([0] * 7)
        self.plays = plays
        self.last_state = state
        average_score = self.score_sum / self.steps
        return state, average_score, done

        pass
    def reset(self):
        self.tile_bag = TileBag()
        self.game_board = GameBoard()
        self.player = Player(self.game_board, self.tile_bag)
        self.score_sum = 0.0
        self.steps = 0.0
        self.player.DrawTiles()
        self.plays.clear()
        state, plays = self.player.GetTopMoves(self.game_board.FindPlays(self.player.rack))
        while len(state) != 11:
            state.append([0] * 7)
        self.plays = plays
        self.last_state = state
        return state
