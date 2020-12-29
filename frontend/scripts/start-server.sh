#!/bin/sh

set -e

cp /app/package.json /node_env/
cd /node_env && npm install