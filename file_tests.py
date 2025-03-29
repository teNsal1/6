from file_classes import JsonFile, TxtFile, CsvFile

if __name__ == "__main__":

    json_file = JsonFile("test.json")
    json_file.write({"name": "Alice", "age": 30})
    print(json_file.read())
    json_file.append({{"city": "Moscow"}})
    print(json_file.read())

    txt_file = TxtFile("test.txt")
    txt_file.write("Hello World")
    print(txt_file.read())
    txt_file.append("New Line")
    print(txt_file.read())

    csv_file = CsvFile("test.csv")
    csv_file.write([["Name", "Age"], ["Alice", "30"]])
    print(csv_file.read())
    csv_file.append([["Bob", "25"]])
    print(csv_file.read())
