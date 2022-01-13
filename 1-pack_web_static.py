#!/usr/bin/python3

"""
Compress before sending

"""
from fabric.api import local
from os.path import isdir
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
