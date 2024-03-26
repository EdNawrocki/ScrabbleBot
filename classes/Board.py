from enum import Enum
import pickle
from string import ascii_uppercase


class BoardScore(Enum):
    DOUBLE_LETTER = 1
    DOUBLE_WORD = 2
    TRIPLE_LETTER = 3
    TRIPLE_WORD = 4

class Square():
    def __init__(self, row, col, val='.', prev=None, next=None, mult=0) -> None:
        self.val = val
        self.multiplier = mult
        self.prev = prev
        self.next = next
        self.cross_checks = {
            'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1,
            'F': 1, 'G': 1, 'H': 1, 'I': 1, 'J': 1,
            'K': 1, 'L': 1, 'M': 1, 'N': 1, 'O': 1,
            'P': 1, 'Q': 1, 'R': 1, 'S': 1, 'T': 1,
            'U': 1, 'V': 1, 'W': 1, 'X': 1, 'Y': 1, 
            'Z': 1
        }
        self.cross_score = 0
        self.isAnchor = False
        self.row= row
        self.col = col
    
    def reset_cross_check(self):
        self.cross_checks = {
            'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1,
            'F': 1, 'G': 1, 'H': 1, 'I': 1, 'J': 1,
            'K': 1, 'L': 1, 'M': 1, 'N': 1, 'O': 1,
            'P': 1, 'Q': 1, 'R': 1, 'S': 1, 'T': 1,
            'U': 1, 'V': 1, 'W': 1, 'X': 1, 'Y': 1, 
            'Z': 1
        }
        self.cross_score = 0

class Play():
    def __init__(self) -> None:
        self.leave = []
        self.tilesPlayed = 0
        self.score = 0
        self.wordScore = 0
        self.tiles = []
        self.word = ""
        self.multiplier = 1
        self.perpendicular_scores = 0
        self.isAnchored = False

    def clone(self, p):
        p.leave = self.leave.copy()
        p.tilesPlayed = self.tilesPlayed
        p.score = self.score
        p.wordScore = self.wordScore
        p.tiles = self.tiles.copy()
        p.word = self.word
        p.multiplier = self.multiplier
        p.perpendicular_scores = self.perpendicular_scores
        p.isAnchored = self.isAnchored


class GameBoard():
    def __init__(self) -> None:
        self.horizontal = True
        self.rows, self.cols = (15, 15)
        self.board = [[Square(j, i) for i in range(self.cols)] for j in range(self.rows)]
        self.board[0][0].multiplier = BoardScore.TRIPLE_WORD
        self.board[0][7].multiplier = BoardScore.TRIPLE_WORD
        self.board[0][14].multiplier = BoardScore.TRIPLE_WORD
        self.board[7][0].multiplier = BoardScore.TRIPLE_WORD
        self.board[7][14].multiplier = BoardScore.TRIPLE_WORD
        self.board[14][0].multiplier = BoardScore.TRIPLE_WORD
        self.board[14][7].multiplier = BoardScore.TRIPLE_WORD
        self.board[14][14].multiplier = BoardScore.TRIPLE_WORD

        self.board[0][3].multiplier = BoardScore.DOUBLE_LETTER
        self.board[0][11].multiplier = BoardScore.DOUBLE_LETTER
        self.board[2][6].multiplier = BoardScore.DOUBLE_LETTER
        self.board[2][8].multiplier = BoardScore.DOUBLE_LETTER
        self.board[3][0].multiplier = BoardScore.DOUBLE_LETTER
        self.board[3][7].multiplier = BoardScore.DOUBLE_LETTER
        self.board[3][14].multiplier = BoardScore.DOUBLE_LETTER
        self.board[6][2].multiplier = BoardScore.DOUBLE_LETTER
        self.board[6][6].multiplier = BoardScore.DOUBLE_LETTER
        self.board[6][8].multiplier = BoardScore.DOUBLE_LETTER
        self.board[6][12].multiplier = BoardScore.DOUBLE_LETTER
        self.board[7][3].multiplier = BoardScore.DOUBLE_LETTER
        self.board[7][11].multiplier = BoardScore.DOUBLE_LETTER
        self.board[8][2].multiplier = BoardScore.DOUBLE_LETTER
        self.board[8][6].multiplier = BoardScore.DOUBLE_LETTER
        self.board[8][8].multiplier = BoardScore.DOUBLE_LETTER
        self.board[8][12].multiplier = BoardScore.DOUBLE_LETTER
        self.board[11][0].multiplier = BoardScore.DOUBLE_LETTER
        self.board[11][7].multiplier = BoardScore.DOUBLE_LETTER
        self.board[11][14].multiplier = BoardScore.DOUBLE_LETTER
        self.board[12][6].multiplier = BoardScore.DOUBLE_LETTER
        self.board[12][8].multiplier = BoardScore.DOUBLE_LETTER
        self.board[14][3].multiplier = BoardScore.DOUBLE_LETTER
        self.board[14][11].multiplier = BoardScore.DOUBLE_LETTER

        self.board[1][1].multiplier = BoardScore.DOUBLE_WORD
        self.board[13][13].multiplier = BoardScore.DOUBLE_WORD
        self.board[2][2].multiplier = BoardScore.DOUBLE_WORD
        self.board[12][12].multiplier = BoardScore.DOUBLE_WORD
        self.board[11][11].multiplier = BoardScore.DOUBLE_WORD
        self.board[3][3].multiplier = BoardScore.DOUBLE_WORD
        self.board[10][10].multiplier = BoardScore.DOUBLE_WORD
        self.board[4][4].multiplier = BoardScore.DOUBLE_WORD
        self.board[7][7].multiplier = BoardScore.DOUBLE_WORD
        self.board[1][13].multiplier = BoardScore.DOUBLE_WORD
        self.board[2][12].multiplier = BoardScore.DOUBLE_WORD
        self.board[3][11].multiplier = BoardScore.DOUBLE_WORD
        self.board[4][10].multiplier = BoardScore.DOUBLE_WORD
        self.board[13][1].multiplier = BoardScore.DOUBLE_WORD
        self.board[12][2].multiplier = BoardScore.DOUBLE_WORD
        self.board[11][3].multiplier = BoardScore.DOUBLE_WORD
        self.board[10][4].multiplier = BoardScore.DOUBLE_WORD

        self.board[1][5].multiplier = BoardScore.TRIPLE_LETTER
        self.board[1][9].multiplier = BoardScore.TRIPLE_LETTER
        self.board[5][1].multiplier = BoardScore.TRIPLE_LETTER
        self.board[5][5].multiplier = BoardScore.TRIPLE_LETTER
        self.board[5][9].multiplier = BoardScore.TRIPLE_LETTER
        self.board[5][13].multiplier = BoardScore.TRIPLE_LETTER
        self.board[9][1].multiplier = BoardScore.TRIPLE_LETTER
        self.board[9][5].multiplier = BoardScore.TRIPLE_LETTER
        self.board[9][9].multiplier = BoardScore.TRIPLE_LETTER
        self.board[9][13].multiplier = BoardScore.TRIPLE_LETTER
        self.board[13][5].multiplier = BoardScore.TRIPLE_LETTER
        self.board[13][9].multiplier = BoardScore.TRIPLE_LETTER

        for i in range(15):
            for j in range(15):
                self.board[i][j].next = None if j == 14 else self.board[i][j+1]
                self.board[i][j].prev = None if j == 0 else self.board[i][j-1]

        self.PlayBoard = [['.' for i in range(self.cols)] for j in range(self.rows)]

        self.TileScore = {
            'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
            'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
            'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
            'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
            'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 
            'Z': 10, '?': 0
                    }
        
        self.AnchorList = [self.board[7][7]]
        self.board[7][7].isAnchor = True
        self.PlayList = []

        with open('../ValidList.pickle', 'rb') as handle:
            self.word_list = pickle.load(handle)
        with open('Tree.pickle', 'rb') as handle:
            self.root = pickle.load(handle)

    def TransposeBoard(self):
        for i in range(15):
            for j in range(15):
                if self.horizontal == True:
                    self.board[i][j].next = None if i == 14 else self.board[i+1][j]
                    self.board[i][j].prev = None if i == 0 else self.board[i-1][j]
                else:
                    self.board[i][j].next = None if j == 14 else self.board[i][j+1]
                    self.board[i][j].prev = None if j == 0 else self.board[i][j-1]
        self.horizontal = not self.horizontal

    def GetLetterMultiplier(self, square: Square):
        val = square.multiplier
        if val == BoardScore.DOUBLE_LETTER:
            return 2
        elif val == BoardScore.TRIPLE_LETTER:
            return 3
        return 1
    def GetWordMultiplier(self, square: Square):
        val = square.multiplier
        if val == BoardScore.DOUBLE_WORD:
            return 2
        elif val == BoardScore.TRIPLE_WORD:
            return 3
        return 1

    def DrawBoard(self):
        for i in range(15):
            for j in range(15):
                if self.board[i][j].val == '.':
                    if self.board[i][j].multiplier == BoardScore.DOUBLE_LETTER:
                        print('*', end =" ")
                    elif self.board[i][j].multiplier == BoardScore.DOUBLE_WORD:
                        print('!', end =" ")
                    elif self.board[i][j].multiplier == BoardScore.TRIPLE_LETTER:
                        print('#', end =" ")
                    elif self.board[i][j].multiplier == BoardScore.TRIPLE_WORD:
                        print('~', end =" ")
                    else:
                        print('·', end =" ")
                else:
                    print(self.board[i][j].val, end =" ")
            print()
    def ClearBoard(self):
        for i in range(15):
            for j in range(15):
                self.board[i][j].val = '.'

    def build_postfix(self, rack:list, tree:dict, square:Square, play:Play):
            if square == None:
                return
            if square.val.isalpha():
                if square.val in tree:
                    play.score += self.TileScore[square.val]
                    new_node = tree[square.val]
                    play.tiles.append(square)
                    self.build_postfix(rack, new_node, square.next, play)
            else:
                if "END" in tree and play.isAnchored:
                    #We need to score the current word
                    new_play = Play()
                    play.clone(new_play)
                    new_play.word = tree["WORD"]
                    new_play.leave = rack
                    new_play.score = new_play.perpendicular_scores + new_play.score * new_play.multiplier
                    if new_play.tilesPlayed == 7:
                        new_play.score += 50
                    self.PlayList.append(new_play)
                for letter in rack:
                    if letter == '?':
                        for c in ascii_uppercase:
                            if c in tree and square.cross_checks[c] == 1:
                                new_node = tree[c]
                                new_rack = rack.copy()
                                new_rack.remove(letter)
                                p = Play()
                                play.clone(p)
                                p.perpendicular_scores += square.cross_score * self.GetWordMultiplier(square)
                                if square.isAnchor:
                                    p.isAnchored = True
                                p.tiles.append(square)
                                p.tilesPlayed += 1
                                self.build_postfix(new_rack, new_node, square.next, p)
                    elif letter in tree and square.cross_checks[letter] == 1:
                        new_node = tree[letter]
                        new_rack = rack.copy()
                        new_rack.remove(letter)
                        p = Play()
                        play.clone(p)
                        if square.cross_score != 0:
                            p.perpendicular_scores += (square.cross_score + self.TileScore[letter] * self.GetLetterMultiplier(square)) * self.GetWordMultiplier(square)
                        p.score += self.GetLetterMultiplier(square) * self.TileScore[letter]
                        p.multiplier *= self.GetWordMultiplier(square)
                        if square.isAnchor:
                                p.isAnchored = True
                        p.tiles.append(square)
                        p.tilesPlayed += 1
                        self.build_postfix(new_rack, new_node, square.next, p)
        
    def build_prefix(self, rack, square:Square, limit:int):
        if limit > 0 and square != None:
            p = Play()
            while square.prev != None and square.prev.val.isalpha():
                square = square.prev
            self.build_postfix(rack, self.root, square, p)
            self.build_prefix(rack, square.prev, limit-1)

    #so we update the cross checks, run the word finding algo, update the cross checks again
    def UpdateCrossChecks(self):
        #for each tile in the anchor list, go all the way to the left, then all the way to the right,
        #and see which tiles can be played in the square
        for s in self.AnchorList:
            lead = s
            while lead.prev != None and lead.prev.val.isalpha():
                lead = lead.prev
            word = ""
            while lead.val.isalpha():
                word += lead.val
                lead = lead.next
            word += '?'
            lead = lead.next
            while lead != None and lead.val.isalpha():
                word += lead.val
                lead = lead.next
            if word != "?":
                self.isValidCross(0, word, self.root, s.cross_checks)
                s.cross_score = 0
                for c in word:
                    if c == '?':
                        continue
                    s.cross_score += self.TileScore[c]
            else:
                s.reset_cross_check()
            

    def isValidCross(self, i: int, word: str, tree:dict, result: dict) -> bool:
        if i == len(word):
            if "END" in tree:
                return True
            return False
        if word[i] == '?':
            for c in ascii_uppercase:
                if c not in tree or not self.isValidCross(i+1, word, tree[c], result):
                        result[c] = 0  
                else:
                    result[c] = 1
        else:
            if word[i] not in tree:
                return False
            return self.isValidCross(i+1, word, tree[word[i]], result)
        return True
    
    def PruneAnchors(self):
        res = []
        for s in self.AnchorList:
            if s.isAnchor:
                res.append(s)
        self.AnchorList = res
        
    def FindPlays(self, rack) -> list:
        self.PlayList.clear()
        self.PruneAnchors()
        self.UpdateCrossChecks()
        self.TransposeBoard()
        for s in self.AnchorList:
            self.build_prefix(rack, s, len(rack))
        self.UpdateCrossChecks()
        self.TransposeBoard()
        for s in self.AnchorList:
            self.build_prefix(rack, s, len(rack))
        return self.PlayList
    
    def MakePlay(self, play: Play):
        num = len(play.tiles)
        for i in range(num):
            play.tiles[i].val = play.word[i]
            play.tiles[i].isAnchor = False
        for i in range(num):
            r = play.tiles[i].row
            c = play.tiles[i].col
            if r != 14 and not self.board[r+1][c].isAnchor and not self.board[r+1][c].val.isalpha():
                self.AnchorList.append(self.board[r+1][c])
                self.board[r+1][c].isAnchor = True
            if r != 0 and not self.board[r-1][c].isAnchor and not self.board[r-1][c].val.isalpha():
                self.AnchorList.append(self.board[r-1][c])
                self.board[r-1][c].isAnchor = True
            if c != 14 and not self.board[r][c+1].isAnchor and not self.board[r][c+1].val.isalpha():
                self.AnchorList.append(self.board[r][c+1])
                self.board[r][c+1].isAnchor = True
            if c != 0 and not self.board[r][c-1].isAnchor and not self.board[r][c-1].val.isalpha():
                self.AnchorList.append(self.board[r][c-1])
                self.board[r][c-1].isAnchor = True 