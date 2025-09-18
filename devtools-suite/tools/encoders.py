#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de herramientas de codificación
Incluye JWT decoder, URL encoder/decoder, HTML encoder/decoder
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import urllib.parse
import html
import json
import base64
from datetime import datetime


class EncodersTool:
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
        # Frame principal
        main_frame = ttk.Frame(self.parent)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Crear notebook para diferentes herramientas
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestañas para diferentes codificadores
        self.create_jwt_tab()
        self.create_url_tab()
        self.create_html_tab()
    
    def create_jwt_tab(self):
        """Crear pestaña de JWT decoder"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="JWT Decoder")
        
        # Frame superior para entrada
        input_frame = ttk.LabelFrame(frame, text="Token JWT", padding=10)
        input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.jwt_input = ttk.Entry(input_frame, font=('Consolas', 10))
        self.jwt_input.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(input_frame, text="Decodificar JWT", 
                  command=self.decode_jwt).pack()
        
        # Frame para resultados
        result_frame = ttk.LabelFrame(frame, text="Resultado", padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.jwt_output = scrolledtext.ScrolledText(result_frame, height=15)
        self.jwt_output.pack(fill=tk.BOTH, expand=True)
    
    def create_url_tab(self):
        """Crear pestaña de URL encoder/decoder"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="URL Encoder/Decoder")
        
        # Frame superior para entrada
        input_frame = ttk.LabelFrame(frame, text="Texto a codificar/decodificar", padding=10)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.url_input = scrolledtext.ScrolledText(input_frame, height=8)
        self.url_input.pack(fill=tk.BOTH, expand=True)
        
        # Botones
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(button_frame, text="Codificar URL", 
                  command=self.encode_url).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Decodificar URL", 
                  command=self.decode_url).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", 
                  command=self.clear_url).pack(side=tk.RIGHT, padx=5)
        
        # Frame inferior para salida
        output_frame = ttk.LabelFrame(frame, text="Resultado", padding=10)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.url_output = scrolledtext.ScrolledText(output_frame, height=8)
        self.url_output.pack(fill=tk.BOTH, expand=True)
    
    def create_html_tab(self):
        """Crear pestaña de HTML encoder/decoder"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="HTML Encoder/Decoder")
        
        # Frame superior para entrada
        input_frame = ttk.LabelFrame(frame, text="Texto a codificar/decodificar", padding=10)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.html_input = scrolledtext.ScrolledText(input_frame, height=8)
        self.html_input.pack(fill=tk.BOTH, expand=True)
        
        # Botones
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(button_frame, text="Codificar HTML", 
                  command=self.encode_html).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Decodificar HTML", 
                  command=self.decode_html).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", 
                  command=self.clear_html).pack(side=tk.RIGHT, padx=5)
        
        # Frame inferior para salida
        output_frame = ttk.LabelFrame(frame, text="Resultado", padding=10)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.html_output = scrolledtext.ScrolledText(output_frame, height=8)
        self.html_output.pack(fill=tk.BOTH, expand=True)
    
    def decode_jwt(self):
        """Decodificar token JWT"""
        try:
            token = self.jwt_input.get().strip()
            if not token:
                messagebox.showwarning("Advertencia", "Por favor ingresa un token JWT")
                return
            
            # Dividir el token en sus partes
            parts = token.split('.')
            if len(parts) != 3:
                messagebox.showerror("Error", "Token JWT inválido. Debe tener 3 partes separadas por puntos.")
                return
            
            header, payload, signature = parts
            
            # Decodificar header
            header_decoded = self.decode_jwt_part(header)
            payload_decoded = self.decode_jwt_part(payload)
            
            # Mostrar resultados
            result = f"HEADER:\n{json.dumps(header_decoded, indent=2, ensure_ascii=False)}\n\n"
            result += f"PAYLOAD:\n{json.dumps(payload_decoded, indent=2, ensure_ascii=False)}\n\n"
            result += f"SIGNATURE:\n{signature}\n\n"
            
            # Verificar expiración si existe
            if 'exp' in payload_decoded:
                exp_timestamp = payload_decoded['exp']
                exp_date = datetime.fromtimestamp(exp_timestamp)
                current_date = datetime.now()
                
                if current_date > exp_date:
                    result += f"⚠️  ADVERTENCIA: Este token ha expirado el {exp_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
                else:
                    result += f"✅ Token válido hasta: {exp_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
            
            self.jwt_output.delete("1.0", tk.END)
            self.jwt_output.insert("1.0", result)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al decodificar JWT: {str(e)}")
    
    def decode_jwt_part(self, part):
        """Decodificar una parte del JWT"""
        # Agregar padding si es necesario
        missing_padding = len(part) % 4
        if missing_padding:
            part += '=' * (4 - missing_padding)
        
        decoded = base64.urlsafe_b64decode(part)
        return json.loads(decoded.decode('utf-8'))
    
    def encode_url(self):
        """Codificar texto a URL"""
        try:
            input_data = self.url_input.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa texto para codificar")
                return
            
            encoded = urllib.parse.quote(input_data, safe='')
            self.url_output.delete("1.0", tk.END)
            self.url_output.insert("1.0", encoded)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en la codificación: {str(e)}")
    
    def decode_url(self):
        """Decodificar URL a texto"""
        try:
            input_data = self.url_input.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa URL para decodificar")
                return
            
            decoded = urllib.parse.unquote(input_data)
            self.url_output.delete("1.0", tk.END)
            self.url_output.insert("1.0", decoded)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en la decodificación: {str(e)}")
    
    def encode_html(self):
        """Codificar texto a HTML"""
        try:
            input_data = self.html_input.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa texto para codificar")
                return
            
            encoded = html.escape(input_data)
            self.html_output.delete("1.0", tk.END)
            self.html_output.insert("1.0", encoded)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en la codificación: {str(e)}")
    
    def decode_html(self):
        """Decodificar HTML a texto"""
        try:
            input_data = self.html_input.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa HTML para decodificar")
                return
            
            decoded = html.unescape(input_data)
            self.html_output.delete("1.0", tk.END)
            self.html_output.insert("1.0", decoded)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en la decodificación: {str(e)}")
    
    def clear_url(self):
        """Limpiar texto URL"""
        self.url_input.delete("1.0", tk.END)
        self.url_output.delete("1.0", tk.END)
    
    def clear_html(self):
        """Limpiar texto HTML"""
        self.html_input.delete("1.0", tk.END)
        self.html_output.delete("1.0", tk.END)
    
    def create_interface(self):
        """Crear la interfaz (método requerido por la aplicación principal)"""
        pass  # La interfaz ya se crea en __init__
