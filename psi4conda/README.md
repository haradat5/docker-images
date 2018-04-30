# Psi4 container

Example run with [`psi4_test.py`](https://github.com/paesanilab/potential_fitting/blob/master/qm_mb_energy_calculator/tests/psi4/psi4_test.py):

```
docker run -it -v $(pwd)/psi4_test.py:/psi4_test.py psi4conda python /psi4_test.py
/opt/conda/lib/python3.6/site-packages/v2rdm_casscf/v2rdm_casscf.so loaded.

 O      -6.738646395e-02  -1.491617397e+00  -1.095035971e-10
 H       8.141855337e-01  -1.866159045e+00  -2.044214632e-10
 H       7.436878209e-02  -5.443285903e-01   4.259078718e-11

E(BLYP/cc-pvdz) = -76.3979871345321
```
