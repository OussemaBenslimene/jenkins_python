#!/bin/bash
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Building application..."
python -m compileall app
