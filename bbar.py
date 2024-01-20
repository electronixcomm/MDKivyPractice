from kivy.lang import Builder
from kivymd.app import MDApp

class NavigationBarApp(MDApp):
    def build(self):
        self.theme_cls.theme_style='Light'
        self.theme_cls.material_style='M3'
        self.theme_cls.primary_palette='Indigo'
        return Builder.load_file('bbar.kv')
    def gmail_icon(self):
        print('gmail icon pressed')
if __name__ == '__main__':
    NavigationBarApp().run()