import subprocess
import webbrowser
import sys

url = 'http://stackoverflow.com/'
if sys.platform == 'darwin':    # in case of OS X
    subprocess.Popen(['open', url])
else:
    webbrowser.open_new_tab(url)