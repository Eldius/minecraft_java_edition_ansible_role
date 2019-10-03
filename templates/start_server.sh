#!/bin/bash

java -Xmx{{ minecraft_max_memory }} -Xms{{ minecraft_min_memory }} -jar {{ minecraft_install_folder }}/server.jar nogui
