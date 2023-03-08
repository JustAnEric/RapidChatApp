import os,shutil,time,json,requests

loadVersion = json.load(open('../version.json'))

def checkForUpdates(): 
  resp = requests.get('https://rapidchat.ericplayzyt.repl.co/updates/getLastestVersion')
  if resp.json()["version"] == loadVersion["latestUpdatedVersion"]:
    return "No updates found. Opening client..."
  else: _updateClient({"version": "latest"}); return "An update was found. Please wait for client to update..."
  
def _updateClient(updater_info):
  newversion = updater_info["version"]
  if newversion == "latest":
    #update software to latest version
    os.system('git clone https://github.com/WWEMGamer2/RapidChatApp.git ../../ --quiet') #update the client quietly
    os.remove('./') # remove parent folder
    return "Please close and re-open this program."
 
