from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from flowers import FlowersApp
from login import LoginApp


class MainFlowersApp(App):

    def build(self):
        catalog_flowers = FlowersApp()
        login_app = LoginApp()
        return catalog_flowers.build()

if __name__ == '__main__':
    MainFlowersApp().run()
