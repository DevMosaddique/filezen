import os
import pathlib
import shutil
import hashlib

# Set the base and target directories
base_dir = '/storage/emulated/0'
target_dir = '/storage/emulated/0/Organized'

EXCLUDE_FOLDERS = ["Android", "DCIM", "Organized", "Ncert_Book", "Notes", "Acode"]

fileFormat = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".csv", ".ppt", ".pptx", ".tex", ".epub", ".log"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".psd", ".ico", ".heif"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".3gp", ".mpeg", ".mpg", ".ts", ".m4v", ".vob", ".mxf"],
    "Audio": [".mp3", ".aac", ".wav", ".flac", ".ogg", ".wma", ".m4a", ".aiff", ".opus", ".alac", ".amr", ".mid", ".midi"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz", ".iso", ".jar", ".apk", ".dmg", ".tgz"],
    "Programming": [".py", ".java", ".c", ".cpp", ".cs", ".js", ".ts", ".html", ".css", ".php", ".xml", ".json", ".yaml", ".yml", ".go", ".rs", ".swift", ".sh", ".bat", ".pl", ".rb", ".m", ".kt"],
    "System": [".exe", ".dll", ".sys", ".iso", ".bin", ".msi", ".ini", ".cfg", ".log", ".bak"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2", ".eot"],
    "DiskImages": [".iso", ".img", ".vhd", ".vmdk", ".dmg", ".qcow2"],
    "CAD3D": [".dwg", ".dxf", ".stl", ".obj", ".fbx", ".step", ".iges", ".skp", ".blend"],
    "DesignGraphics": [".psd", ".ai", ".eps", ".svg", ".cdr", ".xcf"],
    "Ebooks": [".epub", ".mobi", ".azw", ".azw3", ".lit"],
    "Miscellaneous": [".torrent", ".ics", ".dat", ".tmp", ".bak"]
}

def calculate_hash(file_path):
    hasher = hashlib.md5()  # MD5 hash
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
    except Exception as e:
        print(f"Could not hash file {file_path}: {e}")
        return None
    return hasher.hexdigest()

def remove_duplicates(base_dir):
    hash_map = {}  # Stores hashes of files and their paths
    duplicates = []  # List of duplicate file paths

    for root, dirs, files in os.walk(base_dir, topdown=True):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_FOLDERS]

        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)
            if file_hash:
                if file_hash in hash_map:
                    duplicates.append(file_path)
                else:
                    hash_map[file_hash] = file_path

    for duplicate in duplicates:
        try:
            os.remove(duplicate)
        except Exception as e:
            print(f"Could not delete duplicate {duplicate}: {e}")

def organize_files(base_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, dirs, files in os.walk(base_dir, topdown=True):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_FOLDERS]

        for file in files:
            file_path = os.path.join(root, file)
            fileName = pathlib.Path(file_path)
            fileFormatType = fileName.suffix.lower()

            dest = os.path.join(target_dir, "Other")  # Default destination

            if fileFormatType:
                for category, extensions in fileFormat.items():
                    if fileFormatType in extensions:
                        dest = os.path.join(target_dir, category)
                        break

            if not os.path.exists(dest):
                os.makedirs(dest)

            try:
                shutil.move(file_path, dest)
            except Exception as e:
                print(f"Failed to move {file_path}: {e}")

def delete_empty_folders(base_dir):
    for root, dirs, files in os.walk(base_dir, topdown=False):  # Reverse order
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
            except PermissionError:
                pass
            except Exception as e:
                print(f"Failed to delete {dir_path}: {e}")

# Remove duplicates first[1] ==> Delete empty folders after organizing[1]
remove_duplicates(base_dir)  # 1
organize_files(base_dir, target_dir)
delete_empty_folders(base_dir)  # 2

print("File organization completed.")
input("\nPress Enter to exit.")
