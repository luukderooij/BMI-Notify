import os
import configparser

from bminotify import settings


class Configuration:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

    def check_section(self, section):
        if not section in self.config:
            self.config.add_section(section)

    def check_key_str(self, section, key, default_value):
        if not default_value:
            default_value = ""

        try:
            return self.config.get(section, key)
        except:
            self.config.set(section, key, default_value)
            return default_value

    def check_key_int(self, section, key, default_value):
        try:
            return self.config.getint(section, key)
        except:
            self.config.set(section, key, str(default_value))
            return default_value

    def check_key_bool(self, section, key, default_value):
        try:
            return self.config.getboolean(section, key)
        except:
            self.config.set(section, key, str(default_value))
            return default_value   
        
    def initialize(self):
        sections = {
            'General',
            'Customer',
            'Telegram',
            'Serial', 
            'Logger'
        }

        for section in sections:
            self.check_section(section)

        # Klant
        settings.KLANT_NAAM = self.check_key_str('Customer', 'Customer_name', None)
        settings.BMC = self.check_key_str('Customer', 'System', None)

        #Telegram
        settings.BOT_TOKEN = self.check_key_str("Telegram", "bot_token", None)
        settings.CHAT_ID = self.check_key_str("Telegram", "chat_id", None)

        #Serial
        settings.COM_PORT = self.check_key_str("Serial", "port", "COM1")
        settings.BAUDRATE = self.check_key_int("Serial", "baudrate", 9600)
        settings.PARITY = self.check_key_str("Serial", "parity", "N") # PARITY_NONE
        settings.STOPBITS = self.check_key_int("Serial", "stopbits", 1) # STOPBITS_ONE
        settings.BYTESIZE = self.check_key_int("Serial", "bytesize", 8) # EIGHTBITS
        settings.TIMEOUT = self.check_key_int("Serial", "timeout", 1)

        # General
        settings.INSTALLER = self.check_key_str('General', 'installer_name', 'BMI-Notify!')
        settings.DEVELOPMENT = self.check_key_bool('General', 'development', False)
        settings.STARTUP_MSG = self.check_key_bool('General', 'startupmsg', True)

        # Logger
        settings.LOG_FILE = self.check_key_str('Logger', 'log_file', os.path.join(settings.DATA_DIR, "bminotify.log"))

        with open(self.config_file, 'w') as file:
            self.config.write(file)


 