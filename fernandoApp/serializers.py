import re
from datetime import date
from rest_framework import serializers
from .models import Paciente


def calcular_dv_rut(cuerpo: str) -> str:
   
    suma = 0
    multiplicador = 2
    for caracter in reversed(str(cuerpo)):
        suma += int(caracter) * multiplicador
        multiplicador = 2 if multiplicador == 7 else multiplicador + 1
    
    resto = suma % 11
    esperado = 11 - resto
    
    if esperado == 11:
        return '0'
    elif esperado == 10:
        return 'K'
    return str(esperado)


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['run', 'nombre', 'apellido', 'email', 'fecha_nacimiento']

    def validate_run(self, value):
    
        valor_limpio = value.strip().upper()
        patron = r'^\d{7,8}-[\dK]$'
        
        if not re.match(patron, valor_limpio):
            raise serializers.ValidationError(
            )
        
        cuerpo, dv_ingresado = valor_limpio.split('-')
        dv_calculado = calcular_dv_rut(cuerpo)
        
        if dv_calculado != dv_ingresado:
            raise serializers.ValidationError(
                f"El dígito verificador es inválido. Para el cuerpo {cuerpo}, el DV correcto es {dv_calculado}."
            )
        
        return valor_limpio

    def validate_fecha_nacimiento(self, value):
        if value > date.today():
            raise serializers.ValidationError("La fecha de nacimiento no puede ser una fecha futura.")
        return value