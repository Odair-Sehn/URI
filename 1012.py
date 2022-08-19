entry = input().split()
a, b, c = entry
triangulo = float(a) * float(c) / 2
circulo = 3.14159 * (float(c) * float(c))
trapezio = ((float(a) + float(b)) * float(c)) / 2
quadrado = float(b) * float(b)
retangulo = float(a) * float(b)
print('TRIANGULO: %.3f' % triangulo)
print('CIRCULO: %.3f' % circulo)
print('TRAPEZIO: %.3f' % trapezio)
print('QUADRADO: %.3f' % quadrado)
print('RETANGULO: %.3f' % retangulo)