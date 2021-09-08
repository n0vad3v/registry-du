# registry-du

![](https://img.shields.io/pypi/pyversions/Django.svg)

> Give you a better view of your Docker registry disk usage.

This small tool will analysis your Docker registry(vanilla or Harbor both work), and shows how many space does those project use, it also shows top disk-consuming 20 images in the registry.

## Installation

```
pip3 install registry-du
```

## Usage

```
registry-du /path/to/registry/docker/registry/v2
```

## Example output

```
➜  registry-du /home/X/du-demo/registry/data/docker/registry/v2

Registry Path is: /home/X/du-demo/registry/data/docker/registry/v2
+Project-Size----------+-----------+
| Project Name         | Size(MiB) |
+----------------------+-----------+
| jellyfin             | 277.55    |
| library              | 147.62    |
| mongo-express:latest | 47.2      |
+----------------------+-----------+
+Image-Size----------------+-----------+
| Image Name               | Size(MiB) |
+--------------------------+-----------+
| jellyfin/jellyfin:latest | 277.55    |
| library/mysql:5.7        | 147.62    |
| mongo-express:latest     | 47.2      |
+--------------------------+-----------+
```