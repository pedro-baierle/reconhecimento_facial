import face_recognition
import cv2
import time

#########################################################

eu  = face_recognition.load_image_file("/home/reconhecimento_facial/eu_1.jpg")


eu_encoding = face_recognition.face_encodings(eu)[0]
faces_conhecidas = [eu_encoding]
known_face_names = ['Pedro']

############################################################


while True:
	cap = cv2.VideoCapture(0)
	ret, frame = cap.read()

	rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	face_locations = face_recognition.face_locations(rgb_frame)
	face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

	for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
		matches = face_recognition.compare_faces(faces_conhecidas, face_encoding)
		
########################################################################### 
		if True in matches:
			print('rosto conhecido')
	time.sleep(1)
	cap.release()
