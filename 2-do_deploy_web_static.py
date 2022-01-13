#!/usr/bin/python3

"""
Files deployment

"""
from fabric.api import *
# from os.path import isdir
# import datetime


env.hosts = [
    '35.237.25.66',
    '34.234.71.240'
]

env.user = "ubuntu"


def do_deploy(archive_path):
    """ Deploy files """
    if archive_path is False:
        return False
    try:
        filename = archive_path.split('/')[1].split('.')[0]
        final_path = "/data/web_static/releases/"

        # Upload file into the tmp directory
        put('{}, /tmp/'.format(archive_path))
        # Create a folder into the server
        run('mkdir -p {}{}'.format(final_path, filename))
        # Uncompress file
        run('tar -zxvf /tmp/{} -C {}{}/'.format(archive_path, final_path, filename))
        # Delete tgz file
        run('rm /tmp/{}.tgz'.format(filename))
        # Move
        run('mv {}{}/web_static/* /data/web_static/releases/{}/'.format(final_path, filename, filename))
        run('rm -rf {}{}/web_static'.format(final_path, filename))
        # Delete current simbolic link
        run('rm -rf /data/web_static/current')
        # Create new simbolic link
        run('ln -s {}{}/ /data/web_static/current'.format(final_path, filename))
    except Exception:
        return False
