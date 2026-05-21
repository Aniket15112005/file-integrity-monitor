import os
import hashlib
def load_ignore_rules():

    try:
        with open("ignore_rules.txt", "r") as file:
            return [line.strip() for line in file]

    except:
        return []

def generate_hash(file_path):

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:

            while chunk := file.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except Exception as e:
        print(f"[ERROR] Hashing failed for {file_path}: {e}")
        return None


def scan_directory(directory, ignore_extensions=None):

    baseline = {}

    ignore_extensions = load_ignore_rules()

    for root, dirs, files in os.walk(directory):

        for file in files:

            if any(file.endswith(ext) for ext in ignore_extensions):
                continue

            file_path = os.path.join(root, file)

            file_hash = generate_hash(file_path)

            if file_hash:
                baseline[file_path] = file_hash

    return baseline