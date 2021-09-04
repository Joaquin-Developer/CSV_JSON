import json

def load_csv_file():
    f = open("csv_data.csv", "r")
    data = f.read()
    f.close()
    return data     # Returns str
    
def create_json():
    data = load_csv_file()
    arr = data.split("\n")
    json_file = open("json_generate_data.json", "w")
    json_file.write("[")

    for i in range(2, 10):
        rows = arr[i].split(":")
        obj = {}
        for j in range(0, len(rows)):
            obj[arr[0].split(":")[j]] = rows[j]
        json_file.write(f"{json.dumps(obj)}")

        if i < 9: json_file.write(",")

    json_file.write("]")
    json_file.close()


if __name__ == "__main__": 
    create_json()
