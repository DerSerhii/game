import os

import settings as st


class GameOver(Exception):
    """
    Class GameOver включает механизм сохранения финального счета игрока
    по завершению игры в файл scores.txt
    """

    def __init__(self, name_player, score):
        self.name_player = name_player
        self.score = score

    @staticmethod
    def get_score_list():
        if not os.path.exists(st.FILE_SCORE):
            return
        else:
            list_score = []
            with open(st.FILE_SCORE, 'r', encoding='utf-8') as file:
                for line in file:
                    row = line.replace('.', ' ').split()
                    row.pop(0)
                    list_score.append(row)
            return list_score

    @staticmethod
    def create_best_ten_score(list_score: list) -> list:
        list_score.sort(key=lambda i: int(i[1]), reverse=True)
        while len(list_score) > 10:
            list_score.pop()
        return list_score

    def create_score_file(self):
        score_file = GameOver.get_score_list()
        new_result = [self.name_player, self.score]

        if score_file:
            score_file.append(new_result)
            score = GameOver.create_best_ten_score(score_file)
        else:
            score = [new_result]

        with open(st.FILE_SCORE, 'w', encoding='utf-8') as file:
            for i, row in enumerate(score):
                print(f"{i + 1}.{' '.ljust(3 -len(str(i+1)), ' ')}{str(row[0]).ljust(40, '.')} {row[1]}", file=file)


class EnemyDown(Exception):
    pass
