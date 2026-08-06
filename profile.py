import sys

class Profile:

    def __init__(self, name):
        self.name = name
        self.score = 0

        # Browser can't use highscore.txt
        if sys.platform == "emscripten":
            self.best_score = 0
        else:
            self.best_score = self.load_high_score()

    def increase_score(self):

        self.score += 1

        if self.score > self.best_score:

            self.best_score = self.score

            if sys.platform != "emscripten":
                self.save_high_score()

    def reset_score(self):
        self.score = 0

    def save_high_score(self):

        try:
            with open("highscore.txt", "w") as file:
                file.write(f"{self.name},{self.best_score}")
        except:
            pass

    def load_high_score(self):

        try:
            with open("highscore.txt", "r") as file:

                data = file.read().split(",")

                if len(data) == 2 and data[0] == self.name:
                    return int(data[1])

        except:
            pass

        return 0