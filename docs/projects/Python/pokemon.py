class Pokemon:
    def __init__(self, _name,_level): # constructor
        self.name=_name
        self.__level=_level # __makes the variable private within the calss and inaccessible directly from outside the class

    def introduction(self): # pokemon introduction method
        print(f"{self.name}, {self.name}!")

    def get_level(self):
        return self.__level

if __name__=="__main__":
    pickachu=Pokemon("Pickachu", 0)
    pickachu.introduction()
    print(pickachu.get_level())
