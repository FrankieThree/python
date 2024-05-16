import pygame
import sys
import os

# code to add images to exe
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class LockBase(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(resource_path('Lock base.png'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class ShackleClosed(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(resource_path('ShackleClosed.png'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.hidden = False

class ShackleOpen(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(resource_path('ShackleOpen.png'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.hidden = True

class CombinationScreen(pygame.sprite.Sprite):
    def __init__(self, x, y, size = (350, 105)):
        super().__init__()
        self.input = ""
        self.font = pygame.font.Font(None, 140)
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.input = self.input[:-1]
            else:
                if(len(self.input) <= 5):
                    self.input += event.unicode

        self.render_text(self.input)

    def render_text(self, input, color = (255, 255, 255)):
        self.image.fill((0, 0, 0))
        text_surface = self.font.render(input, True, color)
        self.image.blit(text_surface, (5, 5))

class LockSprite(pygame.sprite.Group):
    def __init__(self,pygame):
        super().__init__()
        self.base = LockBase(250, -60)
        self.shackleClosed = ShackleClosed(250, -60)
        self.shackleOpen = ShackleOpen(250, -60)
        self.comboScreen = CombinationScreen(475, 350)

        self.add(self.base)
        self.add(self.shackleClosed)
        self.add(self.comboScreen)

        self.input_cooldown = 0

    def shackle(self):
        if(self.shackleClosed.hidden):
            self.remove(self.shackleOpen)
            self.add(self.shackleClosed)

            self.shackleClosed.hidden = False
            self.shackleOpen.hidden = True

    def unshackle(self):
        if(self.shackleOpen.hidden):
            self.remove(self.shackleClosed)
            self.add(self.shackleOpen)

            self.shackleClosed.hidden = True
            self.shackleOpen.hidden = False

    def update(self, event):
        if(self.input_cooldown != 0):
            current_time = pygame.time.get_ticks()
            if current_time > self.input_cooldown:
                self.comboScreen.update(event)
                self.input_cooldown = 0

        elif(self.input_cooldown == 0):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.check_combination()
                else:
                    self.comboScreen.update(event)

    def check_combination(self):
        if(self.comboScreen.input == "6H1Dr4"):
            self.comboScreen.render_text("OPEN!", (0, 250, 0))
            self.unshackle()
            if(self.input_cooldown == 0):
                self.input_cooldown = pygame.time.get_ticks() + 1000
        else:
            self.comboScreen.render_text("NOPE!", (255, 0, 0))
            #start a cooldown
            if(self.input_cooldown == 0):
                self.input_cooldown = pygame.time.get_ticks() + 1000
        
