#!/bin/bash
ansible all -m setup -a 'filter=ansible_hostname'