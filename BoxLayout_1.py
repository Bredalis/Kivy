
# Librerias

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""

<Contenido>:
	spacing: 30
	padding: 30
	orientation: "vertical"

	canvas:
		Color:
			rgb: 1, 1, 1

		Rectangle:
			size: self.size
			pos: self.pos

	BoxLayout:
		size_hint: 1, 1
		width: 100
		canvas:
			Color:
				rgb: 1, 0, 0

			Rectangle: 
				size: self.size
				pos: self.pos

	BoxLayout:
		size_hint: 1, 1
		canvas:
			Color:
				rgb: 1, 1, 0

			Rectangle: 
				size: self.size
				pos: self.pos

		BoxLayout:
			size_hint: None, 1
			width: 100
			canvas:
				Color:
					rgba: 1, 1, 1, .7

				Rectangle: 
					size: self.size
					pos: self.pos

""")

class Contenido(BoxLayout):
	pass

class Metodo1(App):
	title = "BoxLayout Metodo 1"

	def build(self):
		return Contenido()

if __name__ == "__main__":
	Metodo1().run()