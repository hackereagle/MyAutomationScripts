#!/bin/bash

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com//Homebrew/install/HEAD/install.sh)"
echo export PATH=$PATH:/opt/homebrew/bin >> ~/.zshrc

brew install build-essential
brew install cmake
