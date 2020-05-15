import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'

print(pickDirectory('.pdf'))

def organizeDirectory():
    for item in os.scandir():
        # we skip the directories & we take just files
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        # check if directory exist, if not we create it
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        # we move the file inside the right directory
        filePath.rename(directoryPath.joinpath(filePath))