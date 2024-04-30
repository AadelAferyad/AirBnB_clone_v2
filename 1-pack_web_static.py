#!/usr/bin/python3
""" deploy using fabric """


from datetime import datetime
from fabric.api import *


def do_pack():
    """ create archive"""
    local("mkdir -p versions")
    current_t = datetime.now().strftime("%Y%m%d%H%M%S")
    path = f"versions/web_static_{current_t}.tgz"

    r = local(f"tar czf {path} web_static/")

    if r.succeeded:
        return path
    else:
        return None
