from src.controller.TicketController import TicketController

first_file_data = {'path': '../data/input/Tickets_List_From_01.2018.csv',
                   'modes': 'r',
                   'deli': ',',
                   'encode': 'utf8'}
second_file_data = {'path': '../data/input/Interactions_Tickets_List_From_01.2018.csv',
                    'modes': 'r',
                    'deli': ',',
                    'encode': 'utf8'}
# second_file_data = { path: str, modes: str, deli: str, encode: str }
print(TicketController.comparison(first_file_data, second_file_data))
