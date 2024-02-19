class Semester:
    topic_list = []
    def __init__(self, coef, nbr_topics):
        self.coef = coef
        self.nbr_topics = nbr_topics
        self.topics = [None for _ in range(1, nbr_topics)]
        Semester.topic_list.append(self)
    def __str__(self):
        return f"Coef: {self.coef}, Number of topics: {self.nbr_topics}"
