from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class ProductApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        my_products_button = Button(text='Мои товары', size_hint=(None, None))
        my_products_button.bind(on_press=self.My_products)
        layout.add_widget(my_products_button)

        search_products_button = Button(text='Поиск товаров', size_hint=(None, None))
        search_products_button.bind(on_press=self.Search_products)
        layout.add_widget(search_products_button)

        return layout

    def My_products(self, instance):
        pass

    def Search_products(self, instance):
        pass

if __name__ == '__main__':
    ProductApp().run()

