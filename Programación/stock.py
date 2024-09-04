class Stock:

    def __init__(self) -> None:
        self.__tipos_marcas = [];
        self.__tipos_cuerdas = [];
        self.__tipos_modelos = [];
        self.__violines_electricos = [];
        self.cargar_datos();
        
    def get_tipos_marcas(self):
        return self.__tipos_marcas;
    
    def set_tipos_marcas(self, tipos_marcas):
        self.__tipos_marcas = tipos_marcas;

    def get_tipos_cuerdas(self):
        return self.__tipos_cuerdas;
    
    def set_tipos_cuerdas(self, tipos_cuerdas):
        self.__tipos_cuerdas = tipos_cuerdas;
    
    def get_tipos_modelos(self):
        return self.__tipos_modelos;
    
    def set_tipos_modelos(self, tipos_modelos):
        self.__tipos_modelos = tipos_modelos; 

    def get_violines_electricos (self):
        return self.__violines_electricos;
    
    def set_violines_electricos (self, violines_electricos):
        self.__violines_electricos  = violines_electricos;   
    
    def cargar_datos(self):
        self.cargar_tipos_cuerdas();
        self.cargar_tipos_marcas();
        self.cargar_tipos_modelos();
        self.cargar_violines_electronicos();
        return;
    

    def cargar_tipos_marcas(self):
        self.set_tipos_marcas([
                (1, 'VX-Pro', 'Modelo profesional de alta gama con sonido envolvente.'),
                (2, 'Eclipse 300', 'Modelo compacto ideal para principiantes.'),
                (3, 'Zephyr Z5', 'Sonido claro y brillante, excelente para grabaciones.'),
                (4, 'Starlight', None),
                (5, 'Thunderbolt', 'Diseño robusto y potente, ideal para presentaciones en vivo.'),
                (6, 'Aurora Elite', 'Violín eléctrico con tecnología avanzada y diseño elegante.'),
                (7, 'Phantom X', 'Modelo ligero con sonido potente, ideal para giras.'),
                (8, 'Luna 500', 'Perfecto para músicos intermedios que buscan calidad.'),
                (9, 'Solaris', 'Modelo con acabados premium y excelente resonancia.'),
                (10, 'Nebula V', 'Innovador diseño con opciones de personalización.')
            ]);
      
        return;

    def cargar_tipos_modelos(self):
        self.set_tipos_modelos([
                (1, 'VX-Pro', 'Modelo profesional de alta gama con sonido envolvente.'),
                (2, 'Eclipse 300', 'Modelo compacto ideal para principiantes.'),
                (3, 'Zephyr Z5', 'Sonido claro y brillante, excelente para grabaciones.'),
                (4, 'Starlight', None),
                (5, 'Thunderbolt', 'Diseño robusto y potente, ideal para presentaciones en vivo.'),
                (6, 'Aurora Elite', 'Violín eléctrico con tecnología avanzada y diseño elegante.'),
                (7, 'Phantom X', 'Modelo ligero con sonido potente, ideal para giras.'),
                (8, 'Luna 500', 'Perfecto para músicos intermedios que buscan calidad.'),
                (9, 'Solaris', 'Modelo con acabados premium y excelente resonancia.'),
                (10, 'Nebula V', 'Innovador diseño con opciones de personalización.')
            ]);
        return;

    def cargar_tipos_cuerdas(self):
        self.set_tipos_cuerdas(
            [(1, 'Acero Inoxidable', 'Cuerda de alta resistencia y durabilidad.'),
            (2, 'Nylon', 'Cuerda con sonido suave y cálido.'),
            (3, 'Titanio', 'Proporciona un tono brillante y una gran resistencia.'),
            (4, 'Kevlar', None),
            (5, 'Carbono', 'Ligera y resistente, ideal para tonos agudos.'),
            (6, 'Fibra de Vidrio', 'Cuerda económica con buena durabilidad.'),
            (7, 'Bronce Fosforado', 'Ofrece un sonido cálido con buenos armónicos.'),
            (8, 'Aluminio', 'Ligera y con una respuesta rápida.'),
            (9, 'Oro', 'Cuerda premium con un sonido excepcionalmente claro.'),
            (10, 'Plata', 'Tono brillante y excelente respuesta al arco.')]);
        return;

    def cargar_violines_electronicos(self):
        self.set_violines_electricos([
                (1, 2, 'YV2001234', 'Negro', 'Regulable', 3, True, 100),
                (2, 3, 'FN3005678', 'Blanco', 'Fijo', 5, True, 85),
                (3, 4, 'STV1009876', 'Rojo', 'Regulable', 2, True, 90),
                (4, 5, 'GB5004567', 'Azul', 'Fijo', 6, True, 75),
                (6, 7, 'IV7001234', 'Verde', 'Regulable', 7, True, 80),
                (7, 8, 'YV2002345', 'Gris', 'Regulable', 1, True, 65),
                (8, 9, 'JK4007890', 'Naranja', 'Fijo', 8, True, 95),
                (9, 10, 'CT5502341', 'Madera', 'Regulable', 4, True, 70),
                (10, 1, 'SC6003456', 'Morado', 'Fijo', 9, True, 60),
                (1, 2, 'EP7004568', 'Amarillo', 'Regulable', 10, True, 85)
              ]);
        return;

    def agregar_elemento(self, lista, elemento):
            lista.append(elemento);
            return;
    
    def tamanio_lista(self, lista):
        return lista.count();
  
    def eliminar_elemento_lista(self, lista, elemento):
        return lista.remove(elemento);