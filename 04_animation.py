
import cv2

image = cv2.imread("images/machine.jpg")

if image is None:
    print("Erreur : image introuvable !")
    exit()

hauteur, largeur = image.shape[:2]

w = 300
h = 300

x = 0
y = (hauteur - h) // 2

while x + w < largeur:

    frame = image.copy()

    cv2.rectangle(
        frame,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        "MOTEUR",
        (x + 20, y + 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 0),
        2
    )

    cv2.putText(
        frame,
        "Temperature : 65 C",
        (x + 20, y + 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 0),
        2
    )

    cv2.putText(
        frame,
        "Etat : NORMAL",
        (x + 20, y + 140),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 0),
        2
    )

    cv2.imshow("RA animee", frame)

    x += 5

    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()
