import random
from enum import Enum

import settings as st
from exceptions import EnemyDown, GameOver


class Enemy:
    """
    Class Enemy:
    свойства - level, lives.
    конструктор принимает уровень. Уровень жизней противнка = уровень противника.
    содержит два метода:
    Статический - select_attack(): возвращает случайное число от одного до трёх.
    decrease_lives(self): уменьшает количество жизней. Когда жизней становится 0 вызывает исключение EnemyDown.
    """

    def __init__(self, level):
        self.level = level
        self.lives = level
        self.text_lives = f"Enemy| {self.lives} of {self.level}"

    @staticmethod
    def select_attack() -> int:
        return random.choice(range(1, 4))

    @staticmethod
    def convert_attack_number_to_value(number) -> str:
        return st.DICT_ATTACK.get(int(number))

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown


class Player:
    """
    class Player:
    свойства: name, lives, score, allowed_attacks.
    конструктор принимает имя игрока. Количество жизней указывается из настроек. Счет равен нулю.
    методы:
    статический fight(attack, defense) - возвращает результат раунда - 0 если ничья,
                                        -1 если атака неуспешна, 1 если атака успешна.
    decrease_lives(self) - то же, что и Enemy.decrease_lives(), вызывает исключение GameOver.
    attack(self, enemy_obj) - получает ввод от пользователя (1, 2, 3),
                              выбирает атаку противника из объекта enemy_obj;
                              вызывает метод fight();
                              Если результат боя 0 - вывести "It's a draw!", если 1 = "You attacked successfully!"
                              и уменьшает количество жизней противника на 1, если -1 = "You missed!"
    defence(self, enemy_obj) - то же самое, что и метод attack(),
                               только в метод fight первым передается атака противника,
                               и при удачной атаке противника вызывается метод decrease_lives игрока.
    """

    def __init__(self, name, lives, score, allowed_attacks):
        self.name = name
        self.lives = lives
        self.score = score
        self.allowed_attacks = allowed_attacks
        self.text_lives = f"LIVES: {self.name}| {self.lives} of {st.START_PLAYER_LIVES}"
        self.text_score = f"SCORE: {self.name}| "

    @staticmethod
    def fight(attack_num: int, defense_num: int) -> int:
        """возвращает результат раунда -
           0 если ничья, -1 если атака неуспешна, 1 если атака успешна

           Волшебник побеждает воина. Воин побеждает разбойника. Разбойник побеждает волшебника.
        """

        dict_opponents = {
            "wizard": "warrior",
            "warrior": "robber",
            "robber": "wizard"
        }

        attack = Enemy.convert_attack_number_to_value(attack_num)
        defense = Enemy.convert_attack_number_to_value(defense_num)

        if attack == defense:
            return 0
        for i, j in dict_opponents.items():
            if attack == i and defense == j:
                return 1
            elif defense == i and attack == j:
                return -1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            print(self.text_score, self.score)
            raise GameOver(self.name, self.score)

    def attack(self, enemy_obj) -> None:
        """
        Если результат боя 0 - выводится "It's a draw!",
        если 1 = "You attacked successfully!" и уменьшает количество жизней противника на 1,
        если -1 = "You missed!"
        """

        attack_player = self.allowed_attacks
        print(f"\n\t\t\t\t\033[7m {Enemy.convert_attack_number_to_value(attack_player).upper()} \033[27m", end=" vs ")

        defence_enemy = Enemy.select_attack()
        print(f"{Enemy.convert_attack_number_to_value(defence_enemy).upper()}\n")

        battle_result = self.fight(attack_player, defence_enemy)

        if battle_result == 0:
            print("\033[33mIt's a draw!\033[38m")
        elif battle_result == 1:
            print("\033[32mYou attacked successfully!\033[38m")
            self.score += 1
            enemy_obj.decrease_lives()
        elif battle_result == -1:
            print("\033[31mYou missed!\033[38m")

        print(f"LIVES: {self.name}| {self.lives} of {st.START_PLAYER_LIVES}\t\t"
              f"Computer| {enemy_obj.lives} of {enemy_obj.level}\n"
              f"SCORE: {self.score}")

    def defence(self, enemy_obj) -> None:
        attack_enemy = Enemy.select_attack()
        print(f"\n\t\t\t\t{Enemy.convert_attack_number_to_value(attack_enemy).upper()}", end=" vs ")

        defence_player = self.allowed_attacks
        print(f"\033[7m {Enemy.convert_attack_number_to_value(defence_player).upper()} \033[27m")

        battle_result = self.fight(attack_enemy, defence_player)

        if battle_result == 0:
            print("\033[33mIt's a draw!\033[38m")
        elif battle_result == 1:
            print("\033[31mYou missed!\033[38m")
            self.decrease_lives()
        elif battle_result == -1:
            print("\033[32mYou defenced successfully!\033[38m")

        print(f"LIVES: {self.name}| {self.lives} of {st.START_PLAYER_LIVES}\t\t"
              f"Computer| {enemy_obj.lives} of {enemy_obj.level}\n"
              f"SCORE: {self.score}")

    @staticmethod
    def input_attack_valid(text=None):
        text_select = f"{st.TEXT_SELECT_ATTACK}\nWhat is your choice?..."
        while True:
            input_attack = input(f"{text}{text_select}")
            if input_attack.isdigit() \
                    and int(input_attack) \
                    in [KindOfAttack.WARRIOR.value, KindOfAttack.WIZARD.value, KindOfAttack.ROBBER.value]:
                return input_attack
            print("\033[31mPress only keys: '1', '2', '3', please\033[38m")


class KindOfAttack(Enum):
    WIZARD = 1
    WARRIOR = 2
    ROBBER = 3
