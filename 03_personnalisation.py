
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

x = 85
y = 130
w = 260
h = 220

cv2.rectangle(
    image,
    point(x, y),
    point(x + w, y + h),
    (255, 0, 0),
    3
)

cv2.putText(
    image,
    "MOTEUR PRINCIPAL",
    point(x, y - 15),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (255, 0, 0),
    2
)

cv2.putText(
    image,
    "Temperature : 80 C",
    point(x, y + h + 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (0, 0, 255),
    2
)

cv2.putText(
    image,
    "Etat : SURCHAUFFE",
    point(x, y + h + 60),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (0, 0, 255),
    2
)

cv2.imshow("Exercice 1 - Personnalisation", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
