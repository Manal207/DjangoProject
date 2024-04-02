#!/bin/sh

if [ "$NODE_ENV" == "dev" ]; then
	npm install --verbose
	npm run start
else
	npm run build
	npm run start
fi
