
import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Erreur : impossible d'ouvrir la camera")
    exit()

while True:
    ret, frame = camera.read()

    if not ret:
        print("Erreur : image non capturee")
        break

    hauteur, largeur = frame.shape[:2]

    x = largeur // 2 - 150
    y = hauteur // 2 - 100
    w = 300
    h = 200

    cv2.rectangle(
        frame,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        3
    )

    cv2.putText(
        frame,
        "MOTEUR",
        (x, y - 15),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        "Temperature : 65 C",
        (x + 10, y + 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        "Etat : NORMAL",
        (x + 10, y + 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )

    cv2.imshow("Exercice 6 - RA Camera", frame)

    touche = cv2.waitKey(30) & 0xFF

    if touche == 27 or touche == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
