#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase base para todas las herramientas de DevTools Suite
Implementa el patrón Template Method para garantizar consistencia en la interfaz
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
from config import COLORS, FONTS, TOOL_WINDOW_CONFIG


class BaseTool:
    """
    Clase base abstracta para todas las herramientas.
    
    Esta clase define la estructura común que deben seguir todas las herramientas,
    implementando el patrón Template Method para garantizar consistencia.
    """
    
    def __init__(self, parent, tool_name):
        """
        Inicializa la herramienta base.
        
        Args:
            parent: Widget padre (ventana principal)
            tool_name (str): Nombre de la herramienta
        """
        self.parent = parent
        self.tool_name = tool_name
        self.colors = COLORS
        self.fonts = FONTS
        
        # Configurar la ventana de la herramienta
        self._setup_tool_window()
        
        # Crear la interfaz específica de la herramienta
        self.create_interface()
    
    def _setup_tool_window(self):
        """
        Configura la ventana de la herramienta con estilo consistente.
        Método privado que no debe ser sobrescrito por las subclases.
        """
        # Configurar el fondo de la ventana
        self.parent.configure(bg=self.colors['background'])
        
        # Configurar transparencia si es compatible
        try:
            self.parent.attributes('-alpha', 0.95)
        except:
            pass
    
    def create_interface(self):
        """
        Método abstracto que debe ser implementado por cada herramienta.
        Define la interfaz específica de cada herramienta.
        """
        raise NotImplementedError("Las subclases deben implementar create_interface()")
    
    def create_modern_button(self, parent, text, command, **kwargs):
        """
        Crea un botón con estilo moderno consistente.
        
        Args:
            parent: Widget padre
            text (str): Texto del botón
            command: Función a ejecutar al hacer clic
            **kwargs: Argumentos adicionales para el botón
            
        Returns:
            tk.Button: Botón configurado con estilo moderno
        """
        default_config = {
            'font': self.fonts['button'],
            'fg': 'white',
            'bg': self.colors['primary'],
            'activebackground': self.colors['primary_hover'],
            'activeforeground': 'white',
            'relief': 'flat',
            'bd': 0,
            'padx': 20,
            'pady': 8,
            'cursor': 'hand2'
        }
        
        # Actualizar con configuración personalizada
        default_config.update(kwargs)
        
        button = tk.Button(parent, text=text, command=command, **default_config)
        
        # Agregar efectos hover
        self._add_hover_effects(button, self.colors['primary'], self.colors['primary_hover'])
        
        return button
    
    def create_modern_text_widget(self, parent, height=10, **kwargs):
        """
        Crea un widget de texto con estilo moderno.
        
        Args:
            parent: Widget padre
            height (int): Altura del widget
            **kwargs: Argumentos adicionales
            
        Returns:
            scrolledtext.ScrolledText: Widget de texto configurado
        """
        default_config = {
            'bg': self.colors['input_bg'],
            'fg': self.colors['input_fg'],
            'font': self.fonts['body'],
            'insertbackground': self.colors['text'],
            'selectbackground': self.colors['primary'],
            'selectforeground': 'white',
            'relief': 'flat',
            'bd': 1,
            'highlightthickness': 1,
            'highlightcolor': self.colors['primary'],
            'highlightbackground': self.colors['border']
        }
        
        # Actualizar con configuración personalizada
        default_config.update(kwargs)
        
        return scrolledtext.ScrolledText(parent, height=height, **default_config)
    
    def create_modern_entry(self, parent, **kwargs):
        """
        Crea un campo de entrada con estilo moderno.
        
        Args:
            parent: Widget padre
            **kwargs: Argumentos adicionales
            
        Returns:
            tk.Entry: Campo de entrada configurado
        """
        default_config = {
            'font': self.fonts['body'],
            'bg': self.colors['input_bg'],
            'fg': self.colors['input_fg'],
            'insertbackground': self.colors['text'],
            'relief': 'flat',
            'bd': 1,
            'highlightthickness': 1,
            'highlightcolor': self.colors['primary'],
            'highlightbackground': self.colors['border']
        }
        
        # Actualizar con configuración personalizada
        default_config.update(kwargs)
        
        return tk.Entry(parent, **default_config)
    
    def create_modern_label_frame(self, parent, text, **kwargs):
        """
        Crea un LabelFrame con estilo moderno.
        
        Args:
            parent: Widget padre
            text (str): Texto del LabelFrame
            **kwargs: Argumentos adicionales
            
        Returns:
            tk.LabelFrame: LabelFrame configurado
        """
        default_config = {
            'fg': self.colors['text'],
            'bg': self.colors['background'],
            'font': self.fonts['subtitle'],
            'padx': 15,
            'pady': 15
        }
        
        # Actualizar con configuración personalizada
        default_config.update(kwargs)
        
        return tk.LabelFrame(parent, text=text, **default_config)
    
    def create_modern_frame(self, parent, **kwargs):
        """
        Crea un Frame con estilo moderno.
        
        Args:
            parent: Widget padre
            **kwargs: Argumentos adicionales
            
        Returns:
            tk.Frame: Frame configurado
        """
        default_config = {
            'bg': self.colors['background']
        }
        
        # Actualizar con configuración personalizada
        default_config.update(kwargs)
        
        return tk.Frame(parent, **default_config)
    
    def create_modern_radiobutton(self, parent, text, variable, value, **kwargs):
        """
        Crea un RadioButton con estilo moderno.
        
        Args:
            parent: Widget padre
            text (str): Texto del RadioButton
            variable: Variable asociada
            value: Valor del RadioButton
            **kwargs: Argumentos adicionales
            
        Returns:
            tk.Radiobutton: RadioButton configurado
        """
        default_config = {
            'fg': self.colors['text'],
            'bg': self.colors['background'],
            'font': self.fonts['body'],
            'selectcolor': self.colors['primary'],
            'activebackground': self.colors['background'],
            'activeforeground': self.colors['text']
        }
        
        # Actualizar con configuración personalizada
        default_config.update(kwargs)
        
        return tk.Radiobutton(parent, text=text, variable=variable, 
                             value=value, **default_config)
    
    def create_modern_checkbutton(self, parent, text, variable, **kwargs):
        """
        Crea un CheckButton con estilo moderno.
        
        Args:
            parent: Widget padre
            text (str): Texto del CheckButton
            variable: Variable asociada
            **kwargs: Argumentos adicionales
            
        Returns:
            tk.Checkbutton: CheckButton configurado
        """
        default_config = {
            'fg': self.colors['text'],
            'bg': self.colors['background'],
            'font': self.fonts['body'],
            'selectcolor': self.colors['primary'],
            'activebackground': self.colors['background'],
            'activeforeground': self.colors['text']
        }
        
        # Actualizar con configuración personalizada
        default_config.update(kwargs)
        
        return tk.Checkbutton(parent, text=text, variable=variable, **default_config)
    
    def setup_notebook_style(self, notebook):
        """
        Configura el estilo de un notebook TTK.
        
        Args:
            notebook: Widget notebook TTK
        """
        style = ttk.Style()
        style.configure('TNotebook', background=self.colors['background'])
        style.configure('TNotebook.Tab', 
                       background=self.colors['card_bg'], 
                       foreground=self.colors['text'], 
                       padding=[20, 10])
        style.map('TNotebook.Tab', 
                 background=[('selected', self.colors['primary'])],
                 foreground=[('selected', 'white')])
    
    def _add_hover_effects(self, widget, normal_color, hover_color):
        """
        Agrega efectos hover a un widget.
        
        Args:
            widget: Widget al que agregar efectos
            normal_color (str): Color normal
            hover_color (str): Color en hover
        """
        def on_enter(event):
            widget.config(bg=hover_color)
        
        def on_leave(event):
            widget.config(bg=normal_color)
        
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)
