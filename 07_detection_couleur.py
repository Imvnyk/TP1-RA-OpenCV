
import cv2
import numpy as np

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Erreur : impossible d'ouvrir la camera")
    exit()

while True:
    ret, frame = camera.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    rouge_min1 = np.array([0, 120, 70])
    rouge_max1 = np.array([10, 255, 255])

    rouge_min2 = np.array([170, 120, 70])
    rouge_max2 = np.array([180, 255, 255])

    masque1 = cv2.inRange(hsv, rouge_min1, rouge_max1)
    masque2 = cv2.inRange(hsv, rouge_min2, rouge_max2)

    masque = cv2.bitwise_or(masque1, masque2)

    contours, _ = cv2.findContours(
        masque,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        if cv2.contourArea(contour) > 1000:

            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                3
            )

            cv2.putText(
                frame,
                "OBJET DETECTE",
                (x, max(y - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "Etat : NORMAL",
                (x, min(y + h + 30, frame.shape[0] - 10)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    cv2.imshow("Exercice 7 - Detection couleur", frame)

    touche = cv2.waitKey(30) & 0xFF

    if touche == 27 or touche == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
