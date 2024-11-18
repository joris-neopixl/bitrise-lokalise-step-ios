import os
import json
import subprocess

print("""\n\n\n
 __                  __                  __  __                     
/  |                /  |                /  |/  |                    
$$ |        ______  $$ |   __   ______  $$ |$$/   _______   ______  
$$ |       /      \\ $$ |  /  | /      \\ $$ |/  | /       | /      \\ 
$$ |      /$$$$$$  |$$ |_/$$/  $$$$$$  |$$ |$$ |/$$$$$$$/ /$$$$$$  |
$$ |      $$ |  $$ |$$   $$<   /    $$ |$$ |$$ |$$      \\ $$    $$ |
$$ |_____ $$ \\__$$ |$$$$$$  \\ /$$$$$$$ |$$ |$$ | $$$$$$  |$$$$$$$$/ 
$$       |$$    $$/ $$ | $$  |$$    $$ |$$ |$$ |/     $$/ $$       |
$$$$$$$$/  $$$$$$/  $$/   $$/  $$$$$$$/ $$/ $$/ $$$$$$$/   $$$$$$$/ 
\n""", flush=True)


# Install requests for manage api call in python
exit_code = os.system("python -m pip install requests")
if exit_code != 0:
    print("\n exit_code : instal pyhon requests === %s" % exit_code, flush=True)
    os._exit(1)


# Retrieve all user injected variables
project_root_path = "/Users/vagrant/git"
lokalise_token = "%s" % os.getenv('lokalise_token')
lokalise_project_id = "%s" % os.getenv('lokalise_project_id')
file_path = "%s/%s" % (project_root_path, os.getenv('file_path'))


# Get all translations from Lokalise 
import requests
url = "https://api.lokalise.com/api2/projects/%s/keys?include_comments=0&include_translations=1&pagination=offset&limit=500" % lokalise_project_id
headers = {
    "accept": "application/json",
    "X-Api-Token": "%s" % lokalise_token
}
response = requests.get(url, headers=headers)


# Read & Parse JSON
json = response.json()

for key in json['keys']:
    for translation in key['translations']:
	    status = translation['is_unverified']
	    if status == True
	        print("\n Verified :check:", flush=True)
	    else:
	    	print("\n UNVERIFIED :red_cross:", flush=True)


print("""\n\n
 ________  __    __  _______  
/        |/  \\  /  |/       \\ 
$$$$$$$$/ $$  \\ $$ |$$$$$$$  |
$$ |__    $$$  \\$$ |$$ |  $$ |
$$    |   $$$$  $$ |$$ |  $$ |
$$$$$/    $$ $$ $$ |$$ |  $$ |
$$ |_____ $$ |$$$$ |$$ |__$$ |
$$       |$$ | $$$ |$$    $$/ 
$$$$$$$$/ $$/   $$/ $$$$$$$/  
\n""", flush=True)

