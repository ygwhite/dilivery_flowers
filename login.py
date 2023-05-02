from kivy.app import App
from kivy.lang import Builder
import psycopg2
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.uix.label import Label
from Data_base import DataOutput
from login_sql import RegData, SearchEmailAndUsername


class LoginScreen(Screen):
    pass


customer = None
user_cart_id = None


class RegisterMenuScreen(Screen):
    def registration(self):
        global customer
        global user_cart_id
        response_reg = SearchEmailAndUsername(self.ids.email.text, self.ids.user.text)
        print(self.ids.name.text)
        if "Accepted!" == response_reg.response:
            customer = RegData(self.ids.name.text, self.ids.user.text, self.ids.email.text, self.ids.password.text)
            print('Регистрация прошла успешно!')
            button = self.ids.Register
            button.callback = self.manager.current = 'flower_app'
            flower_delivery = self.manager.get_screen('flower_app')
            username = flower_delivery.ids['Username']
            user_cart_id = customer.id_user_cart[0][0]
            customer = str(customer.id_user[0][1])
            username.text = customer

        else:
            button = self.ids.welcome_label
            button.text = "Такой аккаунт уже есть("
            print('Этот аккаунт уже существует!')


class LoginApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='log_menu'))
        sm.add_widget(RegisterMenuScreen(name='register_menu'))
        return sm


if __name__ == '__main__':
    LoginApp().run()
