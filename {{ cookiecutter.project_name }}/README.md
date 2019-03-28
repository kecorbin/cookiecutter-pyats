# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Setup / Running

### Local

Create venv & install requirements.txt

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run kicoff the tests

```
./run.sh
```

### Docker

Build an image from the [Dockerfile](./Dockerfile)

```
docker build -t {{ cookiecutter.github_org }}/{{cookiecutter.github_id}} . && \
```

Launch a container from the image

```
docker run --rm {{ cookiecutter.github_org }}/{{cookiecutter.github_id}}
```

**Note:** You'll likely want to mount some volumes so that you can persist logs, etc. see [here](https://docs.docker.com/storage/volumes/) for more information

## Project Structure

A quick overview of the project structure


```
.
├── Dockerfile
├── Makefile
├── README
├── VERSION
├── {{cookiecutter.project_name}}_job.py
├── data          
├── easypy_config.yaml
├── plugins
│   ├── README.md
│   ├── __init__.py
│   └── {{cookiecutter.project_name}}.py
├── processors
│   ├── README.md
│   └── {{cookiecutter.project_name}}.py
├── requirements.txt
├── run.sh
├── testbeds
│   └── default.yaml
└── testscripts
    ├── README.md
    ├── Test{{cookiecutter.testcase_class}}Device.py
    ├── Test{{cookiecutter.testcase_class}}.py
    └── libs
        ├── README.md
        ├── __init__.py
        └── {{cookiecutter.project_name}}.py
```

## Background

Generated from [cookiecutter-pyats](https://github.com/kecorbin/cookiecutter-pyats)
