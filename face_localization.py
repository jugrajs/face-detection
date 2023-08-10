import cv2


face_cascade= cv2.CascadeClassifier('path/haarcascade_frontalface_default.xml')


def localize_face(img, sf=1.2, nb=5):
    face_img= img #cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    face_dims= []
    
    face_localizer= face_cascade.detectMultiScale(face_img, sf, nb)
    count= len(face_localizer)

    for x,y,w,h in face_localizer:
        #count +=1
        face_dims.append((x,y,w,h))
        face_rect= cv2.rectangle(face_img, (x, y), (x+w,y+h), (255,0,0), 5)

    return face_rect, face_dims, count

if __name__ == "__main__":
    DEFAULT_CAMERA= 0
    vid= cv2.VideoCapture(DEFAULT_CAMERA)
    
    while True:

        bol, frame= vid.read()

        if bol:
            k= cv2.waitKey(1)

            frame, dims, count= localize_face(frame)
            cv2.imshow("video", frame)

            if k == 27:
                break

        
    vid.release()
    cv2.destroyAllWindows()


