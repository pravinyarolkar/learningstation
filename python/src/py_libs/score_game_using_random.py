import random

number = list(range(1,7))

__all__=[
     "Players",
     "roll_dice",
     "get_score",
     "get_winner",
     "start_a_game"
]

class Players:
    '''
    This is Players class to store players information and methods to process data
    '''
    def __init__(self) -> None:
        self.user1 = "user1"
        self.user2 = "user2"
        self.score = {self.user1:0,
                      self.user2:0}
        
    def roll_dice(self) -> int:
        '''
        roll_dice() is a method of Players() class
        Function is to roll a dice and get random number between 1 - 6
        '''
        num = random.choice(number)
        return num
    
    def get_score(self, user):
            '''
            get_score() is a method of Players() class
            Function is to provide players score
            '''
            if user == self.user1:
                 return self.score[self.user1]
            else:
                 return self.score[self.user2]
            
    def get_winner(self):
         '''
         get_winner() is a method from Players() class
         function is to provide winner name
         '''
         if self.score[self.user1] > self.score[self.user2]:
              return f"Winner is - user1"
         else:
              return f"Winner is - user2"
         
    def start_a_game(self):
        '''
        start_a_game() is a method of Players class and function is to start a game.
        '''
        while True:
            while True:
                ret = self.roll_dice()
                print(f"User 1 -- {ret}")
                self.score[obj.user1] += ret
                if ret != 6:
                    break
                else:
                    print("got 6 rolling again\n")

            while True:
                ret = self.roll_dice()
                print(f"User 2 -- {ret}")
                self.score[self.user2] += ret
                if ret != 6:
                    break
                else:
                    print("got 6 rolling again\n")
            
            ch = input("want to continue?y/n")
            if ch == "n":
                break
        
        print("Printing game score :\n")
        print("User 1 score : {}".format(self.get_score("user1")))
        print("User 2 score : {}".format(self.get_score("user2")))

        print(self.get_winner())
        
if __name__ == "__main__":
    obj = Players()

    obj.start_a_game()

_inst = Players()
rolldice = _inst.roll_dice
getwinner = _inst.get_winner
startgame = _inst.start_a_game