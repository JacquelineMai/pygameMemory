import pygame

class Card():
	def __init__(self, img_id, size, x_coord = -1, y_coord = -1):
		self.img_id = img_id
		self.x = x_coord
		self.y = y_coord
		self.size = size
		self.rect = pygame.Rect(self.x,self.y,size,size)
		self.face_up = False
		self.solved = False
	def flip(self):
		self.face_up = not(self.face_up)
	def detectMouse(self):
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			if pygame.mouse.get_pressed()[0] and not(self.solved):
				self.flip()
				pygame.time.delay(500)
#				self.flip()
				
