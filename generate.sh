#!/bin/bash

echo "Generating game models from sample..."
datamodel-codegen --input-file-type json --input samples/game.json --output src/models/game.py --class-name Game
echo "Done."

echo "Generating player models from sample..."
datamodel-codegen --input-file-type json --input samples/player.json --output src/models/player.py --class-name Player
echo "Done."