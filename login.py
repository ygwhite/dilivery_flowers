from kivy.lang.builder import Builder
from kivymd.app import MDApp


class LoginApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        # return Builder.load_file('login.kv')

    def logger(self):
        print(f'sup {self.root.ids.user.text}!')


LoginApp().run()
