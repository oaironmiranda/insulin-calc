from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_file('main.kv')

    def mode(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        elif self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"

    def calc(self):
        if str(self.root.ids.num.text) == '':
            self.root.ids.label.text = "Try Again"
        else:
            a = int(self.root.ids.num.text)
            if a < 190:
                self.root.ids.label.text = "You don't need to Add more insuline"
                if a <= 85:
                    self.root.ids.label.text = "You need to fix your blood sugar"
            elif a >= 190:
                b = (a - 120) / 70
                self.root.ids.label.text = f'Add {round(b)}UI'




MainApp().run()
