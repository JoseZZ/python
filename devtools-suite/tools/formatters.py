#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de herramientas de formateo
Incluye formateador JSON, SQL, y XML
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import xml.dom.minidom
import sqlparse


class FormattersTool:
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
        
        # Pestañas para diferentes formateadores
        self.create_json_tab()
        self.create_sql_tab()
        self.create_xml_tab()
    
    def create_json_tab(self):
        """Crear pestaña de formateador JSON"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Formateador JSON")
        
        # Frame superior para entrada
        input_frame = ttk.LabelFrame(frame, text="JSON a formatear", padding=10)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.json_input = scrolledtext.ScrolledText(input_frame, height=8)
        self.json_input.pack(fill=tk.BOTH, expand=True)
        
        # Botones
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(button_frame, text="Formatear JSON", 
                  command=self.format_json).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Validar JSON", 
                  command=self.validate_json).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Minificar JSON", 
                  command=self.minify_json).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", 
                  command=self.clear_json).pack(side=tk.RIGHT, padx=5)
        
        # Frame inferior para salida
        output_frame = ttk.LabelFrame(frame, text="JSON formateado", padding=10)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.json_output = scrolledtext.ScrolledText(output_frame, height=8)
        self.json_output.pack(fill=tk.BOTH, expand=True)
    
    def create_sql_tab(self):
        """Crear pestaña de formateador SQL"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Formateador SQL")
        
        # Frame superior para entrada
        input_frame = ttk.LabelFrame(frame, text="SQL a formatear", padding=10)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.sql_input = scrolledtext.ScrolledText(input_frame, height=8)
        self.sql_input.pack(fill=tk.BOTH, expand=True)
        
        # Botones
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(button_frame, text="Formatear SQL", 
                  command=self.format_sql).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", 
                  command=self.clear_sql).pack(side=tk.RIGHT, padx=5)
        
        # Frame inferior para salida
        output_frame = ttk.LabelFrame(frame, text="SQL formateado", padding=10)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.sql_output = scrolledtext.ScrolledText(output_frame, height=8)
        self.sql_output.pack(fill=tk.BOTH, expand=True)
    
    def create_xml_tab(self):
        """Crear pestaña de formateador XML"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Formateador XML")
        
        # Frame superior para entrada
        input_frame = ttk.LabelFrame(frame, text="XML a formatear", padding=10)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.xml_input = scrolledtext.ScrolledText(input_frame, height=8)
        self.xml_input.pack(fill=tk.BOTH, expand=True)
        
        # Botones
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(button_frame, text="Formatear XML", 
                  command=self.format_xml).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Validar XML", 
                  command=self.validate_xml).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Minificar XML", 
                  command=self.minify_xml).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", 
                  command=self.clear_xml).pack(side=tk.RIGHT, padx=5)
        
        # Frame inferior para salida
        output_frame = ttk.LabelFrame(frame, text="XML formateado", padding=10)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.xml_output = scrolledtext.ScrolledText(output_frame, height=8)
        self.xml_output.pack(fill=tk.BOTH, expand=True)
    
    def format_json(self):
        """Formatear JSON"""
        try:
            input_data = self.json_input.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa JSON para formatear")
                return
            
            # Parsear y formatear JSON
            json_data = json.loads(input_data)
            formatted = json.dumps(json_data, indent=2, ensure_ascii=False, sort_keys=True)
            
            self.json_output.delete("1.0", tk.END)
            self.json_output.insert("1.0", formatted)
            
        except json.JSONDecodeError as e:
            messagebox.showerror("Error", f"JSON inválido: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al formatear JSON: {str(e)}")
    
    def validate_json(self):
        """Validar JSON"""
        try:
            input_data = self.json_input.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa JSON para validar")
                return
            
            json.loads(input_data)
            messagebox.showinfo("Éxito", "JSON válido")
            
        except json.JSONDecodeError as e:
            messagebox.showerror("Error", f"JSON inválido: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al validar JSON: {str(e)}")
    
    def minify_json(self):
        """Minificar JSON"""
        try:
            input_data = self.json_input.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa JSON para minificar")
                return
            
            # Parsear y minificar JSON
            json_data = json.loads(input_data)
            minified = json.dumps(json_data, separators=(',', ':'), ensure_ascii=False)
            
            self.json_output.delete("1.0", tk.END)
            self.json_output.insert("1.0", minified)
            
        except json.JSONDecodeError as e:
            messagebox.showerror("Error", f"JSON inválido: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al minificar JSON: {str(e)}")
    
    def format_sql(self):
        """Formatear SQL"""
        try:
            input_data = self.sql_input.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa SQL para formatear")
                return
            
            # Formatear SQL usando sqlparse
            formatted = sqlparse.format(input_data, 
                                      reindent=True, 
                                      keyword_case='upper',
                                      identifier_case='lower')
            
            self.sql_output.delete("1.0", tk.END)
            self.sql_output.insert("1.0", formatted)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al formatear SQL: {str(e)}")
    
    def format_xml(self):
        """Formatear XML"""
        try:
            input_data = self.xml_input.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa XML para formatear")
                return
            
            # Parsear y formatear XML
            dom = xml.dom.minidom.parseString(input_data)
            formatted = dom.toprettyxml(indent="  ")
            
            # Remover la primera línea (declaración XML)
            lines = formatted.split('\n')
            if lines[0].startswith('<?xml'):
                lines = lines[1:]
            formatted = '\n'.join(lines).strip()
            
            self.xml_output.delete("1.0", tk.END)
            self.xml_output.insert("1.0", formatted)
            
        except xml.parsers.expat.ExpatError as e:
            messagebox.showerror("Error", f"XML inválido: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al formatear XML: {str(e)}")
    
    def validate_xml(self):
        """Validar XML"""
        try:
            input_data = self.xml_input.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa XML para validar")
                return
            
            xml.dom.minidom.parseString(input_data)
            messagebox.showinfo("Éxito", "XML válido")
            
        except xml.parsers.expat.ExpatError as e:
            messagebox.showerror("Error", f"XML inválido: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al validar XML: {str(e)}")
    
    def minify_xml(self):
        """Minificar XML"""
        try:
            input_data = self.xml_input.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Advertencia", "Por favor ingresa XML para minificar")
                return
            
            # Parsear XML
            dom = xml.dom.minidom.parseString(input_data)
            
            # Obtener el XML sin formateo
            minified = dom.toxml()
            
            self.xml_output.delete("1.0", tk.END)
            self.xml_output.insert("1.0", minified)
            
        except xml.parsers.expat.ExpatError as e:
            messagebox.showerror("Error", f"XML inválido: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al minificar XML: {str(e)}")
    
    def clear_json(self):
        """Limpiar JSON"""
        self.json_input.delete("1.0", tk.END)
        self.json_output.delete("1.0", tk.END)
    
    def clear_sql(self):
        """Limpiar SQL"""
        self.sql_input.delete("1.0", tk.END)
        self.sql_output.delete("1.0", tk.END)
    
    def clear_xml(self):
        """Limpiar XML"""
        self.xml_input.delete("1.0", tk.END)
        self.xml_output.delete("1.0", tk.END)
    
    def create_interface(self):
        """Crear la interfaz (método requerido por la aplicación principal)"""
        pass  # La interfaz ya se crea en __init__
