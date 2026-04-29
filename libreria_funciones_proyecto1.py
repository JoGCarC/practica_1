"""
Librería de Funciones - Proyecto Python for Analytics
Módulo 1: Python Fundamentals

Contiene funciones auxiliares para análisis y cálculos
"""

import numpy as np
import pandas as pd
from datetime import datetime

# =====================================================
# FUNCIONES DE SALUD Y BIENESTAR
# =====================================================

def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC)
    
    Args:
        peso (float): Peso en kilogramos
        altura (float): Altura en metros
        
    Returns:
        dict: Diccionario con IMC y categoría
    """
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso y altura deben ser mayores a cero")
    
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        categoria = "Bajo peso"
        recomendacion = "Consulta con un nutricionista"
    elif imc < 25:
        categoria = "Normal"
        recomendacion = "Mantén un estilo de vida saludable"
    elif imc < 30:
        categoria = "Sobrepeso"
        recomendacion = "Considera mejorar tu alimentación y ejercicio"
    else:
        categoria = "Obesidad"
        recomendacion = "Consulta con un médico especialista"
    
    return {
        'imc': round(imc, 2),
        'categoria': categoria,
        'recomendacion': recomendacion
    }

def calcular_calorias_diarias(peso, altura, edad, sexo, nivel_actividad):
    """
    Calcula las calorías diarias recomendadas usando la fórmula de Harris-Benedict
    
    Args:
        peso (float): Peso en kg
        altura (float): Altura en cm
        edad (int): Edad en años
        sexo (str): 'M' o 'F'
        nivel_actividad (str): sedentario, ligero, moderado, activo, muy_activo
        
    Returns:
        float: Calorías diarias recomendadas
    """
    # Tasa Metabólica Basal (TMB)
    if sexo.upper() == 'M':
        tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)
    else:
        tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)
    
    # Factores de actividad
    factores = {
        'sedentario': 1.2,
        'ligero': 1.375,
        'moderado': 1.55,
        'activo': 1.725,
        'muy_activo': 1.9
    }
    
    factor = factores.get(nivel_actividad.lower(), 1.2)
    calorias = tmb * factor
    
    return round(calorias, 2)

# =====================================================
# FUNCIONES FINANCIERAS
# =====================================================

def calcular_interes_compuesto(capital, tasa_anual, años, frecuencia='anual'):
    """
    Calcula el interés compuesto
    
    Args:
        capital (float): Capital inicial
        tasa_anual (float): Tasa de interés anual (en porcentaje)
        años (int): Número de años
        frecuencia (str): anual, semestral, trimestral, mensual
        
    Returns:
        dict: Monto final, ganancia, tasa efectiva
    """
    frecuencias = {
        'anual': 1,
        'semestral': 2,
        'trimestral': 4,
        'mensual': 12,
        'diario': 365
    }
    
    n = frecuencias.get(frecuencia.lower(), 1)
    r = tasa_anual / 100
    
    monto_final = capital * (1 + r/n) ** (n * años)
    ganancia = monto_final - capital
    tasa_efectiva = ((monto_final / capital) ** (1/años) - 1) * 100
    
    return {
        'monto_final': round(monto_final, 2),
        'ganancia': round(ganancia, 2),
        'tasa_efectiva': round(tasa_efectiva, 2),
        'capital_inicial': capital,
        'años': años
    }

def calcular_prestamo(monto, tasa_anual, meses):
    """
    Calcula la cuota mensual de un préstamo
    
    Args:
        monto (float): Monto del préstamo
        tasa_anual (float): Tasa de interés anual (%)
        meses (int): Plazo en meses
        
    Returns:
        dict: Cuota mensual, total a pagar, intereses totales
    """
    tasa_mensual = (tasa_anual / 100) / 12
    
    if tasa_mensual == 0:
        cuota_mensual = monto / meses
    else:
        cuota_mensual = monto * (tasa_mensual * (1 + tasa_mensual)**meses) / \
                       ((1 + tasa_mensual)**meses - 1)
    
    total_pagar = cuota_mensual * meses
    intereses = total_pagar - monto
    
    return {
        'cuota_mensual': round(cuota_mensual, 2),
        'total_pagar': round(total_pagar, 2),
        'intereses_totales': round(intereses, 2),
        'monto_prestamo': monto,
        'plazo_meses': meses
    }

def calcular_roi(inversion_inicial, inversion_final):
    """
    Calcula el Return on Investment (ROI)
    
    Args:
        inversion_inicial (float): Inversión inicial
        inversion_final (float): Valor final de la inversión
        
    Returns:
        dict: ROI en porcentaje y ganancia/pérdida
    """
    ganancia = inversion_final - inversion_inicial
    roi = (ganancia / inversion_inicial) * 100
    
    return {
        'roi_porcentaje': round(roi, 2),
        'ganancia': round(ganancia, 2),
        'inversion_inicial': inversion_inicial,
        'inversion_final': inversion_final,
        'rentable': roi > 0
    }

# =====================================================
# FUNCIONES DE CONVERSIÓN
# =====================================================

def convertir_temperatura(temperatura, de_unidad, a_unidad):
    """
    Convierte temperatura entre diferentes unidades
    
    Args:
        temperatura (float): Temperatura a convertir
        de_unidad (str): celsius, fahrenheit, kelvin
        a_unidad (str): celsius, fahrenheit, kelvin
        
    Returns:
        float: Temperatura convertida
    """
    # Primero convertir a Celsius
    if de_unidad.lower() == 'fahrenheit':
        celsius = (temperatura - 32) * 5/9
    elif de_unidad.lower() == 'kelvin':
        celsius = temperatura - 273.15
    else:
        celsius = temperatura
    
    # Luego convertir de Celsius a la unidad deseada
    if a_unidad.lower() == 'fahrenheit':
        resultado = (celsius * 9/5) + 32
    elif a_unidad.lower() == 'kelvin':
        resultado = celsius + 273.15
    else:
        resultado = celsius
    
    return round(resultado, 2)

def convertir_moneda(monto, de_moneda, a_moneda, tasas_cambio=None):
    """
    Convierte entre diferentes monedas
    
    Args:
        monto (float): Monto a convertir
        de_moneda (str): Moneda origen (USD, EUR, PEN, etc.)
        a_moneda (str): Moneda destino
        tasas_cambio (dict): Diccionario con tasas de cambio
        
    Returns:
        float: Monto convertido
    """
    # Tasas de cambio por defecto (ejemplo)
    if tasas_cambio is None:
        tasas_cambio = {
            'USD': 1.0,
            'EUR': 0.92,
            'PEN': 3.70,
            'MXN': 17.20,
            'COP': 3950.0,
            'ARS': 350.0
        }
    
    # Convertir primero a USD
    monto_usd = monto / tasas_cambio.get(de_moneda.upper(), 1.0)
    
    # Luego convertir a la moneda destino
    resultado = monto_usd * tasas_cambio.get(a_moneda.upper(), 1.0)
    
    return round(resultado, 2)

# =====================================================
# FUNCIONES DE ANÁLISIS DE DATOS
# =====================================================

def estadisticas_basicas(datos):
    """
    Calcula estadísticas básicas de una lista de datos
    
    Args:
        datos (list): Lista de números
        
    Returns:
        dict: Estadísticas descriptivas
    """
    arr = np.array(datos)
    
    return {
        'media': round(np.mean(arr), 2),
        'mediana': round(np.median(arr), 2),
        'moda': float(pd.Series(datos).mode()[0]) if len(pd.Series(datos).mode()) > 0 else None,
        'desviacion_estandar': round(np.std(arr), 2),
        'varianza': round(np.var(arr), 2),
        'minimo': round(np.min(arr), 2),
        'maximo': round(np.max(arr), 2),
        'rango': round(np.max(arr) - np.min(arr), 2),
        'suma': round(np.sum(arr), 2),
        'cantidad': len(arr)
    }

def calcular_percentiles(datos, percentiles=[25, 50, 75]):
    """
    Calcula percentiles de una lista de datos
    
    Args:
        datos (list): Lista de números
        percentiles (list): Lista de percentiles a calcular
        
    Returns:
        dict: Percentiles calculados
    """
    arr = np.array(datos)
    resultado = {}
    
    for p in percentiles:
        resultado[f'percentil_{p}'] = round(np.percentile(arr, p), 2)
    
    return resultado

# =====================================================
# FUNCIONES DE FECHA Y TIEMPO
# =====================================================

def calcular_edad(fecha_nacimiento):
    """
    Calcula la edad a partir de una fecha de nacimiento
    
    Args:
        fecha_nacimiento (str): Fecha en formato YYYY-MM-DD
        
    Returns:
        int: Edad en años
    """
    nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    hoy = datetime.now()
    
    edad = hoy.year - nacimiento.year
    
    # Ajustar si aún no ha cumplido años este año
    if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
        edad -= 1
    
    return edad

def dias_entre_fechas(fecha1, fecha2):
    """
    Calcula los días entre dos fechas
    
    Args:
        fecha1 (str): Primera fecha (YYYY-MM-DD)
        fecha2 (str): Segunda fecha (YYYY-MM-DD)
        
    Returns:
        int: Número de días de diferencia
    """
    f1 = datetime.strptime(fecha1, '%Y-%m-%d')
    f2 = datetime.strptime(fecha2, '%Y-%m-%d')
    
    diferencia = abs((f2 - f1).days)
    
    return diferencia

# =====================================================
# FUNCIONES DE VALIDACIÓN
# =====================================================

def validar_email(email):
    """
    Valida si un email tiene formato correcto
    
    Args:
        email (str): Email a validar
        
    Returns:
        bool: True si es válido, False si no
    """
    import re
    
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, email))

def validar_telefono_peru(telefono):
    """
    Valida si un teléfono peruano tiene formato correcto
    
    Args:
        telefono (str): Número de teléfono
        
    Returns:
        bool: True si es válido, False si no
    """
    import re
    
    # Formato: 9 dígitos comenzando con 9
    patron = r'^9\d{8}$'
    telefono_limpio = telefono.replace(' ', '').replace('-', '')
    
    return bool(re.match(patron, telefono_limpio))

# =====================================================
# FUNCIONES DE FORMATEO
# =====================================================

def formatear_moneda(monto, moneda='USD'):
    """
    Formatea un monto como moneda
    
    Args:
        monto (float): Monto a formatear
        moneda (str): Símbolo de moneda
        
    Returns:
        str: Monto formateado
    """
    simbolos = {
        'USD': '$',
        'EUR': '€',
        'PEN': 'S/',
        'MXN': '$',
        'COP': '$',
        'ARS': '$'
    }
    
    simbolo = simbolos.get(moneda.upper(), '$')
    
    return f"{simbolo}{monto:,.2f}"

def formatear_porcentaje(numero, decimales=2):
    """
    Formatea un número como porcentaje
    
    Args:
        numero (float): Número a formatear
        decimales (int): Decimales a mostrar
        
    Returns:
        str: Número formateado como porcentaje
    """
    return f"{numero:.{decimales}f}%"

# =====================================================
# FUNCIONES ÚTILES ADICIONALES
# =====================================================

def generar_password_seguro(longitud=12):
    """
    Genera una contraseña segura aleatoria
    
    Args:
        longitud (int): Longitud de la contraseña
        
    Returns:
        str: Contraseña generada
    """
    import random
    import string
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return password

def calcular_descuento(precio_original, porcentaje_descuento):
    """
    Calcula el precio final después de aplicar un descuento
    
    Args:
        precio_original (float): Precio original
        porcentaje_descuento (float): Porcentaje de descuento
        
    Returns:
        dict: Precio final, ahorro, descuento aplicado
    """
    descuento = precio_original * (porcentaje_descuento / 100)
    precio_final = precio_original - descuento
    
    return {
        'precio_original': round(precio_original, 2),
        'descuento': round(descuento, 2),
        'precio_final': round(precio_final, 2),
        'porcentaje_descuento': porcentaje_descuento,
        'ahorro_porcentaje': round((descuento / precio_original) * 100, 2)
    }

# =====================================================
# EJEMPLO DE USO
# =====================================================

if __name__ == "__main__":
    # Probar algunas funciones
    print("=== Prueba de Funciones ===")
    
    # IMC
    imc_resultado = calcular_imc(70, 1.75)
    print(f"\nIMC: {imc_resultado}")
    
    # Inversión
    inversion = calcular_interes_compuesto(10000, 5, 10)
    print(f"\nInversión: {inversion}")
    
    # Temperatura
    temp = convertir_temperatura(25, 'celsius', 'fahrenheit')
    print(f"\n25°C = {temp}°F")
    
    # Estadísticas
    datos = [10, 20, 30, 40, 50]
    stats = estadisticas_basicas(datos)
    print(f"\nEstadísticas: {stats}")