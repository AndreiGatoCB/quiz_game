class QuizBrain:

    def __init__(self, p_lista):
        self.numero_pregunta = 0
        self.puntaje = 0
        self.lista_pregunta = p_lista

    def aun_hay_preguntas(self):
        if self.numero_pregunta < len(self.lista_pregunta):
            return True
        else:
            return False

    def siguiente_pregunta(self):
        pregunta_actual = self.lista_pregunta[self.numero_pregunta]
        self.numero_pregunta += 1
        respuesta_usuario = (input(f"P.{self.numero_pregunta}: {pregunta_actual.texto} (Verdadero/Falso): "))
        self.revisa_pregunta(respuesta_usuario, pregunta_actual.respuesta)

    def revisa_pregunta(self, respuesta_usuario, respuesta_correcta):
        if respuesta_usuario.lower() == respuesta_correcta.lower():
            self.puntaje += 1
            print("Tienes razón.")
        else:
            print("Estás equivocado.")
        print(f"La respuesta correcta era: {respuesta_correcta}.")
        print(f"Tu puntaje actual es: {self.puntaje}/{self.numero_pregunta}\n")
