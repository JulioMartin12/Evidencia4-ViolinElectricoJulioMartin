from violinElectronico import ViolinElectronico
import pytest

@pytest.mark.parametrize("violin,resultado", [
    (ViolinElectronico(1, 2, 'YV2001234', 'blanco', 'Regulable', 3, True, 0), False),
    (ViolinElectronico(2, 1, 'YV3001234', 'Negro', 'Regulable', 3, True, 100), True) 
])
def test_prender(violin, resultado):
    assert violin.prender() == resultado;
 
@pytest.mark.parametrize("violin, carga ,resultado", [
    (ViolinElectronico(1, 2, 'YV2001234', 'blanco', 'Regulable', 3, True, 0), 50, 25),
    (ViolinElectronico(1, 2, 'YV2001234', 'blanco', 'Regulable', 3, True, 80), 50, 100)
]) 
def test_cargar_bateria(violin, carga, resultado):
    assert violin.cargar_bateria(carga) == resultado; 
    
    assertRaises(violin.cargar_bateria(-10))
        
        
    