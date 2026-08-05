class Profile:

    def __init__(self, name):

        self.name = name
        self.score = 0
        self.best_score = self.load_high_score()



    def increase_score(self):

        self.score += 1


        if self.score > self.best_score:

            self.best_score = self.score

            self.save_high_score()



    def reset_score(self):

        self.score = 0



    def save_high_score(self):

        with open("highscore.txt", "w") as file:

            file.write(
                f"{self.name},{self.best_score}"
            )



    def load_high_score(self):

        try:

            with open("highscore.txt", "r") as file:

                data = file.read().split(",")


                if data[0] == self.name:

                    return int(data[1])


        except:

            return 0


        return 0