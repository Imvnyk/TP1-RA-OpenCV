
from vpython import *
import math

scene = canvas(
    title="Exercice 8 - Jumeau numerique d'un moteur",
    width=800,
    height=500,
    background=color.white
)

scene.center = vector(0, 0.5, 0)

socle = box(
    pos=vector(0, -0.5, 0),
    size=vector(5, 0.3, 3),
    color=color.gray(0.6)
)

moteur = cylinder(
    pos=vector(-1.5, 0, 0),
    axis=vector(3, 0, 0),
    radius=0.8,
    color=color.blue
)

axe = cylinder(
    pos=vector(1.5, 0, 0),
    axis=vector(1, 0, 0),
    radius=0.15,
    color=color.gray(0.5)
)

voyant = sphere(
    pos=vector(0, 1.5, 0),
    radius=0.2,
    color=color.green,
    emissive=True
)

info = label(
    pos=vector(0, 2.3, 0),
    text="",
    height=15,
    color=color.black,
    box=False
)

temperature = 25
vitesse = 1000
temps = 0

while True:
    rate(10)

    temps += 0.1

    temperature = 25 + 60 * abs(math.sin(temps / 10))
    vitesse = 1000 + 500 * math.sin(temps / 5)

    if temperature >= 75:
        moteur.color = color.red
        voyant.color = color.red
        etat = "ALERTE"
    else:
        moteur.color = color.blue
        voyant.color = color.green
        etat = "NORMAL"

    info.text = (
        "MOTEUR INDUSTRIEL\n"
        f"Temperature : {temperature:.1f} C\n"
        f"Vitesse : {vitesse:.0f} RPM\n"
        f"Etat : {etat}"
    )
