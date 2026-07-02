global_var = 'valor global'

def exemplo_local():

#variável local - só existe dentro desta função

    local_var = 'valor local'
    print('local_var:', local_var)

#acessar variável global para leitura funciona sem declarar "global"

    print('global var:', global_var)

#usar um built-in (len) 

    print('Built-in len(\'abc\'):', len('abc'))

def exemplo_modifica():

    #para modificar a variável global dentro da função, declarar "global"

    global global_var
    global_var = 'novo valor global'
    print('global_var modificado para:', global_var)

print('global_var (antes):', global_var)
exemplo_local()
exemplo_modifica()
print('global_var (depois):', global_var)