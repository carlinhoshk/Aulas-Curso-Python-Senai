# 15:05 - 26/01/2023

# logica and
resultado = (100 > 99) and (500<600)
if resultado==True:
    print('teste-true')
else:
    print('teste-false')    

resultado2 = ( 100 > 99) and (100 > 500)
print(resultado2)    

#Conversao de tipos , coerção, type convertion.
print(int('1'), type(int('1')))
print(type(float("1")))
soma = "5.5 + 5.5"
print(soma)

soma2 = 5.5 + 5.5
print(soma2)

var1 = float("5.5")
var2 = float("5.5")
soma_float = (var1+var2)
print(soma_float)

print(bool(1))
print(bool(0))

print(bool(' '))
print(str(11) + ' b')