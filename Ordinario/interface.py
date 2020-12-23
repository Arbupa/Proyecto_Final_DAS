import abc

#Anime Search class Interface 
class DbInterface(metaclass=abc.ABCMeta):
   @abc.abstractmethod
   def create_table(self):
       pass

   @abc.abstractmethod
   def insert_data(self):
       pass

   @abc.abstractmethod
   def show_data(self):
       pass
    