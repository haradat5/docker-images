PWD=$(pwd)
docker build . -t $(basename $PWD)
