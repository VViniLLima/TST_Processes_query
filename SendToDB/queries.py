
class Queries:
    def insert_data(self, cursor, data_dictionary):
        for key, value in data_dictionary.items():
            if 'process_current_agency' not in data_dictionary[key]:
                cursor.execute(""" INSERT INTO process_info (process_number, date_last_update, info_last_update) VALUES (%s, %s, %s)
                                ON CONFLICT (process_number) 
                                DO UPDATE 
                                SET date_last_update = excluded.date_last_update, info_last_update = excluded.info_last_update;
                                """,
                                (key, value['date_last_update'], value['info_last_update']))
                
            else:
                cursor.execute(""" INSERT INTO process_info (process_number, date_last_update, info_last_update) VALUES (%s, %s, %s)
                                ON CONFLICT (process_number) 
                                DO UPDATE 
                                SET date_last_update = excluded.date_last_update, info_last_update = excluded.info_last_update;
                                """,
                                (key, 'n/a', value['process_current_agency']))

                            
                            

