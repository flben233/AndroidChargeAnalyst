import zipfile


def unzip(zip_file, output_dir):
    zip_ref = zipfile.ZipFile(zip_file, 'r')
    zip_ref.extractall(output_dir)
    zip_ref.close()
