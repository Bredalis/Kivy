
# Librerias

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.config import Config

# Tamaño de la ventana
Config.set("graphics", "width", 400)
Config.set("graphics", "height", 400)

Builder.load_string("""

<Contenido>:
	orientation: "vertical"

	Button:
		text: "Hola, Mundo"

	Button: 
		text: "Python"
""")

class Contenido(BoxLayout):
	pass

class Saludo(App):
	title = "Saludo"

	def build(self):
		return Contenido()

# Instanciar la clase
if __name__ == "__main__":
	Saludo().run()