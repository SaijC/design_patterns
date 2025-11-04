from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):
    def print_data():
        """implement in child class"""


class PersonSingelton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingelton.__instance == None:
            PersonSingelton("Default Name", 0)
        return __instance
    
    def __init__(self, name:str, age: int):
        if PersonSingelton.__instance != None:
            raise Exception("Singelton can't be instantiated more than onece!")
        else:
            self.name = name
            self.age = age
            PersonSingelton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingelton.__instance.name}, age: {PersonSingelton.__instance.age}")
        