import os
from threading import Timer
import MemoryGame
# from time import sleep
# import pygame

SCORES_FILE_NAME = "Scores.txt"
ERROR_MESSAGE = "Something went wrong.."

def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')
    # print("\n" * 100)


def screen_cleaner_with_header_after():
    os.system('cls' if os.name == 'nt' else 'clear')
    MemoryGame.print_memory_game_header()


def freeze_screen(time_sec_float):
    # sleep(time_sec_float)
    # pygame.time.wait(time_sec_float)
    # pygame.time.delay(time_sec_float)

    t = Timer(time_sec_float, screen_cleaner_with_header_after)
    t.start()