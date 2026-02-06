import flet as ft
from dataclasses import field
from bleak import BleakClient
import platform

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

# 各種ボタンなどのコンポーネント
@ft.control
class BLESendButton(ft.Button):
    expand: bool = field(default=True)
    color: ft.Colors = ft.Colors.WHITE

# アプリの本体
@ft.control
class BLEConnectApp(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 350
        self.status_text = ft.Text("待機中...", color=ft.Colors.GREY_400)
        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                BLESendButton(content="Yellow", bgcolor=ft.Colors.YELLOW_300, on_click=self.button_clicked),
                BLESendButton(content="Green", bgcolor=ft.Colors.GREEN_300, on_click=self.button_clicked),
                BLESendButton(content="Off", bgcolor=ft.Colors.WHITE_10, on_click=self.button_clicked),
            ],
            spacing=10,
        )

    async def button_clicked(self, e):
        data = e.control.content
        print(f"[Dev] Button: {data}")

        # 各種ボタンが押されたときの処理
        if data == 'Yellow':
            command = 'y'
        elif data == 'Green':
            command = 'g'
        else:
            command = 'n'
        await self.send_data(command)

        self.update()

    async def send_data(self, data: str):
        try:
            # 毎回送信/切断を行うシンプルな方式
            async with BleakClient(MAC_ADDRESS, timeout=10.0) as client:
                if client.is_connected:
                    print(f"[Dev] Connected")
                    # バイト列に変換して書き込み
                    await client.write_gatt_char(CHARACTERISTIC_UUID, data.encode())
                    self.status_text.value = f"{data} を送信しました"
                    self.status_text.color = ft.Colors.GREEN_400
                else:
                    print(f"[Dev] Cannot connect")
                    self.status_text.value = f"エラー: 接続できませんでした"
                    self.status_text.color = ft.Colors.RED_400
        except Exception as ex:
            self.status_text.value = f"エラー: {str(ex)}"
            self.status_text.color = ft.Colors.RED_400
        self.update()

def main(page: ft.Page):
    page.title = "Flet_BLE"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(BLEConnectApp())


ft.run(main)
