from src.model.TicketModel import TicketModel


class TicketController:

    @staticmethod
    def comparison(first_file_data: dict, second_file_data: dict):
        """
        :type first_file_data: dict { path: str, modes: str, deli: str, encode: str }
        :type second_file_data: dict { path: str, modes: str, deli: str, encode: str }
        """
        first_file_data_list = TicketModel.csv_opener(first_file_data)
        second_file_data_list = TicketModel.csv_opener(second_file_data)

        for row in first_file_data_list:
            for rowsec in second_file_data_list:
                if row[0] == rowsec[0]:
                    print(rowsec)
            return
