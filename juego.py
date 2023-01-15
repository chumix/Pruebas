import pygame

# Inicializar Pygame
pygame.init()

# Establecer tamaño de la ventana
screen = pygame.display.set_mode((400, 300))

# Establecer título de la ventana
pygame.display.set_caption("Juego de laberinto")

# Establecer posición inicial del personaje
x = 50
y = 50

# Establecer velocidad del personaje
velocidad = 5

# Crear un bucle de juego
running = True
while running:
    # Obtener eventos de teclado y ratón
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener entrada del teclado
    keys = pygame.key.get_pressed()

    # Mover personaje según la entrada del teclado
    if keys[pygame.K_LEFT]:
        x -= velocidad
    if keys[pygame.K_RIGHT]:
        x += velocidad
    if keys[pygame.K_UP]:
        y -= velocidad
    if keys[pygame.K_DOWN]:
        y += velocidad

    # Limitar movimiento del personaje dentro de la pantalla
    if x > 350:
        x = 350
    if x < 0:
        x = 0
    if y > 250:
        y = 250
    if y < 0:
        y = 0

    # Borrar pantalla
    screen.fill((0, 0, 0))

    # Dibujar personaje en la nueva posición
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))

    # Actualizar pantalla
    pygame.display.update()

# Finalizar Pygame
pygame.quit()
