# Aplica a index.html el saludo por nombre de pila (nombre_pila.js). Seguro de repetir.
import re, sys
p = 'index.html'; s = open(p, encoding='utf-8').read()
base = sys.argv[1] if len(sys.argv) > 1 else 'AN'
n1 = s.count("name.split(' ')[0]")
s = re.sub(r"\b(st|s)\.name\.split\(' '\)\[0\]", lambda m: 'nombrePila(' + m.group(1) + '.name)', s)
s, n2 = re.subn(r"const primerNombre = n => String\(n \|\| ''\)\.trim\(\)\.split\(/\\s\+/\)\[0\] \|\| '';", "const primerNombre = n => nombrePila(n);", s)
if 'nombre_pila.js' not in s:
    s = s.replace('</head>', '<script>window.NOMBRE_ORDEN_BASE="%s";</script><script src="nombre_pila.js?v=1"></script></head>' % base, 1)
open(p, 'w', encoding='utf-8').write(s)
print('reemplazos', n1, n2, 'script', 'nombre_pila.js' in s)
if n1 + n2 == 0 and 'nombrePila(' not in s: sys.exit('parche sin efecto')
