#!/bin/sh

# Install python3 on Alpine linux (Docker)
if [ "$(command -v apk)" ]; then
  apk add python3
  exit 0
fi

# Install python 3 on Arch Linux (if already does not have)
if [ "$(command -v pacman)" ]; then
  pacman -Sy python

  # To detect where is python
  # pacman -Sy which
  #/bin/sh which python

  exit 0
fi
