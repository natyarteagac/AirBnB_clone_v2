#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
from the contents of the web_static folder of the
AirBnB Clone repo using do_pack.
"""
from fabric.api import local, put, run, env
from os import path
env.hosts = ['34.139.140.249', '100.26.46.66']


def do_deploy(archive_path):
    """Distributes an archive to the web server """

    if not path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        archive_token = archive_path.split("/")[-1]
        archive_tokenized = archive_token.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}".format(archive_tokenized))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            archive_token, archive_tokenized))
        run("rm /tmp/{}".format(archive_token))
        run(
            "mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".format(
                archive_tokenized, archive_tokenized))
        run(
            "rm -rf /data/web_static/releases/{}/web_static/".format(
                archive_tokenized))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} \
            /data/web_static/current".format(archive_tokenized))
        return True
    except:
        return False
