import codecs
import configparser
import os
import platform


class MetronTaggerSettings:
    @staticmethod
    def getSettingsFolder():
        if platform.system() == "Windows":
            folder = os.path.join(os.environ["APPDATA"], "MetronTagger")
        else:
            folder = os.path.join(os.path.expanduser("~"), ".MetronTagger")
        if folder is not None:
            folder = folder
        return folder

    def setDefaultValues(self):
        # Metron creditials
        self.metron_user = ""
        self.metron_pass = ""

    def __init__(self):
        self.settings_file = ""
        self.folder = ""
        self.setDefaultValues()

        self.config = configparser.ConfigParser()
        self.folder = MetronTaggerSettings.getSettingsFolder()

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

        self.settings_file = os.path.join(self.folder, "settings")

        # Write the config file if it doesn't exist
        if not os.path.exists(self.settings_file):
            self.save()
        else:
            self.load()

    def load(self):
        self.config.read(self.settings_file)

        if self.config.has_option("metron", "user"):
            self.metron_user = self.config.get("metron", "user")

        if self.config.has_option("metron", "password"):
            self.metron_pass = self.config.get("metron", "password")

    def save(self):
        if not self.config.has_section("metron"):
            self.config.add_section("metron")

        self.config.set("metron", "user", self.metron_user)
        self.config.set("metron", "password", self.metron_pass)

        with codecs.open(self.settings_file, "wb", "utf8") as configfile:
            self.config.write(configfile)