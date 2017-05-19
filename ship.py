import pygame
class Ship():
	def __init__(self , screen):
		
		self.screen = screen
		
		
		
		image_ship = pygame.image.load('images/ship.bmp')
		self.image = image_ship
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
	def blitme(self):
		
		
		self.screen.blit(self.image, self.rect)
	
