from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp


class LoginMenuScreen(Screen):
    pass


class RegisterMenuScreen(Screen):
    pass


class LoginApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginMenuScreen(name='login_menu'))
        sm.add_widget(RegisterMenuScreen(name='register_menu'))
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        # return Builder.load_file('login.kv')

    def logger(self):
        print(f'sup {self.root.ids.user.text}!')


LoginApp().run()
