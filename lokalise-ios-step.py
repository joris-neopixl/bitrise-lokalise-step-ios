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
lokalise_token = "%s/%s" % (project_root_path, os.getenv('lokalise_token'))
lokalise_project_id = "%s/%s" % (project_root_path, os.getenv('lokalise_project_id'))
file_path = "%s/%s" % (project_root_path, os.getenv('file_path'))

print("\n project_root_path === %s" % project_root_path)
print("\n lokalise_token === %s" % lokalise_token)
print("\n lokalise_project_id === %s" % lokalise_project_id)
print("\n file_path === %s" % file_path)


# Get all translations from Lokalise 
import requests



lokalise_project_id_2 = "test_ID_34234"
lokalise_token_2 = "testTOKEN_222"

url = "https://api.lokalise.com/api2/projects/%s/keys?include_comments=0&include_translations=1&pagination=offset&limit=500" % lokalise_project_id_2

headers = {
    "accept": "application/json",
    "X-Api-Token": "%s" % lokalise_token_2
}

response = requests.get(url, headers=headers)


print("\n API URL === %s" % url, flush=True)
print("\n API HEADER === %s" % headers, flush=True)
print("\n API RESP === %s" % response.text, flush=True)




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

