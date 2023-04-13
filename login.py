from kivy.app import App
from kivy.lang import Builder
import psycopg2
from configBD import host, db_name, password, user
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

from Data_base import DataOutput



sql_request_add_flower = (
                    """INSERT INTO users (name, username, email, password) 
                                        VALUES (%s, %s, %s, %s);"""
)


class RegData:

    def __init__(self, sql_request, name, username, email, password_user):
        self.connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user,
            password=password
        )
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    sql_request, (name, username, email, password_user)
                )
                self.connection.commit()
                # self.list_flower = cursor.fetchall()



        finally:
            if self.connection:
                self.connection.close()


class LoginScreen(Screen):
    pass


class RegisterMenuScreen(Screen):
    def registration(self):
        print(self.ids.name.text)
        RegData(sql_request_add_flower, self.ids.name.text, self.ids.user.text, self.ids.email.text, self.ids.password.text)
        print('Регистрация прошла успешно!')


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
