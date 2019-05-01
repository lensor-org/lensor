#!/bin/bash

scriptPath="${PWD}/${0%/*}"
depsFile="../Pipfile.lock"
hashFile="../Pipfile.lock.hash"

writeHash() {
    echo "Writing hash...";
    cd $scriptPath
    echo $1 > $hashFile
}

updateDeps() {
    echo "Updating dependencies...";
    cd "$scriptPath/.." # Sets workdir to ../ relative to script
    docker build --target dev --build-arg CACHEBUST=$(date +%s) -t lensor-dev .
}

runApp() {
    echo "Running app..."
    cd "$scriptPath/.." # Sets workdir to ../ relative to script
    docker run --rm -w "/app" -v ${PWD}:/app lensor-dev python main.py
}

checkDepsAndRun() {
    cd $scriptPath
    depsHash=($(md5sum $depsFile))

    if [ -e $hashFile ]
    then
        echo "Hash exists, comparing hashes"
        readHash=$(cat $hashFile)

        if [ "$readHash" == "$depsHash" ]
        then
            echo "Hashes are equal"
            runApp;
        else
            echo "Hashes are NOT equal"
            updateDeps;
            writeHash $depsHash;
            runApp;
        fi
    else
        echo "Hash doesnt exist"
        updateDeps;
        writeHash $depsHash;
        runApp;
    fi     
}

checkDepsAndRun