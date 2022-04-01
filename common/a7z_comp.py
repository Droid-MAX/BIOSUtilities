#!/usr/bin/env python3
#coding=utf-8

import os
import subprocess

from common.script_get import get_script_dir
from common.system import get_os_ver
from common.text_ops import padder

# Get 7z path
def get_7z_path(static=False):
    exec_name = '7z.exe' if get_os_ver()[1] else ('7zzs' if static else '7zz')
    
    exec_path = os.path.join(get_script_dir(), '..', 'external', exec_name)
    
    return exec_path

# Check if file is 7z supported
def is_7z_supported(in_path, static=False):
    try:
        subprocess.run([get_7z_path(static), 't', in_path, '-bso0', '-bse0', '-bsp0'], check=True)
    
    except:
        return False
    
    return True

# Archive decompression via 7-Zip
def a7z_decompress(in_path, out_path, in_name, padding, static=False):
    if not in_name: in_name = 'archive'
    
    try:
        subprocess.run([get_7z_path(static), 'x', '-aou', '-bso0', '-bse0', '-bsp0', '-o' + out_path, in_path], check=True)
        
        if not os.path.isdir(out_path): raise Exception('EXTRACT_DIR_MISSING')
    
    except:
        print('\n%sError: 7-Zip could not extract %s file %s!' % (padder(padding), in_name, in_path))
        
        return 1
    
    print('\n%sSuccesfull %s decompression via 7-Zip!' % (padder(padding), in_name))
    
    return 0