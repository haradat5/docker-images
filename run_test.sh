# run this in the docker build folder
PWD=$(pwd)
docker run -v $PWD/../psi4_test.py:/psi4_test.py -it $(basename $PWD) python /psi4_test.py
