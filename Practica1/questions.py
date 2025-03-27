import random
# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
    "// Esto es un comentario",
    "/* Esto es un comentario */",
    "-- Esto es un comentario",
    "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# El usuario deberá contestar 3 preguntas

questions_to_ask = random.sample(list(zip(questions,answers,correct_answers_index)),k=3)
# La funcion sample funciona de la misma manera que la choices pero impide que se repitan elementos
puntaje = 0.0
exit_status = 0
for _ in range(3):
    if(exit_status!= 0):
        break
    # Se selecciona una pregunta aleatoria
    # Se muestra la pregunta y las respuestas posibles
    print(questions_to_ask[_][0])
    for i, answer in enumerate(questions_to_ask[_][1]):
        print(f"{i + 1}. {answer}")
        # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = (input("Respuesta: ")) # Verifico si la respuesta solo contiene digitos, de lo contrario termino el bucle
        if user_answer.isdigit() == True:
            user_answer= int(user_answer)-1
            # Se verifica si la respuesta es correcta
            if user_answer == questions_to_ask[_][2]:
                print("¡Correcto!")
                puntaje+=1
                print('') # Espacio vacio al final de la respuesta
                break
            elif user_answer >=0 and user_answer <=3:
                if intento == 0:
                    print('Incorrecto, Te queda 1 intento restante ')
                    print('Escribe nuevamente tu respuesta ')
                    puntaje-=0.5
                    continue
                # Si el usuario no responde correctamente después de 2 intentos,
                # se muestra la respuesta correcta
                print("Incorrecto. La respuesta correcta es:")
                print(f"{questions_to_ask[_][2]+1}. {questions_to_ask[_][1][questions_to_ask[_][2]]}")
                # Se imprime un blanco al final de la pregunta
                print()
                puntaje -=0.5
                break
            else:
                print('Respuesta invalida! ')
                exit_status = 1
                break
        else:
            print('Respuesta invalida')
            exit_status = 1
            break
print('Juego terminado. ')
print(f'Puntaje final: {puntaje}')
         
    
            
