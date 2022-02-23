import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url=config.get('common info','baseUrl')
        return url

    @staticmethod
    def getUserName():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getUserPassword():
        password=config.get('common info','password')
        return password

    @staticmethod
    def getWorkbook():
        workbook=config.get('common info','workbook_path')
        return workbook