#!/usr/bin/env python3

# Copyright (C) 2016.
# Author: Jesús Manuel Mager Hois
# e-mail: <fongog@gmail.com>
# Project website: http://turing.iimas.unam.mx/wix/

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

def split(infile):
    root = infile
    text = open(infile+".wixes", "r").read().split("\n")
    root = "corp"
    train_es = open(root+"-train.wix", "w")
    train_wix = open(root+"-train.es", "w")
    dev_es = open(root+"-dev.wix", "w")
    dev_wix = open(root+"-dev.es", "w")
    test_es = open(root+"-test.wix", "w")
    test_wix = open(root+"-test.es", "w")

    text = list(set(text))
    total = len(text)
    test_len = int(total*.20)
    dev_len = int(total*.10)

    i = 0
    for line in text:
        print(line)

        paired = line.split("=")
        if len(paired) != 2:
            continue
        wix, es = paired
        if i < test_len:
            print(wix, file=test_wix)
            print(es, file=test_es)
        elif i < dev_len+test_len:
            print(wix, file=dev_wix)
            print(es, file=dev_es)
        else:
            print(wix, file=train_wix)
            print(es, file=train_es)
        i += 1

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("sep.py splits or merges an wixes file. An wixes file contains a pair")
        print("of phrases in wixárika and spanish, separeted by an = symbol")
        print("The in file must be *.wixes; or a root that shares .es and .wix")
        print("usage: sep.py infile")
        sys.exit()

    infile = sys.argv[1] 

    split(infile)

