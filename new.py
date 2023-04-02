from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty





class Test(MDApp):

    def build(self):
        self.gg = '123'
        return Builder.load_string()


Test().run()