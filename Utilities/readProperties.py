import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\cofig.ini")

class readProerty():

    @staticmethod
    def getApplicationUrl():
        url = config.get("common login info","baseUrl")
        return url

    @staticmethod
    def getApplicationUsername():
        username = config.get("common login info", "username")
        return username

    @staticmethod
    def getApplicationpassword():
        password = config.get("common login info", "password")
        return password