#!/bin/bash
# This script is going to remove cmake in OS and install newest version cmake.

apt remove cmake

sudo apt install -y libssl-dev openssl1.0
# For building cmake-gui
sudo apt install -y qt5-default

wget -c --show-progress https://github.com/Kitware/CMake/releases/download/v3.22.1/cmake-3.22.1.tar.gz
tar -xvf cmake*.tar.gz
rm cmake*.tar.gz

cd cmake-3.22.1
./configure
sudo make install

#rm -r cmake-3.22.1

cmake --version
