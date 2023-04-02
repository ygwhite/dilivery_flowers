from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel

cart = []


class FlowerDelivery(BoxLayout):
    def obrabotchick(self, instance):
        cart.append(instance.text)
        print("Добавлено в корзину!\n", cart)


class DeliveryApp(App):
    def build(self):
        return FlowerDelivery()


if __name__ == "__main__":
    DeliveryApp().run()
