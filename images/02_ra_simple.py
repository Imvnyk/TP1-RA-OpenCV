
import cv2

# Charger l'image de la machine
image = cv2.imread("images/machine.jpg")

# Vérifier que l'image est chargée
if image is None:
    print("Erreur : image introuvable !")
    exit()

# Position et dimensions du rectangle
x = 400
y = 250
w = 250
h = 180

# Dessiner le rectangle vert
cv2.rectangle(
    image,
    (x, y),
    (x + w, y + h),
    (0, 255, 0),
    2
)

# Afficher le résultat
cv2.imshow("Premiere RA", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
