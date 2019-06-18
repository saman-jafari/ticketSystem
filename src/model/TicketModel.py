import csv


class TicketModel:

    @staticmethod
    def csv_opener(path: str, modes: str, deli: str, encode: str) -> list:
        with open(path, modes, encoding=encode) as csv_file:
            opened_file = csv.reader(csv_file, delimiter=deli)
            rows = []
            for row in opened_file:
                rows.append(row)
            return rows
