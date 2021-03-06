#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents
   of Airbnb_clone_v2
'''

from datetime import datetime
from fabric.api import *
from time import strftime
import os
env.hosts = ["34.73.0.225", "35.229.78.70"]


def do_pack():
    """function"""
    local("mkdir -p versions")
    full = local("tar -cvzf versions/web_static_{}.tgz\
        web_static".format(strftime("%Y%m%d%H%M%S")))
    if full:
        return ("versions/web_static_{}".format(strftime("%Y%m%d%H%M%S")))
    return (None)


def do_deploy(archive_path):
    '''func deploy'''
    if not os.path.exists(archive_path):
        return(False)
