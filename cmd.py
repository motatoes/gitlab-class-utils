from loader import get_settings
from gitlab import GitlabAPI


if __name__ == '__main__':
    print("command line args")

    config = get_settings()

    private_token = config['GITLAB_PRIVATE_TOKEN']

    private_token
    gl = GitlabAPI(private_token)

    group_id = gl.get_group_details(config['GROUPNAME'])["id"]
    print(group_id)

    # i = 1
    # allmembers = []
    # while True:
    #     members = gl.get_group_members(group_id, page=i, perpage=100)
    #     print(members)
    #     if len(members) == 0:
    #         break
    #     i = i + 1
    #     allmembers.append(members)

    # allmembers = [item for sublist in allmembers for item in sublist]
    # print(allmembers)


    