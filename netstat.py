#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import os
import sys
import glob

PROC_FILE = {
    'tcp': '/proc/net/tcp',
    'tcp6': '/proc/net/tcp6',
    'udp': '/proc/net/udp',
    'udp6': '/proc/net/udp6'
}

STATUS = {
    '01': 'ESTABLISHED',
    '02': 'SYN_SENT',
    '03': 'SYN_RECV',
    '04': 'FIN_WAIT1',
    '05': 'FIN_WAIT2',
    '06': 'TIME_WAIT',
    '07': 'CLOSE',
    '08': 'CLOSE_WAIT',
    '09': 'LAST_ACK',
    '0A': 'LISTEN',
    '0B': 'CLOSING'
}

def get_content(type):
    with open(PROC_FILE[type],'r') as file:
        content = file.readlines()
        content.pop(0)
    return content

def get_programe_name(pid):
    path = '/proc/' + str(pid) + '/comm'
    with open(path,'r') as file:
        content = file.read()
    content = content.strip()
    return content

def convert_ip_port(ip_port):
    ip,port = ip_port.split(':')
    port = int(port, 16)
    ip = [str(int(ip[6:8],16)),str(int(ip[4:6],16)),str(int(ip[2:4],16)),str(int(ip[0:2],16))]
    ip =  '.'.join(ip)
    return ip, port

def get_pid(inode):
    for path in glob.glob('/proc/[1-9]*/fd/[1-9]*'):
        try:
            if str(inode) in os.readlink(path):
                return path.split('/')[2]
            else:
                continue
        except:
            pass
    return None


def main(choose):
    content = get_content(choose)
    for info in content:
        iterms = info.split(' ')
        iterms_list = [x for x in iterms if x != '']
        proto = choose
        locals_address = "%s:%s" % convert_ip_port(iterms_list[1])
        status = STATUS[iterms_list[3]]
        if status == 'LISTEN':
            remote_address = '_'
        else:
            remote_address = "%s:%s" % convert_ip_port(iterms_list[2])
        pid = get_pid(iterms_list[9])
        programe_name = ''
        if pid:
            programe_name = get_programe_name(pid)
        print(temp1 % (
            proto,
            locals_address,
            remote_address,
            status,
            pid or '_',
            programe_name or '_',
        ))

if __name__ == '__main__':
    temp1 = "%-5s %-30s %-30s %-13s %-6s %s"
    print(temp1 % ( 
        "Proto","Local address",'Remote address','Status',"PID","Program name"))
    argv_list = ('tcp','tcp6','udp','udp6')
    if len(sys.argv) == 1 or sys.argv[1] == 'all':
        for arg in argv_list:
            choose = arg
            main(choose)
    else:
        for arg in sys.argv[1:]:
            choose = arg
            main(choose)
