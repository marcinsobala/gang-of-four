"""
This can be achieved either with interfaces or with functions since functions are first-class
citizens in python. Now in order to add new publishing strategy all you need to do is
create a new subclass of the interface and pass it in as argument.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import shuffle


@dataclass
class Review:
    score: int
    title: str


class PublishingStrategy(ABC):
    @abstractmethod
    def order_reviews(self, reviews: list[Review]) -> list[Review]:
        pass


class FifoStrategy(PublishingStrategy):
    def order_reviews(self, reviews: list[Review]) -> list[Review]:
        return reviews.copy()


class FiloStrategy(PublishingStrategy):
    def order_reviews(self, reviews: list[Review]) -> list[Review]:
        return reviews[::-1]


class RandomStrategy(PublishingStrategy):
    def order_reviews(self, reviews: list[Review]) -> list[Review]:
        reviews_copy = reviews.copy()
        shuffle(reviews_copy)
        return reviews_copy


class BlackHoleStrategy(PublishingStrategy):
    def order_reviews(self, reviews: list[Review]) -> list[Review]:
        return []


class GameReviewer:
    reviews: list[Review] = []

    @staticmethod
    def publish_review(review: Review):
        print(f"{review.title} got score of {review.score}!")

    def write_review(self, title: str, score: int):
        self.reviews.append(Review(score, title))

    def publish_reviews(self, publishing_strategy: PublishingStrategy):
        reviews = publishing_strategy.order_reviews(self.reviews)
        if not reviews:
            print("No games were reviewed!")
            return

        for review in reviews:
            self.publish_review(review)


app = GameReviewer()

app.write_review("Tekken 7", 9)
app.write_review("Resident Evil: Village", 10)
app.write_review("Silent Hill 2", 10)
app.write_review("Magical adventures of ferocious hamster", 3)

app.publish_reviews(FiloStrategy())

print("\nUsing Black Hole strategy now...\n")
app.publish_reviews(BlackHoleStrategy())
