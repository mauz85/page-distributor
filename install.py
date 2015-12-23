#!/usr/bin/env python2

import subprocess, os, shutil
from subprocess import check_call

NAME='page-distributor'

projDir = os.path.dirname(os.path.realpath(__file__))

check_call(['docker', 'build', '-t', NAME, projDir])

serviceFileName = NAME + '.service'
serviceFile = os.path.join(projDir, serviceFileName)
serviceFileDest = os.path.join('/etc/systemd/system/', serviceFileName) 
shutil.copy(serviceFile, serviceFileDest)

check_call(['systemctl', 'enable', serviceFileDest])
check_call(['systemctl', 'start', serviceFileName])
