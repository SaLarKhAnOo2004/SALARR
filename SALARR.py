#!/usr/bin/env python3
import os

TARGET_EXTENSIONS = {'.py', '.txt'}

DIRECTORIES_TO_SCAN = [
    os.path.expanduser('~/storage/shared'),      # Internal storage
    os.path.expanduser('~/storage/external-1'),  # SD card (if exists)
]

def delete_all_target_files():
    deleted_count = 0
    total_freed = 0

    for base_dir in DIRECTORIES_TO_SCAN:
        if not os.path.exists(base_dir):
            print(f"Path not found, skipping: {base_dir}")
            continue

        for root, _, files in os.walk(base_dir):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext not in TARGET_EXTENSIONS:
                    continue

                file_path = os.path.join(root, file)
                try:
                    file_size = os.path.getsize(file_path)
                    os.remove(file_path)
                    deleted_count += 1
                    total_freed += file_size
                    print(f"Deleted: {file_path} ({file_size} bytes)")
                except Exception as e:
                    print(f"Error with {file_path}: {e}")

    print(f"\nDone. Deleted {deleted_count} files. Freed {total_freed} bytes (approx {total_freed/(1024*1024):.2f} MB).")

if __name__ == "__main__":
    delete_all_target_files()
