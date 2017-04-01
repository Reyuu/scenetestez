import pygame
import ezpygame
import math

class Player:
    def __init__(self, pos):
        self.pos = pos
        self.surf = pygame.Surface((16, 16))
        self.surf.fill((144, 12, 66))

class Game(ezpygame.Scene):
    def __init__(self):
        self.player = Player((int(640/2),int(480/2)))
        self.draw_index = 0
        self.faster = 0
        self.offset = 0
        self.font = pygame.font.SysFont("Monospace", size=10)
    def on_enter(self, previous_scene):
        self.previous_scene = previous_scene
        self.application.title = "Game(1)"
    def draw(self, scene):
        scene.fill((0,0,0))
        #self.draw_index += 1
        #scene.blit(self.player.surf, self.player.pos)
        previous = 0
        for i in range(0, 640, 6):
            pygame.draw.rect(scene, (255,0,0), (i, int(640/2)+int(math.sin(i+self.draw_index)*100)+self.offset, 2, 2))
            pygame.draw.line(scene, (0,0,255), (previous, int(640/2)+int(math.sin(previous+self.draw_index)*100)+self.offset), (i, int(640/2)+int(math.sin(i+self.draw_index)*100)+self.offset))
            previous = [i][0]
        pygame.display.flip()
    def update(self, dt):
        self.draw_index += 0.2+self.faster
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.offset += 5
            if event.key == pygame.K_DOWN:
                self.offset -= 5
            if event.key == pygame.K_LEFT:
                self.faster -= 0.1
            if event.key == pygame.K_RIGHT:
                self.faster += 0.1

app = ezpygame.Application(
    title='Test',
    resolution=(640, 480),
    update_rate=60,
)
app.run(Game())
