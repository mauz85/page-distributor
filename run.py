#!/usr/bin/env python3

import subprocess, os, shutil
from subprocess import check_call

NAME='page-distributor'

check_call(['docker', 'build', '-t', NAME, '.'])

check_call(['docker', 'run', '--rm', '-it', '-p', '80:80', '-p', '443:443', '--name', 'page-distributor', NAME, '/usr/sbin/apache2ctl', '-D', 'FOREGROUND'])

 

