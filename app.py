"""
PROYECTO APLICADO EN STREAMLIT - FUNDAMENTOS DE PROGRAMACIÓN
Especialización en Python for Analytics - Módulo 1

Desarrollado por: Jonatan Gabriel Carbajal Carmen  
Fecha: 29 Abril del 2026
Módulo: Python Fundamentals
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Importar librerías personalizadas (opcionales)
try:
    from libreria_funciones_proyecto1 import *
except ImportError:
    pass
    
try:
    from libreria_clases_proyecto1 import *
except ImportError:
    pass

# ===== CONFIGURACIÓN =====
st.set_page_config(
    page_title="Python Analytics - Proyecto Módulo 1",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== ESTILOS CSS =====
st.markdown("""
<style>
    .main { padding: 2rem; }
    .stButton>button { width: 100%; border-radius: 0.5rem; padding: 0.5rem 1rem; font-weight: 600; }
    .card { background-color: #000040; padding: 1.5rem; border-radius: 0.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin: 1rem 0; }
    .header-section { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 2rem; border-radius: 1rem; margin-bottom: 2rem; text-align: center; }
</style>
""", unsafe_allow_html=True)

# ===== SESSION STATE =====
def init_session_state():
    if 'movimientos' not in st.session_state:
        st.session_state.movimientos = []
    if 'productos_nombres' not in st.session_state:
        st.session_state.productos_nombres = []
    if 'productos_categorias' not in st.session_state:
        st.session_state.productos_categorias = []
    if 'productos_precios' not in st.session_state:
        st.session_state.productos_precios = []
    if 'productos_cantidades' not in st.session_state:
        st.session_state.productos_cantidades = []
    if 'productos_totales' not in st.session_state:
        st.session_state.productos_totales = []
    if 'historico_funciones' not in st.session_state:
        st.session_state.historico_funciones = []
    if 'registros_crud' not in st.session_state:
        st.session_state.registros_crud = []
    if 'id_counter' not in st.session_state:
        st.session_state.id_counter = 1

init_session_state()

# ===== FUNCIONES AUXILIARES =====
def mostrar_footer():
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**📚 Módulo:** Python Fundamentals")
    with col2:
        st.markdown("**🏛️ Institución:** DMC Institute")
    with col3:
        st.markdown("**📅 Año:** 2026")

def limpiar_datos_ejercicio(ejercicio):
    if ejercicio == 1:
        st.session_state.movimientos = []
        st.success("✅ Datos del Ejercicio 1 limpiados")
    elif ejercicio == 2:
        st.session_state.productos_nombres = []
        st.session_state.productos_categorias = []
        st.session_state.productos_precios = []
        st.session_state.productos_cantidades = []
        st.session_state.productos_totales = []
        st.success("✅ Datos del Ejercicio 2 limpiados")
    elif ejercicio == 3:
        st.session_state.historico_funciones = []
        st.success("✅ Histórico del Ejercicio 3 limpiado")
    elif ejercicio == 4:
        st.session_state.registros_crud = []
        st.session_state.id_counter = 1
        st.success("✅ Datos del Ejercicio 4 limpiados")

# ===== HOME =====
def pagina_home():
    st.markdown("""
    <div class="header-section">
        <h1>🐍 Proyecto Aplicado en Streamlit</h1>
        <h2>Python Fundamentals - Módulo 1</h2>
        <p style="font-size: 1.2rem; margin-top: 1rem;">Especialización en Python for Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>👨‍💻 Información del Estudiante</h3>
            <p><strong>Nombre:</strong> Jonatan Gabriel Carbajal Carmen</p>
            <p><strong>Módulo:</strong> Python Fundamentals</p>
            <p><strong>Institución:</strong> DMC Institute</p>
            <p><strong>Fecha:</strong> 29 de Abril del 2026</p>
            <p><strong>Especialización:</strong> Python for Analytics</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("https://www.python.org/static/community_logos/python-logo-master-v3-TM.png", width=250)
    
    st.markdown("## 📖 Descripción del Proyecto")
    st.markdown("""
    <div class="card">
        <p style="font-size: 1.1rem; line-height: 1.6;">
        Este proyecto integra los conceptos fundamentales aprendidos durante el Módulo 1, 
        incluyendo <strong>variables</strong>, <strong>estructuras de datos</strong>, 
        <strong>control de flujo</strong>, <strong>funciones</strong>, 
        <strong>programación funcional</strong> y <strong>programación orientada a objetos (POO)</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## 🛠️ Tecnologías Utilizadas")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="card" style="text-align: center;"><h3>🐍</h3><p><strong>Python</strong></p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card" style="text-align: center;"><h3>🎈</h3><p><strong>Streamlit</strong></p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card" style="text-align: center;"><h3>🐼</h3><p><strong>Pandas</strong></p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="card" style="text-align: center;"><h3>🔢</h3><p><strong>NumPy</strong></p></div>', unsafe_allow_html=True)
    
    st.markdown("## 📋 Estructura de Ejercicios")
    
    ejercicios = [
        {"numero": "1", "titulo": "Flujo de Caja con Listas", "descripcion": "Sistema de registro de movimientos financieros usando listas", "icono": "💰"},
        {"numero": "2", "titulo": "Registro con NumPy y DataFrame", "descripcion": "Registro de productos utilizando arrays de NumPy y conversión a DataFrame", "icono": "📊"},
        {"numero": "3", "titulo": "Uso de Funciones Externas", "descripcion": "Implementación de funciones desde librería externa con histórico de resultados", "icono": "⚙️"},
        {"numero": "4", "titulo": "Clases con CRUD", "descripcion": "Sistema CRUD completo utilizando programación orientada a objetos", "icono": "🗂️"}
    ]
    
    for ej in ejercicios:
        st.markdown(f"""
        <div class="card">
            <h3>{ej['icono']} Ejercicio {ej['numero']}: {ej['titulo']}</h3>
            <p style="font-size: 1rem; color: #666;">{ej['descripcion']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <h3>🚀 ¡Selecciona un ejercicio del menú lateral para comenzar!</h3>
    </div>
    """, unsafe_allow_html=True)
    
    mostrar_footer()

# ===== EJERCICIO 1 =====
def ejercicio_1():
    st.markdown("""
    <div class="header-section">
        <h1>💰 Ejercicio 1: Flujo de Caja con Listas</h1>
        <p>Sistema de registro de movimientos financieros</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ➕ Registrar Nuevo Movimiento")
    
    col1, col2 = st.columns(2)
    
    with col1:
        concepto = st.text_input("💡 Concepto", placeholder="Ej: Venta de productos")
        tipo = st.selectbox("📌 Tipo de Movimiento", ["Ingreso", "Gasto"])
    
    with col2:
        valor = st.number_input("💵 Valor ($)", min_value=0.0, step=0.01, format="%.2f")
        st.markdown("<br>", unsafe_allow_html=True)
        agregar_btn = st.button("➕ Agregar Movimiento", type="primary", use_container_width=True)
    
    if agregar_btn:
        if not concepto:
            st.error("❌ Por favor ingresa un concepto")
        elif valor <= 0:
            st.error("❌ El valor debe ser mayor a cero")
        else:
            movimiento = {
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "concepto": concepto,
                "tipo": tipo,
                "valor": valor
            }
            st.session_state.movimientos.append(movimiento)
            st.success(f"✅ Movimiento agregado: {concepto} - ${valor:,.2f}")
            st.rerun()
    
    st.markdown("---")
    
    if st.session_state.movimientos:
        st.markdown("### 📊 Movimientos Registrados")
        
        df_movimientos = pd.DataFrame(st.session_state.movimientos)
        df_display = df_movimientos.copy()
        df_display['valor'] = df_display['valor'].apply(lambda x: f"${x:,.2f}")
        
        st.dataframe(df_display, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        st.markdown("### 💰 Resumen Financiero")
        
        total_ingresos = sum([m['valor'] for m in st.session_state.movimientos if m['tipo'] == 'Ingreso'])
        total_gastos = sum([m['valor'] for m in st.session_state.movimientos if m['tipo'] == 'Gasto'])
        saldo_final = total_ingresos - total_gastos
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("📈 Total Ingresos", f"${total_ingresos:,.2f}")
        with col2:
            st.metric("📉 Total Gastos", f"${total_gastos:,.2f}")
        with col3:
            st.metric("💼 Saldo Final", f"${saldo_final:,.2f}")
        
        if saldo_final >= 0:
            st.success(f"✅ El flujo de caja está **A FAVOR** con un saldo de ${saldo_final:,.2f}")
        else:
            st.error(f"❌ El flujo de caja está **EN CONTRA** con un déficit de ${abs(saldo_final):,.2f}")
        
        st.markdown("### 📊 Visualización")
        
        fig = go.Figure(data=[
            go.Bar(name='Ingresos', x=['Ingresos'], y=[total_ingresos], marker_color='#28a745'),
            go.Bar(name='Gastos', x=['Gastos'], y=[total_gastos], marker_color='#dc3545')
        ])
        
        fig.update_layout(title="Comparación Ingresos vs Gastos", yaxis_title="Monto ($)", template="plotly_white", height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        if st.button("🗑️ Limpiar Todos los Movimientos", use_container_width=True):
            limpiar_datos_ejercicio(1)
            st.rerun()
    else:
        st.info("ℹ️ No hay movimientos registrados. Agrega tu primer movimiento.")
    
    mostrar_footer()

# ===== EJERCICIO 2 =====
def ejercicio_2():
    st.markdown("""
    <div class="header-section">
        <h1>📊 Ejercicio 2: Registro con NumPy y DataFrame</h1>
        <p>Sistema de registro de productos usando arrays</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📦 Registrar Nuevo Producto")
    
    col1, col2 = st.columns(2)
    
    with col1:
        nombre_producto = st.text_input("🏷️ Nombre del Producto", placeholder="Ej: Laptop HP")
        categoria = st.selectbox("📁 Categoría", ["Electrónica", "Alimentos", "Ropa", "Hogar", "Deportes", "Libros", "Otros"])
        precio = st.number_input("💰 Precio Unitario ($)", min_value=0.0, step=0.01, format="%.2f")
    
    with col2:
        cantidad = st.number_input("📦 Cantidad", min_value=1, step=1)
        total = precio * cantidad
        st.metric("💵 Total", f"${total:,.2f}")
        agregar_producto_btn = st.button("➕ Agregar Producto", type="primary", use_container_width=True)
    
    if agregar_producto_btn:
        if not nombre_producto:
            st.error("❌ Por favor ingresa un nombre para el producto")
        elif precio <= 0:
            st.error("❌ El precio debe ser mayor a cero")
        else:
            st.session_state.productos_nombres.append(nombre_producto)
            st.session_state.productos_categorias.append(categoria)
            st.session_state.productos_precios.append(precio)
            st.session_state.productos_cantidades.append(cantidad)
            st.session_state.productos_totales.append(total)
            
            st.success(f"✅ Producto agregado: {nombre_producto} - {cantidad} unidades - ${total:,.2f}")
            st.rerun()
    
    st.markdown("---")
    
    if st.session_state.productos_nombres:
        st.markdown("### 📋 Productos Registrados")
        
        arr_nombres = np.array(st.session_state.productos_nombres)
        arr_categorias = np.array(st.session_state.productos_categorias)
        arr_precios = np.array(st.session_state.productos_precios)
        arr_cantidades = np.array(st.session_state.productos_cantidades)
        arr_totales = np.array(st.session_state.productos_totales)
        
        df_productos = pd.DataFrame({
            'Producto': arr_nombres,
            'Categoría': arr_categorias,
            'Precio Unitario': arr_precios,
            'Cantidad': arr_cantidades,
            'Total': arr_totales
        })
        
        st.dataframe(df_productos, use_container_width=True, hide_index=False)
        
        st.markdown("---")
        st.markdown("### 📈 Estadísticas (NumPy)")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("📦 Total Productos", len(arr_nombres))
        with col2:
            st.metric("💰 Total Ventas", f"${np.sum(arr_totales):,.2f}")
        with col3:
            st.metric("📊 Precio Máximo", f"${np.max(arr_precios):,.2f}")
        with col4:
            st.metric("🔢 Cantidad Total", int(np.sum(arr_cantidades)))
        
        if st.button("🗑️ Limpiar Todos los Productos", use_container_width=True):
            limpiar_datos_ejercicio(2)
            st.rerun()
    else:
        st.info("ℹ️ No hay productos registrados. Agrega tu primer producto.")
    
    mostrar_footer()

# ===== EJERCICIO 3 =====
def ejercicio_3():
    st.markdown("""
    <div class="header-section">
        <h1>⚙️ Ejercicio 3: Funciones desde Librería Externa</h1>
        <p>Implementación de funciones especializadas con histórico</p>
    </div>
    """, unsafe_allow_html=True)
    
    funciones_disponibles = {
        "Calcular IMC": {"descripcion": "Calcula el Índice de Masa Corporal"},
        "Conversión de Temperatura": {"descripcion": "Convierte temperatura entre Celsius y Fahrenheit"},
        "Cálculo de Descuento": {"descripcion": "Calcula el precio final con descuento"},
        "Análisis de Inversión": {"descripcion": "Calcula el retorno de inversión"}
    }
    
    st.markdown("### 🔧 Seleccionar Función")
    
    funcion_seleccionada = st.selectbox("📌 Función a Ejecutar", list(funciones_disponibles.keys()))
    st.info(f"ℹ️ {funciones_disponibles[funcion_seleccionada]['descripcion']}")
    
    st.markdown("### 📥 Ingresar Parámetros")
    
    parametros_valores = {}
    
    if funcion_seleccionada == "Calcular IMC":
        col1, col2 = st.columns(2)
        with col1:
            parametros_valores['peso'] = st.number_input("⚖️ Peso (kg)", min_value=0.0, step=0.1)
        with col2:
            parametros_valores['altura'] = st.number_input("📏 Altura (m)", min_value=0.0, step=0.01)
    
    elif funcion_seleccionada == "Conversión de Temperatura":
        col1, col2, col3 = st.columns(3)
        with col1:
            parametros_valores['temperatura'] = st.number_input("🌡️ Temperatura", step=0.1)
        with col2:
            parametros_valores['de'] = st.selectbox("De", ["Celsius", "Fahrenheit"])
        with col3:
            parametros_valores['a'] = st.selectbox("A", ["Fahrenheit", "Celsius"])
    
    elif funcion_seleccionada == "Cálculo de Descuento":
        col1, col2 = st.columns(2)
        with col1:
            parametros_valores['precio'] = st.number_input("💰 Precio Original ($)", min_value=0.0, step=0.01)
        with col2:
            parametros_valores['descuento'] = st.number_input("🎯 Descuento (%)", min_value=0.0, max_value=100.0, step=1.0)
    
    elif funcion_seleccionada == "Análisis de Inversión":
        col1, col2, col3 = st.columns(3)
        with col1:
            parametros_valores['capital'] = st.number_input("💵 Capital Inicial ($)", min_value=0.0, step=100.0)
        with col2:
            parametros_valores['tasa'] = st.number_input("📈 Tasa Anual (%)", min_value=0.0, step=0.1)
        with col3:
            parametros_valores['años'] = st.number_input("📅 Años", min_value=1, step=1)
    
    ejecutar_btn = st.button("▶️ Ejecutar Función", type="primary", use_container_width=True)
    
    if ejecutar_btn:
        try:
            resultado = None
            
            if funcion_seleccionada == "Calcular IMC":
                if parametros_valores['peso'] > 0 and parametros_valores['altura'] > 0:
                    imc = parametros_valores['peso'] / (parametros_valores['altura'] ** 2)
                    categoria = "Bajo peso" if imc < 18.5 else "Normal" if imc < 25 else "Sobrepeso" if imc < 30 else "Obesidad"
                    resultado = f"IMC: {imc:.2f} - Categoría: {categoria}"
                else:
                    st.error("❌ Peso y altura deben ser mayores a cero")
            
            elif funcion_seleccionada == "Conversión de Temperatura":
                temp = parametros_valores['temperatura']
                if parametros_valores['de'] == "Celsius" and parametros_valores['a'] == "Fahrenheit":
                    convertida = (temp * 9/5) + 32
                    resultado = f"{temp}°C = {convertida:.2f}°F"
                elif parametros_valores['de'] == "Fahrenheit" and parametros_valores['a'] == "Celsius":
                    convertida = (temp - 32) * 5/9
                    resultado = f"{temp}°F = {convertida:.2f}°C"
                else:
                    resultado = f"Sin conversión necesaria: {temp}°"
            
            elif funcion_seleccionada == "Cálculo de Descuento":
                precio = parametros_valores['precio']
                descuento = parametros_valores['descuento']
                precio_final = precio * (1 - descuento/100)
                ahorro = precio - precio_final
                resultado = f"Precio Final: ${precio_final:.2f} (Ahorro: ${ahorro:.2f})"
            
            elif funcion_seleccionada == "Análisis de Inversión":
                capital = parametros_valores['capital']
                tasa = parametros_valores['tasa'] / 100
                años = parametros_valores['años']
                monto_final = capital * ((1 + tasa) ** años)
                ganancia = monto_final - capital
                resultado = f"Monto Final: ${monto_final:,.2f} (Ganancia: ${ganancia:,.2f})"
            
            if resultado:
                registro = {
                    'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'funcion': funcion_seleccionada,
                    'parametros': str(parametros_valores),
                    'resultado': resultado
                }
                st.session_state.historico_funciones.append(registro)
                
                st.success(f"✅ {resultado}")
                st.rerun()
        
        except Exception as e:
            st.error(f"❌ Error al ejecutar la función: {str(e)}")
    
    st.markdown("---")
    
    if st.session_state.historico_funciones:
        st.markdown("### 📜 Histórico de Resultados")
        
        df_historico = pd.DataFrame(st.session_state.historico_funciones)
        st.dataframe(df_historico, use_container_width=True, hide_index=False)
        
        if st.button("🗑️ Limpiar Histórico", use_container_width=True):
            limpiar_datos_ejercicio(3)
            st.rerun()
    else:
        st.info("ℹ️ No hay resultados en el histórico. Ejecuta una función para comenzar.")
    
    mostrar_footer()

# ===== EJERCICIO 4 =====
def ejercicio_4():
    st.markdown("""
    <div class="header-section">
        <h1>🗂️ Ejercicio 4: Clases con CRUD</h1>
        <p>Sistema completo de Create, Read, Update, Delete</p>
    </div>
    """, unsafe_allow_html=True)
    
    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(["➕ Crear", "📖 Leer", "✏️ Actualizar", "🗑️ Eliminar"])
    
    with tab_crear:
        st.markdown("### ➕ Crear Nuevo Registro")
        
        col1, col2 = st.columns(2)
        
        with col1:
            nombre = st.text_input("👤 Nombre", key="crear_nombre")
            email = st.text_input("📧 Email", key="crear_email")
            telefono = st.text_input("📞 Teléfono", key="crear_telefono")
        
        with col2:
            edad = st.number_input("🎂 Edad", min_value=1, max_value=120, key="crear_edad")
            ciudad = st.text_input("🏙️ Ciudad", key="crear_ciudad")
            profesion = st.text_input("💼 Profesión", key="crear_profesion")
        
        if st.button("➕ Crear Registro", type="primary", use_container_width=True, key="btn_crear"):
            if not nombre or not email:
                st.error("❌ Nombre y email son obligatorios")
            else:
                registro = {
                    'id': st.session_state.id_counter,
                    'nombre': nombre,
                    'email': email,
                    'telefono': telefono,
                    'edad': edad,
                    'ciudad': ciudad,
                    'profesion': profesion,
                    'fecha_creacion': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                st.session_state.registros_crud.append(registro)
                st.session_state.id_counter += 1
                
                st.success(f"✅ Registro creado exitosamente con ID: {registro['id']}")               
                st.rerun()
    
    with tab_leer:
        st.markdown("### 📖 Ver Registros")
        
        if st.session_state.registros_crud:
            df_registros = pd.DataFrame(st.session_state.registros_crud)
            st.dataframe(df_registros, use_container_width=True, hide_index=False)
            
            st.markdown("---")
            st.markdown("### 📊 Estadísticas")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("👥 Total Registros", len(st.session_state.registros_crud))
            with col2:
                edad_promedio = sum([r['edad'] for r in st.session_state.registros_crud]) / len(st.session_state.registros_crud)
                st.metric("📊 Edad Promedio", f"{edad_promedio:.1f} años")
            with col3:
                ciudades_unicas = len(set([r['ciudad'] for r in st.session_state.registros_crud if r['ciudad']]))
                st.metric("🏙️ Ciudades", ciudades_unicas)
        else:
            st.info("ℹ️ No hay registros creados. Crea tu primer registro en la pestaña 'Crear'")
    
    with tab_actualizar:
        st.markdown("### ✏️ Actualizar Registro")
        
        if st.session_state.registros_crud:
            ids_disponibles = [r['id'] for r in st.session_state.registros_crud]
            nombres_registros = {r['id']: f"ID {r['id']} - {r['nombre']}" for r in st.session_state.registros_crud}
            
            id_actualizar = st.selectbox(
                "📌 Seleccionar registro a actualizar",
                ids_disponibles,
                format_func=lambda x: nombres_registros[x],
                key="select_actualizar"
            )
            
            registro_actual = next((r for r in st.session_state.registros_crud if r['id'] == id_actualizar), None)
            
            if registro_actual:
                col1, col2 = st.columns(2)
                
                with col1:
                    nuevo_nombre = st.text_input("👤 Nombre", value=registro_actual['nombre'], key="actualizar_nombre")
                    nuevo_email = st.text_input("📧 Email", value=registro_actual['email'], key="actualizar_email")
                    nuevo_telefono = st.text_input("📞 Teléfono", value=registro_actual['telefono'], key="actualizar_telefono")
                
                with col2:
                    nueva_edad = st.number_input("🎂 Edad", min_value=1, max_value=120, value=registro_actual['edad'], key="actualizar_edad")
                    nueva_ciudad = st.text_input("🏙️ Ciudad", value=registro_actual['ciudad'], key="actualizar_ciudad")
                    nueva_profesion = st.text_input("💼 Profesión", value=registro_actual['profesion'], key="actualizar_profesion")
                
                if st.button("💾 Guardar Cambios", type="primary", use_container_width=True, key="btn_actualizar"):
                    if not nuevo_nombre or not nuevo_email:
                        st.error("❌ Nombre y email son obligatorios")
                    else:
                        for r in st.session_state.registros_crud:
                            if r['id'] == id_actualizar:
                                r['nombre'] = nuevo_nombre
                                r['email'] = nuevo_email
                                r['telefono'] = nuevo_telefono
                                r['edad'] = nueva_edad
                                r['ciudad'] = nueva_ciudad
                                r['profesion'] = nueva_profesion
                                r['fecha_actualizacion'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                break
                        
                        st.success(f"✅ Registro ID {id_actualizar} actualizado exitosamente")
                        st.rerun()
        else:
            st.info("ℹ️ No hay registros para actualizar")
    
    with tab_eliminar:
        st.markdown("### 🗑️ Eliminar Registro")
        
        if st.session_state.registros_crud:
            st.warning("⚠️ **Advertencia:** Esta acción no se puede deshacer")
            
            ids_disponibles = [r['id'] for r in st.session_state.registros_crud]
            nombres_registros = {r['id']: f"ID {r['id']} - {r['nombre']}" for r in st.session_state.registros_crud}
            
            id_eliminar = st.selectbox(
                "📌 Seleccionar registro a eliminar",
                ids_disponibles,
                format_func=lambda x: nombres_registros[x],
                key="select_eliminar"
            )
            
            registro_eliminar = next((r for r in st.session_state.registros_crud if r['id'] == id_eliminar), None)
            
            if registro_eliminar:
                st.markdown("#### 📋 Información del Registro")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.text_input("👤 Nombre", value=registro_eliminar['nombre'], disabled=True)
                    st.text_input("📧 Email", value=registro_eliminar['email'], disabled=True)
                
                with col2:
                    st.number_input("🎂 Edad", value=registro_eliminar['edad'], disabled=True)
                    st.text_input("🏙️ Ciudad", value=registro_eliminar['ciudad'], disabled=True)
                
                confirmar = st.checkbox("⚠️ Confirmo que deseo eliminar este registro", key="confirmar_eliminar")
                
                if st.button("🗑️ Eliminar Registro", type="primary", disabled=not confirmar, use_container_width=True, key="btn_eliminar"):
                    st.session_state.registros_crud = [r for r in st.session_state.registros_crud if r['id'] != id_eliminar]
                    st.success(f"✅ Registro ID {id_eliminar} eliminado exitosamente")
                    st.rerun()
        else:
            st.info("ℹ️ No hay registros para eliminar")
    
    st.markdown("---")
    
    if st.session_state.registros_crud:
        if st.button("🗑️ Limpiar Todos los Registros", use_container_width=True):
            limpiar_datos_ejercicio(4)
            st.rerun()
    
    mostrar_footer()

# ===== MAIN =====
def main():
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h1 style="color: #667eea;">🐍 Python Analytics</h1>
        <p style="color: #666;">Módulo 1 - Fundamentals</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    
    pagina = st.sidebar.selectbox(
        "📍 Navegación",
        ["🏠 Home", "💰 Ejercicio 1", "📊 Ejercicio 2", "⚙️ Ejercicio 3", "🗂️ Ejercicio 4"],
        index=0
    )
    
    st.sidebar.markdown("---")
    
    st.sidebar.markdown("### 📖 Información")
    st.sidebar.markdown("""
    **Contenido:**
    - Estructuras de datos
    - Control de flujo
    - Funciones
    - POO (Clases)
    - NumPy & Pandas
    """)
    
    if pagina == "🏠 Home":
        pagina_home()
    elif pagina == "💰 Ejercicio 1":
        ejercicio_1()
    elif pagina == "📊 Ejercicio 2":
        ejercicio_2()
    elif pagina == "⚙️ Ejercicio 3":
        ejercicio_3()
    elif pagina == "🗂️ Ejercicio 4":
        ejercicio_4()

if __name__ == "__main__":
    main()