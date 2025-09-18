# DevTools Suite

Una aplicación de escritorio inspirada en DevToys que proporciona herramientas útiles para desarrolladores.

## Características

La aplicación incluye las siguientes categorías de herramientas:

### 🔄 Convertidores
- **JSON ↔ YAML**: Convierte entre formatos JSON y YAML
- **Base64 Texto**: Codifica y decodifica texto en Base64
- **Conversión de Números**: Convierte entre diferentes bases numéricas (decimal, binario, octal, hexadecimal)

### 🔐 Codificadores
- **JWT Decoder**: Decodifica y valida tokens JWT
- **URL Encoder/Decoder**: Codifica y decodifica URLs
- **HTML Encoder/Decoder**: Codifica y decodifica entidades HTML

### 🔑 Generadores
- **Generador de Contraseñas**: Genera contraseñas seguras con configuraciones personalizables
- **Generador de UUID**: Genera identificadores únicos universales (v1 y v4)
- **Generador de Hash**: Genera hashes MD5, SHA1, SHA256, SHA512

### 📋 Formateadores
- **Formateador JSON**: Formatea, valida y minifica JSON
- **Formateador SQL**: Formatea consultas SQL
- **Formateador XML**: Formatea, valida y minifica XML

### 📊 Utilidades de Texto
- **Comparador de Texto**: Compara dos textos y muestra diferencias
- **Escape/Unescape**: Escapa y desescapa caracteres especiales (JSON, Regex)
- **Analizador de Texto**: Analiza estadísticas del texto (caracteres, palabras, frecuencia)

### 🖼️ Gráficos
- **Convertidor de Imágenes**: Convierte entre formatos de imagen (PNG, JPG, BMP, GIF, TIFF)
- **Generador de QR**: Genera códigos QR
- **Simulador de Daltonismo**: Simula diferentes tipos de daltonismo

## Instalación

### Requisitos
- Python 3.7 o superior
- tkinter (incluido con Python)

### Pasos de instalación

1. **Clona o descarga el proyecto**
   ```bash
   git clone <url-del-repositorio>
   cd devtools-suite
   ```

2. **Instala las dependencias básicas**
   ```bash
   pip install pyyaml sqlparse
   ```

3. **Instala dependencias opcionales (para funcionalidades avanzadas)**
   ```bash
   pip install Pillow qrcode PyJWT opencv-python colorspacious
   ```

   O instala todas las dependencias de una vez:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Ejecutar la aplicación

```bash
python main.py
```

### Navegación

1. **Panel lateral**: Selecciona una categoría de herramientas
2. **Panel principal**: Haz clic en cualquier herramienta para abrirla
3. **Ventanas de herramientas**: Cada herramienta se abre en una ventana separada con pestañas para diferentes funciones

### Funcionalidades principales

- **Interfaz moderna**: Diseño limpio inspirado en DevToys
- **Herramientas organizadas**: Categorías claras para fácil navegación
- **Ventanas modales**: Cada herramienta se abre en su propia ventana
- **Validación de entrada**: Verificación de datos de entrada con mensajes de error claros
- **Resultados en tiempo real**: Conversiones y análisis instantáneos

## Estructura del proyecto

```
devtools-suite/
├── main.py                 # Aplicación principal
├── requirements.txt        # Dependencias
├── README.md              # Este archivo
└── tools/                 # Módulos de herramientas
    ├── __init__.py
    ├── converters.py      # Herramientas de conversión
    ├── encoders.py        # Herramientas de codificación
    ├── generators.py      # Herramientas de generación
    ├── formatters.py      # Herramientas de formateo
    ├── text_utils.py      # Utilidades de texto
    └── graphics.py        # Herramientas gráficas
```

## Dependencias

### Básicas (requeridas)
- `pyyaml`: Para conversión JSON/YAML
- `sqlparse`: Para formateo de SQL

### Opcionales (para funcionalidades avanzadas)
- `Pillow`: Para conversión de imágenes
- `qrcode`: Para generación de códigos QR
- `PyJWT`: Para decodificación de JWT
- `opencv-python`: Para procesamiento de imágenes
- `colorspacious`: Para simulación de daltonismo

## Solución de problemas

### Error: "ModuleNotFoundError"
Si encuentras errores de módulos no encontrados:

1. Verifica que Python esté instalado correctamente
2. Instala las dependencias básicas:
   ```bash
   pip install pyyaml sqlparse
   ```
3. Para funcionalidades específicas, instala las dependencias opcionales correspondientes

### Error: "tkinter no encontrado"
En algunos sistemas Linux, tkinter puede no estar instalado por defecto:

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**CentOS/RHEL:**
```bash
sudo yum install tkinter
```

### La aplicación no se ejecuta
1. Verifica que estés en el directorio correcto
2. Asegúrate de que `main.py` existe
3. Verifica que todas las dependencias estén instaladas

## Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-herramienta`)
3. Commit tus cambios (`git commit -am 'Agrega nueva herramienta'`)
4. Push a la rama (`git push origin feature/nueva-herramienta`)
5. Crea un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Créditos

Inspirado en [DevToys](https://github.com/veler/DevToys) - Una herramienta de desarrollador para Windows.
