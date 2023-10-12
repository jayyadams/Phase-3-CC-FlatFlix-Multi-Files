class Movie:
    def __init__(self, title):
        self.title = title

        self._reviewers = []
        self._reviews = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0:
            self._title = title
        else:
            raise Exception("Title must be a string greater then 0 characters!")


    def reviews(self):
        return self._reviews

    def reviewers(self):
        return list(set(self._reviewers))

    def average_rating(self):
        if self._reviews:
            average_rating = sum([review.rating for review in self._reviews]) / len(self._reviews)
            return round(average_rating, 1)
        else:
            return None 