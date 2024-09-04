from violinElectronico import ViolinElectico
from stock import Stock
import time

almacen = Stock();
print(almacen.get_violines_electricos());

""" violin = ViolinElectico(marca = "Yamaha",
    modelo = "SV-200",
    numero_serie="123456789",
    color = "Negro",
    tipo_puente = "Regulable",
    tipo_cuerdas = "Sintéticas",
    amplificador_incluido = True,
    nivel_bateria = 0
    );
print(f"Los datos {violin}");
violin.prender(); """
""" print(f"Horario de encendido {violin.get_horario_encendido()}");
time.sleep(25);
violin.apagar();
print(f"Bateria restante {round(violin.get_nivel_bateria(),2)}%") """
