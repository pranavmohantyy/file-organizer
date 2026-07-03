import os
import shutil

def organize_files(directory, by_date=False):
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Videos': ['.mp4', '.mkv'],
        'Audio': ['.mp3', '.wav'],
        'Archives': ['.zip', '.tar', '.gz'],
    }

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        file_ext = os.path.splitext(filename)[1]

        if by_date:
            mod_time = os.path.getmtime(file_path)
            year = str(os.path.getmtime(file_path)).split('-')[0]
            month = str(os.path.getmtime(file_path)).split('-')[1]
            date_folder = os.path.join(directory, year, month)
            os.makedirs(date_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(date_folder, filename))
            continue

        folder_name = 'Other'

        for category, extensions in categories.items():
            if file_ext in extensions:
                folder_name = category
                break

        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        shutil.move(file_path, os.path.join(folder_path, filename))
