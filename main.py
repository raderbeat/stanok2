from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
import random


class RootWidget(BoxLayout):
    def generate_promo_code(self):
        all_symbols = list('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        random.shuffle(all_symbols)
        promocode = ''.join([random.choice(all_symbols) for i in range(12)])
        Clipboard.copy(promocode)
        print(promocode)
        return promocode

class PromoCodeApp(App):
    def build(self):
        return RootWidget()

Builder.load_string('''
<RootWidget>:
    orientation: 'vertical'
    padding: 50
    spacing: 50
    canvas.before:
        Color:
            rgba: 0.52, 0.13, 0.47, 1
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        id: promo_code_label
        text: ''
        font_size: 25
        font_name: 'fonts/Roboto-Bold.ttf'
        color: (1, 1, 1, 1)
        halign: 'center'
    Button:
        text: 'Генерировать промокод'
        font_size: 30
        font_name: 'fonts/Roboto-Bold.ttf'
        background_color: 0.6, 0.2, 0.6, 1
        on_press: 
            root.generate_promo_code()
            self.background_color = .74, .20, .64, 1
        on_release:
            self.background_color = 0.6, 0.2, 0.6, 1
    Label:
        text: 'Тг создателя: @Borshbeats'
        font_size: 20
        font_name: 'fonts/Roboto-Bold.ttf'
        color: (1, 1, 1, 1)
        halign: 'center'
''')



if __name__ == '__main__':
    PromoCodeApp().run()