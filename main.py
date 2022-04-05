from question_model import Pregunta
from data import data_2
from quiz_brain import QuizBrain

banco_de_preguntas = []

for pregunta in data_2:
    texto_pregunta = pregunta["pregunta"]
    rta_pregunta = pregunta["respuesta"]
    pregunta_nueva = Pregunta(texto_pregunta, rta_pregunta)
    banco_de_preguntas.append(pregunta_nueva)

quiz = QuizBrain(banco_de_preguntas)

while quiz.aun_hay_preguntas():
    quiz.siguiente_pregunta()

print("Has completado el quiz.")
print(f'Tu puntaje final es: {quiz.puntaje}/{quiz.numero_pregunta}')
