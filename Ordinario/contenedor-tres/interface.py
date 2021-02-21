from abc import ABCMeta, abstractclassmethod

class DbInterface():

    @abstractclassmethod
    def create_tables():
        pass

    @abstractclassmethod
    def insert_data_anime_search():
        pass

    @abstractclassmethod
    def insert_data_anime_by_id():
        pass

    @abstractclassmethod
    def insert_data_genre_anime():
        pass
    
    @abstractclassmethod
    def insert_data_manga_search():
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