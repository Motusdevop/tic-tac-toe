import pygame as pg

pg.init()

screen = pg.display.set_mode((900, 900))
pg.display.set_caption("Tic-Tac-Toe by Motus")
timer = pg.time.Clock()
icon = pg.image.load('table.png')
pg.display.set_icon(icon)

class Rects():
	def __init__(self, x, y):
		self.rect = pg.Rect(x, y, 150, 150)

	def collidepoint(self, x, y):
		return self.rect.collidepoint(x, y)


#Lib:
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
table = pg.transform.scale(pg.image.load("table.png"), (500, 500))
rects = [
	Rects(215, 214),
	Rects(375, 214),
	Rects(536, 214),
	Rects(215, 374),
	Rects(375, 374),
	Rects(536, 374),
	Rects(215, 537),
	Rects(375, 537),
	Rects(536, 537),
]

#varials:
play = True
FPS = 60
motion = True

while play:
	timer.tick(FPS)
	screen.fill(WHITE)
	screen.blit(table, (200, 200))

	for event in pg.event.get():
		if event.type == pg.QUIT:
			play = False
		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and motion:
			x, y = event.pos
			for rect in rects:
				if rect.collidepoint(x, y):
					print(x, y)

	pg.display.flip()

pg.quit()
