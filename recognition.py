import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier("data\\xml\\haarcascade_frontalface_default.xml")
mouth_cascade = cv2.CascadeClassifier("data\\xml\\haarcascade_mcs_mouth.xml")
nose_cascade = cv2.CascadeClassifier("data\\xml\\haarcascade_mcs_nose.xml")


def update(img):
    img = cv2.flip(img, 1)
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

        # Draw rectangle on mouth
        for (x, y, w, h) in mouth_rects:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Draw rectangle on nose
        for (x, y, w, h) in nose_rects:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Draw rectangle on face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)

        status = True
        if not (len(mouth_rects) == 0 and len(nose_rects) == 0):
            for (mx, my, mw, mh) in mouth_rects:
                if y < my < y + h:
                    status = False
                    break
            for (mx, my, mw, mh) in nose_rects:
                if y < my < y + h:
                    status = False
                    break

    img = cv2.flip(img, 0)

    return img, status
