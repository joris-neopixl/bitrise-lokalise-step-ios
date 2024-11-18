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

url_translations = "https://api.lokalise.com/api2/projects/%s/keys?include_comments=0&include_translations=1&pagination=offset&limit=500&page=1" % lokalise_project_id
response_translation = requests.get(url_translations, headers=headers)


# Read & Parse JSON
json_project = response_project.json()
json_translation = response_translation.json()

print("\n Verifing the setting of the project...", flush=True)

keys_total = json_project['statistics']['keys_total']
print("\n  -> There is %s keys in the project\n" % keys_total, flush=True)

print("\n Verifing %s translations status..." % len(json['keys']), flush=True)

for key in json['keys']:
    for translation in key['translations']:
	    status = translation['is_unverified']
	    if status == True:
	        print("\n\n\n ! ! ! ERROR ! ! ! \n\n\n\n\n: SOME KEY(S) (%s) ARE NOT VERIFIED, PLEASE VERIFY ALL KEYS BEFORE CREATING A RELASE \n\n\n\n\n ! ! ! ERROR ! ! !\n\n\n" % key['key_name']['ios'], flush=True)
	        os._exit(12)

print("\n All keys are 'verified', let's continue and update the project with fresh translations :D", flush=True)

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

