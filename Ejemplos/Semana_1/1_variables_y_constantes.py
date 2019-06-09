'''
    Author: Paolo
    EJEMPLO GLOBAL
'''

v_global = 10

def lee_v_global():
    print(v_global)

def escribe_v_global_y_no_funciona():
    v_global = 20    # Crea en realidad una local
    print(v_global)

def escribe_v_global_bien():
    global v_global    # Declaramos explícitamente la variable
    v_global = 20      # Ahora sí, asignamos la global

print(v_global) # Saldrá 10
lee_v_global()  # Saldrá 10

escribe_v_global_y_no_funciona()  # Saldrá 20
print(v_global) # Sigue siendo 10

escribe_v_global_bien()
print(v_global) #Saldra 20
