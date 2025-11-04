from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):
    def print_data():
        """implement in child class"""

class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance
    
    def __init__(self, name:str, age: int):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton can't be instantiated more than ones!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, age: {PersonSingleton.__instance.age}")
        