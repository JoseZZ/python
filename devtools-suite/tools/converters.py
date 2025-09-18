#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de herramientas de conversión
Incluye conversores de JSON/YAML, Base64, y números
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import yaml
import base64
import binascii


class ConvertersTool:
    def __init__(self, parent, tool_name):
        self.parent = parent
        self.tool_name = tool_name
        
        # Colores glassmorfista dark (compatibles con tkinter)
        self.colors = {
            'primary': '#00d4ff',
            'primary_hover': '#00b8e6',
            'background': '#141419',
            'card_bg': '#282832',
            'text': '#ffffff',
            'text_secondary': '#b8b8b8',
            'border': '#404040',
            'input_bg': '#3c3c48',
            'input_fg': '#ffffff',
            'glass_effect': '#2a2a35',
            'shadow': '#0a0a0a'
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
        
        self.setup_ui()
    
    def setup_ui(self):
        """Configurar la interfaz de usuario"""
        # Frame principal con fondo oscuro
        main_frame = tk.Frame(self.parent, bg=self.colors['background'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Crear notebook con estilo moderno
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Configurar estilo del notebook
        style = ttk.Style()
        style.configure('TNotebook', background=self.colors['background'])
        style.configure('TNotebook.Tab', background=self.colors['card_bg'], 
                       foreground=self.colors['text'], padding=[20, 10])
        style.map('TNotebook.Tab', background=[('selected', self.colors['primary'])],
                 foreground=[('selected', 'white')])
        
        # Pestañas para diferentes conversores
        self.create_json_yaml_tab()
        self.create_base64_tab()
        self.create_number_conversion_tab()
    
    def create_json_yaml_tab(self):
        """Crear pestaña de conversión JSON/YAML"""
        frame = tk.Frame(self.notebook, bg=self.colors['background'])
        self.notebook.add(frame, text="JSON ↔ YAML")
        
        # Frame superior para entrada
        input_frame = tk.LabelFrame(frame, text="Entrada", 
                                   fg=self.colors['text'],
                                   bg=self.colors['background'],
                                   font=self.fonts['subtitle'],
                                   padx=15, pady=15)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Texto de entrada con estilo moderno
        self.input_text = scrolledtext.ScrolledText(input_frame, height=10,
                                                   bg=self.colors['input_bg'],
                                                   fg=self.colors['input_fg'],
                                                   font=self.fonts['body'],
                                                   insertbackground=self.colors['text'],
                                                   selectbackground=self.colors['primary'],
                                                   selectforeground='white',
                                                   relief='flat',
                                                   bd=1,
                                                   highlightthickness=1,
                                                   highlightcolor=self.colors['primary'],
                                                   highlightbackground=self.colors['border'])
        self.input_text.pack(fill=tk.BOTH, expand=True)
        
        # Botones de conversión con estilo moderno
        button_frame = tk.Frame(frame, bg=self.colors['background'])
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.create_modern_button(button_frame, "JSON → YAML", self.json_to_yaml).pack(side=tk.LEFT, padx=5)
        self.create_modern_button(button_frame, "YAML → JSON", self.yaml_to_json).pack(side=tk.LEFT, padx=5)
        self.create_modern_button(button_frame, "Limpiar", self.clear_text).pack(side=tk.RIGHT, padx=5)
        
        # Frame inferior para salida
        output_frame = tk.LabelFrame(frame, text="Salida", 
                                    fg=self.colors['text'],
                                    bg=self.colors['background'],
                                    font=self.fonts['subtitle'],
                                    padx=15, pady=15)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.output_text = scrolledtext.ScrolledText(output_frame, height=10,
                                                    bg=self.colors['input_bg'],
                                                    fg=self.colors['input_fg'],
                                                    font=self.fonts['body'],
                                                    insertbackground=self.colors['text'],
                                                    selectbackground=self.colors['primary'],
                                                    selectforeground='white',
                                                    relief='flat',
                                                    bd=1,
                                                    highlightthickness=1,
                                                    highlightcolor=self.colors['primary'],
                                                    highlightbackground=self.colors['border'])
        self.output_text.pack(fill=tk.BOTH, expand=True)
    
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
    
    def create_base64_tab(self):
        """Crear pestaña de codificación Base64"""
        frame = tk.Frame(self.notebook, bg=self.colors['background'])
        self.notebook.add(frame, text="Base64")
        
        # Frame superior para entrada
        input_frame = tk.LabelFrame(frame, text="Texto a codificar/decodificar", 
                                   fg=self.colors['text'],
                                   bg=self.colors['background'],
                                   font=self.fonts['subtitle'],
                                   padx=15, pady=15)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.base64_input = scrolledtext.ScrolledText(input_frame, height=8,
                                                     bg=self.colors['input_bg'],
                                                     fg=self.colors['input_fg'],
                                                     font=self.fonts['body'],
                                                     insertbackground=self.colors['text'],
                                                     selectbackground=self.colors['primary'],
                                                     selectforeground='white',
                                                     relief='flat',
                                                     bd=1,
                                                     highlightthickness=1,
                                                     highlightcolor=self.colors['primary'],
                                                     highlightbackground=self.colors['border'])
        self.base64_input.pack(fill=tk.BOTH, expand=True)
        
        # Botones
        button_frame = tk.Frame(frame, bg=self.colors['background'])
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.create_modern_button(button_frame, "Codificar Base64", self.encode_base64).pack(side=tk.LEFT, padx=5)
        self.create_modern_button(button_frame, "Decodificar Base64", self.decode_base64).pack(side=tk.LEFT, padx=5)
        self.create_modern_button(button_frame, "Limpiar", self.clear_base64).pack(side=tk.RIGHT, padx=5)
        
        # Frame inferior para salida
        output_frame = tk.LabelFrame(frame, text="Resultado", 
                                    fg=self.colors['text'],
                                    bg=self.colors['background'],
                                    font=self.fonts['subtitle'],
                                    padx=15, pady=15)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.base64_output = scrolledtext.ScrolledText(output_frame, height=8,
                                                      bg=self.colors['input_bg'],
                                                      fg=self.colors['input_fg'],
                                                      font=self.fonts['body'],
                                                      insertbackground=self.colors['text'],
                                                      selectbackground=self.colors['primary'],
                                                      selectforeground='white',
                                                      relief='flat',
                                                      bd=1,
                                                      highlightthickness=1,
                                                      highlightcolor=self.colors['primary'],
                                                      highlightbackground=self.colors['border'])
        self.base64_output.pack(fill=tk.BOTH, expand=True)
    
    def create_number_conversion_tab(self):
        """Crear pestaña de conversión de números"""
        frame = tk.Frame(self.notebook, bg=self.colors['background'])
        self.notebook.add(frame, text="Conversión de Números")
        
        # Frame principal
        main_frame = tk.Frame(frame, bg=self.colors['background'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Entrada
        input_frame = tk.LabelFrame(main_frame, text="Número a convertir", 
                                   fg=self.colors['text'],
                                   bg=self.colors['background'],
                                   font=self.fonts['subtitle'],
                                   padx=15, pady=15)
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.number_input = tk.Entry(input_frame, 
                                    font=self.fonts['body'],
                                    bg=self.colors['input_bg'],
                                    fg=self.colors['input_fg'],
                                    insertbackground=self.colors['text'],
                                    relief='flat',
                                    bd=1,
                                    highlightthickness=1,
                                    highlightcolor=self.colors['primary'],
                                    highlightbackground=self.colors['border'])
        self.number_input.pack(fill=tk.X, pady=5)
        
        # Selección de base
        base_frame = tk.LabelFrame(main_frame, text="Base de entrada", 
                                  fg=self.colors['text'],
                                  bg=self.colors['background'],
                                  font=self.fonts['subtitle'],
                                  padx=15, pady=15)
        base_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.input_base = tk.StringVar(value="10")
        bases = [("Decimal (10)", "10"), ("Binario (2)", "2"), 
                ("Octal (8)", "8"), ("Hexadecimal (16)", "16")]
        
        for text, value in bases:
            radio = tk.Radiobutton(base_frame, text=text, variable=self.input_base, 
                                  value=value, fg=self.colors['text'],
                                  bg=self.colors['background'],
                                  font=self.fonts['body'],
                                  selectcolor=self.colors['primary'],
                                  activebackground=self.colors['background'],
                                  activeforeground=self.colors['text'])
            radio.pack(anchor=tk.W, pady=2)
        
        # Botón de conversión
        self.create_modern_button(main_frame, "Convertir", self.convert_number).pack(pady=15)
        
        # Resultados
        result_frame = tk.LabelFrame(main_frame, text="Resultados", 
                                    fg=self.colors['text'],
                                    bg=self.colors['background'],
                                    font=self.fonts['subtitle'],
                                    padx=15, pady=15)
        result_frame.pack(fill=tk.BOTH, expand=True)
        
        self.result_text = scrolledtext.ScrolledText(result_frame, height=10,
                                                    bg=self.colors['input_bg'],
                                                    fg=self.colors['input_fg'],
                                                    font=self.fonts['body'],
                                                    insertbackground=self.colors['text'],
                                                    selectbackground=self.colors['primary'],
                                                    selectforeground='white',
                                                    relief='flat',
                                                    bd=1,
                                                    highlightthickness=1,
                                                    highlightcolor=self.colors['primary'],
                                                    highlightbackground=self.colors['border'])
        self.result_text.pack(fill=tk.BOTH, expand=True)
    
    def json_to_yaml(self):
        """Convertir JSON a YAML"""
        try:
            input_data = self.input_text.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa texto JSON")
                return
            
            json_data = json.loads(input_data)
            yaml_data = yaml.dump(json_data, default_flow_style=False, allow_unicode=True)
            
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", yaml_data)
            
        except json.JSONDecodeError as e:
            messagebox.showerror("Error", f"JSON inválido: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error en la conversión: {str(e)}")
    
    def yaml_to_json(self):
        """Convertir YAML a JSON"""
        try:
            input_data = self.input_text.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa texto YAML")
                return
            
            yaml_data = yaml.safe_load(input_data)
            json_data = json.dumps(yaml_data, indent=2, ensure_ascii=False)
            
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", json_data)
            
        except yaml.YAMLError as e:
            messagebox.showerror("Error", f"YAML inválido: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error en la conversión: {str(e)}")
    
    def encode_base64(self):
        """Codificar texto a Base64"""
        try:
            input_data = self.base64_input.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa texto para codificar")
                return
            
            encoded = base64.b64encode(input_data.encode('utf-8')).decode('utf-8')
            self.base64_output.delete("1.0", tk.END)
            self.base64_output.insert("1.0", encoded)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en la codificación: {str(e)}")
    
    def decode_base64(self):
        """Decodificar Base64 a texto"""
        try:
            input_data = self.base64_input.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa texto Base64 para decodificar")
                return
            
            decoded = base64.b64decode(input_data).decode('utf-8')
            self.base64_output.delete("1.0", tk.END)
            self.base64_output.insert("1.0", decoded)
            
        except binascii.Error:
            messagebox.showerror("Error", "Base64 inválido")
        except UnicodeDecodeError:
            messagebox.showerror("Error", "No se puede decodificar como texto UTF-8")
        except Exception as e:
            messagebox.showerror("Error", f"Error en la decodificación: {str(e)}")
    
    def convert_number(self):
        """Convertir número entre diferentes bases"""
        try:
            input_data = self.number_input.get().strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa un número")
                return
            
            input_base = int(self.input_base.get())
            
            # Convertir a decimal primero
            decimal_value = int(input_data, input_base)
            
            # Convertir a todas las bases
            results = []
            results.append(f"Decimal (10): {decimal_value}")
            results.append(f"Binario (2): {bin(decimal_value)[2:]}")
            results.append(f"Octal (8): {oct(decimal_value)[2:]}")
            results.append(f"Hexadecimal (16): {hex(decimal_value)[2:].upper()}")
            
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert("1.0", "\n".join(results))
            
        except ValueError as e:
            messagebox.showerror("Error", f"Número inválido para la base {input_base}: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error en la conversión: {str(e)}")
    
    def clear_text(self):
        """Limpiar texto de entrada y salida"""
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
    
    def clear_base64(self):
        """Limpiar texto Base64"""
        self.base64_input.delete("1.0", tk.END)
        self.base64_output.delete("1.0", tk.END)
    
    def create_interface(self):
        """Crear la interfaz (método requerido por la aplicación principal)"""
        pass  # La interfaz ya se crea en __init__
