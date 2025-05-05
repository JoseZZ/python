from collections import Counter, defaultdict, namedtuple, deque

numeros = [8,6,5,4,3,3,4,6,7,8,9,8,6,5,4,3,3,4,6,7,8,9,8,6,5,4,3,3,4,6,7,8,9]

print(Counter(numeros))
print("El número 8 aparece: ", Counter(numeros)[8], " veces")
print(Counter("Mississipi"))
frase = "Al pan pan y al vino vino"
print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6])
print(serie.most_common(2))
print(list(serie))

mi_dic = {"uno":"verde", "dos":"rojo", "tres":"azul"}
otro_dic = defaultdict(lambda :"nada")
otro_dic["uno"] = "verde"
print(otro_dic["turron"])
print(otro_dic)

mi_tupla = (500,18,27)
Persona = namedtuple("Persona", ["nombre", "edad", "altura"])
juan = Persona("Juan", 18, 1.75)
print(juan)
print(juan.nombre)
print(juan.edad)
print(juan.altura)
print(juan[2])


d = deque('ghi')                 # make a new deque with three items
for elem in d:                   # iterate over the deque's elements
    print(elem.upper())

d.append('j')                    # add a new entry to the right side
d.appendleft('f')                # add a new entry to the left side

d.pop()                          # return and remove the rightmost item

d.popleft()                      # return and remove the leftmost item

list(d)                          # list the contents of the deque

d[0]                             # peek at leftmost item

d[-1]                            # peek at rightmost item


list(reversed(d))                # list the contents of a deque in reverse

'h' in d                         # search the deque

d.extend('jkl')                  # add multiple elements at once

d.rotate(1)                      # right rotation
d.rotate(-1)                     # left rotation

deque(reversed(d))               # make a new deque in reverse order

d.clear()                        # empty the deque
d.pop()                          # cannot pop from an empty deque
d.extendleft('abc')              # extendleft() reverses the input order