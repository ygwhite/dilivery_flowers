from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.


# Declare both screens

# Builder.load_string(r'E:\Программирование\Проекты\Python\PycharmProjects\kivi\login.kv')

class LoginScreen(Screen):
    pass

class RegisterMenuScreen(Screen):
    pass

class LoginApp(MDApp):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='menu'))
        sm.add_widget(RegisterMenuScreen(name='register_menu'))
        return sm

if __name__ == '__main__':
    LoginApp().run()