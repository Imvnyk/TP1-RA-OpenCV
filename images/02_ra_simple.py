
import cv2

image = cv2.imread("images/machine.jpg")

if image is None:
    print("Erreur : image introuvable !")
    exit()

# Adapter les coordonnees a la taille de l'image
hauteur, largeur = image.shape[:2]
sx = largeur / 640
sy = hauteur / 640

def point(x, y):
    return (int(x * sx), int(y * sy))

def texte(contenu, x, y, couleur):
    cv2.putText(
        image, contenu, point(x, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55, couleur, 2
    )

# Premier composant : moteur
cv2.rectangle(
    image, point(100, 115), point(320, 300),
    (0, 255, 0), 2
)

texte("MOTEUR", 100, 105, (0, 255, 0))
texte("Temperature : 65 C", 100, 330, (0, 180, 0))
texte("Etat : NORMAL", 100, 355, (0, 180, 0))

# Deuxieme composant : poulie
cv2.rectangle(
    image, point(400, 270), point(535, 455),
    (0, 0, 255), 2
)

texte("POULIE", 400, 260, (0, 0, 255))
texte("Temperature : 45 C", 390, 480, (0, 0, 255))
texte("Etat : NORMAL", 390, 505, (0, 0, 255))


cv2.putText(
    image,
    "Vitesse : 1500 RPM",
    point(100, 380),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.55,
    (0, 180, 0),
    2
)
 
cv2.imshow("RA - Deux composants", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
