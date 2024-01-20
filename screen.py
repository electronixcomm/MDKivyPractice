from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager

class MenuScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class UploadScreen(Screen):
    pass
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(ProfileScreen(name='upload'))

class DemoScreenApp(MDApp):
    def build(self):
        screen = Builder.load_file('screen.kv')
        return screen


DemoScreenApp().run()