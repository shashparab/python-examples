#!/usr/bin/env bash


DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

virtualenv -p python3.7 ${DIR}/../venv
source ${DIR}/../venv/bin/activate
pip install -r ${DIR}/../requirements.txt