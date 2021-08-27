#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
from the contents of the web_static folder of the
AirBnB Clone repo using do_pack.
"""
from fabric.api import local, put, run, env
from datetime import datetime
from os import path


def do_pack():
    """Extract the content of an archive"""
    hour = datetime.now().strftime('%Y%m%dT%H%M%S')
    name_of_file = "web_static_" + hour + ".tgz"
    try:
        print("Packing web_static to versions/{}".format(name_of_file))
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(name_of_file))
    except:
        return None


def do_deploy(archive_path):
    """Distributes an archive to the web server """
    hour = datetime.now().strftime('%Y%m%dT%H%M%S')
    name_of_file = "web_static_" + hour + ".tgz"
    name_of_file_two = "web_static_" + hour
    env.hosts = ['34.139.140.249 web-01', '100.26.46.66 web-02']

    if not path.exists(archive_path):
        return False
    try:
        put('{}', '/tmp/'.format(name_of_file))
        run("mkdir -p /data/web_static/{}".format(name_of_file_two))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(name_of_file, name_of_file_two))
        run("rm /tmp/{}".format(name_of_file))
        run("mv /data/web_static/releases/{}/web_static /data/web_static/{}".format(name_of_file_two))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name_of_file))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current".format(name_of_file_two))
    except:
        return None
