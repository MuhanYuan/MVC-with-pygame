import pygame
import view
import model

pygame.init()

screen = pygame.display.set_mode((1200, 800))

pygame.display.set_caption("Election Data Viewer")
pygame.display.update()

party = "dem"
raw = True
sortas = True

data = model.get_data(party=party, raw=raw, sort_ascending=sortas)
bc = view.BarChart(pygame.Rect(50,50,1100,800), values=data,plot_area_width_ratio=0.9,ticks=5,max_val=10000000)
button1 = view.Button("dem",pygame.Rect(bc.rect.width-100 ,50, 50, 20))
button2 = view.Button("gop",pygame.Rect(bc.rect.width-100 ,70, 50, 20))

button3 = view.Button("up",pygame.Rect(bc.rect.width-100 ,120, 50, 20))
button4 = view.Button("down",pygame.Rect(bc.rect.width-100 ,140, 50, 20))

button5 = view.Button("raw",pygame.Rect(bc.rect.width-100 ,190, 50, 20))
button6 = view.Button("%",pygame.Rect(bc.rect.width-100 ,210, 50, 20))
# display loop

b1c = view.RED
b2c = view.GRAY
b3c = view.RED
b4c = view.GRAY
b5c = view.RED
b6c = view.GRAY
mv = 10000000

done = False
while not done:
	screen.fill(view.BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		else:
			button1.handle_event(event)
			if button1.chosen == True:
				b1c = view.RED
				b2c = view.GRAY
				party = "dem"
				data = model.get_data(party=party, raw=raw, sort_ascending=sortas)
				bc = view.BarChart(pygame.Rect(50,50,1100,800), values=data,plot_area_width_ratio=0.9,ticks=5, max_val = mv)
				button2.chosen = False

			button2.handle_event(event)
			if button2.chosen == True:
				b2c = view.RED
				b1c = view.GRAY
				party = "gop"
				data = model.get_data(party=party, raw=raw, sort_ascending=sortas)
				bc =view.BarChart(pygame.Rect(50,50,1100,800), values=data,plot_area_width_ratio=0.9,ticks=5, max_val = mv)
				button1.chosen = False
				# break
			button3.handle_event(event)
			if button3.chosen == True:
				b3c = view.RED
				b4c = view.GRAY
				sortas = True
				data = model.get_data(party=party, raw=raw, sort_ascending=sortas)
				bc = view.BarChart(pygame.Rect(50,50,1100,800), values=data,plot_area_width_ratio=0.9,ticks=5, max_val = mv)
				button4.chosen = False
				# break
			button4.handle_event(event)
			if button4.chosen == True:
				b4c = view.RED
				b3c = view.GRAY
				sortas = False
				data = model.get_data(party=party, raw=raw, sort_ascending=sortas)
				bc = view.BarChart(pygame.Rect(50,50,1100,800), values=data,plot_area_width_ratio=0.9,ticks=5, max_val = mv)
				button3.chosen = False
				# break
			button5.handle_event(event)
			if button5.chosen == True:
				b5c = view.RED
				b6c = view.GRAY
				raw = True
				mv = 10000000
				data = model.get_data(party=party, raw=raw, sort_ascending=sortas)
				bc =view.BarChart(pygame.Rect(50,50,1100,800), values=data,plot_area_width_ratio=0.9,ticks=5,max_val = mv)
				button6.chosen = False
				# break
			button6.handle_event(event)
			if button6.chosen == True:
				b6c = view.RED
				b5c = view.GRAY
				raw = False
				mv = 1
				data = model.get_data(party=party, raw=raw, sort_ascending=sortas)
				bc = view.BarChart(pygame.Rect(50,50,1100,800), values=data,plot_area_width_ratio=0.9,ticks=5, max_val = mv)
				button5.chosen = False
				# break



	bc.draw(screen)
	button1.draw(screen,b1c)
	button2.draw(screen,b2c)
	button3.draw(screen,b3c)
	button4.draw(screen,b4c)
	button5.draw(screen,b5c)
	button6.draw(screen,b6c)

	pygame.display.update()
