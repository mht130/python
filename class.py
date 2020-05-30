class living():
    def __init__(self,species:str):
        self.species=species
    def info(self):
        print(
        f'''
        Species : {self.species}
        Name : { self.name}
        Age  : {self.age}
        '''
    )



class human(living):
    humans=[]
    def __init__(self,name:str,age:int):
        super().__init__("Human")
        self.name=name
        self.age=age
        self.humans.append(self.name)

    def speak(self,msg:str):
        print(self.name+" : "+msg)
    
    def __add__(self,p):
        print(f"{self.name}")

    def __str__(self):
        return self.name

    @classmethod
    def counter(cls):
        return len(cls.humans)



class math():
    @staticmethod
    def add(a:int,b:int)->int:
        return a+b




ali=human("Ali",12)
reza=human("Reza",13)
