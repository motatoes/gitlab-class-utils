import sys, os
import requests
import json
from loader import get_settings

CONFIG = get_settings()
BASE_URL = CONFIG.get('HOSTNAME', "https://gitlab.com/")

class GitlabAPI:
    
    def __init__(self, private_token, *args, **kwargs):

        self.private_token = private_token

    def get_user_details(self, username):
        private_token = self.private_token

        res = requests.get(BASE_URL + "api/v3/users/?username=%s" % username, headers={"PRIVATE-TOKEN": private_token} )
        print(res.text, file=sys.stderr)

        resJson = json.loads(res.text)

        if len(resJson) == 0:
            raise Exception("The user was not found")

        if "error" in resJson:
            raise Exception("The server returned an error")

        userid = resJson[0]

        return userid

    def get_group_details(self, groupname):
        private_token = self.private_token
        print('fetching group info', file=sys.stderr)
        groupsRes = requests.get(BASE_URL + "api/v3/groups/?search=%s" % groupname, headers={"PRIVATE-TOKEN": private_token} )
        print(groupsRes.text, file=sys.stderr)
        groupsResJson = json.loads(groupsRes.text)

        if len(groupsResJson) == 0:
            raise Exception("The group was not found")

        if "error" in groupsResJson:
            raise Exception("The server returned an error")

        for group in groupsResJson:
            if group['name'].lower() == groupname.lower():
                return group

        raise("The group was not found")

    def get_project_details(self, namespace, projectname):
        request_url = BASE_URL + "api/v3/projects/" + namespace + "%2F" + projectname + "%s"        
        result = requests.post( request_url, headers={"PRIVATE-TOKEN": private_token})
        resultJson = json.loads(result.text)
        return resultJson

    def add_user_to_group(self, userid, groupid, access_level):
        private_token = self.private_token
        groupAddParams = {
            "id": groupid,
            "user_id": userid, # anon.r4bia
            "access_level": access_level
        }

        result = requests.post( BASE_URL + "api/v3/groups/%s/members" % groupid, 
                    data=groupAddParams, headers={"PRIVATE-TOKEN": private_token} )

        print(groupid, file=sys.stderr)
        print(result.text, file=sys.stderr)

        resultJson = json.loads(result.text)
        return resultJson


    def get_group_members(self, groupid, page=1, perpage=20):
        private_token = self.private_token
        request_url = BASE_URL + "api/v3/groups/%s/members?page=%s&per_page=%s" % (groupid, page, perpage)
        result = requests.post( request_url, headers={"PRIVATE-TOKEN": private_token})
        resultJson = json.loads(result.text)
        return resultJson

