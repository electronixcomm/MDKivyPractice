# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivymd.app import MDApp
from datetime import datetime, date, time
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton,MDFlatButton
import nepali_datetime




class BButtonBarApp(MDApp):
    dialog_clock= None
    dialog_calendar=None
    def build(self):
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_palette='Indigo'
        return Builder.load_file('bbuttonbar.kv')


    def show_clock_dialog(self):
        if not self.dialog_clock:
            self.dialog = MDDialog(
                title='Current Time:',
                text=datetime.now().strftime('%H:%M:%S'),
                buttons=[
                    MDRaisedButton(
                        text='Cancel', text_color='red',on_release= self.close_dialog_clock
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

if __name__=='__main__':
    BButtonBarApp().run()