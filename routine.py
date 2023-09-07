from process_number import Process
from connection import Connection
from data_scrape import DataScrape
from data_treatment import DataTreatment
import time
import json


def routine(process_list):
    start = time.time()

    process_number = Process()
    data_treatment = DataTreatment()
    last_updated_data_dictionary = {}

    for process in process_list:
        connection = Connection()
        scrape_process = DataScrape()

        request = connection.create_request_object(process_number.process_number_to_parts(process))
        data_last_update, info_last_update = scrape_process.extract_data(request)
        last_updated_data_dictionary[process] = data_treatment.last_update_data(data_last_update, info_last_update)
        
        request.close()
        time.sleep(10)

    with open("100Processes.json", "w", encoding='utf-8') as outfile:
        json.dump(last_updated_data_dictionary, outfile)

    end = time.time()
    print("Elapsed time: ", end-start)
    return last_updated_data_dictionary