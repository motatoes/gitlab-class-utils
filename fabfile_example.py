from fabric.api import *

# the user to use for the remote commands
env.user = 'hostmachine_username'
# the servers where the commands are executed
env.hosts = ['myserver.domain.com']

def pack():
    # build the package
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    # figure out the package name and version
    dist = local('python setup.py --fullname', capture=True).strip()
    filename = '%s.tar.gz' % dist

    # upload the package to the temporary folder on the server
    put('dist/%s' % filename, '/tmp/%s' % filename)

    # install the package in the application's virtualenv with pip
    run('/home/gitlabku/kuworkshops/env/bin/pip install /tmp/%s' % filename)

    # remove the uploaded package
    run('rm -r /tmp/%s' % filename)

    # touch the .wsgi file to trigger a reload in mod_wsgi
    # run('home/gitlabku/kuworkshops/yourapplication.wsgi')
