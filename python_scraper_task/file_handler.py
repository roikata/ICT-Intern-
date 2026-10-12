import os
from datetime import datetime

def save_data(data, name):
    os.makedirs("output", exist_ok=True)

    time_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    filename = f"{name}_{time_now}.txt"
    file_path = os.path.join("output", filename)

    with open(file_path, "w", encoding="utf-8") as file:
        for item in data:
            for key, value in item.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")

    return file_path