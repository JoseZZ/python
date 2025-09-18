#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuración de estilos compartidos para DevTools Suite
"""

import tkinter as tk
from tkinter import ttk, scrolledtext


class ModernStyles:
    """Clase para manejar estilos modernos consistentes"""
    
    def __init__(self):
        # Colores glassmorfista dark
        self.colors = {
            'primary': '#00d4ff',
            'primary_hover': '#00b8e6',
            'secondary': 'rgba(45, 45, 48, 0.8)',
            'secondary_hover': 'rgba(62, 62, 66, 0.9)',
            'accent': '#00d4ff',
            'text': '#ffffff',
            'text_secondary': '#b8b8b8',
            'text_muted': '#8a8886',
            'background': 'rgba(20, 20, 25, 0.95)',
            'card_bg': 'rgba(40, 40, 50, 0.7)',
            'card_hover': 'rgba(60, 60, 70, 0.8)',
            'border': 'rgba(255, 255, 255, 0.1)',
            'border_hover': '#00d4ff',
            'sidebar_bg': 'rgba(30, 30, 35, 0.9)',
            'sidebar_hover': 'rgba(50, 50, 55, 0.9)',
            'input_bg': 'rgba(60, 60, 70, 0.6)',
            'input_fg': '#ffffff',
            'glass_effect': 'rgba(255, 255, 255, 0.05)',
            'shadow': 'rgba(0, 0, 0, 0.3)'
        }
        
        # Fuentes modernas y claras
        self.fonts = {
            'title': ('Segoe UI', 18, 'bold'),
            'subtitle': ('Segoe UI', 14, 'bold'),
            'body': ('Segoe UI', 11),
            'body_bold': ('Segoe UI', 11, 'bold'),
            'small': ('Segoe UI', 9),
            'button': ('Segoe UI', 10)
        }
    
    def create_modern_button(self, parent, text, command):
        """Crear botón con estilo moderno"""
        button = tk.Button(parent, text=text, command=command,
                          font=self.fonts['button'],
                          fg='white',
                          bg=self.colors['primary'],
                          activebackground=self.colors['primary_hover'],
                          activeforeground='white',
                          relief='flat',
                          bd=0,
                          padx=20,
                          pady=8,
                          cursor='hand2')
        
        # Efecto hover
        def on_enter(event):
            button.config(bg=self.colors['primary_hover'])
        
        def on_leave(event):
            button.config(bg=self.colors['primary'])
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
        return button
    
    def create_modern_text_widget(self, parent, height=10, **kwargs):
        """Crear widget de texto con estilo moderno"""
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
        """Crear campo de entrada con estilo moderno"""
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
        """Crear LabelFrame con estilo moderno"""
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
        """Crear Frame con estilo moderno"""
        default_config = {
            'bg': self.colors['background']
        }
        
        # Actualizar con configuración personalizada
        default_config.update(kwargs)
        
        return tk.Frame(parent, **default_config)
    
    def create_modern_radiobutton(self, parent, text, variable, value, **kwargs):
        """Crear RadioButton con estilo moderno"""
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
        """Crear CheckButton con estilo moderno"""
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
    
    def create_modern_spinbox(self, parent, **kwargs):
        """Crear Spinbox con estilo moderno"""
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
        
        return tk.Spinbox(parent, **default_config)
    
    def create_modern_combobox(self, parent, **kwargs):
        """Crear Combobox con estilo moderno"""
        default_config = {
            'font': self.fonts['body'],
            'background': self.colors['input_bg'],
            'foreground': self.colors['input_fg'],
            'relief': 'flat',
            'borderwidth': 1,
            'highlightthickness': 1,
            'highlightcolor': self.colors['primary'],
            'highlightbackground': self.colors['border']
        }
        
        # Actualizar con configuración personalizada
        default_config.update(kwargs)
        
        return ttk.Combobox(parent, **default_config)
    
    def setup_notebook_style(self, notebook):
        """Configurar estilo del notebook"""
        style = ttk.Style()
        style.configure('TNotebook', background=self.colors['background'])
        style.configure('TNotebook.Tab', background=self.colors['card_bg'], 
                       foreground=self.colors['text'], padding=[20, 10])
        style.map('TNotebook.Tab', background=[('selected', self.colors['primary'])],
                 foreground=[('selected', 'white')])
