import os

import models as md
import settings as st
from exceptions import EnemyDown, GameOver


def game_progress(player_name):
    start_score_player = 0

    choice_attack = md.Player.input_attack_valid("\nLet's go. You attack first...")
    player = md.Player(player_name, st.START_PLAYER_LIVES, start_score_player, choice_attack)

    level_enemy = 1
    enemy = md.Enemy(level_enemy)

    while True:
        try:
            player.attack(enemy)
            player.allowed_attacks = md.Player.input_attack_valid("Now I will attack...defend yourself...")
            player.defence(enemy)
            player.allowed_attacks = md.Player.input_attack_valid("Attack again...")
        except EnemyDown:
            player.score += 5
            level_enemy += 1
            print(f"You won!!! The enemy is destroyed! Bonus +5\n"
                  f"LIVES: {player.name}| {player.lives} of {st.START_PLAYER_LIVES}\n"
                  f"SCORE: {player.score}\n")
            enemy = md.Enemy(level_enemy)
            player.allowed_attacks = md.Player.input_attack_valid("This time I will beat you...Start attacking...")


def play():
    player_name = input("Who are you? If you're not afraid then tell me your name...")

    while True:
        query = input("Do you want to fight? If ready then enter 'start'\n(for a description enter 'help')...")

        if query.lower() == 'start':
            game_progress(player_name)

        if query.lower() == 'show scores':
            if not os.path.exists(st.FILE_SCORE):
                print("No statistics yet (:")
            else:
                with open(st.FILE_SCORE, 'r', encoding='utf-8') as file:
                    for line in file:
                        print(line, end='')
                print()

        if query.lower() == 'help':
            print(st.TEXT_HELP)

        if query.lower() == 'exit':
            print("had a good time :)")
            break


if __name__ == '__main__':
    try:
        play()
    except GameOver as ex:
        print("Game over!!!")
        ex.create_score_file()
    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye!")
