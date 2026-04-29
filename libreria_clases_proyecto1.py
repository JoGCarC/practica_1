"""
Librería de Clases - Proyecto Python for Analytics
Módulo 1: Python Fundamentals

Contiene clases para manejo de datos con POO
"""

from datetime import datetime
import pandas as pd
import json

# =====================================================
# CLASE PERSONA
# =====================================================

class Persona:
    """Clase para representar una persona con sus datos básicos"""
    
    def __init__(self, nombre, email, telefono='', edad=0, ciudad='', profesion=''):
        self.id = None
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.edad = edad
        self.ciudad = ciudad
        self.profesion = profesion
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.fecha_actualizacion = None
    
    def __str__(self):
        return f"Persona: {self.nombre} ({self.email})"
    
    def __repr__(self):
        return f"Persona(nombre='{self.nombre}', email='{self.email}')"
    
    def to_dict(self):
        """Convierte el objeto a diccionario"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono,
            'edad': self.edad,
            'ciudad': self.ciudad,
            'profesion': self.profesion,
            'fecha_creacion': self.fecha_creacion,
            'fecha_actualizacion': self.fecha_actualizacion
        }
    
    def actualizar(self, **kwargs):
        """Actualiza los atributos de la persona"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.fecha_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def obtener_info_completa(self):
        """Retorna información completa formateada"""
        return f"""
        Información de Persona:
        - ID: {self.id}
        - Nombre: {self.nombre}
        - Email: {self.email}
        - Teléfono: {self.telefono}
        - Edad: {self.edad} años
        - Ciudad: {self.ciudad}
        - Profesión: {self.profesion}
        - Creado: {self.fecha_creacion}
        - Actualizado: {self.fecha_actualizacion or 'Nunca'}
        """

# =====================================================
# CLASE PRODUCTO
# =====================================================

class Producto:
    """Clase para representar un producto"""
    
    contador_id = 1
    
    def __init__(self, nombre, categoria, precio, cantidad=1):
        self.id = Producto.contador_id
        Producto.contador_id += 1
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
        self.fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @property
    def total(self):
        """Calcula el total del producto"""
        return self.precio * self.cantidad
    
    def __str__(self):
        return f"{self.nombre} - {self.categoria} - ${self.precio:.2f} x {self.cantidad} = ${self.total:.2f}"
    
    def to_dict(self):
        """Convierte el producto a diccionario"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'categoria': self.categoria,
            'precio': self.precio,
            'cantidad': self.cantidad,
            'total': self.total,
            'fecha_registro': self.fecha_registro
        }
    
    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del producto"""
        if nuevo_precio > 0:
            self.precio = nuevo_precio
            return True
        return False
    
    def agregar_cantidad(self, cantidad):
        """Agrega cantidad al producto"""
        if cantidad > 0:
            self.cantidad += cantidad
            return True
        return False
    
    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento al precio"""
        if 0 < porcentaje < 100:
            descuento = self.precio * (porcentaje / 100)
            self.precio -= descuento
            return True
        return False

# =====================================================
# CLASE ESTUDIANTE
# =====================================================

class Estudiante(Persona):
    """Clase que hereda de Persona para estudiantes"""
    
    def __init__(self, nombre, email, telefono='', edad=0, ciudad='', 
                 codigo_estudiante='', carrera='', semestre=1):
        super().__init__(nombre, email, telefono, edad, ciudad)
        self.codigo_estudiante = codigo_estudiante
        self.carrera = carrera
        self.semestre = semestre
        self.cursos = []
        self.notas = {}
    
    def inscribir_curso(self, curso):
        """Inscribe al estudiante en un curso"""
        if curso not in self.cursos:
            self.cursos.append(curso)
            return True
        return False
    
    def registrar_nota(self, curso, nota):
        """Registra una nota para un curso"""
        if 0 <= nota <= 20:  # Sistema vigesimal
            self.notas[curso] = nota
            return True
        return False
    
    def calcular_promedio(self):
        """Calcula el promedio de notas"""
        if not self.notas:
            return 0
        return sum(self.notas.values()) / len(self.notas)
    
    def obtener_estado_academico(self):
        """Retorna el estado académico del estudiante"""
        promedio = self.calcular_promedio()
        
        if promedio >= 16:
            estado = "Excelente"
        elif promedio >= 14:
            estado = "Bueno"
        elif promedio >= 11:
            estado = "Regular"
        else:
            estado = "Desaprobado"
        
        return {
            'promedio': round(promedio, 2),
            'estado': estado,
            'cursos_inscritos': len(self.cursos),
            'cursos_evaluados': len(self.notas)
        }
    
    def to_dict(self):
        """Convierte el estudiante a diccionario"""
        datos = super().to_dict()
        datos.update({
            'codigo_estudiante': self.codigo_estudiante,
            'carrera': self.carrera,
            'semestre': self.semestre,
            'cursos': self.cursos,
            'notas': self.notas,
            'promedio': self.calcular_promedio()
        })
        return datos

# =====================================================
# CLASE GESTOR DE REGISTROS (CRUD)
# =====================================================

class GestorRegistros:
    """Clase para gestionar registros con operaciones CRUD"""
    
    def __init__(self):
        self.registros = []
        self.id_counter = 1
    
    def crear(self, registro):
        """Crea un nuevo registro (Create)"""
        registro.id = self.id_counter
        self.id_counter += 1
        self.registros.append(registro)
        return registro
    
    def leer_todos(self):
        """Lee todos los registros (Read)"""
        return self.registros
    
    def leer_por_id(self, id_registro):
        """Lee un registro por ID (Read)"""
        for registro in self.registros:
            if registro.id == id_registro:
                return registro
        return None
    
    def actualizar(self, id_registro, **kwargs):
        """Actualiza un registro (Update)"""
        registro = self.leer_por_id(id_registro)
        if registro:
            registro.actualizar(**kwargs)
            return True
        return False
    
    def eliminar(self, id_registro):
        """Elimina un registro (Delete)"""
        registro = self.leer_por_id(id_registro)
        if registro:
            self.registros.remove(registro)
            return True
        return False
    
    def buscar(self, campo, valor):
        """Busca registros por un campo específico"""
        resultados = []
        for registro in self.registros:
            if hasattr(registro, campo):
                if str(getattr(registro, campo)).lower() == str(valor).lower():
                    resultados.append(registro)
        return resultados
    
    def filtrar(self, condicion):
        """Filtra registros usando una función de condición"""
        return [r for r in self.registros if condicion(r)]
    
    def contar(self):
        """Cuenta el total de registros"""
        return len(self.registros)
    
    def limpiar(self):
        """Elimina todos los registros"""
        self.registros = []
        self.id_counter = 1
    
    def to_dataframe(self):
        """Convierte los registros a DataFrame de Pandas"""
        if not self.registros:
            return pd.DataFrame()
        
        datos = [r.to_dict() for r in self.registros]
        return pd.DataFrame(datos)
    
    def exportar_json(self, archivo):
        """Exporta los registros a un archivo JSON"""
        datos = [r.to_dict() for r in self.registros]
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
    
    def importar_json(self, archivo, clase_objeto):
        """Importa registros desde un archivo JSON"""
        with open(archivo, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        
        for dato in datos:
            # Crear objeto de la clase especificada
            obj = clase_objeto(**dato)
            self.crear(obj)

# =====================================================
# CLASE CUENTA BANCARIA
# =====================================================

class CuentaBancaria:
    """Clase para representar una cuenta bancaria"""
    
    def __init__(self, titular, numero_cuenta, saldo_inicial=0):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial
        self.movimientos = []
        self.fecha_apertura = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def depositar(self, monto, concepto="Depósito"):
        """Realiza un depósito en la cuenta"""
        if monto > 0:
            self.saldo += monto
            self._registrar_movimiento("Depósito", monto, concepto)
            return True
        return False
    
    def retirar(self, monto, concepto="Retiro"):
        """Realiza un retiro de la cuenta"""
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            self._registrar_movimiento("Retiro", monto, concepto)
            return True
        return False
    
    def transferir(self, cuenta_destino, monto, concepto="Transferencia"):
        """Transfiere dinero a otra cuenta"""
        if self.retirar(monto, f"Transferencia a {cuenta_destino.numero_cuenta}"):
            cuenta_destino.depositar(monto, f"Transferencia de {self.numero_cuenta}")
            return True
        return False
    
    def _registrar_movimiento(self, tipo, monto, concepto):
        """Registra un movimiento en el historial"""
        movimiento = {
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'tipo': tipo,
            'monto': monto,
            'concepto': concepto,
            'saldo_resultante': self.saldo
        }
        self.movimientos.append(movimiento)
    
    def obtener_saldo(self):
        """Retorna el saldo actual"""
        return self.saldo
    
    def obtener_movimientos(self):
        """Retorna todos los movimientos"""
        return self.movimientos
    
    def obtener_estado_cuenta(self):
        """Retorna un resumen del estado de cuenta"""
        total_depositos = sum(m['monto'] for m in self.movimientos if m['tipo'] == 'Depósito')
        total_retiros = sum(m['monto'] for m in self.movimientos if m['tipo'] == 'Retiro')
        
        return {
            'titular': self.titular,
            'numero_cuenta': self.numero_cuenta,
            'saldo_actual': self.saldo,
            'total_depositos': total_depositos,
            'total_retiros': total_retiros,
            'cantidad_movimientos': len(self.movimientos),
            'fecha_apertura': self.fecha_apertura
        }

# =====================================================
# CLASE INVENTARIO
# =====================================================

class Inventario:
    """Clase para gestionar un inventario de productos"""
    
    def __init__(self, nombre_inventario):
        self.nombre = nombre_inventario
        self.productos = {}
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def agregar_producto(self, producto):
        """Agrega un producto al inventario"""
        self.productos[producto.id] = producto
        return True
    
    def eliminar_producto(self, producto_id):
        """Elimina un producto del inventario"""
        if producto_id in self.productos:
            del self.productos[producto_id]
            return True
        return False
    
    def buscar_producto(self, producto_id):
        """Busca un producto por ID"""
        return self.productos.get(producto_id)
    
    def actualizar_stock(self, producto_id, nueva_cantidad):
        """Actualiza el stock de un producto"""
        producto = self.buscar_producto(producto_id)
        if producto:
            producto.cantidad = nueva_cantidad
            return True
        return False
    
    def obtener_valor_total(self):
        """Calcula el valor total del inventario"""
        return sum(p.total for p in self.productos.values())
    
    def obtener_productos_por_categoria(self, categoria):
        """Obtiene productos de una categoría específica"""
        return [p for p in self.productos.values() if p.categoria == categoria]
    
    def obtener_productos_bajo_stock(self, minimo=5):
        """Obtiene productos con stock bajo"""
        return [p for p in self.productos.values() if p.cantidad < minimo]
    
    def generar_reporte(self):
        """Genera un reporte del inventario"""
        return {
            'nombre_inventario': self.nombre,
            'total_productos': len(self.productos),
            'valor_total': self.obtener_valor_total(),
            'categorias': len(set(p.categoria for p in self.productos.values())),
            'fecha_creacion': self.fecha_creacion
        }

# =====================================================
# EJEMPLO DE USO
# =====================================================

if __name__ == "__main__":
    print("=== Prueba de Clases ===\n")
    
    # Probar Persona
    persona1 = Persona("Juan Pérez", "juan@email.com", "999888777", 30, "Lima", "Ingeniero")
    print(persona1)
    print(persona1.obtener_info_completa())
    
    # Probar Gestor de Registros
    gestor = GestorRegistros()
    gestor.crear(persona1)
    
    persona2 = Persona("María López", "maria@email.com", "999777666", 25, "Arequipa", "Doctora")
    gestor.crear(persona2)
    
    print(f"\nTotal de registros: {gestor.contar()}")
    print("\nDataFrame de registros:")
    print(gestor.to_dataframe())
    
    # Probar Producto
    print("\n=== Productos ===")
    producto1 = Producto("Laptop HP", "Electrónica", 1200, 5)
    print(producto1)
    
    # Probar Cuenta Bancaria
    print("\n=== Cuenta Bancaria ===")
    cuenta = CuentaBancaria("Juan Pérez", "001-123456", 1000)
    cuenta.depositar(500, "Depósito inicial")
    cuenta.retirar(200, "Compra en tienda")
    print(f"Saldo actual: ${cuenta.obtener_saldo()}")
    print(f"Movimientos: {len(cuenta.obtener_movimientos())}")