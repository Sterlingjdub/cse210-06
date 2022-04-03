
class Score_handler():

    def __init__(self) -> None:
        self.__score = 0
        self.__life = 3
    
    def increase_score(self, value):
        self.__score = self.__score + value

    def reduce_life(self):
        self.__life = self.__life -1
    
    def get_score(self):
        return str(self.__score)