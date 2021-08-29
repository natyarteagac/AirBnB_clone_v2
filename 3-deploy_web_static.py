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
    file_token_one = archive_path.split("/")[-1]
    file_token_two = file_token_one.split(".")[0]
    path_tokenized = ("/data/web_static/releases/" +
                      file_token_two.split(".")[0])
    try:
        put(archive_path, '/tmp/')
        run("sudo mkdir -p {}".format(path_tokenized))
        run("sudo tar -xzf /tmp/{} -C {}".format(
            file_token_one, path_tokenized))
        run("sudo rm /tmp/{}".format(file_token_one))
        run("sudo mv {}/web_static/* {}/".format(
            path_tokenized, path_tokenized))
        run("sudo rm -rf {}/web_static".format(
            path_tokenized))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(path_tokenized))
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
