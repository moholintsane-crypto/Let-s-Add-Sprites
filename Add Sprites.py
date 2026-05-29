import pygame

# Define a Player sprite class that inherits from pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Initialize the parent Pygame Sprite class 
        super().__init__()
        # Create a surface for the sprite (e.g., a 50width x 50height pixel box)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255) + (0, 255, 0))  # Fills the sprite with blue and 
                                                      # green colors inside the box  
        
        # Get or fetch the bounding rectangle object of the 
        # sprite surface that has dimensions of the image
        self.rect = self.image.get_rect()

        # Set the initial position of the sprite
        self.rect.x = x
        self.rect.y = y

        # Set the speed of the sprite movement property
        self.speed = 5

    def update(self):
        # Basic logic to control handle movements for the sprite 
        # horizontally and vertically based on key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
