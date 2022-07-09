#!/bin/bash

echo "Generating game models from sample..."
datamodel-codegen --input-file-type json --input samples/game.json --output cflpy/models/game.py --class-name Game
echo "Done."

echo "Generating player models from sample..."
datamodel-codegen --input-file-type json --input samples/player.json --output cflpy/models/player.py --class-name Player
echo "Done."

echo "Generating standings modesl from sample..."
datamodel-codegen --input-file-type json --input samples/standings.json --output cflpy/models/standings.py --class-name Standings
echo "Done."