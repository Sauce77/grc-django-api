#!/usr/bin/env bash
# exit or error

set -o errexit

pip install -r requirements.txt

python grcapi/manage.py collectstatic --no-input
python grcapi/manage.py migrate