#!/bin/sh
# Install and configure a plugin: ctrlp.vim
# github repo url: https://github.com/ctrlpvim/ctrlp.vim

# Create the plugins directory
mkdir -p ~/.vim/pack/vendor/start

# Download the plugin with git
cd ~/.vim/pack/vendor/start; git clone https://github.com/ctrlpvim/ctrlp.vim

# Read the documentation for the plugin.
# DOCUMENTATION URL:
# https://github.com/ctrlpvim/ctrlp.vim/blob/master/readme.md

echo "let g:ctrlp_map = '<c-p>'" >> ~/.vimrc
