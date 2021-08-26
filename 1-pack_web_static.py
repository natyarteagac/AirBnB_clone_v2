#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
from the contents of the web_static folder of the
AirBnB Clone repo using do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Extract the content of an archive"""
    hour = datetime.now().strftime('%Y%m%dT%H%M%S')
    name_of_file = "web_static_" + hour + ".tgz"
    try:
        print("Packing web_static to versions/{}".format(name_of_file))
        local("mkdir -p version")
        local("tar -cvzf versions/{} web_static".format(name_of_file))
    except:
        return None
