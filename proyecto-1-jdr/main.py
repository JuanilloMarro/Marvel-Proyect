import sys
import requests
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPalette, QColor

ts = 1
new_public_key = "57cb5ae41e9c6b861edbabaa11d0142e"
new_private_key = "b3ae51f4c3455d0917df338d4a4c24754c43633a"
new_hashed = "b151e8397ef1bbbbee4d6975595fe07e"
#1b3ae51f4c3455d0917df338d4a4c24754c43633a57cb5ae41e9c6b861edbabaa11d0142e

class ColorWidget(QWidget):
	def __init__(self, color):
		super(ColorWidget, self).__init__()
		self.setAutoFillBackground(True)

		pallete = self.palette()
		pallete.setColor(QPalette.ColorRole.Window, QColor(color))
		self.setPalette(pallete)


class DetailsWindowCharacter(QMainWindow):
	def __init__(self):
		super().__init__()

		self.id = 1009146

		self.characters = requests.get(
			f"https://gateway.marvel.com:443/v1/public/characters/{self.id}"
			f"?ts=1&apikey=57cb5ae41e9c6b861edbabaa11d0142e&hash=b151e8397ef1bbbbee4d6975595fe07e").json()

		self.superheroes = self.characters['data']['results']

		self.layout_principal = QVBoxLayout()

		self.layout_details = QVBoxLayout()
		self.layout_image = QVBoxLayout()
		self.layout_name = QVBoxLayout()
		self.layout_description = QVBoxLayout()
		self.layout_character = QVBoxLayout()
		self.layout_characters = QGridLayout(self)
		self.layout_event = QVBoxLayout()
		self.layout_events = QGridLayout(self)

		self.details = QLabel('Character Details')
		self.layout_details.addWidget(self.details)

		self.character_name = QLabel()
		self.layout_name.addWidget(self.character_name)

		self.character_description = QLabel()
		self.layout_description.addWidget(self.character_description)

		self.comic = QLabel('Comics available:')
		self.layout_character.addWidget(self.comic)

		columna = 0
		fila = 0
		for i in self.superheroes:
			for comic in i['comics']['items']:
				self.comics = comic['name']
				self.details_comic_name = QLabel(self.comics)
				columna += 1
				if columna > 2:
					fila += 1
					columna = 0

		self.event = QLabel('Events available:')
		self.layout_event.addWidget(self.event)

		for i in self.superheroes:
			for events in i['events']['items']:
				self.events = events['name']
				self.events_character = QLabel(self.events)
				columna += 1
				if columna > 2:
					fila += 1
					columna = 0

		self.layout_principal.addLayout(self.layout_details)
		self.layout_principal.addLayout(self.layout_image)
		self.layout_principal.addLayout(self.layout_name)
		self.layout_principal.addLayout(self.layout_description)
		self.layout_principal.addLayout(self.layout_character)
		self.layout_principal.addLayout(self.layout_characters)
		self.layout_principal.addLayout(self.layout_event)
		self.layout_principal.addLayout(self.layout_events)

		widget = QWidget(self)
		widget.setLayout(self.layout_principal)
		self.setCentralWidget(widget)

	def load_image(self, image_details):
		image_data = requests.get(image_details).content
		pixmap = QPixmap()
		pixmap.loadFromData(image_data)
		self.image = QLabel()
		self.image.setPixmap(pixmap)
		self.image.setFixedWidth(300)
		self.image.setFixedHeight(300)
		self.image.setScaledContents(True)
		self.layout_image.addWidget(self.image)

	def render_widget(self, id_character):
		self.id = id_character

		self.characters = requests.get(
			f"https://gateway.marvel.com:443/v1/public/characters/{self.id}"
			f"?ts=1&apikey=57cb5ae41e9c6b861edbabaa11d0142e&hash=b151e8397ef1bbbbee4d6975595fe07e").json()

		self.superheroes = self.characters['data']['results']

		for i in self.superheroes:
			self.name_character = i['name']
			self.description_character = i['description']
			self.image_details = i['thumbnail']['path'] + '.' + i['thumbnail']['extension']

		self.load_image(self.image_details)
		self.character_name.setText(f'Name: {self.name_character}')
		self.character_description.setText(f'Description: {self.description_character}')

		columna = 0
		fila = 0
		for i in self.superheroes:
			for comic in i['comics']['items']:
				self.comics = comic['name']
				self.details_comic_name = QLabel(self.comics)
				self.layout_characters.addWidget(self.details_comic_name, fila, columna)
				columna += 1
				if columna > 2:
					fila += 1
					columna = 0

		self.details_comic_name.setText(self.comics)

		for i in self.superheroes:
			for events in i['events']['items']:
				self.events = events['name']
				self.events_character = QLabel(self.events)
				self.layout_events.addWidget(self.events_character, fila, columna)
				columna += 1
				if columna > 2:
					fila += 1
					columna = 0

		self.events_character.setText(self.events)


class DetailsWindowComics(QMainWindow):
	def __init__(self):
		super().__init__()

		self.id = 103243

		self.comics = requests.get(
			f"https://gateway.marvel.com:443/v1/public/comics/{self.id}"
			f"?ts=1&apikey=57cb5ae41e9c6b861edbabaa11d0142e&hash=b151e8397ef1bbbbee4d6975595fe07e").json()

		self.comic = self.comics['data']['results']

		self.layout_principal = QVBoxLayout()
		self.layout_details = QVBoxLayout()
		self.layout_image = QVBoxLayout()
		self.layout_name = QVBoxLayout()
		self.layout_description = QVBoxLayout()
		self.layout_isbn = QVBoxLayout()
		self.layout_character = QVBoxLayout()
		self.all_name_characters = QHBoxLayout()
		self.all_image_characters = QHBoxLayout()
		self.all_characters = QVBoxLayout()
		self.principal_character = QHBoxLayout()
		self.layout_creator = QVBoxLayout()
		self.all_name_creators = QHBoxLayout()
		self.all_image_creators = QHBoxLayout()
		self.all_creators = QVBoxLayout()
		self.principal_comics = QHBoxLayout()

		self.details = QLabel('Comic details')
		self.layout_details.addWidget(self.details)

		self.name = QLabel()
		self.layout_name.addWidget(self.name)

		self.isbn_ = QLabel()
		self.layout_isbn.addWidget(self.isbn_)

		self.description = QLabel()
		self.layout_description.addWidget(self.description)

		self.character = QLabel('Characters available:')
		self.layout_character.addWidget(self.character)

		for i in self.comic:
			for characters in i['characters']['items']:
				self.comic_characters = QLabel()

				self.resourceURi_characters = characters['resourceURI']

				ts_apikey_hash = '?ts=1&apikey=57cb5ae41e9c6b861edbabaa11d0142e&hash=b151e8397ef1bbbbee4d6975595fe07e'
				uri = self.resourceURi_characters + ts_apikey_hash

				characters_uri = requests.get(uri).json()

				character = characters_uri['data']['results']

				for i in character:
					self.image_character = i['thumbnail']['path'] + '.' + i['thumbnail']['extension']

		self.creator = QLabel('Creator available:')
		self.layout_creator.addWidget(self.creator)

		for i in self.comic:
			for creators in i['creators']['items']:
				self.comic_creators = QLabel()
				self.resourceURi_creators = creators['resourceURI']

				ts_apikey_hash = '?ts=1&apikey=57cb5ae41e9c6b861edbabaa11d0142e&hash=b151e8397ef1bbbbee4d6975595fe07e'
				uri = self.resourceURi_creators + ts_apikey_hash

				creators_uri = requests.get(uri).json()

				creator = creators_uri['data']['results']

				for i in creator:
					self.image_creators = i['thumbnail']['path'] + '.' + i['thumbnail']['extension']

		self.layout_principal.addLayout(self.layout_details)
		self.layout_principal.addLayout(self.layout_image)
		self.layout_principal.addLayout(self.layout_name)
		self.layout_principal.addLayout(self.layout_isbn)
		self.layout_principal.addLayout(self.layout_description)
		self.layout_principal.addLayout(self.layout_character)
		self.layout_principal.addLayout(self.principal_character)
		self.layout_principal.addLayout(self.layout_creator)
		self.layout_principal.addLayout(self.principal_comics)

		widget = QWidget(self)
		widget.setLayout(self.layout_principal)
		self.setCentralWidget(widget)

	def load_image(self, image_details):
		image_data = requests.get(image_details).content
		pixmap = QPixmap()
		pixmap.loadFromData(image_data)
		self.image = QLabel()
		self.image.setPixmap(pixmap)
		self.image.setFixedWidth(300)
		self.image.setFixedHeight(300)
		self.image.setScaledContents(True)
		self.layout_image.addWidget(self.image)

	def load_image_character(self, image_character):
		image_data = requests.get(image_character).content
		pixmap = QPixmap()
		pixmap.loadFromData(image_data)
		self.image = QLabel()
		self.image.setPixmap(pixmap)
		self.image.setFixedWidth(50)
		self.image.setFixedHeight(50)
		self.image.setScaledContents(True)
		self.all_image_characters.addWidget(self.image)

	def load_image_creators(self, image_creators):
		image_data = requests.get(image_creators).content
		pixmap = QPixmap()
		pixmap.loadFromData(image_data)
		self.image = QLabel()
		self.image.setPixmap(pixmap)
		self.image.setFixedWidth(50)
		self.image.setFixedHeight(50)
		self.image.setScaledContents(True)
		self.all_image_creators.addWidget(self.image)

	def render_widget(self, id_comics):
		self.id = id_comics

		self.comics = requests.get(
			f"https://gateway.marvel.com:443/v1/public/comics/{self.id}"
			f"?ts=1&apikey=57cb5ae41e9c6b861edbabaa11d0142e&hash=b151e8397ef1bbbbee4d6975595fe07e").json()

		self.comic = self.comics['data']['results']

		for i in self.comic:
			self.name_comics = i['title']
			self.image_comics = i['thumbnail']['path'] + '.' + i['thumbnail']['extension']
			self.comic_description = i['description']
			self.isbn_comics = i['isbn']

		self.load_image(self.image_comics)
		self.layout_image.addWidget(self.image)

		self.name.setText(f'Name: {self.name_comics}')

		self.isbn_.setText(f'ISBN: {self.isbn_comics}')

		self.description.setText(f'Description: {self.comic_description}')

		self.fila = 0
		self.columna = 0

		for i in self.comic:
			for characters in i['characters']['items']:
				self.characters_ = characters['name']
				self.comic_characters = QLabel(self.characters_)
				self.comic_characters.setText(self.characters_)

				self.all_name_characters.addWidget(self.comic_characters)

				self.resourceURi_characters = characters['resourceURI']

				ts_apikey_hash = '?ts=1&apikey=57cb5ae41e9c6b861edbabaa11d0142e&hash=b151e8397ef1bbbbee4d6975595fe07e'
				uri = self.resourceURi_characters + ts_apikey_hash

				characters_uri = requests.get(uri).json()

				character = characters_uri['data']['results']

				for i in character:
					self.image_character = i['thumbnail']['path'] + '.' + i['thumbnail']['extension']
					self.load_image_character(self.image_character)
					self.all_characters.addLayout(self.all_name_characters)
					self.all_characters.addLayout(self.all_image_characters)

		self.principal_character.addLayout(self.all_characters)

		for i in self.comic:
			for creators in i['creators']['items']:
				self.creators_ = creators['name']
				self.comic_creators = QLabel(self.creators_)
				self.comic_creators.setText(self.creators_)

				self.all_name_creators.addWidget(self.comic_creators)

				self.resourceURi_creators = creators['resourceURI']

				ts_apikey_hash = '?ts=1&apikey=57cb5ae41e9c6b861edbabaa11d0142e&hash=b151e8397ef1bbbbee4d6975595fe07e'
				uri = self.resourceURi_creators + ts_apikey_hash

				creators_uri = requests.get(uri).json()

				creator = creators_uri['data']['results']

				for i in creator:
					self.image_creators = i['thumbnail']['path'] + '.' + i['thumbnail']['extension']
					self.load_image_creators(self.image_creators)
					self.all_creators.addLayout(self.all_name_creators)
					self.all_creators.addLayout(self.all_image_creators)

		self.principal_comics.addLayout(self.all_creators)


class Characters(QWidget):
	def __init__(self):
		super().__init__()
		self.count_pages = 1
		self.offset = 0

		self.principal = QVBoxLayout(self)
		self.grid_info = QGridLayout(self)
		self.buttons = QHBoxLayout(self)

		self.function(self.offset)

		self.btn_next = QPushButton('Siguiente')
		self.btn_previous = QPushButton('Atras')
		self.pages = QLabel(f'Page {self.count_pages}')
		self.pages.setAlignment(Qt.AlignmentFlag.AlignCenter)

		self.btn_next.setStyleSheet("QPushbutton:"
									"{"
									"color : rgb(255, 255, 255);"
									"background-color : rgb(209, 172, 127);"
									"font : 75 9pt Open Sans Semibold"
									"}")
		self.btn_next.setStyleSheet("QPushButton::hover"
									"{"
									"color : rgb(255, 255, 255);"
									"background-color : rgb(164,18,4);"
									"font : 75 9pt Open Sans Semibold"
									"}")
		self.btn_previous.setStyleSheet("QPushbutton:"
										"{"
										"color : rgb(255, 255, 255);"
										"background-color : rgb(209, 172, 127);"
										"font : 75 9pt Open Sans Semibold"
										"}")
		self.btn_previous.setStyleSheet("QPushButton::hover"
										"{"
										"color : rgb(255, 255, 255);"
										"background-color : rgb(164,18,4);"
										"font : 75 9pt Open Sans Semibold"
										"}")

		self.btn_previous.clicked.connect(self.page_previous)
		self.btn_next.clicked.connect(self.page_next)

		self.buttons.addWidget(self.btn_previous)
		self.buttons.addWidget(self.pages)
		self.buttons.addWidget(self.btn_next)

		self.principal.addLayout(self.grid_info)
		self.principal.addLayout(self.buttons)

	def function(self, offset):
		self.offset = offset

		self.characters = requests.get(
			f"https://gateway.marvel.com:443/v1/public/characters?limit=10&offset={self.offset}&ts=1&apikey"
			f"=57cb5ae41e9c6b861edbabaa11d0142e&hash=b151e8397ef1bbbbee4d6975595fe07e").json()

		self.superheroes = self.characters['data']['results']

		self.fila = 0
		self.columna = 0

		for i in self.superheroes:
			self.id_character = i['id']
			self.name_character = i['name']
			self.image_characters = i['thumbnail']['path'] + '.' + i['thumbnail']['extension']

			self.layout_image = QVBoxLayout(self)
			self.layout_name = QVBoxLayout(self)
			self.layout_details = QVBoxLayout(self)
			self.layout_on_sale_date = QVBoxLayout(self)
			self.all = QVBoxLayout(self)

			image_data = requests.get(self.image_characters).content
			pixmap = QPixmap()
			pixmap.loadFromData(image_data)
			self.image = QLabel()
			self.image.setPixmap(pixmap)
			self.image.setFixedWidth(300)
			self.image.setFixedHeight(300)
			self.image.setScaledContents(True)
			self.layout_image.addWidget(self.image)

			self.name = QLabel()
			self.name.setStyleSheet('background-color: rgba(240,240,240,255)')
			self.name.resize(250, 250)
			self.name.setAlignment(Qt.AlignmentFlag.AlignCenter)
			self.name.setText(self.name_character)
			self.layout_name.addWidget(self.name)

			self.date = QLabel('')
			self.layout_on_sale_date.addWidget(self.date)

			self.layout_details.addWidget(CharactersButton(self.id_character))

			self.all.addLayout(self.layout_image)
			self.all.addLayout(self.layout_on_sale_date)
			self.all.addLayout(self.layout_name)
			self.all.addLayout(self.layout_details)

			self.grid_info.addLayout(self.all, self.fila, self.columna)

			self.columna += 1
			if self.columna == 5:
				self.fila = 2
				self.columna = 0

	def page_next(self):
		self.offset += 10
		if self.count_pages == 100:
			self.count_pages = 100
			self.pages.setText(f'Page {self.count_pages}')
		elif 1 <= self.count_pages < 100:
			self.count_pages += 1
			self.pages.setText(f'Page {self.count_pages}')
			self.function(self.offset)

	def page_previous(self):
		self.offset -= 10
		if self.count_pages == 1:
			self.count_pages = 1
			self.pages.setText(f'Page {self.count_pages}')
		elif 1 <= self.count_pages <= 100:
			self.count_pages -= 1
			self.pages.setText(f'Page {self.count_pages}')
			self.function(self.offset)


class Comics(QWidget):
	def __init__(self):
		super().__init__()
		self.count_pages = 1
		self.offset = 0

		self.principal = QVBoxLayout(self)
		self.grid_info = QGridLayout(self)
		self.buttons = QHBoxLayout(self)

		self.function(self.offset)

		self.btn_next = QPushButton('Siguiente')
		self.btn_previous = QPushButton('Atras')
		self.pages = QLabel(f'Page {self.count_pages}')
		self.pages.setAlignment(Qt.AlignmentFlag.AlignCenter)

		self.btn_next.setStyleSheet("QPushbutton:"
									"{"
									"color : rgb(255, 255, 255);"
									"background-color : rgb(209, 172, 127);"
									"font : 75 9pt Open Sans Semibold"
									"}")
		self.btn_next.setStyleSheet("QPushButton::hover"
									"{"
									"color : rgb(255, 255, 255);"
									"background-color : rgb(164,18,4);"
									"font : 75 9pt Open Sans Semibold"
									"}")
		self.btn_previous.setStyleSheet("QPushbutton:"
										"{"
										"color : rgb(255, 255, 255);"
										"background-color : rgb(209, 172, 127);"
										"font : 75 9pt Open Sans Semibold"
										"}")
		self.btn_previous.setStyleSheet("QPushButton::hover"
										"{"
										"color : rgb(255, 255, 255);"
										"background-color : rgb(164,18,4);"
										"font : 75 9pt Open Sans Semibold"
										"}")

		self.btn_previous.clicked.connect(self.page_previous)
		self.btn_next.clicked.connect(self.page_next)

		self.buttons.addWidget(self.btn_previous)
		self.buttons.addWidget(self.pages)
		self.buttons.addWidget(self.btn_next)

		self.principal.addLayout(self.grid_info)
		self.principal.addLayout(self.buttons)

	def function(self, offset):
		self.offset = offset

		self.comics = requests.get(
			f"https://gateway.marvel.com:443/v1/public/comics?limit=10&offset={self.offset}"
			f"&ts=1&apikey=57cb5ae41e9c6b861edbabaa11d0142e&hash=b151e8397ef1bbbbee4d6975595fe07e").json()

		self.comic = self.comics['data']['results']

		self.fila = 0
		self.columna = 0

		for i in self.comic:
			self.id_comic = i['id']
			self.comic_name = i['title']
			self.comic_image = i['thumbnail']['path'] + '.' + i['thumbnail']['extension']

			self.layout_image = QVBoxLayout(self)
			self.layout_name = QVBoxLayout(self)
			self.layout_on_sale_date = QVBoxLayout(self)
			self.layout_details = QVBoxLayout(self)
			self.all = QVBoxLayout(self)

			image_data = requests.get(self.comic_image).content
			pixmap = QPixmap()
			pixmap.loadFromData(image_data)
			self.image = QLabel()
			self.image.setPixmap(pixmap)
			self.image.setFixedWidth(300)
			self.image.setFixedHeight(300)
			self.image.setScaledContents(True)
			self.layout_image.addWidget(self.image)

			self.name = QLabel()
			self.name.setStyleSheet('background-color: rgba(240,240,240,255)')
			self.name.resize(250, 250)
			self.name.setAlignment(Qt.AlignmentFlag.AlignCenter)
			self.name.setText(self.comic_name)
			self.layout_name.addWidget(self.name)

			self.date = QLabel('')
			self.layout_on_sale_date.addWidget(self.date)

			self.layout_details.addWidget(ComicsButton(self.id_comic))

			self.all.addLayout(self.layout_image)
			self.all.addLayout(self.layout_on_sale_date)
			self.all.addLayout(self.layout_name)
			self.all.addLayout(self.layout_details)

			self.grid_info.addLayout(self.all, self.fila, self.columna)

			self.columna += 1
			if self.columna == 5:
				self.fila = 2
				self.columna = 0

	def page_next(self):
		self.offset += 10
		if self.count_pages == 100:
			self.count_pages = 100
			self.pages.setText(f'Page {self.count_pages}')
		elif 1 <= self.count_pages < 100:
			self.count_pages += 1
			self.pages.setText(f'Page {self.count_pages}')
			self.function(self.offset)

	def page_previous(self):
		self.offset -= 10
		if self.count_pages == 1:
			self.count_pages = 1
			self.pages.setText(f'Page {self.count_pages}')
		elif 1 <= self.count_pages <= 100:
			self.count_pages -= 1
			self.pages.setText(f'Page {self.count_pages}')
			self.function(self.offset)


class Marvel(QWidget):
	def __init__(self):
		super().__init__()

		self.layout_image = QVBoxLayout()

		url = 'https://i.pinimg.com/originals/71/5c/fa/715cfa9145ffebbdf3581af61d0dba2d.jpg'

		self.layout = QVBoxLayout(self)
		self.image = QImage()
		self.image.loadFromData(requests.get(url).content)

		self.label = QLabel()
		self.label.setPixmap(QPixmap(self.image).scaled(1500, 1500, Qt.AspectRatioMode.KeepAspectRatio))

		self.layout.addWidget(self.label)

		self.layout_image.addLayout(self.layout)


class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()

		self.all = QVBoxLayout()
		self.menu = QHBoxLayout()
		self.stacked_info = QStackedWidget(self)

		self.page_characters = Characters()
		self.page_comics = Comics()
		self.page_marvel = Marvel()

		self.stacked_info.addWidget(self.page_characters)
		self.stacked_info.addWidget(self.page_comics)
		self.stacked_info.addWidget(self.page_marvel)

		self.btn_marvel = QPushButton('Marvel')
		self.btn_characters = QPushButton('Characters')
		self.btn_comics = QPushButton('Comics')
		self.menu.addWidget(self.btn_marvel)
		self.menu.addWidget(self.btn_comics)
		self.menu.addWidget(self.btn_characters)

		self.btn_marvel.setStyleSheet("QPushbutton:"
									  "{"
									  "color : rgb(255, 255, 255);"
									  "background-color : rgb(209, 172, 127);"
									  "font : 75 9pt Open Sans Semibold"
									  "}")
		self.btn_marvel.setStyleSheet("QPushButton::hover"
									  "{"
									  "color : rgb(255, 255, 255);"
									  "background-color : rgb(164,18,4);"
									  "font : 75 9pt Open Sans Semibold"
									  "}")
		self.btn_characters.setStyleSheet("QPushbutton:"
										  "{"
										  "color : rgb(255, 255, 255);"
										  "background-color : rgb(209, 172, 127);"
										  "font : 75 9pt Open Sans Semibold"
										  "}")
		self.btn_characters.setStyleSheet("QPushButton::hover"
										  "{"
										  "color : rgb(255, 255, 255);"
										  "background-color : rgb(164,18,4);"
										  "font : 75 9pt Open Sans Semibold"
										  "}")
		self.btn_comics.setStyleSheet("QPushbutton:"
									  "{"
									  "color : rgb(255, 255, 255);"
									  "background-color : rgb(209, 172, 127);"
									  "font : 75 9pt Open Sans Semibold"
									  "}")
		self.btn_comics.setStyleSheet("QPushButton::hover"
									  "{"
									  "color : rgb(255, 255, 255);"
									  "background-color : rgb(164,18,4);"
									  "font : 75 9pt Open Sans Semibold"
									  "}")

		self.all.addLayout(self.menu)
		self.all.addWidget(self.stacked_info)

		widget = QWidget(self)
		widget.setLayout(self.all)
		self.setCentralWidget(widget)

		self.start()

	def start(self):
		self.conections()

	def conections(self):
		self.btn_characters.clicked.connect(self.change_page_characters)
		self.btn_comics.clicked.connect(self.change_page_comics)
		self.btn_marvel.clicked.connect(self.change_page_marvel)

	def change_page_characters(self):
		self.stacked_info.setCurrentWidget(self.page_characters)

	def change_page_comics(self):
		self.stacked_info.setCurrentWidget(self.page_comics)

	def change_page_marvel(self):
		self.stacked_info.setCurrentWidget(self.page_marvel)


class CharactersButton(QPushButton):
	def __init__(self, id_character):
		super().__init__()
		self.id = id_character
		self.setText('Details')
		self.setStyleSheet("QPushbutton:"
						   "{"
						   "color : rgb(255, 255, 255);"
						   "background-color : rgb(209, 172, 127);"
						   "font : 75 9pt Open Sans Semibold"
						   "}")
		self.setStyleSheet("QPushButton::hover"
						   "{"
						   "color : rgb(255, 255, 255);"
						   "background-color : rgb(81,140,202);"
						   "font : 75 9pt Open Sans Semibold"
						   "}")
		self.clicked.connect(self.open_window)
		self.details_window = DetailsWindowCharacter()

	def open_window(self):
		self.details_window.render_widget(self.id)
		self.details_window.show()


class ComicsButton(QPushButton):
	def __init__(self, id_comic):
		super().__init__()
		self.id = id_comic
		self.setText('Details')
		self.setStyleSheet("QPushbutton:"
						   "{"
						   "color : rgb(255, 255, 255);"
						   "background-color : rgb(209, 172, 127);"
						   "font : 75 9pt Open Sans Semibold"
						   "}")
		self.setStyleSheet("QPushButton::hover"
						   "{"
						   "color : rgb(255, 255, 255);"
						   "background-color : rgb(81,140,202);"
						   "font : 75 9pt Open Sans Semibold"
						   "}")
		self.clicked.connect(self.open_window)
		self.details_window = DetailsWindowComics()

	def open_window(self):
		self.details_window.render_widget(self.id)
		self.details_window.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())
