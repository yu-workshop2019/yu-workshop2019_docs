#!/usr/bin/env python
# -*- coding: utf-8 -*-

filename = "output_for.txt"

with open(filename, mode='a') as f:
    for i in range(0, 100):
        f.write(str(i) + "\n")
