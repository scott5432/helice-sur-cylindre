import numpy as np
import matplotlib.pyplot as plt

# Paramètres de l'hélice
rayon_cylindre = 1.0
hauteur_cylindre = 2.0
nombre_de_points = 100

# Générer les coordonnées de l'hélice
theta = np.linspace(0, 2 * np.pi, nombre_de_points)
z = np.linspace(0, hauteur_cylindre, nombre_de_points)
r = np.linspace(0, rayon_cylindre, nombre_de_points)
x = r * np.cos(theta)
y = r * np.sin(theta)

# Créer la figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tracer l'hélice sur le cylindre
ax.plot(x, y, z, 'b.')

# Configurer les limites des axes
ax.set_xlim(-rayon_cylindre, rayon_cylindre)
ax.set_ylim(-rayon_cylindre, rayon_cylindre)
ax.set_zlim(0, hauteur_cylindre)

# Afficher la figure
plt.show()
