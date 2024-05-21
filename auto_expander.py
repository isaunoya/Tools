# !/usr/bin/env python3
import re
import sys
import argparse
from logging import Logger, basicConfig, getLogger
from os import getenv, environ
from pathlib import Path
from typing import List
import pyperclip
import subprocess
import logging
import time

logger = getLogger(__name__)  # type: Logger

atcoder_include = re.compile('#include\s*["<](atcoder/[a-z_]*(|.hpp))[">]\s*')

include_guard = re.compile('#.*ATCODER_[A-Z_]*_HPP')

lib_path = Path("D:\\MSYS2\\mingw64\\include\\c++\\13.2.0\\x86_64-w64-mingw32")

defined = set()
basicConfig(
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
        level=getenv('LOG_LEVEL', 'INFO'),
    )


def dfs(f: str) -> List[str]:
    global defined
    if f in defined:
        logger.info('already included {}, skip'.format(f))
        return []
    defined.add(f)

    logger.info('include {}'.format(f))

    s = open(str(lib_path / f)).read()
    result = []
    for line in s.splitlines():
        if include_guard.match(line):
            continue

        m = atcoder_include.match(line)
        if m:
            result.extend(dfs(m.group(1)))
            continue
        result.append(line)
    return result

def expander_operation():
    s = current_clipboard
    result = []
    for line in s.splitlines():
        m = atcoder_include.match(line)
        if m:
            result.extend(dfs(m.group(1)))
            continue
        result.append(line)

    output = '\n'.join(result) + '\n'
    pyperclip.copy(output)

if __name__ == "__main__":
    previous_clipboard = ''

    while True:
        logger.info('running')

        current_clipboard = pyperclip.paste()
        ok = False
        for line in current_clipboard.splitlines():
            m = atcoder_include.match(line)
            if m:
                ok = True
                break
        if ok:
            logger.info('expanding')
            defined = set()
            expander_operation()
        time.sleep(0.2)
