# File Organizer

This script helps in organizing files on your device by categorizing them into different folders based on file types. It also removes duplicate files and deletes empty folders to maintain a clean file structure. The script supports a variety of file formats, including documents, images, videos, audio, and more.

## Features

- **File Categorization**: Files are moved to specific folders based on their types (e.g., Documents, Images, Videos, Audio, etc.).
- **Remove Duplicates**: Duplicate files are identified and removed based on their MD5 hash.
- **Delete Empty Folders**: After organizing the files, the script will clean up any empty directories.

## Requirements

- Python 3.x
- The `os`, `pathlib`, `shutil`, and `hashlib` modules (standard Python libraries)

## Setup

1. **Base Directory**: Set the `base_dir` to the location where your files are stored (e.g., `/storage/emulated/0`).
2. **Target Directory**: Set the `target_dir` to the directory where you want your files to be organized (e.g., `/storage/emulated/0/Organized`).
3. **Excluded Folders**: You can specify folders to exclude from the organization process by editing the `EXCLUDE_FOLDERS` list (e.g., `"Android"`, `"DCIM"`, `"Organized"`).

## File Format Categories

Files are categorized into the following types:
- **Documents**: PDF, Word, Excel, etc.
- **Images**: JPG, PNG, GIF, etc.
- **Videos**: MP4, MKV, AVI, etc.
- **Audio**: MP3, WAV, AAC, etc.
- **Archives**: ZIP, RAR, TAR, etc.
- **Programming**: Python, Java, JavaScript, etc.
- **System**: EXE, DLL, SYS, etc.
- **Fonts**: TTF, OTF, WOFF, etc.
- **Disk Images**: ISO, IMG, VHD, etc.
- **CAD3D**: DWG, STL, OBJ, etc.
- **Design Graphics**: PSD, AI, EPS, etc.
- **Ebooks**: EPUB, MOBI, AZW, etc.
- **Miscellaneous**: Torrent, ICS, DAT, etc.

## Usage

1. **Run the script**: After configuring the `base_dir`, `target_dir`, and `EXCLUDE_FOLDERS`, simply run the script. It will:
   - Remove duplicate files.
   - Organize files into categorized folders.
   - Delete any empty folders.

2. **After Completion**: The script will output "File organization completed" and prompt you to press Enter to exit.

## Example Configuration
```python
base_dir = '/storage/emulated/0'
target_dir = '/storage/emulated/0/Organized'
EXCLUDE_FOLDERS = ["Android", "DCIM", "Organized"]
```

## Notes

- Ensure that the paths for `base_dir` and `target_dir` are correct for your system.
- The script excludes folders like `"Android"`, `"DCIM"`, and `"Organized"` to avoid unintended modifications.
- You can customize the file categories by modifying the `fileFormat` dictionary.

- ## License

This script is open-source and free to use. Contributions are welcome!
