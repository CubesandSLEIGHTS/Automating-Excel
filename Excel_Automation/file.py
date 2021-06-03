from openpyxl import load_workbook as lwb
from Error_message import valid_input
from add_movie import add_movie

we_have_it = False

wb = lwb('Excel_Automation/Movies_in_the_house.xlsx')
ws = wb.active

while True:
	trying_to_find=valid_input(input('Are you trying to find a movie? Enter yes or no: '))
	if trying_to_find:break
print()

if trying_to_find.lower() in 'yyes':
	name=input('What movie are you looking for? ')
	print()
	for row in ws.iter_rows(min_row=2, max_col=1, max_row=520):
			for cell in row:
				if cell.value == name:
					print('We have it!')
					print()
					we_have_it = True
	if we_have_it == False:
		print('We don\'t have it.', end=" ")
		while True:
			add=valid_input(input('Do you want to add it to the movie collection? Enter yes or no: '))
			if add:break
		print()
		if add in 'yyes':
			rated = input('What is the movie rated? G, PG, PG-13, R, NR: ')
			print()
			disk_type = input('What type of disk is the movie on? DVD, Blu-ray/Bluray, or 4K ')
			print()
			add_movie(name, rated, disk_type)
				#print(cell.value)
else:
	while True:
		add_a_movie=valid_input(input('Are you trying to add a movie? Enter yes or no: '))
		if add_a_movie:break
	if add_a_movie == 1:
		add_movie()