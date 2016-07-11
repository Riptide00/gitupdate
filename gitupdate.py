"""Auto updating module."""
import config
import requests
import zipfile
import shutil


def check():
    """Public method."""
    _compare(_get_local_version(), _get_remote_version())


def _get_remote_version():
    """Check wich version remote repo is at."""
    page = requests.get(config.master_url)
    line = page.text.split()[4]
    version = line.split('/')[4]
    version_number = version.split('-')[1]
    return version_number


def _get_local_version():
    """Check wich version local app is at."""
    readme = "app/README.md"
    try:
        f = open(readme, "r")
    except:
        _install()
        return
    line = f.readlines()[4]
    version = line.split('/')[4]
    version_number = version.split('-')[1]
    return version_number


def _compare(local, remote):
    """Compare versions."""
    if local == remote:
        print("Your app is up-to-date.")
        _start_app()
    else:
        _update()


def _update():
    """Update app."""
    print("Update available!")
    print("Do you want to update?")
    if _yn_prompt():
        print("Updating...")
        _install()
        print("Done!")
    else:
        _start_app()


def _download():
    """Download remote repo."""
    url = config.zip_url
    local_filename = 'temp/' + url.split('/')[-1] + '.zip'
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local_filename


def _remove_old_app():
    """Remove old app."""
    shutil.rmtree('app/')


def _unzip():
    """Unzip downloaded repo."""
    nn = ""
    with zipfile.ZipFile('temp/master.zip', "r") as z:
        z.extractall("temp/")
        nn = z.namelist()[0].split('/')[0]
    copy_these = "temp/" + nn
    shutil.copytree(copy_these, 'app/')


def _yn_prompt():
    """Yes/no prompt."""
    i = input("y/n: ")
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
    _remove_old_app()
    _download()
    _unzip()


if __name__ == '__main__':
    print("Auto-updating module.")
    check()
