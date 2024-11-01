#!/bin/bash
for i in {0..3}; do
    journalctl -b-$i
done
