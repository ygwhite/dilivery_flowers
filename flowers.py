import psycopg2
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from cart_sql import CartFlowerUser
from login import LoginScreen, RegisterMenuScreen
from Data_base import DataOutput
from add_flower_to_cart_sql import add_flower_to_cart
from sql_request import sql_request_name_flower

flowers_data = DataOutput(sql_request_name_flower)


class FlowerDelivery(Screen):

    def on_press_flower(self, instance):
        grid = GridLayout(cols=2)
        for flower in range(len(flowers_data.list_flower)):
            flower_list = Button(
                text=f"Купить:\n{flowers_data.list_flower[flower][1]}\nЦена: {flowers_data.list_flower[flower][4]}",
                font_size=20, on_press=self.on_press_buy_factory(flowers_data.list_flower[flower][0]))
            self.ids['test'] = flower_list
            img = Image(
                source='C:\\Users\\vasya\\Downloads\\14cebc37739c2c9379e523c4143d57f0.jpg',
                size_hint=(1, 1))
            grid.add_widget(img)
            grid.add_widget(flower_list)
            print(flower)
        return grid

    def on_press_buy_factory(self, id):
        return lambda instance: self.on_press_buy(id)

    def on_press_buy(self, id):
        from login import user_cart_id
        print(user_cart_id)
        result = add_flower_to_cart(id, user_cart_id, 1)
        print('Товар добавлен!')
        print(result.id_cart_flower)

    def on_press_cart(self, instance):
        from login import customer
        cart_flower_user = CartFlowerUser(customer)
        print(customer)
        print(cart_flower_user.cart_user_flower)
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


class FlowersApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        sm = ScreenManager()
        sm.add_widget(FlowerDelivery(name='flower_app'))
        sm.add_widget(LoginScreen(name='log_menu'))
        sm.add_widget(RegisterMenuScreen(name='register_menu'))
        return sm


if __name__ == '__main__':
    FlowersApp().run()
