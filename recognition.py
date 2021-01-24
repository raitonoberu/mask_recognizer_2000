import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier("data\\xml\\haarcascade_frontalface_default.xml")
mouth_cascade = cv2.CascadeClassifier("data\\xml\\haarcascade_mcs_mouth.xml")
nose_cascade = cv2.CascadeClassifier("data\\xml\\haarcascade_mcs_nose.xml")


def update(img, face_color=(255, 255, 255), mouth_color=(0, 0, 255), nose_color=(0, 0, 255)):
    # Convert Image into gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detect face
    faces = face_cascade.detectMultiScale(gray)

    if len(faces) == 0:
        status = None
    else:
        # Detect lips counters
        mouth_rects = mouth_cascade.detectMultiScale(gray, 1.3, 5)
        # Detect nose counters
        nose_rects = nose_cascade.detectMultiScale(gray, 1.3, 5)

        # Draw rectangle on face
        for (fx, fy, fw, fh) in faces:
            if face_color:
                cv2.rectangle(img, (fx, fy), (fx + fw, fy + fh), face_color, 2)

        status = True
        if not (len(mouth_rects) == 0 and len(nose_rects) == 0):
            for (mx, my, mw, mh) in mouth_rects:
                if fy < my < fy + fh and fx < mx < fx + fw:
                    cv2.rectangle(img, (mx, my), (mx + mw, my + mh), mouth_color, 2)
                    status = False
                    break
            for (nx, ny, nw, nh) in nose_rects:
                if fy < ny < fy + fh and fx < nx < fx + fw:
                    cv2.rectangle(img, (nx, ny), (nx + nw, ny + nh), nose_color, 2)
                    status = False
                    break

    return img, status
