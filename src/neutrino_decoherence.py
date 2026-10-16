"""
QG neutrino decoherence: E^-4 vs E^n scaling.

IceCube constraint: no decoherence for 0 <= n <= 3 at Planck scale.
Open-system prediction: n = -4 (strongest at LOW energy).
"""
import numpy as np


def Gamma_QG(E_GeV, n, E_Pl=1.22e19, xi=1.0):
    """
    Decoherence rate from QG fluctuations.
        Gamma(E) = xi * E^(n+2) / E_Pl^n
    """
    return xi * E_GeV**(n + 2) / E_Pl**n


def P_survival(L_km, E_GeV, n, xi=1.0, dE_eV2=2.5e-3):
    """
    Two-flavor survival probability with decoherence:
        P = 1 - 0.5 sin^2(2theta) [1 - cos(Delta m^2 L / 2E) e^{-Gamma L}]
    """
    L_m = L_km * 1e3
    # Oscillation phase
    phase = dE_eV2 * L_m / (2.0 * E_GeV * 1e9)  # eV -> natural
    G = Gamma_QG(E_GeV, n)
    # Convert Gamma (GeV) to per-length: Gamma / c, in natural units
    G_per_m = G / 1.97e-16  # GeV -> 1/m
    decay = np.exp(-G_per_m * L_m)
    return 1.0 - 0.5 * (1.0 - np.cos(phase) * decay)


def icecube_bound(n, E_range=(1e2, 1e5)):
    """Approximate IceCube bound on xi for given n."""
    # IceCube is sensitive to Gamma(E) ~ H_0 ~ 1e-42 GeV
    E_ref = np.sqrt(E_range[0] * E_range[1])
    E_Pl = 1.22e19
    xi_max = 1e-42 * E_Pl**n / E_ref**(n + 2)
    return xi_max


if __name__ == "__main__":
    print("=" * 74)
    print("QG neutrino decoherence: E^-4 loophole")
    print("=" * 74)

    print(f"\nIceCube sensitivity range: E in [1e2, 1e5] GeV")
    print(f"Reference energy (geometric mean): 1e3.5 GeV")
    print(f"\n{'n':>4}  {'xi_IC bound':>16}  {'xi_required':>16}  status")
    print("-" * 60)
    for n in (-4, -3, -2, -1, 0, 1, 2, 3):
        xi_b = icecube_bound(n)
        # "Required" for observable at low E:
        E_low = 1e-3  # GeV (reactor neutrinos)
        E_Pl = 1.22e19
        # For Gamma(low-E) ~ 1e-42 GeV (observable over cosmological L)
        xi_req = 1e-42 * E_Pl**n / E_low**(n + 2)
        status = "SAFE" if xi_req < xi_b else "CONSTRAINED"
        print(f"{n:>4}  {xi_b:>16.3e}  {xi_req:>16.3e}  {status}")

    print(f"\n" + "=" * 74)
    print("Interpretation")
    print("=" * 74)
    print("""
    IceCube rules out n = 0, 1, 2, 3 at xi = 1 (Planck-suppressed).
    For n = -4 (open-system framework), the constraint is WEAK at
    IceCube energies but STRONG at low energies.

    Reactor neutrinos (E ~ MeV) and solar neutrinos (E ~ 0.1-20 MeV)
    probe the n = -4 regime where IceCube is blind.

    This is a live loophole: existing low-E neutrino experiments
    can constrain n = -4 decoherence better than IceCube.
    """)
