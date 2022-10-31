"""
Strategy pattern is commonly used when you have more than one way of solving generic problem.
It allows to use polymorphism in place of ugly if-else structures.
In this here anti-example if you wanted to create a new strategy, you would have to modify
the method publish_reviews() by extending already bulky if-else monstrosity.
"""

from dataclasses import dataclass
from random import shuffle


@dataclass
class Review:
    score: int
    title: str


class GameReviewer:

    reviews: list[Review] = []

    def write_review(self, title: str, score: int):
        self.reviews.append(Review(score, title))

    @staticmethod
    def publish_review(game: Review):
        print(f"{game.title} got score of {game.score}!")

    def publish_reviews(self, publishing_strategy: str = "fifo"):
        if not self.reviews:
            print("No games to review!")
            return

        if publishing_strategy == "fifo":
            for game in self.reviews:
                self.publish_review(game)
        elif publishing_strategy == "filo":
            for game in self.reviews[::-1]:
                self.publish_review(game)
        elif publishing_strategy == "random":
            games_copy = self.reviews.copy()
            shuffle(games_copy)
            for game in games_copy:
                self.publish_review(game)


app = GameReviewer()

app.write_review("Tekken 7", 9)
app.write_review("Resident Evil: Village", 10)
app.write_review("Silent Hill 2", 10)
app.write_review("Magical adventures of ferocious hamster", 3)

app.publish_reviews("fifo")