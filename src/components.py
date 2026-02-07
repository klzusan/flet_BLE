import flet as ft
from dataclasses import field

# 各種ボタンなどのコンポーネント
@ft.control
class BLESendButton(ft.Button):
    expand: bool = field(default=True)
    color: ft.Colors = ft.Colors.WHITE