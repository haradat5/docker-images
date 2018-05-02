# PSI4 Dockerfile
#
# credits to:
#
# https://github.com/cgsanchez/ScienceContainers/Psi4

FROM continuumio/miniconda3:4.4.10

MAINTAINER A. Zonca <zonca@sdsc.edu>

RUN conda config --add channels http://conda.anaconda.org/psi4 && \
    conda install --yes psi4

#
# The scratch_dir should be used for scratch files, mounted at runtime
# The run_dir would contain the input and output files, mounted at runtime
#
#VOLUME /scratch_dir
#VOLUME /run_dir

#
# Set one thread by default, can be overriden at runtime
#
ENV MKL_NUM_THREADS=1
ENV OMP_NUM_THREADS=1
#
# Point scratch space to mounted scratch directory
#
#ENV PSI_SCRATCH=/scratch_dir

#WORKDIR /run_dir
