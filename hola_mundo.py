# 1. TAREA: imprime "Hola, mundo"
print( 'Hola, mundo' )
# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Mitchell"
print( 'Hola,' , name )	# con una coma
print( 'Hola, ' + name )	# con un +
# 3. imprimir "Hola 42!" con el número en una variable
name = 23
print( 'Hola' , name , '!' )	# con una coma
print( 'Hola ' + str(name) + '!' )	# con una +	-- este debería arrojar un error!
# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "lomo saltado"
fave_food2 = "ceviche"
print( 'Amo comer {} y {}'.format(fave_food1, fave_food2)) # con .format()
print(f'Amo comer {fave_food1} y {fave_food2}') # con una cadena f
# Bonus Ninja
track = 'Python'
year = 2022
print('Este es el track de %s de %d' % (track, year))

from string import Template

bootcamp = 'Coding Dojo'
template = Template('$name es genial')
print(template.substitute(name = bootcamp))