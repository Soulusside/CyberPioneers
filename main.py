from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ProductApp(App):
    def build(self):
        self.products = []
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Продукты:')
        layout.add_widget(self.label)
        self.product_list = Label(text='\n'.join(self.products))
        layout.add_widget(self.product_list)
        self.text_input = TextInput(hint_text='Введите продукт')
        layout.add_widget(self.text_input)
        btn_add = Button(text='Добавить продукт', on_press=self.add_product)
        layout.add_widget(btn_add)
        return layout

    def add_product(self, instance):
        product_name = self.text_input.text.strip()  # Удаляем пробелы в начале и конце строки
        if product_name:
            self.products.append(product_name)
            self.product_list.text = '\n'.join(self.products)
            self.text_input.text = ''

if __name__ == '__main__':
    ProductApp().run()

print()
