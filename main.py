import os

from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from dotenv import load_dotenv

load_dotenv()
Window.size = (310, 580)


class Toko(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        return screen_manager


if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular=f"{os.environ['MPoppins']}")
    LabelBase.register(name="BPoppins", fn_regular=f"{os.environ['BPoppins']}")

    Toko().run()

