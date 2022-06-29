START_PLAYER_LIVES = 3

FILE_SCORE = 'scores.txt'

DICT_ATTACK = {
    1: 'wizard',
    2: 'warrior',
    3: 'robber'
}

TEXT_SELECT_ATTACK = f"""
*****************  SELECT A HERO  ****************\033[34m
-= {DICT_ATTACK.get(1).upper()} =-      -= {DICT_ATTACK.get(2).upper()} =-       -= {DICT_ATTACK.get(3).upper()} =-
 \033[37m(press 1)          (press 2)          (press 3)\033[38m
"""

TEXT_HELP = f"""
DESCRIPTION:
Game principle:
The {DICT_ATTACK.get(1).upper()} defeats the {DICT_ATTACK.get(2).upper()}. 
The {DICT_ATTACK.get(2).upper()} defeats the {DICT_ATTACK.get(3).upper()}. 
The {DICT_ATTACK.get(3).upper()} defeats the {DICT_ATTACK.get(1).upper()}.
You can choose any of them. 
(you can only use the keys '1', '2', '3')

With a successful attack, the opponent's life decreases, the player receives one point.
If the defense fails, the player loses one life.
When a player runs out of lives, it's game over.
When an opponent runs out of lives, the player receives an additional five points.
-----------------------------------------------------------------------------------------------
Enter the command 'show scores' to see the ranking of the best players with their achievements.
Enter the command 'exit' to exit the program
"""
