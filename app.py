from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from Data_base import CatalogFlowers
from kivy.uix.textinput import TextInput


class MyApp(App):

    def build(self):
        first_button = BoxLayout()
        grid = GridLayout(cols=1)

        label = Label(text='Доставка цветов', font_size=17)
        catalog = Button(text="Каталог цветов", font_size=20,
                         background_color='pink',
                         on_press=self.CatalogFlowersFunc)
        cart = Button(text="Моя корзина товаров",
                      font_size=20,
                      background_color='red')
        login = Button(text="Вход", font_size=15,
                       background_color='black')
        first_button.add_widget(catalog)
        first_button.add_widget(cart)
        first_button.add_widget(login)
        grid.add_widget(label)
        grid.add_widget(first_button)

        return grid

    def CatalogFlowersFunc(self, instance):
        print(CatalogFlowers())

# class LoginScreen(GridLayout):
#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
#         self.cols = 2
#         self.add_widget(Label(text='User Name'))
#         self.username = TextInput(multiline=False)
#         self.add_widget(self.username)
#         self.add_widget(Label(text='Password'))
#         self.password = TextInput(password=True, multiline=False)
#         self.add_widget(self.password)


if __name__ == '__main__':
    MyApp().run()
