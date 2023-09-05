import os
import glob
import json
import httpx

TOP_LEVEL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTOMATION_DIR = os.path.dirname(os.path.abspath(__file__))

DIRECTORY_LIST = [ y for y in glob.glob(os.path.join(TOP_LEVEL_DIR, '*')) if os.path.isdir(y) ]
DIRECTORY_LIST.sort()

SUB_DIRECTORY_LIST = [ y for x in DIRECTORY_LIST for y in glob.glob(os.path.join(x, '*')) if os.path.isdir(y) ]
SUB_DIRECTORY_LIST.sort()
# call the CTF Time API from the url in event.txt

with open(os.path.join(AUTOMATION_DIR, 'event.txt'), 'r') as f:
    event_url = f.read()
    # generate the api url from the event url
    api_url = event_url.replace('ctftime.org/event/', 'ctftime.org/api/v1/events/')

# get the event description from the api url
r = httpx.get(api_url)
event_description = r.json()['description']
event_name = r.json()['title']

# Open the descriptions file and read the descriptions into a list
with open(os.path.join(AUTOMATION_DIR, 'descriptions.json'), 'r') as f:
    descriptions = json.load(f)

# generate the README.md file. 
# generate an unordered list of the directories and subdirectories in the repository. 
# should be in the format of:
# * [directory name](directory link)
#   * [subdirectory name](subdirectory link)
#   * [subdirectory name](subdirectory link)
# and so on...

with open(os.path.join(TOP_LEVEL_DIR, 'README.md'), 'w') as f:
    f.write('# ' + event_name + '\n\n')
    f.write(event_url + '\n\n')
    f.write('## Event Description\n\n')
    f.write(event_description + '\n\n')
    for directory in DIRECTORY_LIST:
        f.write('## [{}](<{}>)\n'.format(os.path.basename(directory), os.path.basename(directory)))
        for subdirectory in SUB_DIRECTORY_LIST:
            if os.path.dirname(subdirectory) == directory:
                f.write(' * #### [{}](<{}/{}/>)\n'.format(os.path.basename(subdirectory), os.path.basename(directory), os.path.basename(subdirectory) ))

# do the same thing for the README in each directory
for directory in DIRECTORY_LIST:
    with open(os.path.join(directory, 'README.md'), 'w') as f:
        f.write('# ' + os.path.basename(directory) + '\n\n')
        # From the descriptions var, check if the directory name is contained in the category and if so, write the description to the README
        f.write('### Category Description\n\n')
        for category in descriptions['categories']:
            if os.path.basename(directory) in category['name']:
                f.write(category['details']['description'] + '\n\n')
        f.write('## Challenges\n\n')
        for subdirectory in SUB_DIRECTORY_LIST:
            if os.path.dirname(subdirectory) == directory:
                f.write('- ### [{}](<{}>)\n'.format(os.path.basename(subdirectory), os.path.basename(subdirectory)))