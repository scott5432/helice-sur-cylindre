import numpy as np                # Importation de la bibliothèque NumPy pour effectuer des calculs mathématiques
import matplotlib.pyplot as plt  # Importation de la bibliothèque Matplotlib pour créer des graphiques
from mpl_toolkits.mplot3d import Axes3D  # Importation de la classe Axes3D de la bibliothèque mpl_toolkits.mplot3d pour les graphiques en 3D


# Paramétrage de l'hélice et du cylindre
rayon_cylindre = 2.0
hauteur_cylindre = 3.0
nombre_de_points = 150

# les coordonnées de l'hélice
theta = np.linspace(0, 2 * np.pi, nombre_de_points)  # Angles theta de 0 à 2pi
h = np.linspace(0, hauteur_cylindre, nombre_de_points)  # Coordonnées h sur la hauteur du cylindre
r = np.linspace(0, rayon_cylindre, nombre_de_points)  # Coordonnées r sur le rayon du cylindre
x = r * np.cos(theta)  # Coordonnées x en fonction de r et theta
y = r * np.sin(theta)  # Coordonnées y en fonction de r et theta

# Céation de la figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # création un sous-ensemble d'axes en 3D dans la figure

# traçage de l'hélice sur le cylindre
ax.scatter(x, y, h, c='b', marker='.')  # Traçage des points de l'hélice en bleu

# Configuration des limites des axes
ax.set_xlim(-rayon_cylindre, rayon_cylindre)  # Limite des valeurs x
ax.set_ylim(-rayon_cylindre, rayon_cylindre)  # Limite des valeurs y
ax.set_zlim(0, hauteur_cylindre)  # Limite des valeurs h

# Affichage de la figure
plt.show()
