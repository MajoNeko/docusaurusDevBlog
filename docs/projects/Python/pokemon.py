class Pokemon:
    def __init__(self, _name,_level): # constructor
        self.name=_name
        self.level=_level

    def introduction(self):
        print(f"{self.name}, {self.name}!")

if __name__=="__main__":
    pickachu=Pokemon("Pickachu", 0)
    pickachu.introduction()