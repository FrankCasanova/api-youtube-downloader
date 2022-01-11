import os
import shutil
import time


def cleaner():
    """
    This function cleans the path of the file.
    """
    time.sleep(60)
    if os.path.exists("downloads/"):
        shutil.rmtree("downloads/", ignore_errors=True)
        return True
    else:
        return False
