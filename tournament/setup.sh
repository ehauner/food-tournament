#!/bin/sh
echo "Setting up ..."

echo ">> Installing pip"
echo "Enter your computer's password..."
sudo easy_install pip

echo ">> Updating pip"
pip install --upgrade pip

echo ">> Installing numpy"
pip install numpy

echo ">> Installing pandas"
pip install pandas

echo ">> Installing Django"
pip install Django

echo ">> Done"
