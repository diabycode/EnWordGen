
from kivy.config import Config
Config.set('graphics', 'width', '550')
Config.set('graphics', 'height', '288')
Config.set('graphics', 'resizable', False)
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.uix.widget import Widget

import json
import random


# Loading data
with open("./irregular_verbs.json", "r") as f:
    VERBS = json.load(f)

# loading settings
with open("./settings.json", "r") as f:
    SETTINGS = json.load(f)


class MainWidget(Widget):

    current_verb = None
    verb_index = 0
    infinitif = ObjectProperty(None)
    preterit_ppasse = ObjectProperty(None)
    in_frensh = ObjectProperty(None)

    switch = ObjectProperty(None)

    def __int__(self, **kwargs):
        super(MainWidget, self).__int__(**kwargs)

    def change_curent_theme(self, widget):
        if self.switch.active:
            SETTINGS[0][1] = "_dark"
        else:
            SETTINGS[0][1] = "_default"
        with open("./settings.json", "w") as file:
            json.dump(SETTINGS, file, indent=4)

    def show_correction(self, widget):
        self.preterit_ppasse.text = self.current_verb[1] + "\n" + self.current_verb[2]
        self.in_frensh.text = self.current_verb[3]

    def on_parent(self, parent, widget):
        self.verb_index = random.randint(0, len(VERBS))
        self.current_verb = VERBS[self.verb_index]
        self.infinitif.text = self.current_verb[0].upper()

        if not SETTINGS[0][1] == "_default":
            self.switch.active = True


class EnWordGenApp(App):
    main_app = ObjectProperty()

    if SETTINGS[0][1] == "_default":
        BACKGROUND_COLOR = "#F3F3F3"
        SECTION_BODY_BACKGROUND_COLOR = "#E4E4E4"
        TEXT_COLOR = "#3A3A3A"
    else:
        BACKGROUND_COLOR = "#3A3A3A"
        SECTION_BODY_BACKGROUND_COLOR = "#2B2B2B"
        TEXT_COLOR = "#F3F3F3"

    def build(self):

        self.icon = "images/icon-app.png"
        self.main_app = MainWidget()
        return self.main_app


if __name__ == "__main__":
    EnWordGenApp().run()












