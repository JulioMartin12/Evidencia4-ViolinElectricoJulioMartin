class ViolinElectico:
    def __init__(self, marca, modelo, numero_serie, color, tipo_puente, tipo_cuerdas, amplificador_incluido):
        self.marca = marca;
        self.modelo = modelo;
        self.numero_serie = numero_serie;
        self.color = color;
        self.tipo_puente = tipo_puente;
        self.tipo_cuerdas = tipo_cuerdas;
        self.amplificador_incluido = amplificador_incluido;
       
    def get_marca(self):
           return self._marca;
       
    def set_marca(self, marca):
           self._marca = marca;
    
    def get_modelo(self):
        return self._modelo;
    
    def set_modelo(self, modelo):
        self._modelo = modelo;

    def get_numero_serie(self):
        return self._numero_serie;
    
    def set_numero_serie(self, numero_serie):
        self._numero_serie = numero_serie;

    def get_color(self):
        return self._color;
    
    def set_color(self, color):
        self._color = color;

    def get_tipo_puente(self):
        return self._tipo_puente
    
    def set_tipo_puente(self, tipo_puente):
        self._tipo_puente = tipo_puente;

    def get_tipo_cuerdas(self):
        return self._tipo_cuerdas;
    
    def set_tipo_cuerdas(self, tipo_cuerdas):
        self._tipo_cuerdas = tipo_cuerdas;

    def get_amplificador_incluido(self):
        return self._amplificador_incluido;
    
    def set_amplificador_incluido(self, amplificador_incluido):
        self._amplificador_incluido = amplificador_incluido;

    def __str__(self):
        return (f"ViolinElectrico(marca={self._marca}, modelo={self._modelo}, "
                f"numero_serie={self._numero_serie}, color={self._color}, "
                f"tipo_puente={self._tipo_puente}, tipo_cuerdas={self._tipo_cuerdas}, "
                f"amplificador_incluido={self._amplificador_incluido})")