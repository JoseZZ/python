#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de utilidades de texto
Incluye comparador de texto, escape/unescape, y analizador de texto
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import difflib
import re
from collections import Counter


class TextUtilsTool:
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
        
        # Pestañas para diferentes utilidades
        self.create_text_diff_tab()
        self.create_escape_tab()
        self.create_text_analyzer_tab()
    
    def create_text_diff_tab(self):
        """Crear pestaña de comparador de texto"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Comparador de Texto")
        
        # Frame superior con dos paneles
        input_frame = ttk.Frame(frame)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Panel izquierdo
        left_frame = ttk.LabelFrame(input_frame, text="Texto 1", padding=5)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        self.text1_input = scrolledtext.ScrolledText(left_frame, height=10)
        self.text1_input.pack(fill=tk.BOTH, expand=True)
        
        # Panel derecho
        right_frame = ttk.LabelFrame(input_frame, text="Texto 2", padding=5)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        self.text2_input = scrolledtext.ScrolledText(right_frame, height=10)
        self.text2_input.pack(fill=tk.BOTH, expand=True)
        
        # Botones
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(button_frame, text="Comparar Textos", 
                  command=self.compare_texts).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", 
                  command=self.clear_diff).pack(side=tk.RIGHT, padx=5)
        
        # Frame inferior para resultado
        result_frame = ttk.LabelFrame(frame, text="Diferencias", padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.diff_output = scrolledtext.ScrolledText(result_frame, height=8)
        self.diff_output.pack(fill=tk.BOTH, expand=True)
    
    def create_escape_tab(self):
        """Crear pestaña de escape/unescape"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Escape/Unescape")
        
        # Frame superior para entrada
        input_frame = ttk.LabelFrame(frame, text="Texto a procesar", padding=10)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.escape_input = scrolledtext.ScrolledText(input_frame, height=8)
        self.escape_input.pack(fill=tk.BOTH, expand=True)
        
        # Botones
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(button_frame, text="Escape JSON", 
                  command=self.escape_json).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Unescape JSON", 
                  command=self.unescape_json).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Escape Regex", 
                  command=self.escape_regex).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", 
                  command=self.clear_escape).pack(side=tk.RIGHT, padx=5)
        
        # Frame inferior para salida
        output_frame = ttk.LabelFrame(frame, text="Resultado", padding=10)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.escape_output = scrolledtext.ScrolledText(output_frame, height=8)
        self.escape_output.pack(fill=tk.BOTH, expand=True)
    
    def create_text_analyzer_tab(self):
        """Crear pestaña de analizador de texto"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Analizador de Texto")
        
        # Frame superior para entrada
        input_frame = ttk.LabelFrame(frame, text="Texto a analizar", padding=10)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.analyzer_input = scrolledtext.ScrolledText(input_frame, height=8)
        self.analyzer_input.pack(fill=tk.BOTH, expand=True)
        
        # Botones
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(button_frame, text="Analizar Texto", 
                  command=self.analyze_text).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", 
                  command=self.clear_analyzer).pack(side=tk.RIGHT, padx=5)
        
        # Frame inferior para resultado
        result_frame = ttk.LabelFrame(frame, text="Estadísticas", padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.analyzer_output = scrolledtext.ScrolledText(result_frame, height=8)
        self.analyzer_output.pack(fill=tk.BOTH, expand=True)
    
    def compare_texts(self):
        """Comparar dos textos y mostrar diferencias"""
        try:
            text1 = self.text1_input.get("1.0", tk.END).strip()
            text2 = self.text2_input.get("1.0", tk.END).strip()
            
            if not text1 and not text2:
                messagebox.showwarning("Advertencia", "Por favor ingresa al menos un texto para comparar")
                return
            
            # Dividir en líneas
            lines1 = text1.splitlines(keepends=True)
            lines2 = text2.splitlines(keepends=True)
            
            # Generar diferencias
            diff = difflib.unified_diff(lines1, lines2, 
                                      fromfile='Texto 1', 
                                      tofile='Texto 2', 
                                      lineterm='')
            
            diff_text = '\n'.join(diff)
            
            if not diff_text:
                diff_text = "Los textos son idénticos."
            
            self.diff_output.delete("1.0", tk.END)
            self.diff_output.insert("1.0", diff_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al comparar textos: {str(e)}")
    
    def escape_json(self):
        """Escapar texto para JSON"""
        try:
            input_data = self.escape_input.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa texto para escapar")
                return
            
            # Escapar caracteres especiales para JSON
            escaped = json.dumps(input_data)[1:-1]  # Remover las comillas externas
            
            self.escape_output.delete("1.0", tk.END)
            self.escape_output.insert("1.0", escaped)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al escapar JSON: {str(e)}")
    
    def unescape_json(self):
        """Desescapar texto JSON"""
        try:
            input_data = self.escape_input.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa texto JSON para desescapar")
                return
            
            # Desescapar JSON
            unescaped = json.loads(f'"{input_data}"')
            
            self.escape_output.delete("1.0", tk.END)
            self.escape_output.insert("1.0", unescaped)
            
        except json.JSONDecodeError as e:
            messagebox.showerror("Error", f"JSON inválido: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al desescapar JSON: {str(e)}")
    
    def escape_regex(self):
        """Escapar texto para expresiones regulares"""
        try:
            input_data = self.escape_input.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa texto para escapar")
                return
            
            # Escapar caracteres especiales de regex
            escaped = re.escape(input_data)
            
            self.escape_output.delete("1.0", tk.END)
            self.escape_output.insert("1.0", escaped)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al escapar regex: {str(e)}")
    
    def analyze_text(self):
        """Analizar texto y mostrar estadísticas"""
        try:
            input_data = self.analyzer_input.get("1.0", tk.END)
            if not input_data.strip():
                messagebox.showwarning("Advertencia", "Por favor ingresa texto para analizar")
                return
            
            # Estadísticas básicas
            char_count = len(input_data)
            char_count_no_spaces = len(input_data.replace(' ', '').replace('\n', '').replace('\t', ''))
            line_count = len(input_data.splitlines())
            word_count = len(input_data.split())
            
            # Contar caracteres únicos
            char_freq = Counter(input_data.lower())
            most_common_chars = char_freq.most_common(10)
            
            # Contar palabras
            words = re.findall(r'\b\w+\b', input_data.lower())
            word_freq = Counter(words)
            most_common_words = word_freq.most_common(10)
            
            # Generar reporte
            report = []
            report.append("=== ESTADÍSTICAS DE TEXTO ===")
            report.append(f"Caracteres totales: {char_count}")
            report.append(f"Caracteres (sin espacios): {char_count_no_spaces}")
            report.append(f"Líneas: {line_count}")
            report.append(f"Palabras: {word_count}")
            report.append("")
            
            report.append("=== CARACTERES MÁS FRECUENTES ===")
            for char, count in most_common_chars:
                if char.isprintable() and char != ' ':
                    report.append(f"'{char}': {count}")
            report.append("")
            
            report.append("=== PALABRAS MÁS FRECUENTES ===")
            for word, count in most_common_words:
                report.append(f"'{word}': {count}")
            
            self.analyzer_output.delete("1.0", tk.END)
            self.analyzer_output.insert("1.0", "\n".join(report))
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al analizar texto: {str(e)}")
    
    def clear_diff(self):
        """Limpiar comparador de texto"""
        self.text1_input.delete("1.0", tk.END)
        self.text2_input.delete("1.0", tk.END)
        self.diff_output.delete("1.0", tk.END)
    
    def clear_escape(self):
        """Limpiar escape/unescape"""
        self.escape_input.delete("1.0", tk.END)
        self.escape_output.delete("1.0", tk.END)
    
    def clear_analyzer(self):
        """Limpiar analizador"""
        self.analyzer_input.delete("1.0", tk.END)
        self.analyzer_output.delete("1.0", tk.END)
    
    def create_interface(self):
        """Crear la interfaz (método requerido por la aplicación principal)"""
        pass  # La interfaz ya se crea en __init__
