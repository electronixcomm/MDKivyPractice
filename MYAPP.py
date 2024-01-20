from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen,ScreenManager
from datetime import datetime, date, time
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton,MDFlatButton
import nepali_datetime
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar

class Card(MDCard):
    source=StringProperty()

class RootScreen(Screen):
    pass
class MenuScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(RootScreen(name='rootScreen'))
sm.add_widget(MenuScreen(name='menuScreen'))

class MainApp(MDApp):
    dialog_clock = None
    dialog_calendar = None
    datta = {
        'Python': ['language-python',"on_press", lambda x: print("pressed PHP")

        ],
        'PHP': 'language-php',
        'C++': 'language-cpp',
    }

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(RootScreen(name='rootScreen'))
        self.sm.add_widget(MenuScreen(name='menuScreen'))

        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Item {i}",
                "height": dp(56),
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(10)
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
            border_margin=dp(35)
        )


        self.theme_cls.theme_style = 'Dark'

        self.theme_cls.primary_palette = 'Indigo'
        self.root= Builder.load_file('MYAPP.kv')
        return self.root

    def menu_callback(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()


    def checkbox_state(self, active):
        #print(type(active))
        print(f"Checkbox state: {'checked' if active else 'unchecked'}")

    def button_press(self, checkbox_state):
        print(f"Button pressed with checkbox state: {'checked' if checkbox_state else 'unchecked'}")

    def gmail_icon(self):
        print('gmail icon pressed')
    def show_clock_dialog(self):
        if not self.dialog_clock:
            self.dialog = MDDialog(
                title='Current Time:',
                text=datetime.now().strftime('%H:%M:%S'),
                buttons=[
                    MDRaisedButton(
                        text='Close', text_color='red',on_release= self.close_dialog_clock
                    )
                ],
            )

        self.dialog.open()


    def close_dialog_clock(self,instance):
        self.dialog.dismiss()

    def show_calendar_dialog(self):
        temp = nepali_datetime.datetime.now().strftime('%K-%n-%D (२०%k %N %G)')
        if not self.dialog_clock:
            self.dialog_calendar = MDDialog(
                title='Today Date:',
                text=datetime.now().strftime('%Y-%m-%d'),

                buttons=[
                    MDFlatButton(
                        text=temp, font_name='./NotoSansDevanagari-VariableFont_wdth,wght.ttf', text_color='red'
                    ),
                    MDRaisedButton(
                        text='close',font_name='./NotoSansDevanagari-VariableFont_wdth,wght.ttf' ,text_color='red',on_release= self.close_dialog_calendar
                    )

                ],
            )
        print(nepali_datetime.datetime.now().strftime('%K-%n-%D (%k %N %G)'))
        self.dialog_calendar.open()

    def close_dialog_calendar(self,instance):
        self.dialog_calendar.dismiss()


if __name__ == '__main__':
    MainApp().run()