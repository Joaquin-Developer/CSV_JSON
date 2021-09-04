import json
    
def load_json_file():
    file_data = open("data.json", "r")
    data = file_data.read()
    file_data.close()
    return data

def get_json_data(file_data):
    return json.loads(file_data)
    
def create_csv():
    data = get_json_data(load_json_file())
    csv_file = open("csv_data.csv", "a")
    csv_file.write("albumId:title:url:thumbnailUrl\n\n")

    for i in range(0, 200):
        url = data[i].get('url').split('//')[1]
        thumb_url = data[i].get('thumbnailUrl').split('//')[1]
        csv_file.write(f"{data[i].get('albumId')}:{data[i].get('title')}:{url}:{thumb_url}\n")
    
    csv_file.close()


if __name__ == "__main__": create_csv()

