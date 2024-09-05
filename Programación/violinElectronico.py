import datetime
class ViolinElectronico:
    def __init__(self, marca, modelo, numero_serie, color, tipo_puente, tipo_cuerdas, amplificador_incluido, nivel_bateria ):
        self.__marca = marca;
        self.__modelo = modelo;
        self.__numero_serie = numero_serie;
        self.__color = color;
        self.__tipo_puente = tipo_puente;
        self.__tipo_cuerdas = tipo_cuerdas;
        self.__amplificador_incluido = amplificador_incluido;
        self.__nivel_bateria = nivel_bateria;
        self.__horario_encendido = 0;
        self.__horario_apagado = 0;
       
    def get_marca(self):
           return self.__marca;
       
    def set_marca(self, marca):
           self.__marca = marca;
    
    def get_modelo(self):
        return self.__modelo;
    
    def set_modelo(self, modelo):
        self.__modelo = modelo;

    def get_numero_serie(self):
        return self.__numero_serie;
    
    def set_numero_serie(self, numero_serie):
        self.__numero_serie = numero_serie;

    def get_color(self):
        return self.__color;
    
    def set_color(self, color):
        self.__color = color;

    def get_tipo_puente(self):
        return self.__tipo_puente;
    
    def set_tipo_puente(self, tipo_puente):
        self.__tipo_puente = tipo_puente;

    def get_tipo_cuerdas(self):
        return self.__tipo_cuerdas;
    
    def set_tipo_cuerdas(self, tipo_cuerdas):
        self.__tipo_cuerdas = tipo_cuerdas;

    def get_amplificador_incluido(self):
        return self.__amplificador_incluido;
    
    def set_amplificador_incluido(self, amplificador_incluido):
        self.__amplificador_incluido = amplificador_incluido;
    
    def get_nivel_bateria(self):
        return float(self.__nivel_bateria);
    
    def set_nivel_bateria(self, value):
        self.__nivel_bateria = value;
    
    def get_horario_encendido(self):
        return self.__horario_encendido
    
    def set_horario_encendido(self, horario_encendido):
        self.__horario_encendido = horario_encendido;
        self.set_horario_apagado(0);
    
    def get_horario_apagado (self):
        return self.__horario_apagado; 
    
    def set_horario_apagado (self, horario_apagado ):
        self.__horario_apagado  = horario_apagado;
        self.__nivel_bateria

    def apagar(self):
        self.set_horario_apagado(datetime.datetime.now());
        self.set_nivel_bateria(self.get_nivel_bateria() -  self.calcular_tiempo_consumo_bateria());
        self.set_horario_encendido(0);
        return self.get_horario_encendido();

    def prender(self):
        if (self.get_nivel_bateria() != 0):
            self.set_horario_encendido(datetime.datetime.now());
            return True;
        else:
            return False; 
          
    def cargar_bateria(self, tiempo_segundo):
        if(tiempo_segundo < 0):
            raise ValueError("Debe ingresar un valor mayor a 0");
        carga = tiempo_segundo / 2;
        nuevaCarga = self.get_nivel_bateria()+carga;
        if(nuevaCarga > 100):
            self.set_nivel_bateria(100);
        else:
            self.set_nivel_bateria(nuevaCarga);  
        return self.get_nivel_bateria();
    
    def calcular_tiempo_consumo_bateria(self):
        minutos=((self.get_horario_apagado().hour)* 360 + self.get_horario_apagado().minute*60 + self.get_horario_apagado().second) - ((self.get_horario_encendido().hour)* 360 + self.get_horario_encendido().minute*60 + self.get_horario_encendido().second);
        return ((100 * minutos)/90);

    def __str__(self):
        return (f"ViolinElectrico(marca={self.__marca}, modelo={self.__modelo}, "
                f"numero_serie={self.__numero_serie}, color={self.__color}, "
                f"tipo_puente={self.__tipo_puente}, tipo_cuerdas={self.__tipo_cuerdas}, "
                f"amplificador_incluido={self.__amplificador_incluido})");
        
