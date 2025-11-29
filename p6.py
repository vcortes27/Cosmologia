import camb
import numpy as np
import matplotlib.pyplot as plt

# Configurar parámetros cosmológicos
pars = camb.CAMBparams()
pars.set_cosmology(H0=67.36, ombh2=0.02237, omch2=0.12, mnu=0.06, omk=0, tau=0.0544)
pars.InitPower.set_params(As=2.1e-9, ns=0.9649, r=0)

pars.set_matter_power(redshifts=[0], kmax=10.0)

# Calcular y obtener mps
results = camb.get_results(pars)
k, z, Pk = results.get_matter_power_spectrum(minkh=1e-4, maxkh=10, npoints=200)
Pk_matter = Pk[0]

# Obtener datos de transferencia para graficar
transfer = results.get_matter_transfer_data()

# Graficar el espectro de potencia
plt.figure(figsize=(10, 6))
plt.loglog(k, Pk_matter)
plt.xlabel('k [h/Mpc]')
plt.ylabel('P(k) [Mpc/h]³')
plt.title('MPS con CAMB')
plt.grid(True)
plt.show()