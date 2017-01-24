# docker-images-cleanup
This tool is designed to remove all unused docker images from your host.

# How in works
Algorythm is pretty simple:
* Collect list of all images
* Scan existing containers and remove corresponding images from the list
* Remove all remaining images from the list

# How to use
```
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock docker-images-cleanup
```
