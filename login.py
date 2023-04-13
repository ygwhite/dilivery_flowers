from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp


class LoginScreen(Screen):
    pass


class RegisterMenuScreen(Screen):
    def registration(self):
        print(self.ids.name.text)


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
