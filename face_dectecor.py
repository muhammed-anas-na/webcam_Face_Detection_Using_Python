import cv2
face_face_data = cv2.CascadeClassifier('D:\works_2\Video_capture_face_detection\haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)
while True:
    sucessfull_frame_read,frame = webcam.read()

    gray_scale_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_face_data.detectMultiScale(gray_scale_image)

    print(faces)

    for (x,y,w,h) in faces:
        cv2.rectangle(gray_scale_image,(x,y),(x+w,y+h),(0,0,225),2)

    cv2.imshow('webcam',gray_scale_image)


    key=cv2.waitKey(1)   
    if key==81 or key==113:
        break 

    
webcam.release()
print('Code completed')