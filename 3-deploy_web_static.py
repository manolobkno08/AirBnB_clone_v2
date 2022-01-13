#!/usr/bin/python3

"""
Compress before sending

"""
from os.path import exists
from fabric.api import env, put, run, local
from os.path import isdir, exists
import datetime

date_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def do_pack():
    """ Compress to tgz """
    try:
        if isdir('versions') is False:
            local("mkdir versions")
        filename = "versions/web_static_{}.tgz".format(date_now)
        local('tar -cvzf {} web_static'.format(filename))
        return filename
    except Exception:
        return None


"""
Files deployment 2

"""

env.hosts = [
    '35.237.25.66',
    '34.234.71.240'
]
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Deploy files """
    if exists(archive_path) is False:
        return False
    try:
        filename = archive_path.split('/')[1]
        no_ext = archive_path.split('/')[1].split('.')[0]
        final_path = "/data/web_static/releases/"

        # Upload file into the tmp directory
        put('{}, /tmp/'.format(archive_path))
        # Create a folder into the server
        run('sudo mkdir -p {}{}/'.format(final_path, no_ext))
        # Uncompress file
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(
            filename, final_path, no_ext))
        # Delete tgz file
        run('sudo rm /tmp/{}'.format(filename))
        # Move
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(
            final_path, no_ext))
        run('sudo rm -rf {}{}/web_static'.format(final_path, no_ext))
        # Delete current simbolic link
        run('sudo rm -rf /data/web_static/current')
        # Create new simbolic link
        run('sudo ln -s {}{}/ /data/web_static/current'.format(
            final_path, no_ext))
        return True
    except Exception:
        return False


"""
Deploy 3

"""


def deploy():
    """ Deployment 3 """
    try:
        new_filename = do_pack()
        x = do_deploy(new_filename)
        return x
    except Exception:
        return False
