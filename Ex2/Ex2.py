print('Tabuada de qual numero? ')
aux = int(input())

print('Entre um Intervalo [x , y]')
print('X? ')
x = int(input())
print('Y? ')
y = int(input())


for i in range(x,y+1):
        print('Resultado de ', i , " * ", aux, ':', i*aux)