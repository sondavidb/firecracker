#!/bin/bash

task(){
    echo "Running iteration $1";
    mkdir testing$1;
    (cd testing$1; git clone git@github.com:firecracker-microvm/firecracker.git;
    firecracker/tools/devtool build_rootfs) 2>&1 | tee logs/logs"$1".txt;
    sudo rm -rf testing$1;
}

loop() {
    for i in {1..100}; do 
        task $i &
    done
}

mkdir logs
time loop 2>&1 | tee logs/logs.txt