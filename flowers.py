from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem

from Data_base import DataOutput
from sql_request import sql_request_name_flower

flowers_data = DataOutput(sql_request_name_flower)


class FlowerDelivery(TabbedPanel):

    def on_press_flower(self, instance):
        grid = GridLayout(cols=2)
        for flower in range(len(flowers_data.list_flower)):
            self.flower_list = Button(text=f"Купить:\n{flowers_data.list_flower[flower][0]}\nЦена: {flowers_data.list_flower[flower][3]}", font_size=20, on_press=self.on_press_buy)
            img = Image(
                source='C:\\Users\\vasya\\Downloads\\1630656867_47-oir-mobi-p-tyulpani-kazakhstana-tsveti-krasivo-foto-53.jpg',
                size_hint=(1, 1))
            grid.add_widget(img)
            grid.add_widget(self.flower_list)
        return grid

    def on_press_buy(self, instance):
        pass


class FlowersApp(App):
    def build(self):
        self.flower = 'Роза'
        return FlowerDelivery()


if __name__ == '__main__':
    FlowersApp().run()
