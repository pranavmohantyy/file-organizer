import os
import shutil

def organize_files(directory):
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
        file_ext = os.path.splitext(filename)[1]
        folder_name = 'Other'

        for category, extensions in categories.items():
            if file_ext in extensions:
                folder_name = category
                break

        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))

if __name__ == '__main__':
    organize_files('your_directory_here')