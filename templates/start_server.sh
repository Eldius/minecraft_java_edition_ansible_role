#!/bin/bash

JAVA_OPTS="${JAVA_OPTS} -XX:+UseG1GC"
JAVA_OPTS="${JAVA_OPTS} -XX:MaxRAM=512m"
JAVA_OPTS="${JAVA_OPTS} -XX:+UseStringDeduplication"
JAVA_OPTS="${JAVA_OPTS} -XX:+OptimizeStringConcat"
JAVA_OPTS="${JAVA_OPTS} -XX:+UseLWPSynchronization"
JAVA_OPTS="${JAVA_OPTS} -Xmx{{ minecraft_max_memory }}"
JAVA_OPTS="${JAVA_OPTS} -Xms{{ minecraft_min_memory }}"

java $JAVA_OPTS -jar {{ minecraft_install_folder }}/server.jar nogui
