#!/usr/bin/python3

"""
Files deployment

"""
from fabric.api import env, put, run
from os.path import exists

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
        filename = archive_path.split('/')[1].split('.')[0]
        final_path = "/data/web_static/releases/"

        # Upload file into the tmp directory
        put('{}, /tmp/'.format(archive_path))
        # Create a folder into the server
        run('sudo mkdir -p {}{}'.format(final_path, filename))
        # Uncompress file
        run('sudo tar -xzf /tmp/{}.tgz -C {}{}/'.format(
            filename, final_path, filename))
        # Move
        run('sudo mv {}{}/web_static/* /data/web_static/releases/{}/'.format(
            final_path, filename, filename))
        # Delete tgz file
        run('sudo rm /tmp/{}.tgz'.format(filename))
        run('sudo rm -rf {}{}/web_static'.format(final_path, filename))
        # Delete current simbolic link
        run('sudo rm -rf /data/web_static/current')
        # Create new simbolic link
        run('sudo ln -s {}{}/ /data/web_static/current'.format(
            final_path, filename))
    except Exception:
        return False
