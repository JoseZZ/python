#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DevTools Suite - Aplicación de escritorio para desarrolladores
Inspirada en DevToys, proporciona herramientas útiles para desarrolladores

Autor: DevTools Suite Team
Versión: 1.0.0
"""

# =============================================================================
# IMPORTS
# =============================================================================

import tkinter as tk
from tkinter import ttk, messagebox
import json
from typing import Dict, List, Any
import os
import sys

# Importar configuración centralizada
from config import (
    APP_NAME, WINDOW_CONFIG, COLORS, FONTS, 
    TOOL_CATEGORIES, GALLERY_CONFIG, TOOL_WINDOW_CONFIG
)

# Importar módulos de herramientas
from tools.converters import ConvertersTool
from tools.encoders import EncodersTool
from tools.generators import GeneratorsTool
from tools.formatters import FormattersTool
from tools.text_utils import TextUtilsTool


# =============================================================================
# CLASE PRINCIPAL DE LA APLICACIÓN
# =============================================================================

class DevToolsSuite:
    """
    Clase principal de la aplicación DevTools Suite.
    
    Esta clase maneja la ventana principal, la navegación entre categorías
    y la gestión de las herramientas disponibles.
    
    Atributos:
        root (tk.Tk): Ventana principal de la aplicación
        colors (dict): Paleta de colores de la aplicación
        fonts (dict): Configuración de fuentes
        current_category (tk.StringVar): Categoría actualmente seleccionada
        tools (dict): Diccionario con todas las herramientas disponibles
        category_buttons (dict): Botones de categorías del sidebar
        category_title (tk.Label): Título de la categoría actual
        tools_frame (tk.Frame): Frame contenedor de la galería de herramientas
        canvas (tk.Canvas): Canvas para scroll de la galería
        scrollable_frame (tk.Frame): Frame scrolleable con las tarjetas
    """
    
    def __init__(self):
        """
        Inicializa la aplicación DevTools Suite.
        
        Configura la ventana principal, estilos, variables y crea la interfaz.
        """
        # Configurar ventana principal
        self._setup_main_window()
        
        # Configurar estilos y colores
        self._setup_styles()
        
        # Inicializar variables de la aplicación
        self._initialize_variables()
        
        # Crear la interfaz de usuario
        self.create_interface()
        
        # Cargar herramientas disponibles
        self.load_tools()
        
        # Configurar categoría inicial
        self._set_initial_category()
    
    def _setup_main_window(self):
        """
        Configura la ventana principal de la aplicación.
        Método privado que maneja la configuración inicial de la ventana.
        """
        self.root = tk.Tk()
        self.root.title(WINDOW_CONFIG['title'])
        self.root.geometry(WINDOW_CONFIG['geometry'])
        self.root.minsize(*WINDOW_CONFIG['min_size'])
        self.root.configure(bg=WINDOW_CONFIG['background'])
        
        # Configurar transparencia de la ventana (si es compatible)
        try:
            self.root.attributes('-alpha', 0.95)
        except:
            pass
    
    def _setup_styles(self):
        """
        Configura los estilos de la aplicación.
        Método privado que inicializa colores, fuentes y estilos TTK.
        """
        # Usar colores y fuentes de la configuración centralizada
        self.colors = COLORS
        self.fonts = FONTS
        
        # Configurar estilos TTK
        self._configure_ttk_styles()
    
    def _configure_ttk_styles(self):
        """
        Configura los estilos para widgets TTK.
        Método privado que personaliza la apariencia de los widgets TTK.
        """
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar estilos de botones de categoría
        style.configure('Category.TButton',
                       background=self.colors['sidebar_bg'],
                       foreground=self.colors['text'],
                       borderwidth=0,
                       focuscolor='none',
                       padding=(15, 12),
                       font=self.fonts['button'])
        
        style.map('Category.TButton',
                 background=[('active', self.colors['sidebar_hover']),
                           ('pressed', self.colors['primary'])],
                 foreground=[('active', self.colors['text']),
                           ('pressed', 'white')])
        
        # Configurar estilo de tarjetas
        style.configure('Card.TFrame',
                       background=self.colors['card_bg'],
                       relief='flat',
                       borderwidth=1)
        
        # Configurar estilo para tarjetas hover
        style.configure('CardHover.TFrame',
                       background=self.colors['card_hover'],
                       relief='flat',
                       borderwidth=1)
    
    def _initialize_variables(self):
        """
        Inicializa las variables de la aplicación.
        Método privado que configura las variables de estado.
        """
        self.current_category = tk.StringVar()
        self.tools = {}
        self.category_buttons = {}
    
    def _set_initial_category(self):
        """
        Establece la categoría inicial de la aplicación.
        Método privado que configura la primera categoría a mostrar.
        """
        self.current_category.set("Convertidores")
        self.show_category_tools("Convertidores")
    
    # =========================================================================
    # MÉTODOS DE INTERFAZ DE USUARIO
    # =========================================================================
    
    def create_interface(self):
        """
        Crea la interfaz principal de la aplicación.
        
        Organiza la interfaz en dos paneles principales:
        - Panel lateral izquierdo: Navegación por categorías
        - Panel principal derecho: Galería de herramientas
        """
        # Frame principal con fondo glassmorfista
        main_frame = tk.Frame(self.root, bg=self.colors['background'])
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Crear panel lateral de navegación
        self._create_sidebar(main_frame)
        
        # Crear panel principal con galería
        self._create_main_panel(main_frame)
    
    def _create_sidebar(self, parent):
        """
        Crea el panel lateral de navegación.
        
        Args:
            parent: Widget padre para el sidebar
        """
        # Frame del sidebar con ancho fijo
        sidebar_frame = tk.Frame(parent, bg=self.colors['sidebar_bg'], width=250)
        sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
        sidebar_frame.pack_propagate(False)
        
        # Título de la aplicación
        self._create_sidebar_title(sidebar_frame)
        
        # Botones de navegación por categorías
        self._create_category_buttons(sidebar_frame)
    
    def _create_sidebar_title(self, parent):
        """
        Crea el título del sidebar.
        
        Args:
            parent: Widget padre para el título
        """
        title_label = tk.Label(parent, text=APP_NAME, 
                              font=self.fonts['subtitle'],
                              fg=self.colors['primary'],
                              bg=self.colors['sidebar_bg'])
        title_label.pack(pady=(20, 30))
    
    def _create_category_buttons(self, parent):
        """
        Crea los botones de navegación por categorías.
        
        Args:
            parent: Widget padre para los botones
        """
        for category in TOOL_CATEGORIES:
            btn = tk.Button(parent, 
                           text=category,
                           font=self.fonts['button'],
                           fg=self.colors['text'],
                           bg=self.colors['sidebar_bg'],
                           activebackground=self.colors['sidebar_hover'],
                           activeforeground=self.colors['text'],
                           relief='flat',
                           bd=0,
                           padx=20,
                           pady=12,
                           anchor='w',
                           command=lambda c=category: self.show_category_tools(c))
            btn.pack(fill=tk.X, pady=1)
            self.category_buttons[category] = btn
            
            # Agregar efectos hover
            self._add_button_hover_effects(btn)
    
    def _add_button_hover_effects(self, button):
        """
        Agrega efectos hover a un botón.
        
        Args:
            button: Botón al que agregar efectos
        """
        def on_enter(event):
            button.config(bg=self.colors['sidebar_hover'])
        
        def on_leave(event):
            button.config(bg=self.colors['sidebar_bg'])
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def _create_main_panel(self, parent):
        """
        Crea el panel principal con la galería de herramientas.
        
        Args:
            parent: Widget padre para el panel principal
        """
        # Frame principal con padding
        main_panel = tk.Frame(parent, bg=self.colors['background'])
        main_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(20, 20), pady=20)
        
        # Título de la categoría actual
        self._create_category_title(main_panel)
        
        # Frame para la galería de herramientas
        self.tools_frame = tk.Frame(main_panel, bg=self.colors['background'])
        self.tools_frame.pack(fill=tk.BOTH, expand=True)
        
        # Crear galería con scroll
        self._create_tools_gallery()
    
    def _create_category_title(self, parent):
        """
        Crea el título de la categoría actual.
        
        Args:
            parent: Widget padre para el título
        """
        self.category_title = tk.Label(parent, 
                                      text="Convertidores",
                                      font=self.fonts['title'],
                                      fg=self.colors['text'],
                                      bg=self.colors['background'])
        self.category_title.pack(pady=(0, 30), anchor='w')
    
    def _create_tools_gallery(self):
        """
        Crea la galería de herramientas con funcionalidad de scroll.
        """
        # Canvas para scroll
        self.canvas = tk.Canvas(self.tools_frame, 
                               bg=self.colors['background'],
                               highlightthickness=0,
                               bd=0)
        
        # Scrollbar personalizada
        scrollbar = tk.Scrollbar(self.tools_frame, orient="vertical", 
                                command=self.canvas.yview,
                                bg=self.colors['background'],
                                troughcolor=self.colors['card_bg'],
                                activebackground=self.colors['primary'])
        
        # Frame scrolleable
        self.scrollable_frame = tk.Frame(self.canvas, bg=self.colors['background'])
        
        # Configurar scroll
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Posicionar canvas y scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Agregar scroll con rueda del mouse
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
    
    def _on_mousewheel(self, event):
        """
        Maneja el scroll del mouse en la galería.
        
        Args:
            event: Evento del mouse
        """
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    # =========================================================================
    # MÉTODOS DE GESTIÓN DE HERRAMIENTAS
    # =========================================================================
    
    def load_tools(self):
        """
        Carga todas las herramientas disponibles en la aplicación.
        
        Organiza las herramientas por categorías para facilitar la navegación.
        """
        self.tools = {
            "Convertidores": [
                {
                    "name": "JSON ↔ YAML",
                    "description": "Convierte entre formatos JSON y YAML",
                    "icon": "🔄",
                    "tool_class": ConvertersTool
                },
                {
                    "name": "Base64 Texto",
                    "description": "Codifica y decodifica texto en Base64",
                    "icon": "🔤",
                    "tool_class": ConvertersTool
                },
                {
                    "name": "Conversión de Números",
                    "description": "Convierte entre diferentes bases numéricas",
                    "icon": "🔢",
                    "tool_class": ConvertersTool
                }
            ],
            "Codificadores": [
                {
                    "name": "JWT Decoder",
                    "description": "Decodifica y valida tokens JWT",
                    "icon": "🔐",
                    "tool_class": EncodersTool
                },
                {
                    "name": "URL Encoder/Decoder",
                    "description": "Codifica y decodifica URLs",
                    "icon": "🌐",
                    "tool_class": EncodersTool
                },
                {
                    "name": "HTML Encoder/Decoder",
                    "description": "Codifica y decodifica entidades HTML",
                    "icon": "📄",
                    "tool_class": EncodersTool
                }
            ],
            "Generadores": [
                {
                    "name": "Generador de Contraseñas",
                    "description": "Genera contraseñas seguras",
                    "icon": "🔑",
                    "tool_class": GeneratorsTool
                },
                {
                    "name": "Generador de UUID",
                    "description": "Genera identificadores únicos universales",
                    "icon": "🆔",
                    "tool_class": GeneratorsTool
                },
                {
                    "name": "Generador de Hash",
                    "description": "Genera hashes MD5, SHA1, SHA256",
                    "icon": "🔒",
                    "tool_class": GeneratorsTool
                }
            ],
            "Formateadores": [
                {
                    "name": "Formateador JSON",
                    "description": "Formatea y valida JSON",
                    "icon": "📋",
                    "tool_class": FormattersTool
                },
                {
                    "name": "Formateador SQL",
                    "description": "Formatea consultas SQL",
                    "icon": "🗃️",
                    "tool_class": FormattersTool
                },
                {
                    "name": "Formateador XML",
                    "description": "Formatea documentos XML",
                    "icon": "📄",
                    "tool_class": FormattersTool
                }
            ],
            "Utilidades de Texto": [
                {
                    "name": "Comparador de Texto",
                    "description": "Compara dos textos y muestra diferencias",
                    "icon": "📊",
                    "tool_class": TextUtilsTool
                },
                {
                    "name": "Escape/Unescape",
                    "description": "Escapa y desescapa caracteres especiales",
                    "icon": "🔧",
                    "tool_class": TextUtilsTool
                },
                {
                    "name": "Analizador de Texto",
                    "description": "Analiza estadísticas del texto",
                    "icon": "📈",
                    "tool_class": TextUtilsTool
                }
            ]
        }
    
    def show_category_tools(self, category):
        """
        Muestra las herramientas de una categoría específica.
        
        Args:
            category (str): Nombre de la categoría a mostrar
        """
        # Actualizar título de la categoría
        self.category_title.config(text=category)
        
        # Limpiar galería actual
        self._clear_gallery()
        
        # Obtener herramientas de la categoría
        category_tools = self.tools.get(category, [])
        
        # Crear tarjetas de herramientas en grid
        self._create_tool_cards(category_tools)
        
        # Actualizar scroll
        self._update_gallery_scroll()
    
    def _clear_gallery(self):
        """
        Limpia la galería de herramientas actual.
        Método privado que elimina todas las tarjetas existentes.
        """
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
    
    def _create_tool_cards(self, tools):
        """
        Crea las tarjetas de herramientas en un grid.
        
        Args:
            tools (list): Lista de herramientas a mostrar
        """
        cols = GALLERY_CONFIG['columns']
        for i, tool in enumerate(tools):
            row = i // cols
            col = i % cols
            self._create_tool_card(tool, row, col)
    
    def _update_gallery_scroll(self):
        """
        Actualiza el scroll de la galería.
        Método privado que recalcula el área de scroll.
        """
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def _create_tool_card(self, tool, row, col):
        """
        Crea una tarjeta moderna para una herramienta.
        
        Args:
            tool (dict): Información de la herramienta
            row (int): Fila en el grid
            col (int): Columna en el grid
        """
        # Frame principal de la tarjeta
        card_frame = tk.Frame(self.scrollable_frame, 
                             bg=self.colors['card_bg'],
                             relief='flat',
                             bd=0,
                             highlightbackground=self.colors['border'],
                             highlightthickness=1)
        
        # Posicionar en grid
        card_frame.grid(row=row, column=col, 
                       padx=GALLERY_CONFIG['card_padding'], 
                       pady=GALLERY_CONFIG['card_padding'], 
                       sticky='nsew')
        
        # Configurar grid del frame principal
        self.scrollable_frame.grid_columnconfigure(col, weight=1)
        
        # Crear contenido de la tarjeta
        self._create_card_content(card_frame, tool)
        
        # Agregar interactividad
        self._add_card_interactivity(card_frame, tool)
    
    def _create_card_content(self, card_frame, tool):
        """
        Crea el contenido de una tarjeta de herramienta.
        
        Args:
            card_frame: Frame de la tarjeta
            tool (dict): Información de la herramienta
        """
        # Frame interno con padding
        inner_frame = tk.Frame(card_frame, bg=self.colors['card_bg'])
        inner_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Icono de la herramienta
        icon_label = tk.Label(inner_frame, text=tool["icon"], 
                             font=self.fonts['icon'],
                             fg=self.colors['text'],
                             bg=self.colors['card_bg'])
        icon_label.pack(pady=(0, 15))
        
        # Nombre de la herramienta
        name_label = tk.Label(inner_frame, text=tool["name"],
                             font=self.fonts['body_bold'],
                             fg=self.colors['text'],
                             bg=self.colors['card_bg'],
                             wraplength=240)
        name_label.pack(pady=(0, 8))
        
        # Descripción de la herramienta
        desc_label = tk.Label(inner_frame, text=tool["description"],
                             font=self.fonts['small'],
                             fg=self.colors['text_secondary'],
                             bg=self.colors['card_bg'],
                             wraplength=240,
                             justify='center')
        desc_label.pack()
    
    def _add_card_interactivity(self, card_frame, tool):
        """
        Agrega interactividad a una tarjeta de herramienta.
        
        Args:
            card_frame: Frame de la tarjeta
            tool (dict): Información de la herramienta
        """
        # Obtener todos los widgets de la tarjeta
        widgets = [card_frame] + list(card_frame.winfo_children())
        for child in card_frame.winfo_children():
            widgets.extend(child.winfo_children())
        
        # Función para abrir la herramienta
        def on_card_click(event):
            self.open_tool(tool)
        
        # Función para efecto hover
        def on_enter(event):
            self._apply_hover_effect(card_frame, True)
        
        def on_leave(event):
            self._apply_hover_effect(card_frame, False)
        
        # Agregar eventos a todos los widgets
        for widget in widgets:
            widget.bind("<Button-1>", on_card_click)
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
            widget.bind("<Enter>", lambda e: e.widget.config(cursor="hand2"))
            widget.bind("<Leave>", lambda e: e.widget.config(cursor=""))
    
    def _apply_hover_effect(self, card_frame, is_hover):
        """
        Aplica el efecto hover a una tarjeta.
        
        Args:
            card_frame: Frame de la tarjeta
            is_hover (bool): True si está en hover, False si no
        """
        if is_hover:
            bg_color = self.colors['card_hover']
            border_color = self.colors['border_hover']
        else:
            bg_color = self.colors['card_bg']
            border_color = self.colors['border']
        
        # Aplicar colores a todos los widgets de la tarjeta
        self._update_widget_colors(card_frame, bg_color)
        card_frame.config(highlightbackground=border_color)
    
    def _update_widget_colors(self, widget, bg_color):
        """
        Actualiza los colores de fondo de un widget y sus hijos.
        
        Args:
            widget: Widget a actualizar
            bg_color (str): Color de fondo a aplicar
        """
        if hasattr(widget, 'config'):
            try:
                widget.config(bg=bg_color)
            except:
                pass
        
        # Actualizar hijos recursivamente
        for child in widget.winfo_children():
            self._update_widget_colors(child, bg_color)
    
    def open_tool(self, tool):
        """
        Abre una herramienta específica en una nueva ventana.
        
        Args:
            tool (dict): Información de la herramienta a abrir
        """
        try:
            # Crear ventana para la herramienta
            tool_window = tk.Toplevel(self.root)
            tool_window.title(f"{tool['name']} - {APP_NAME}")
            tool_window.geometry(TOOL_WINDOW_CONFIG['geometry'])
            tool_window.minsize(*TOOL_WINDOW_CONFIG['min_size'])
            tool_window.configure(bg=TOOL_WINDOW_CONFIG['background'])
            
            # Configurar el icono de la ventana (si está disponible)
            try:
                tool_window.iconbitmap('icon.ico')
            except:
                pass
            
            # Crear instancia de la herramienta
            tool_instance = tool["tool_class"](tool_window, tool["name"])
            tool_instance.create_interface()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir la herramienta: {str(e)}")
    
    # =========================================================================
    # MÉTODO PRINCIPAL DE EJECUCIÓN
    # =========================================================================
    
    def run(self):
        """
        Inicia el bucle principal de la aplicación.
        
        Este método debe ser llamado para iniciar la aplicación.
        """
        self.root.mainloop()


# =============================================================================
# PUNTO DE ENTRADA DE LA APLICACIÓN
# =============================================================================

def main():
    """
    Función principal de la aplicación.
    
    Crea una instancia de DevToolsSuite y la ejecuta.
    """
    try:
        app = DevToolsSuite()
        app.run()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()