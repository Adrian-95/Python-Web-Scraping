from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import datetime
import pprint
import sys
pp = pprint.PrettyPrinter(indent=5)

def main(): # Main function
	current_year = int(datetime.datetime.now().year)
	for year in range(2000, current_year+1):
		sys.stdout = open('data//IMDB_oscar_winner' + str(year) + '.txt', 'w')
		url = "http://www.imdb.com/search/title?release_date=" + str(year) + "," + str(year) + "&groups=oscar_winner"
		html = urlopen(url)
		soup = BeautifulSoup(html.read(), features="html.parser")
		dataset_oscar_winner = {}
		id = 1
		movies_list = soup.findAll('div', attrs={'class': 'lister-item-content'})
		for each in movies_list:

			# Movie details
			movie_item = {
				'name': '',
				'runtime': '',
				'genre': '',
				'description': '',
			}

			if each.find('h3', attrs={'class': 'lister-item-header'}).find('a').text:
				name_value = each.find('h3', attrs={'class': 'lister-item-header'}).find('a').text.strip()
				movie_item['name'] = name_value

			p_list = each.findAll('p')

			if p_list[0]:
				if p_list[0].find('span', attrs={'class': 'runtime'}):
					runtime_value = p_list[0].find('span', attrs={'class': 'runtime'}).text.strip()
					movie_item['runtime'] = runtime_value

				if p_list[0].find('span', attrs={'class': 'genre'}):
					genre_value = p_list[0].find('span', attrs={'class': 'genre'}).text.strip()
					movie_item['genre'] = genre_value

			if p_list[1]:
				description_value = p_list[1].text.strip()
				movie_item['description'] = description_value

			dataset_oscar_winner[id] = movie_item
			id += 1

		pp.pprint(dataset_oscar_winner)
		print(json.dumps(dataset_oscar_winner, indent=5))

	# End of  main 


main() # Call main 