from kivy.lang import Builder

from kivymd.app import MDApp



class Example(MDApp):
    datta = {
        'Python': ['language-python',"on_press", lambda x: print("pressed Python")

        ],
        'PHP': 'language-php',
        'C++': 'language-cpp',
    }

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file('speeddial.kv')


Example().run()