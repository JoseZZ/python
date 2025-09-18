#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de herramientas de generación
Incluye generador de contraseñas, UUID, y hashes
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import uuid
import hashlib
import secrets
import string
import random


class GeneratorsTool:
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
        
        # Pestañas para diferentes generadores
        self.create_password_tab()
        self.create_uuid_tab()
        self.create_hash_tab()
    
    def create_password_tab(self):
        """Crear pestaña de generador de contraseñas"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Generador de Contraseñas")
        
        # Frame de configuración
        config_frame = ttk.LabelFrame(frame, text="Configuración", padding=10)
        config_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Longitud
        length_frame = ttk.Frame(config_frame)
        length_frame.pack(fill=tk.X, pady=5)
        ttk.Label(length_frame, text="Longitud:").pack(side=tk.LEFT)
        self.password_length = tk.IntVar(value=12)
        length_spinbox = ttk.Spinbox(length_frame, from_=4, to=128, 
                                   textvariable=self.password_length, width=10)
        length_spinbox.pack(side=tk.LEFT, padx=(10, 0))
        
        # Opciones de caracteres
        options_frame = ttk.Frame(config_frame)
        options_frame.pack(fill=tk.X, pady=5)
        
        self.use_uppercase = tk.BooleanVar(value=True)
        self.use_lowercase = tk.BooleanVar(value=True)
        self.use_numbers = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(options_frame, text="Mayúsculas (A-Z)", 
                       variable=self.use_uppercase).pack(anchor=tk.W)
        ttk.Checkbutton(options_frame, text="Minúsculas (a-z)", 
                       variable=self.use_lowercase).pack(anchor=tk.W)
        ttk.Checkbutton(options_frame, text="Números (0-9)", 
                       variable=self.use_numbers).pack(anchor=tk.W)
        ttk.Checkbutton(options_frame, text="Símbolos (!@#$%^&*)", 
                       variable=self.use_symbols).pack(anchor=tk.W)
        
        # Botones
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(button_frame, text="Generar Contraseña", 
                  command=self.generate_password).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Generar Múltiples", 
                  command=self.generate_multiple_passwords).pack(side=tk.LEFT, padx=5)
        
        # Resultado
        result_frame = ttk.LabelFrame(frame, text="Contraseña Generada", padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.password_output = scrolledtext.ScrolledText(result_frame, height=8)
        self.password_output.pack(fill=tk.BOTH, expand=True)
    
    def create_uuid_tab(self):
        """Crear pestaña de generador de UUID"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Generador de UUID")
        
        # Frame de configuración
        config_frame = ttk.LabelFrame(frame, text="Configuración", padding=10)
        config_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Versión de UUID
        version_frame = ttk.Frame(config_frame)
        version_frame.pack(fill=tk.X, pady=5)
        ttk.Label(version_frame, text="Versión:").pack(side=tk.LEFT)
        
        self.uuid_version = tk.StringVar(value="4")
        versions = [("UUID v1 (basado en tiempo)", "1"),
                   ("UUID v4 (aleatorio)", "4")]
        
        for text, value in versions:
            ttk.Radiobutton(version_frame, text=text, variable=self.uuid_version, 
                           value=value).pack(anchor=tk.W)
        
        # Cantidad
        count_frame = ttk.Frame(config_frame)
        count_frame.pack(fill=tk.X, pady=5)
        ttk.Label(count_frame, text="Cantidad:").pack(side=tk.LEFT)
        self.uuid_count = tk.IntVar(value=1)
        count_spinbox = ttk.Spinbox(count_frame, from_=1, to=100, 
                                  textvariable=self.uuid_count, width=10)
        count_spinbox.pack(side=tk.LEFT, padx=(10, 0))
        
        # Botones
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(button_frame, text="Generar UUID", 
                  command=self.generate_uuid).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", 
                  command=self.clear_uuid).pack(side=tk.RIGHT, padx=5)
        
        # Resultado
        result_frame = ttk.LabelFrame(frame, text="UUIDs Generados", padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.uuid_output = scrolledtext.ScrolledText(result_frame, height=10)
        self.uuid_output.pack(fill=tk.BOTH, expand=True)
    
    def create_hash_tab(self):
        """Crear pestaña de generador de hashes"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Generador de Hash")
        
        # Frame de entrada
        input_frame = ttk.LabelFrame(frame, text="Texto a hashear", padding=10)
        input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.hash_input = scrolledtext.ScrolledText(input_frame, height=4)
        self.hash_input.pack(fill=tk.X)
        
        # Frame de configuración
        config_frame = ttk.LabelFrame(frame, text="Algoritmos de Hash", padding=10)
        config_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.hash_algorithms = {
            "MD5": tk.BooleanVar(value=True),
            "SHA1": tk.BooleanVar(value=True),
            "SHA256": tk.BooleanVar(value=True),
            "SHA512": tk.BooleanVar(value=True)
        }
        
        for algo, var in self.hash_algorithms.items():
            ttk.Checkbutton(config_frame, text=algo, variable=var).pack(anchor=tk.W)
        
        # Botones
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(button_frame, text="Generar Hashes", 
                  command=self.generate_hashes).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", 
                  command=self.clear_hash).pack(side=tk.RIGHT, padx=5)
        
        # Resultado
        result_frame = ttk.LabelFrame(frame, text="Hashes Generados", padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.hash_output = scrolledtext.ScrolledText(result_frame, height=10)
        self.hash_output.pack(fill=tk.BOTH, expand=True)
    
    def generate_password(self):
        """Generar una contraseña"""
        try:
            length = self.password_length.get()
            
            # Verificar que al menos una opción esté seleccionada
            if not any([self.use_uppercase.get(), self.use_lowercase.get(), 
                       self.use_numbers.get(), self.use_symbols.get()]):
                messagebox.showwarning("Advertencia", "Selecciona al menos un tipo de carácter")
                return
            
            # Construir conjunto de caracteres
            chars = ""
            if self.use_uppercase.get():
                chars += string.ascii_uppercase
            if self.use_lowercase.get():
                chars += string.ascii_lowercase
            if self.use_numbers.get():
                chars += string.digits
            if self.use_symbols.get():
                chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
            
            # Generar contraseña
            password = ''.join(secrets.choice(chars) for _ in range(length))
            
            self.password_output.delete("1.0", tk.END)
            self.password_output.insert("1.0", password)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar contraseña: {str(e)}")
    
    def generate_multiple_passwords(self):
        """Generar múltiples contraseñas"""
        try:
            length = self.password_length.get()
            count = 10  # Generar 10 contraseñas
            
            # Verificar que al menos una opción esté seleccionada
            if not any([self.use_uppercase.get(), self.use_lowercase.get(), 
                       self.use_numbers.get(), self.use_symbols.get()]):
                messagebox.showwarning("Advertencia", "Selecciona al menos un tipo de carácter")
                return
            
            # Construir conjunto de caracteres
            chars = ""
            if self.use_uppercase.get():
                chars += string.ascii_uppercase
            if self.use_lowercase.get():
                chars += string.ascii_lowercase
            if self.use_numbers.get():
                chars += string.digits
            if self.use_symbols.get():
                chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
            
            # Generar contraseñas
            passwords = []
            for i in range(count):
                password = ''.join(secrets.choice(chars) for _ in range(length))
                passwords.append(f"{i+1:2d}. {password}")
            
            self.password_output.delete("1.0", tk.END)
            self.password_output.insert("1.0", "\n".join(passwords))
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar contraseñas: {str(e)}")
    
    def generate_uuid(self):
        """Generar UUIDs"""
        try:
            version = int(self.uuid_version.get())
            count = self.uuid_count.get()
            
            uuids = []
            for i in range(count):
                if version == 1:
                    uuid_val = uuid.uuid1()
                elif version == 4:
                    uuid_val = uuid.uuid4()
                else:
                    uuid_val = uuid.uuid4()
                
                uuids.append(f"{i+1:2d}. {uuid_val}")
            
            self.uuid_output.delete("1.0", tk.END)
            self.uuid_output.insert("1.0", "\n".join(uuids))
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar UUIDs: {str(e)}")
    
    def generate_hashes(self):
        """Generar hashes del texto"""
        try:
            text = self.hash_input.get("1.0", tk.END).strip()
            if not text:
                messagebox.showwarning("Advertencia", "Por favor ingresa texto para hashear")
                return
            
            # Convertir a bytes
            text_bytes = text.encode('utf-8')
            
            results = []
            for algo, var in self.hash_algorithms.items():
                if var.get():
                    if algo == "MD5":
                        hash_val = hashlib.md5(text_bytes).hexdigest()
                    elif algo == "SHA1":
                        hash_val = hashlib.sha1(text_bytes).hexdigest()
                    elif algo == "SHA256":
                        hash_val = hashlib.sha256(text_bytes).hexdigest()
                    elif algo == "SHA512":
                        hash_val = hashlib.sha512(text_bytes).hexdigest()
                    
                    results.append(f"{algo:8s}: {hash_val}")
            
            if not results:
                messagebox.showwarning("Advertencia", "Selecciona al menos un algoritmo de hash")
                return
            
            self.hash_output.delete("1.0", tk.END)
            self.hash_output.insert("1.0", "\n".join(results))
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar hashes: {str(e)}")
    
    def clear_uuid(self):
        """Limpiar salida de UUID"""
        self.uuid_output.delete("1.0", tk.END)
    
    def clear_hash(self):
        """Limpiar entrada y salida de hash"""
        self.hash_input.delete("1.0", tk.END)
        self.hash_output.delete("1.0", tk.END)
    
    def create_interface(self):
        """Crear la interfaz (método requerido por la aplicación principal)"""
        pass  # La interfaz ya se crea en __init__
