from pathlib import Path
import re

# Folder containing your images
FOLDER = Path(".")

for file in FOLDER.iterdir():
    if not file.is_file():
        continue

    # Remove " Shard" before the extension (case-insensitive)
    new_name = re.sub(r"\s+Shard(?=\.)", "", file.name, flags=re.IGNORECASE)

    if new_name != file.name:
        new_path = file.with_name(new_name)

        # Don't overwrite an existing file
        if new_path.exists():
            print(f"Skipping (already exists): {new_name}")
            continue

        file.rename(new_path)
        print(f"{file.name} -> {new_name}")

print("Done!")