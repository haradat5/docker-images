# Docker Images

* **`psi4`**: install `psi4` with conda on top of `continuumio/miniconda3`, currently fails installing `gcc`
* **`psi4conda`**: install `psi4` on top of `ubuntu:16.04` with the `psi4conda` package provided by `psi4`, works fine but it is very large: 1.5GB

## DockerHub

The container images are automatically built on `DockerHub` at <https://hub.docker.com/r/paesanilab/>

For example you can download the `psi4` container locally with:

    docker pull paesanilab/psi4

Then get a shell inside the container with

    docker run -it paesanilab/psi4 /bin/bash
