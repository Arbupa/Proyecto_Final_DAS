from abc import ABCMeta, abstractclassmethod

#Anime Search class Interface 
# class DbInterface(metaclass=abc.ABCMeta):
#    @abc.abstractmethod
#    def create_table(self):
#        pass
class DbInterface():

    @abstractclassmethod
    def create_table():
        pass

    @abstractclassmethod
    def inserta_data():
        pass

    @abstractclassmethod
    def show_data():
        pass
#    @abc.abstractmethod
#    def insert_data(self):
#        pass

#    @abc.abstractmethod
#    def show_data(self):
#        pass
#def eliminarEquipo(self, equipo: teambase, entrenador_id: int):
#base = DataBaseInteract()
#return base.eliminarEquipo(equipo, entrenador_id)