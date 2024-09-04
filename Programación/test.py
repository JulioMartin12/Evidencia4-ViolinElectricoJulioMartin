from violinElectronico import ViolinElectico

violin = ViolinElectico(marca = "Yamaha",
    modelo = "SV-200",
    numero_serie="123456789",
    color = "Negro",
    tipo_puente = "Regulable",
    tipo_cuerdas = "Sintéticas",
    amplificador_incluido = True,
    nivel_bateria = 100
    );
print(f"Los datos {violin}");