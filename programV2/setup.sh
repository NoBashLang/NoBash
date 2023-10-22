#!/bin/bash
# This is used for testing purposes only

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ln -s "$SCRIPT_DIR/data" ~/.nobash
echo "Created symlink from the data dir to ~/.nobash!"
echo $SCRIPT_DIR