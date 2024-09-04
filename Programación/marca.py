class Marca:

    def __init__(self, id, marca, descripcion):
        self.__id = id;
        self.__marca = marca;
        self.__descripcion = descripcion;
    
    def get_id(self):
        return self.__id;
    
    def get_marca(self):
        return self.__marca;
    
    def set_marca(self, marca):
        self.__marca = marca;

    def get_descripcion(self):
        return self.__descripcion;
    
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion;

     