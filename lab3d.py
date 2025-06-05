#!/usr/bin/env python3
# Author ID: smeep-kaur@myseneca.ca

import subprocess

def free_space():
    cmd = "df -h | grep '/$' | awk '{print $4}'"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output = p.communicate()
    return output[0].decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
