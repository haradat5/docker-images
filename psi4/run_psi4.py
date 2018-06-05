import argparse

import psi4

parser = argparse.ArgumentParser(description="Run psi4")
parser.add_argument("--mol", dest="mol")

args = parser.parse_args()

nthreads = 2

mol = args.mol.replace(",", "\n")
print(mol)

method = "BLYP"
basis = "cc-pvdz"
model = "{}/{}".format(method, basis)

psi4.core.set_output_file("psi4.out", False)
psi4.set_memory("1GB")
psi4.geometry(mol)
psi4.set_num_threads(nthreads)
energy = psi4.energy(model)
print("E({}) = {}".format(model, energy))
