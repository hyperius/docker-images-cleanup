#!/usr/bin/env python

import docker
from docker.errors import APIError


def info(name, status):
    print "[ %s ] %s" % (status, client.images.get(name).short_id.replace('sha256:', ''))


def error(name, desc):
    print "[ error ] %s: %s" % (client.images.get(name).short_id.replace('sha256:', ''), desc)


client = docker.from_env(version="auto")
images = []

for image in client.images.list():
    images.append(image.id)
    info(image.id, 'found')

for container in client.containers.list(all=True):
    image = container.attrs.get('Image')
    if image in images:
        info(image, 'used')
        images.remove(image)

for image in images:
    try:
        client.images.remove(image)
        info(image, 'deleted')
    except APIError as e:
        error(image, e.message)
