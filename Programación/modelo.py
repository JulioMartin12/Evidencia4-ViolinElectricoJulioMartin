class Modelo:

    def __init__(self, id, modelo, descripcion):
        self.__id = id;
        self.__modelo = modelo;
        self.__descripcion = descripcion;
    
    def get_id(self):
        return self.__id;
    
    def get_modelo(self):
        return self.__modelo;
    
    def set_modelo(self, modelo):
        self.__modelo = modelo;

    def get_descripcion(self):
        return self.__descripcion;
    
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion;