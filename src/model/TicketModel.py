import csv


class TicketModel:

    @staticmethod
    def csv_opener(csv_data_dict: dict) -> list:
        rows = []
        with open(csv_data_dict['path'], csv_data_dict['modes'], encoding=csv_data_dict['encode']) as csv_file:
            opened_file = csv.reader(csv_file, delimiter=csv_data_dict['deli'])
            next(opened_file, None)
            for row in opened_file:
                rows.append(row)
            return rows
