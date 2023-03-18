from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.bottomnavigation.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivy.uix.button import Button
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex
from kivy.uix.filechooser import FileChooserListView, FileChooserIconView
from kivymd.uix.dialog import MDDialog
from Encryptor import decode_img, encode_img


class MobileApp(MDApp):
    def __init__(self):
        super().__init__()
        self.load_img_button = None
        self.decode_img_path_input = None
        self.encr_img_path_input = None
        self.encr_text_input = None
        self.decode_button = None
        self.dialog = None
        self.encode_button = None

    def build(self):
        self.theme_cls.theme_style = "Dark"  # main window color "Dark" "Light"
        self.theme_cls.primary_palette = "Green"  # text on main window color
        self.title = "MobileEncryptor"  # application window title name

        self.dialog = MDDialog(
            buttons=[MDRectangleFlatButton(text='Ok', on_release=self.close_dialog)]
        )

        # Buttons initialization

        self.load_img_button = Button(text="Load image", on_release=self.load_img_button_callback)
        self.encode_button = Button(text="Encode image", on_release=self.encode_button_callback)
        self.decode_button = Button(text="Decode image", on_release=self.decode_button_callback)

        for button in [self.encode_button, self.decode_button, self.load_img_button]:
            # Configure common elements
            button.height = 50
            button.size_hint_y = None
            button.background_color = get_color_from_hex("#50C878")
            button.color = get_color_from_hex("#FFBF00")
            button.font_name = "Comic"
            button.font_size = 24

        self.encr_text_input = TextInput(
            size_hint_y=None,
            width=30,
            multiline=False,
            text="This photo is encrypted by this text"
        )

        self.encr_img_path_input = TextInput(
            text=r"C:\Users\Dyushechka\PycharmProjects\androidStenography\lofi.png"
        )

        self.decode_img_path_input = TextInput(
            text=r"C:\Users\Dyushechka\PycharmProjects\androidStenography\lofi_encrypted.png"
        )

        for input in [self.encr_img_path_input, self.decode_img_path_input]:
            input.size_hint_y = None
            input.width = 30
            input.multiline = False

        return MDBoxLayout(
            MDBottomNavigation(
                MDBottomNavigationItem(
                    MDBoxLayout(
                        MDLabel(
                            text="Enter your text for encrypting",
                            height=50,
                            size_hint_y=None,
                        ),
                        self.encr_text_input,
                        MDLabel(
                            text="Enter image path to encode",
                            height=50,
                            size_hint_y=None,
                        ),
                        self.load_img_button,
                        self.encr_img_path_input,
                        self.encode_button,
                        orientation="vertical"
                    ),

                    text="Encode Image",
                    name="EncodeScreen",
                    icon="plus"
                ),
                MDBottomNavigationItem(
                    MDBoxLayout(
                        MDLabel(
                            text="Enter image path to decode",
                            height=50,
                            size_hint_y=None,
                        ),
                        self.decode_img_path_input,
                        self.decode_button,
                        orientation="vertical"
                    ),
                    text="Decode Image",
                    name="DecodeScreen",
                    icon="minus"
                )
            ),
            orientation='vertical',
        )

    def encode_button_callback(self, button):
        """Listener for Encode button"""
        destination: str = self.encr_img_path_input.text
        destination = destination[:destination.rfind('.')] + '_encrypted.png'
        err = encode_img(self.encr_img_path_input.text, destination, self.encr_text_input.text)
        self.dialog.text = f"Successfully encrypted: saved in {destination}"
        if err:
            self.dialog.text = "Error! Check image path!"
        self.dialog.open()

    def decode_button_callback(self, button):
        """Listener for Decode button"""
        message = decode_img(self.decode_img_path_input.text)
        if not message:
            self.dialog.text = "Nothing to decode!"
        else:
            self.dialog.text = f"Message Decoded:\n{message}"
        self.dialog.open()

    def load_img_button_callback(self, button):
        ### Ты получаешь изображение с андроид системы ###
        ###...
        ###
        img_path = r"C:\Users\Dyushechka\PycharmProjects\androidStenography\baba.png"
        self.encr_img_path_input.text = img_path
        self.dialog.text = "Path successfully changed!"
        self.dialog.open()

    def close_dialog(self, button):
        """This method close dialogue window"""
        self.dialog.dismiss()


if __name__ == '__main__':
    MobileApp().run()
