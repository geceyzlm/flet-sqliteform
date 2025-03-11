import flet as ft
from flet import *
from flet import Colors #yeni hal
from flet import Icons #yeni hal

import sqlite3


def main(page: ft.Page):
    page.title = "text"
    page.window.width=375
    page.window.height=500
    page.theme_mode = ThemeMode.LIGHT
    page.vertical_alignment = "center"
    page.horizontal_alignment="center"

    
    page.add()
    page.update()

ft.app(target=main)