from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Indigo'
        return Builder.load_file('login.kv')

if __name__ == '__main__':
    MainApp().run()
