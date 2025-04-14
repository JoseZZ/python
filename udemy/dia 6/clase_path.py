from pathlib import Path

base = Path.home()
guia = Path(base, 'Barcelona', 'Sagrada_Familia')

print(base)
print(guia)

guia2 = guia.with_name("Casa_Batlló.txt")
print(guia2)

print(guia.parent)
print(guia.parent.parent)

guia3 = Path(Path.home(), 'Barcelona')
for txt in Path(guia).glob("*.txt"):
    print(txt)

guia3 = Path(Path.home(), 'Barcelona')
# incluye todas las carpetas y subcarpetas hasta llegar a todos
# los archivos .txt
for txt in Path(guia).glob("**/*.txt"):
    print(txt)

guia4 = Path("Europa", "España", "Barcelona", "Casa_Batlló.txt")
en_europa = guia4.relative_to(Path("Europa"))
en_espania = guia4.relative_to(Path("España"))

