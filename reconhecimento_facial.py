import face_recognition
import cv2
import time
import RPi.GPIO as GPIO


#####		Pinos

GPIO.setmode(GPIO.BOARD)

LED_verde = 12
LED_vermelho = 22
GPIO.setup(LED_verde, GPIO.OUT)
GPIO.setup(LED_vermelho, GPIO.OUT)

botao = 18
GPIO.setup(botao, GPIO.IN)


#####		Rostos

pessoa1 = face_recognition.load_image_file("/home/pedro/Documents/fotos_reconhecimento/eu_1.jpg")
pessoa2 = face_recognition.load_image_file("/home/pedro/Documents/fotos_reconhecimento/mae_1.jpg")

pessoa1_cod = face_recognition.face_encodings(pessoa1)[0]
pessoa2_cod = face_recognition.face_encodings(pessoa2)[0]
faces_conhecidas = [pessoa1_cod, pessoa2_cod]

#####		Reconhecimento facial

while True:
	if GPIO.input(botao) == 1:
		cap = cv2.VideoCapture(0)
		while True:

			ret, frame = cap.read()
			rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			face_locations = face_recognition.face_locations(rgb_frame)
			face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

			for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
				matches = face_recognition.compare_faces(faces_conhecidas, face_encoding)

#####		Emissão do sinal

				if True in matches:
					GPIO.output(LED_verde, True)
					GPIO.output(LED_vermelho, False)

				else:
					GPIO.output(LED_verde, False)
					GPIO.output(LED_vermelho, True)
					

#####		Verificação do acionamento do botão e desligamento dos LEDs
	
			if GPIO.input(botao) == 0:
				GPIO.output(LED_verde, False)
				GPIO.output(LED_vermelho, False)
				break	
		
			time.sleep(1)
		cap.release()
