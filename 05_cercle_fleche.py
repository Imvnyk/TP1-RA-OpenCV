
import cv2

image = cv2.imread("images/machine.jpg")

if image is None:
    print("Erreur : image introuvable !")
    exit()

hauteur, largeur = image.shape[:2]

sx = largeur / 640
sy = hauteur / 640

def point(x, y):
    return (int(x * sx), int(y * sy))

centre = point(210, 210)
rayon = int(115 * min(sx, sy))

deplacement = 0
direction = 1

while True:
    frame = image.copy()

    cv2.circle(frame, centre, rayon, (0, 255, 0), 3)

    depart = point(370, 90 + deplacement)
    arrivee = point(280, 170 + deplacement)

    cv2.arrowedLine(
        frame,
        depart,
        arrivee,
        (0, 0, 255),
        4,
        tipLength=0.2
    )

    cv2.imshow("Exercice 5 - Cercle et fleche", frame)

    deplacement += direction * 2

    if deplacement >= 30 or deplacement <= -30:
        direction *= -1

    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()
