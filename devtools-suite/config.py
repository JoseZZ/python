#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuración centralizada para DevTools Suite
Contiene todas las constantes, colores, fuentes y configuraciones de la aplicación
"""

# =============================================================================
# CONFIGURACIÓN DE LA APLICACIÓN
# =============================================================================

# Información de la aplicación
APP_NAME = "DevTools Suite"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Aplicación de escritorio para desarrolladores inspirada en DevToys"

# Configuración de la ventana principal
WINDOW_CONFIG = {
    'title': APP_NAME,
    'geometry': '1400x900',
    'min_size': (1000, 700),
    'background': '#141419'
}

# =============================================================================
# PALETA DE COLORES GLASSMORFISTA DARK
# =============================================================================

# Colores principales (compatibles con tkinter)
COLORS = {
    # Colores primarios
    'primary': '#00d4ff',           # Cyan brillante para elementos activos
    'primary_hover': '#00b8e6',     # Cyan más oscuro para hover
    'accent': '#00d4ff',            # Color de acento
    
    # Colores de fondo
    'background': '#141419',        # Fondo principal oscuro
    'card_bg': '#282832',           # Fondo de tarjetas
    'card_hover': '#3c3c48',        # Fondo de tarjetas en hover
    'sidebar_bg': '#1e1e23',        # Fondo del sidebar
    'sidebar_hover': '#32323a',     # Fondo del sidebar en hover
    
    # Colores de texto
    'text': '#ffffff',              # Texto principal (blanco)
    'text_secondary': '#b8b8b8',    # Texto secundario (gris claro)
    'text_muted': '#8a8886',        # Texto atenuado (gris)
    
    # Colores de bordes
    'border': '#404040',            # Bordes normales
    'border_hover': '#00d4ff',      # Bordes en hover
    
    # Colores de entrada
    'input_bg': '#3c3c48',          # Fondo de campos de entrada
    'input_fg': '#ffffff',          # Texto de campos de entrada
    
    # Efectos especiales
    'glass_effect': '#2a2a35',      # Efecto de cristal
    'shadow': '#0a0a0a'             # Sombras
}

# =============================================================================
# CONFIGURACIÓN DE FUENTES
# =============================================================================

# Fuentes modernas y claras
FONTS = {
    'title': ('Segoe UI', 24, 'bold'),      # Títulos principales
    'subtitle': ('Segoe UI', 16, 'bold'),   # Subtítulos
    'body': ('Segoe UI', 11),               # Texto del cuerpo
    'body_bold': ('Segoe UI', 11, 'bold'),  # Texto del cuerpo en negrita
    'small': ('Segoe UI', 9),               # Texto pequeño
    'button': ('Segoe UI', 10),             # Botones
    'icon': ('Segoe UI', 32)                # Iconos grandes
}

# =============================================================================
# CONFIGURACIÓN DE HERRAMIENTAS
# =============================================================================

# Categorías de herramientas disponibles
TOOL_CATEGORIES = [
    "Convertidores",
    "Codificadores", 
    "Generadores",
    "Formateadores",
    "Utilidades de Texto"
]

# Configuración de la galería de herramientas
GALLERY_CONFIG = {
    'columns': 3,                   # Número de columnas en la galería
    'card_padding': 15,             # Espaciado entre tarjetas
    'card_size': (280, 200)         # Tamaño de las tarjetas
}

# =============================================================================
# CONFIGURACIÓN DE VENTANAS DE HERRAMIENTAS
# =============================================================================

# Configuración para ventanas de herramientas
TOOL_WINDOW_CONFIG = {
    'geometry': '900x700',
    'min_size': (700, 500),
    'background': COLORS['background']
}

# =============================================================================
# CONFIGURACIÓN DE ESTILOS TTK
# =============================================================================

# Configuración de estilos para widgets TTK
TTK_STYLES = {
    'notebook': {
        'background': COLORS['background'],
        'tab_background': COLORS['card_bg'],
        'tab_foreground': COLORS['text'],
        'tab_padding': [20, 10],
        'selected_background': COLORS['primary'],
        'selected_foreground': 'white'
    }
}
