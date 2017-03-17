import os, sys
import csv
import json
from flask import Flask
from flask import render_template
from flask import request
# from students import userslist
from gitlab import GitlabAPI #get_user_details, get_group_details, add_user_to_group
from loader import get_settings, get_students 

app = Flask(__name__)
app.config.update(get_settings())


@app.route("/", methods = ['GET'])
def adduser():
    private_token = app.config['GITLAB_PRIVATE_TOKEN']
    groupname = app.config['GROUPNAME'] 

    template = 'index.html'
    username = request.args.get("username")
    userslist = get_students()

    if username is not None:
        if username.lower() not in userslist:
            return render_template(template, error='Your username does not appear to be in the list of users. Contact your instructor if you think this is in error')

        gl = GitlabAPI(private_token)
        try:
            userid = gl.get_user_details(username.upper())['id']
        except Exception as e:
            # print(e, file=sys.stderr)
            return render_template(template, error='There was an error while attempting to fetch your userID, are you sure you logged in (or registered) on the site?')

        try:
            groupid = gl.get_group_details(groupname)['id']
        except Exception as e:
            # print(e, file=sys.stderr)
            return render_template(template, error='There was an error while fetching the group ID, are you sure that you specified the right group name?')

        try:
            # Access level is 20 for reporter
            res = gl.add_user_to_group(userid, groupid, 20)
        except Exception as e:
            # print(e, file=sys.stderr)
            return render_template(template, error="A problem occured while adding you to the workshop group .. please contact your instructors")

        return render_template(template, success="You have been successfully added to the group, you can now go back to the site and see the workshops!")
    else:
        return render_template(template)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
