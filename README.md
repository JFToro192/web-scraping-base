# web-scraping-base
Sample procedure for web scraping

### 0. Clone the project

Clone the repository into your local machine.

```Powershell
# Search to the location to clone the repo
cd <"Root directory">

# Clone the repo
{"Root directory"} git clone "https://github.com/JFToro192/web-scraping-base.git"
```

Alternatively, you should download the repository to the location you intend to work on.

### 1. Virtual environment setup

Recreate the virtual environment for installing the packages and dependencies to use the scripts.


>**Note**: The setup requires installing python, [`venv`](https://docs.python.org/3/library/venv.html) and [`pip`](https://pypi.org/project/pip/) in your system. (Python 3.9)

```Powershell
# Access the folder contaning the scripts
<"Root directory"> cd "./web-scraping-base"

# Create the python virtual environment
<"Root directory/web-scraping-base"> python -m venv env

# Activate the virtual environment (Windows Powershell)
<"Root directory/web-scraping-base"> ./env/bin/Activate.ps1

# Install the requirements file in the virtual environment
(env)<"Root directory\web-scraping-base">  
(env)<"Root directory\web-scraping-base">  pip install -r requirements.txt
```
>**Note**: it is possible to setup the environment in windows by executing the `env-setup.bat` file.  

### 2. Test script to extract data

Verify that the environment is correctly working.
```Powershell
#Execute the sample script for extracting data
(env)<"Root directory\web-scraping-base">python ./scripts/test_ws.py
```

The output files can be found in the `./outputs` folder.

>**Note**: the routine can be executed with the `run-scripts.bat` file.