#!/bin/bash

export $(cat .env | xargs) &&
scp ~/prog/Internship-Autumn-ITTP/server-client_picture/server.py $NAME@$IPAD:~/ &&
scp ~/prog/Internship-Autumn-ITTP/server-client_picture/pictures/photo2.jpg $NAME@$IPAD:~/ &&
ssh $NAME@$IPAD "cd && python3 server.py>text.txt" & cd ~/prog/Internship-Autumn-ITTP/server-client_picture/ && python3 client.py

