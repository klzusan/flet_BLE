import flet as ft
import platform

# MyLibrary
import BLE as ble

# コード実行機のOSを判別
os_name = platform.system()
# ESPのアドレスなどを設定
if os_name == 'Windows':
    # Windows / Linux
    MAC_ADDRESS = "90:15:06:7A:92:1A"
elif os_name == 'Darwin':
    # Mac OS
    MAC_ADDRESS = "3C9AF520-9912-127C-6F91-3C0933B44BB6"
# Common
CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"


def main(page: ft.Page):
    page.title = "Flet_BLE"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(ble.BLEConnectApp(
        mac_addr = MAC_ADDRESS,
        char_uuid = CHARACTERISTIC_UUID,
    ))


ft.run(main)
