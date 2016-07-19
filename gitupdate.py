"""Auto updating module."""
import config
import requests
import zipfile
import shutil
import os


def gitupdate():
    """Public method."""
    _setup()
    local = _get_local_version()
    remote = _get_remote_version()
    if local is 0:
        print("No application found, installing...")
        _install()
    else:
        if not _compare(local, remote):
            print("Update available!")
            if _yn_prompt("Do you want to update?"):
                print("Updating...")
                _install()
    print("Done!")
    _start_app()



def _get_remote_version():
    """Check which version remote repo is at."""
    page = requests.get(config.readme_url)
    line = page.text.split()[5]
    latest = line.split('/')[4]
    latest_number = latest.split('-')[1]
    return latest_number


def _get_local_version():
    """Check which version local app is at."""
    readme = "app/README.md"
    try:
        f = open(readme, "r")
    except:
        return 0
    line = f.readlines()[5]
    version = line.split('/')[4]
    version_number = version.split('-')[1]
    return version_number


def _compare(local, remote):
    """Compare versions."""
    if local == remote:
        return True
    else:
        return False


def _download():
    """Download remote repo."""
    url = config.zip_url
    local_filename = 'temp/' + url.split('/')[-1]
    print(local_filename)
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


def _remove_directory(rdir):
    """Remove directoy."""
    shutil.rmtree(rdir)


def _unzip():
    """Unzip downloaded repo."""
    nn = "IGT-master"
    with zipfile.ZipFile('temp/master.zip', "r") as z:
        z.extractall("temp/")
        nn = z.namelist()[0].split('/')[0]
    copy_these = "temp/" + nn
    shutil.copytree(copy_these, 'app/')


def _yn_prompt(question):
    """Yes/no prompt."""
    i = input(question + " y/n: ")
    i = i.lower()
    if i == "y":
        return True
    elif i == "n":
        return False
    else:
        _yn_prompt()


def _start_app():
    """Start app."""
    pass


def _install():
    """Install app."""
    _remove_directory('app/')
    _download()
    _unzip()
    _remove_directory('temp/')


def _setup():
    """Ensure existence of directories."""
    app = "app/"
    temp = "temp/"
    dir_app = os.path.dirname(app)
    dir_temp = os.path.dirname(temp)
    try:
        os.stat(dir_app)
    except:
        os.mkdir(dir_app)
    try:
        os.stat(dir_temp)
    except:
        os.mkdir(dir_temp)

if __name__ == '__main__':
    gitupdate()
