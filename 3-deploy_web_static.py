#!/usr/bin/python3
""" Fabric scrit that creates and distributes an archive you the
web server using the function"""

from datetime import datetime
from os import path
from fabric.api import local, put, run, env
env.hosts = ['34.139.140.249', '100.26.46.66']


def do_pack():
    """Extract the content of an archive"""
    hour = datetime.now().strftime('%Y%m%dT%H%M%S')
    name_of_file = "web_static_" + hour + ".tgz"
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(name_of_file))
        return "versions/{}".format(name_of_file)
    except:
        return None


def do_deploy(archive_path):
    """Distributes an archive to the web server """

    if path.isfile(archive_path) is False:
        return False
    archive_token = archive_path.split("/")[-1]
    archive_tokenized = archive_token.split(".")[0]
    try:
        put(archive_path, '/tmp/')
        run("sudo mkdir -p /data/web_static/releases/{}".format(archive_tokenized))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            archive_token, archive_tokenized))
        run("sudo rm /tmp/{}".format(archive_token))
        run(
            "sudo mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".format(
                archive_tokenized, archive_tokenized))
        run(
            "sudo rm -rf /data/web_static/releases/{}/web_static/".format(
                archive_tokenized))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{} \
            /data/web_static/current".format(archive_tokenized))
        return True
    except:
        return False


def deploy():
    """Using the last created functions"""

    try:
        archive_path = do_pack()
        answer = do_deploy(archive_path)
        return answer
    except:
        return False
