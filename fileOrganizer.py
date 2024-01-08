import os
import shutil

def fileOrganizer(path):
    # Create a dictionary to map file extensions to directory names
    extension_mapping = {
        'jpg': 'Images',
        'jpeg': 'Images',
        'png': 'Images',
        'gif': 'Images',
        'pdf': 'Documents',
        'txt': 'Documents',
        'docx': 'Documents',
        'xlsx': 'Documents',
        'pptx': 'Presentations',
        'mp3': 'Music',
        'wav': 'Music',
        'mp4': 'Videos',
        'mov': 'Videos',
        'py': 'Python',
        # Add more file types and folder names as needed
    }

    for filename in os.listdir(path):
        # Get the file extension
        extension = filename.split('.')[-1].lower()

        if extension in extension_mapping:
            folder_name = extension_mapping[extension]
            folder_path = os.path.join(path, folder_name)

            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move the file to the folder
            shutil.move(os.path.join(path, filename), folder_path)
            print(f"Moved: {filename} to {folder_path}")

Example usage
dirOrganize = input("Enter the path of the directory to organize: ")
fileOrganizer(dirOrganize)
