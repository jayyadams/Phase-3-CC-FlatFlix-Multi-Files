class Review:
    all = []
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        

        self.viewer._reviews.append(self)
        self.viewer._movies.append(self.movie)

        self.movie._reviews.append(self)
        self.movie._reviewers.append(self.viewer)

        Review.all.append(self)


    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if type(rating) == int and 1 <= rating <= 5 and not hasattr(self, "rating"):
            self._rating = rating
        else:
            raise Exception("rating must be a int greater then 1 and less then 5 characters inclusive!")
        


    @property
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer(self, viewer):
        from classes.Viewer import Viewer
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception("Viewer must be an Instance of class Viewer!")
        
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        from classes.Movie import Movie
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception("movie must be an Instance of class movie!")