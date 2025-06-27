# Repository Moved

**This repository has been moved to a new location.**

Development and maintenance of the `waapi-python-tools` are now happening at the new repository. Please update your bookmarks and git remotes.

**New Repository:** [**`ak-brodrigue/waapi-python-tools`**](https://github.com/ak-brodrigue/waapi-python-tools)

This repository is now archived and read-only.

---

# waapi-python-tools

This repository is a collection of tools to be used inside Audiokinetic Wwise. The tools use WAAPI (Wwise Authoring API) and Python to perform several automated tasks.

## Requirements
* Python 3.6+
* Running instance of Wwise.exe with the Wwise Authoring API enabled (Project > User Preferences... > Enable Wwise Authoring API)
* waapi-client python project installed

## Setup

For compatibility with Python 2 on Windows, it is recommended to use the Python Launcher for Windows which is installed with Python 3 from python.org.

### Install Python 3.6

* Install Python 3.6 from: https://www.python.org/downloads/

### Install waapi-client

* **Windows**: `py -3 -m pip install waapi-client`
* **Other platforms**: `python3 -m pip install waapi-client`

Additional instructions can be found at:
https://pypi.org/project/waapi-client/

## Running the script

* **Windows**: `py -3 <tool-name>`
* **Other platforms**: `python3 <tool-name>`

Replace `<tool-name>` by the name of the folder you want to use.

## Setup a menu or command from Wwise

TBD...