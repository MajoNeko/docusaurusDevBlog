class Pokemon:
    def __init__(self, _name,_level, _health): # constructor
        self.__name=_name
        self.__level=_level # __makes the variable private within the calss and inaccessible directly from outside the class
        self.__health=_health
        self.introduction()
    def __str__(self):
         return f"Name: {self.__name}\nHealth: {self.__health}\nLevel {self.__level}" # creats an automated structure for printing an object

    def __gt__(self,other): # defines a greater than method to compare class instances
         return self.__level>other.__level

    def introduction(self): # pokemon introduction method
        print(f"{self.__name}, {self.__name}!")

    def get_level(self):
        return self.__level
    
    def get_health(self):
        return self.__health

    def get_name(self):
            return self.__name

    def level_up(self):
        self.__level+=1

    def attack(self, other, damage):
         other.__health-=damage
    

if __name__=="__main__":
    pickachu=Pokemon("Pickachu", 0, 54)
    charmander=Pokemon("Charmander", 0, 54)
    pickachu.introduction()
    print(pickachu.get_level())

    pickachu.level_up()
    print(pickachu.get_level())
    pickachu.attack(charmander,3)
    print(charmander.get_health())
    print(pickachu)
