from Board import GameBoard, BoardScore
from TileBag import TileBag
from Player import Player
import time
import pygame
import sys

def run():
    while p.rack or t.AvailableLetters:
        if not p.DrawTiles():
            break
        p.DisplayTiles()
        p.Move()
        p.DisplayScore()
        b.DrawBoard()
    print()
    b.DrawBoard()

def draw_board():
    screen.fill((0, 0, 0))
    for i in range(15):
        for j in range(15):
            if board[i][j].val.isalpha():
                if board[i][j].val == "I":
                    letter_x_offset = 15
                else:
                    letter_x_offset = 7
                pygame.draw.rect(screen, (222,184,135), [(margin + square_width) * i + margin + x_offset,
                                                         (margin + square_height) * j + margin + y_offset,
                                                         square_width, square_height])

                letter = tile_font.render(board[i][j].val, True, (0, 0, 0))
                screen.blit(letter, ((margin + square_width) * i + margin + x_offset + letter_x_offset,
                                     (margin + square_height) * j + margin + y_offset + 7))

                letter_score = modifier_font.render(str(b.TileScore[board[i][j].val]), True, (0, 0, 0))
                screen.blit(letter_score, ((margin + square_width) * i + margin + x_offset + 31,
                                           (margin + square_height) * j + margin + y_offset + 30))
            elif board[i][j].multiplier == BoardScore.TRIPLE_LETTER:
                pygame.draw.rect(screen, (0, 100, 200), [(margin + square_width) * i + margin + x_offset,
                                                         (margin + square_height) * j + margin + y_offset,
                                                         square_width, square_height])
                text_top = modifier_font.render("TRIPLE", True, (0, 0, 0))
                text_mid = modifier_font.render("LETTER", True, (0, 0, 0))
                text_bot = modifier_font.render("SCORE", True, (0, 0, 0))
                screen.blit(text_top, ((margin + square_width) * i + margin + x_offset + 5,
                                       (margin + square_height) * j + margin + y_offset + 7))
                screen.blit(text_mid, ((margin + square_width) * i + margin + x_offset + 5,
                                       (margin + square_height) * j + margin + y_offset + 17))
                screen.blit(text_bot, ((margin + square_width) * i + margin + x_offset + 5,
                                       (margin + square_height) * j + margin + y_offset + 27))

            elif board[i][j].multiplier == BoardScore.DOUBLE_LETTER:
                pygame.draw.rect(screen, (173, 216, 230), [(margin + square_width) * i + margin + x_offset,
                                                           (margin + square_height) * j + margin + y_offset,
                                                           square_width, square_height])
                text_top = modifier_font.render("DOUBLE", True, (0, 0, 0))
                text_mid = modifier_font.render("LETTER", True, (0, 0, 0))
                text_bot = modifier_font.render("SCORE", True, (0, 0, 0))
                screen.blit(text_top, ((margin + square_width) * i + margin + x_offset + 3,
                                       (margin + square_height) * j + margin + y_offset + 7))
                screen.blit(text_mid, ((margin + square_width) * i + margin + x_offset + 5,
                                       (margin + square_height) * j + margin + y_offset + 17))
                screen.blit(text_bot, ((margin + square_width) * i + margin + x_offset + 5,
                                       (margin + square_height) * j + margin + y_offset + 27))

            elif board[i][j].multiplier == BoardScore.DOUBLE_WORD:
                pygame.draw.rect(screen, (245, 188, 66), [(margin + square_width) * i + margin + x_offset,
                                                           (margin + square_height) * j + margin + y_offset,
                                                           square_width, square_height])
                if i == 7 and j == 7:
                    screen.blit(center_star, ((margin + square_width) * i + margin + x_offset+1,
                                       (margin + square_height) * j + margin + y_offset+2))
                else:
                    text_top = modifier_font.render("DOUBLE", True, (0, 0, 0))
                    text_mid = modifier_font.render("WORD", True, (0, 0, 0))
                    text_bot = modifier_font.render("SCORE", True, (0, 0, 0))
                    screen.blit(text_top, ((margin + square_width) * i + margin + x_offset + 3,
                                        (margin + square_height) * j + margin + y_offset + 7))
                    screen.blit(text_mid, ((margin + square_width) * i + margin + x_offset + 5,
                                        (margin + square_height) * j + margin + y_offset + 17))
                    screen.blit(text_bot, ((margin + square_width) * i + margin + x_offset + 5,
                                        (margin + square_height) * j + margin + y_offset + 27))

            elif board[i][j].multiplier == BoardScore.TRIPLE_WORD:
                pygame.draw.rect(screen, (237, 28, 36), [(margin + square_width) * i + margin + x_offset,
                                                         (margin + square_height) * j + margin + y_offset,
                                                         square_width, square_height])
                text_top = modifier_font.render("TRIPLE", True, (0, 0, 0))
                text_mid = modifier_font.render("WORD", True, (0, 0, 0))
                text_bot = modifier_font.render("SCORE", True, (0, 0, 0))
                screen.blit(text_top, ((margin + square_width) * i + margin + x_offset + 5,
                                       (margin + square_height) * j + margin + y_offset + 7))
                screen.blit(text_mid, ((margin + square_width) * i + margin + x_offset + 5,
                                       (margin + square_height) * j + margin + y_offset + 17))
                screen.blit(text_bot, ((margin + square_width) * i + margin + x_offset + 5,
                                       (margin + square_height) * j + margin + y_offset + 27))
            else:
                pygame.draw.rect(screen, (250, 218, 221), [(margin + square_width) * i + margin + x_offset,
                                                           (margin + square_height) * j + margin + y_offset,
                                                           square_width, square_height])
                
def draw_rack(rack):
    for i, letter in enumerate(rack):
            if letter == "I":
                letter_x_offset = 15
            else:
                letter_x_offset = 7
            pygame.draw.rect(screen, (222,184,135), [(margin + square_width) * (i + 4) + margin + x_offset,
                                                    700,
                                                    square_width, square_height])

            if letter == "?":
                tile_letter = tile_font.render(" ", True, (0, 0, 0))
            else:
                tile_letter = tile_font.render(letter, True, (0, 0, 0))
            screen.blit(tile_letter, ((margin + square_width) * (i + 4) + margin + x_offset + letter_x_offset,
                                    700 + 7))

            letter_score = modifier_font.render(str(b.TileScore[letter]), True, (0, 0, 0))
            screen.blit(letter_score, ((margin + square_width) * (i + 4) + margin + x_offset + 31,
                                    700 + 30))

if __name__ == "__main__":
    pygame.init()
    screen_width = 1000
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    square_width = 40
    square_height = 40
    margin = 3
    mouse_x = 0
    mouse_y = 0
    x_offset = 20
    y_offset = 20
    modifier_font = pygame.font.Font(None, 12)
    tile_font = pygame.font.Font(None, 45)
    score_font = pygame.font.Font(None, 25)
    image = pygame.image.load("../images/scrabble_star.png")
    center_star = pygame.transform.scale(image, (36, 34.2))
    pygame.display.set_caption("Scrabble")
    b = GameBoard()
    t = TileBag()
    p = Player(b, t)
    board = b.board
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_board()
        if p.DrawTiles():
            draw_rack(p.rack)
            time.sleep(1)
            p.Move()
            print(p.score)
        elif len(p.rack) != 0:
            draw_rack(p.rack)
            time.sleep(1)
            p.Move()
            print(p.score)
        