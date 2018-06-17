from django.core.exceptions import ValidationError
from itertools import cycle

def validar_rut(value):
    rut = value
    opc = 0
    rut = rut.upper()
    rut = rut.replace("-","")
    rut = rut.replace(".","")
    aux = rut[:-1]
    dv = rut[-1:]
    revertido = map(int, reversed(str(aux)))
    factors = cycle(range(2,8))
    s = sum(d * f for d, f in zip(revertido,factors))
    res = (-s)%11
    if str(res) == dv:
        opc = 1
    elif dv=="K" and res==10:
        opc = 1
    else:
        opc = 0

    if opc == 0:
        raise ValidationError('Rut inválido')
    else:
        return rut
