import time

class DataScrape:
    def extract_data(self, request):
        date_last_update = request.html.find('table tr.historicoProcesso')[0].find('td.historicoProcesso')[0].text
        info_last_update = request.html.find('table tr.historicoProcesso')[0].find('td.historicoProcesso')[1].text
        return date_last_update, info_last_update
    
