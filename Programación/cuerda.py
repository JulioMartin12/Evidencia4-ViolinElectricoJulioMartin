class Cuerda:

    def __init__(self, id, cuerda, descripcion):
        self.__id = id;
        self.__cuerda = cuerda;
        self.__descripcion = descripcion;
    
    def get_id(self):
        return self.__id;
  
    def get_cuerda(self):
        return self.__cuerda;
    
    def set_cuerda(self, cuerda):
        self.__cuerda = cuerda;

    def get_descripcion(self):
        return self.__descripcion;
    
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion;