import csv

def load_table(nameFile):
    data = []
    
    try:
        with open(nameFile, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                data.append(row)
                
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")
        
    return data


def save_table(nameFile, data):
    
    try:
        with open(nameFile, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    except FileNotFoundError:
        raise Exception("Файл не найден")
    

