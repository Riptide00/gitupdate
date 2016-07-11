import shutil


def copy(src, dst):
    try:
        shutil.copytree(src, dst)
    except:
        try:
            shutil.copy(src, dst)
        except:
            raise

if __name__ == '__main__':
    print("Copy is a method to copy files and/or directories")
