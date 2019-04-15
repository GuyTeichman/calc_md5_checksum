import hashlib
from pathlib import Path


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def iter_over_paths(paths):
    '''receives a list/tuple of paths (strings). Iterates over the files in each of those paths, and calculate their
    MD5 hash. Returns a list of the file names in the order they were read, and the hash values (checksum) in the same
    order. Example input: [r'D:\Doe\dataForGeo\raw', r'F:\Documents\RawFastq'] '''
    hashes = []
    filenames = []
    for pathname in paths:
        path = Path(pathname)
        for item in path.iterdir():
            if not item.is_dir():
                filenames.append(item.name)
                hashes.append(md5(item))
    return filenames, hashes


if __name__ == '__main__':
    paths = []  # enter your paths in this list
    filenames, hashes = iter_over_paths(paths)
    for filename, hsh in zip(filenames, hashes):
        print(f'{filename}      {hsh}')
