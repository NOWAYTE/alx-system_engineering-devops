#!/bin/bash

echo "SENDER,RECEIVER,FLAGS"
awk -F',' '{print $1","$2","$3}' text_messages.log
