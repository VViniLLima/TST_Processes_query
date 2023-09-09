class DataTreatment:
    def last_update_data(self, date_last_update, info_last_update):
        data_dictionary={}

        data_dictionary = {
            "date_last_update": date_last_update,
            "info_last_update": info_last_update
        }
        return data_dictionary
    
    def current_agency(self, process_url):
        data_dictionary={}
        data_dictionary = {
            "process_current_agency": process_url
        }
        return data_dictionary
    