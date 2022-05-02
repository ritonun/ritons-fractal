import configparser

DEFAULT_FILEPATH = "../data/settings.ini"


class Config:

    """Handle everything related to settings.ini file. Read, write, modify
    
    Attributes:
        config (dict): Dict of all value in settings.ini
        filepath (str): path of the settings.ini file
    """
    
    def __init__(self, filepath=DEFAULT_FILEPATH):
        """Init Config
        
        Args:
            filepath (str, optional): Path of the settings.ini
        """
        self.filepath = filepath
        self.config = self.read_settings(self.filepath)

    def write_default_settings(self):
        """This are the default parameters of the app. By calling this
        function, settings are basically reset to default 
        """
        config = configparser.ConfigParser()
        config['display'] = {
            "width": 600,
            "height": 400
        }

        config['fractal'] = {
            "max_iter": 80,
            "re_start": -2,
            "re_end": 1,
            "im_start": -1,
            "im_end": 1
        }

        config['user'] = {
            "default_path": "../output"
        }

        with open(self.filepath, "w") as configfile:
            config.write(configfile)
        self.config = config

    def read_settings(self, filepath=None):
        """Read settings from the settings.ini file 
        
        Args:
            filepath (str, optional): Path of the settings.ini file
        
        Returns:
            dict: Dict with all settings.ini value
        """
        if filepath is None:
            path = self.filepath
        else:
            path = filepath
        config = configparser.ConfigParser()
        config.read(path)
        return config

    def modify_settings(self, section, data, number, show_succes=False):
        """
        Modify a settings in the setting.ini file. In order to actualise the 
        program with this value, settings.py need to be reload 
        
        Args:
            section (str): Section of the configParser
            data (str): variable name
            number (int, float, double): new value
            show_succes (bool, optional): Print a message to User
        """
        config = configparser.ConfigParser()
        config.read(self.filepath)
        config.set(section, data, str(number))
        with open(self.filepath, "w") as configfile:
            config.write(configfile)
        if show_succes:
            print("Config file written successfully ({})".format(
                  self.filepath))
        self.config = config
