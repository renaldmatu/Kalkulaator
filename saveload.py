import csv

data = [{
    "summa": 12.50,
    "kategooria": "Toit",
    "kirjeldus": "Lõuna",
    "tyyp": "kulu"},
        {
    "summa": 18.99,
    "kategooria": "Meelelahutus",
    "kirjeldus": "Kino",
    "tyyp": "kulu"}]

def save_to_csv_file(filename, data_list):
    keys = data_list[1].keys()
    with open(filename, "w", newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data_list)
        
# save_to_csv_file("test", data)

def load_from_csv_file(filename):
    with open(filename, 'r', newline='') as f:
        dict_reader = csv.DictReader(f)
        data = list(dict_reader)
        return data
    
# print(load_from_csv_file("test"))