#!/usr/bin/env bash

rm db.sqlite
python3 inserts.py
mv db.sqlite ../../db.sqlite
