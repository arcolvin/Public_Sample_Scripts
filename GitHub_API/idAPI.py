import requests
import json
from pathlib import Path

def authenticate(cfgFile):
    # Load user / token from an external file
    # File should have user name on first line and token on second line
    with open(cfgFile) as tokenFile:
        user = tokenFile.readline().strip('\n')
        token = tokenFile.readline().strip('\n')

    return requests.auth.HTTPBasicAuth(user, token)

def getUsers(oname, token):
    usrlst = []
    # Request list of user info for provided organization
    r = requests.get(f'https://api.github.com/orgs/{oname}/members', auth=token)
    usrs = json.loads(r.text)
    # collect user's usernames in list usrlst
    for itm in usrs:
        usrlst.append(itm['login'])
    
    return usrlst
        
def getPic(uname, token):
    # get specific user information
    r = requests.get(f'https://api.github.com/users/{uname}', auth=token)
    userInfo = json.loads(r.text)
    # Request the binary data for the user's picture
    img = requests.get(userInfo['avatar_url'], stream=True)
    #Identify the picture file type (jpg or png ideally)
    typ = img.headers['Content-Type'][img.headers['Content-Type'].find('/') + 1:]
    if typ == 'jpeg':
        typ = 'jpg'

    #Create target directory if it does not exist
    outFile = f"Avatars/{uname}.{typ}"
    Path(outFile).parent.mkdir(exist_ok=True, parents=True)
    
    # If download is successful, save image raw data to a file
    if img.status_code == 200:
        with open(outFile, 'wb') as pic:
            for block in img.iter_content(1024):
                pic.write(block)

if __name__ == '__main__':
    org = 'python'
    config = 'token.cfg'
    usrlst = [org]

    # Auth via external file
    # File formatting explained in related authenticate function 
    basicAuth = authenticate(config)

    # Get Org People List
    usrlst.extend(getUsers(org, basicAuth))

    for user in usrlst:
        getPic(user, basicAuth)
    
    print("Avatars will be found in the avatar folder of your current working directory.")