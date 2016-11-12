#!/bin/sh
echo "Starting ..."

echo ">> Deleting old migrations"
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

rm *.csv

# Optional
echo ">> Deleting database"
find . -name "db.sqlite3" -delete

echo ">> Deleting files in the media folder"
rm media/*.json
rm media/*.csv
rm media/files/*.csv
rm media/*.pkl

echo ">> Deleting files in the data folder"
rm data/*
mkdir data
touch data/dummy_file
echo "..." >> data/dummy_file

echo ">> Deleting all pyc files"
find . -name "*.pyc" -exec rm -rf {} \;

echo ">> Running manage.py makemigrations"
python manage.py makemigrations

echo ">> Running manage.py migrate"
python manage.py migrate

echo ">> Done"
