from kivy.core.text import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout

from cart_sql import CartFlowerUser



class CartFlower(Screen):

    def on_press_by_flower(self, instance):
        from login import customer
        cart_flower_user = CartFlowerUser(customer)
        grid = GridLayout(cols=5)
        for cart_info in range(len(cart_flower_user.cart_user_flower)):
            flower_name = Label(
                text=f"{cart_flower_user.cart_user_flower[cart_info][0]}",
                font_size=20)
            flower_price = Label(
                text=f"{cart_flower_user.cart_user_flower[cart_info][1]}",
                font_size=20)
            flower_quantity = Label(
                text=f"{cart_flower_user.cart_user_flower[cart_info][2]}",
                font_size=20)
            img = Image(
                source='C:\\Users\\vasya\\Downloads\\1630656867_47-oir-mobi-p-tyulpani-kazakhstana-tsveti-krasivo-foto-53.jpg',
                size_hint=(1, 1))
            grid.add_widget(flower_name)
            grid.add_widget(flower_price)
            grid.add_widget(flower_quantity)
            grid.add_widget(img)
            print(cart_info)
        return grid
