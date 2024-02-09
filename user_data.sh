#!/bin/bash
dnf update -y
dnf install git -y
dnf install python3-pip -y
git clone https://github.com/bluehackrafestefano/flask_test_proj.git app
cd app
pip install Flask
python3 hello.py
