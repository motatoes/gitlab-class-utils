from loader import get_settings
from gitlab import GitlabAPI

CONFIG = get_settings()
hostname = CONFIG['HOSTNAME'] = "http://gitlab.kingston.ac.uk/"
groupname = CONFIG['GROUPNAME'] = "CI5100-2016-17"
privateToken = CONFIG['GITLAB_PRIVATE_TOKEN'] = "yoqzJPTcY4siMn_ARWgD"

gapi = GitlabAPI(privateToken)

groupDetails = gapi.get_group_details(groupname)
groupMembers = gapi.get_group_members(groupDetails["id"], perpage=200, page=1)


print("== GROUP DETAILS == ")
print(groupDetails)

print("==  GROUP MEMBERS == ")
print(groupMembers)



