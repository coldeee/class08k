import hashlib

def compute_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def compute_sha256_after(input_string):
    sha256 = hashlib.sha256()
    sha256.update(input_string.encode('utf-8'))
    return sha256.hexdigest()



file_checksum = compute_sha256(image_path)
after_checksum = compute_sha256_after(output_image_path)

print(f"Контрольная сумма исходных данных: {file_checksum}")
print(f"Контрольная сумма после расшифровки: {after_checksum}")
