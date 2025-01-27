class Stats(): # отслеживание статистики

    def __init__(self):
            # инициализирует статистику
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt','r') as f:
            self.high_score = int(f.readline())
        self.high_score = 0



    def reset_stats(self): # статистика игры
         self.guns_left = 2
         self.score = 0
