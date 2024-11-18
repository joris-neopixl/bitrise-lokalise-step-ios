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

headers = {
    "accept": "application/json",
    "X-Api-Token": "%s" % lokalise_token
}

url_project = "https://api.lokalise.com/api2/projects/%s" % lokalise_project_id
response_project = requests.get(url_project, headers=headers)

# Read & Parse JSON
json_project = response_project.json()

print("\n Verifing the setting of the project...", flush=True)

keys_total = json_project['statistics']['keys_total']
print("\n  -> There is %s keys in the project" % keys_total, flush=True)

import math
number_of_page = keys_total / 500
number_of_page_ceil = math.ceil(number_of_page)

print("\n  -> Number of page to fetch %s" % (number_of_page_ceil), flush=True)

number_of_unverified_key = 0

for page in range(1, number_of_page_ceil+1):
    url_translations = "https://api.lokalise.com/api2/projects/%s/keys?include_comments=0&include_translations=1&pagination=offset&limit=500&page=%s" % (lokalise_project_id, page)
    response_translation = requests.get(url_translations, headers=headers)
    json_translation = response_translation.json()
    print("\n Verifing %s translations status for page %s" % (len(json_translation['keys']), page), flush=True)

    for key in json_translation['keys']:
        for translation in key['translations']:
	        status = translation['is_unverified']
	        if status == True:
	        	number_of_unverified_key = number_of_unverified_key + 1

print("\n -> number_of_unverified_key = %s <-" % number_of_unverified_key, flush=True)

if number_of_unverified_key > 0 :
    print("\n\n\n ! ! ! ERROR ! ! ! \n\n\n\n\n: SOME KEY(S) (%s) ARE NOT VERIFIED, PLEASE VERIFY ALL KEYS BEFORE CREATING A RELASE \n\n\n\n\n ! ! ! ERROR ! ! !\n\n\n" % number_of_unverified_key, flush=True)
    os._exit(12)
else:
    print("\n\n ! ! !  SUCCESS ! ! ! \n\nAll keys are 'verified', let's continue and update the project with fresh translations :D\n", flush=True)

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

