from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class ProductApp(App):
    def build(self):
        layout = GridLayout(cols=1, spacing=0, padding=0)

        my_products_button = Button(text='Мои товары', size_hint=(1, None), height=100)
        my_products_button.bind(on_press=self.My_products)
        layout.add_widget(my_products_button)

        search_products_button = Button(text='Поиск товаров', size_hint=(1, None), height=100)
        search_products_button.bind(on_press=self.Search_products)
        layout.add_widget(search_products_button)

        return layout

    def My_products(self, instance):
        pass

    def Search_products(self, instance):
        pass

if __name__ == '__main__':
    ProductApp().run()
