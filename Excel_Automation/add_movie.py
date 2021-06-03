from openpyxl import load_workbook as lwb

wb = lwb('Excel_Automation/Movies_in_the_house.xlsx')
ws = wb.active

def add_movie(name, rated, disk_type):
	a = name
	b = rated.upper()
	c = disk_type

	while True:
		if not b == 'G' or b == 'PG' or b == 'PG-13' or b == 'R'or b == 'NR':
			b = input('Invalid rating; enter one of the following: G, PG, PG-13, R, NR: ')
		else:break
	while True:
		if c.lower() == 'dvd':
			x = ''
			y = ''
			z = 'X'
			break
		elif c.lower() == 'blu-ray' or c.lower == 'bluray':
			x = ''
			y = 'X'
			break
		elif c.lower == '4k':
			x = 'X'
			break
		else:
			print('Invalid disk type, please try again')	
			c = input('What type of disk is the movie on? DVD, Blu-ray/Bluray, or 4K ')
	
	ws.append([a, b, x, y, z])
	wb.save('Excel_Automation/Movies_in_the_house.xlsx')