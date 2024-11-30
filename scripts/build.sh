#!/bin/bash

if [[ "$OSTYPE" == "darwin"* ]] && [[ "$(uname -m)" == "arm64" ]]; then
    
    rm -rf build

    VERSION=$(sed -n 's/^version = "\([^"]*\)"/\1/p' pyproject.toml)

    briefcase build
    briefcase package --adhoc-sign
    
    mv dist/Mangnify-*.dmg "dist/Mangnify_macOS_arm_64-v${VERSION}.dmg"

else
    echo "This script is intended to be run on macOS with Apple Silicon (arm64) only"
fi