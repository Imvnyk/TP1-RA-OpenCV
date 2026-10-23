
import cv2

# Charger l'image de la machine
image = cv2.imread("images/machine.jpg")

# Vérifier que l'image est chargée
if image is None:
    print("Erreur : image introuvable !")
    exit()

# Position du moteur
x = 100
y = 115
w = 220
h = 185

# Activité 9 : Dessiner le rectangle
cv2.rectangle(
    image,
    (x, y),
    (x + w, y + h),
    (0, 255, 0),
    2
)

# Activité 10 : Identifier le moteur
cv2.putText(
    image,
    "MOTEUR",
    (x, y - 10),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 255, 0),
    2
)

# Activité 11 : Afficher la température
cv2.putText(
    image,
    "Temperature : 65 C",
    (x, y + h + 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (0, 255, 0),
    2
)

cv2.putText(
    image,
    "Etat : NORMAL",
    (x, y + h + 60),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (0, 255, 0),
    2
)

cv2.imshow("Premiere RA", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
