import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="registry-du",
    version="0.0.1",
    author="Nova Kwok",
    author_email="noc@nova.moe",
    description="Give you a better view of your Docker registry disk usage.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/n0vad3v/registry-du",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "terminaltables"
    ],
    entry_points={
        'console_scripts': [
            'registry-du=registry_du.registry_du:main',
        ],
    }
)