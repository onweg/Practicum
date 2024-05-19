import pickle

def load_table(nameFile):
    try:
        with open(nameFile, 'rb') as file:
            data = pickle.load(file)
            
     except FileNotFoundError:
        raise FileNotFoundError("File not found.")       
         
    return None


def save_table(nameFile, data):
    try
        with open(nameFile, 'wb') as file:
            pickle.dump(data, file)
            
    except FileNotFoundError:
        raise Exception("Файл не найден")
    


