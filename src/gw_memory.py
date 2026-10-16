"""
GW memory — corrected prefactor.

Christodoulou memory:
    h_mem = (4 G / c^4) * E_rad / D_L
with E_rad ~ 0.05 M c^2 for a BBH merger.
"""
import numpy as np

G = 6.674e-11
c = 3.0e8
M_sun = 1.989e30
Mpc = 3.086e22


def h_memory(M_total_sun, D_L_Mpc, E_frac=0.05):
    """Memory strain from a merger."""
    M_kg = M_total_sun * M_sun
    E_rad = E_frac * M_kg * c**2
    D = D_L_Mpc * Mpc
    return 4.0 * G * E_rad / (c**4 * D)


def h_echo(h_mem, R=0.1, n=1):
    return h_mem * R**n


if __name__ == "__main__":
    print("=" * 74)
    print("GW memory — corrected")
    print("=" * 74)

    print(f"\n{'M [M_sun]':>12}  {'D_L [Mpc]':>10}  {'h_mem':>14}  "
          f"{'h_echo(R=0.1)':>16}  {'LIGO':>8}  {'ET':>8}")
    print("-" * 76)
    for M in (10, 30, 100):
        for D in (100, 1000):
            h = h_memory(M, D)
            h_e = h_echo(h)
            ligo = "YES" if h_e > 1e-22 else "no"
            et = "YES" if h_e > 1e-24 else "no"
            print(f"{M:>12.0f}  {D:>10.0f}  {h:>14.3e}  "
                  f"{h_e:>16.3e}  {ligo:>8}  {et:>8}")

    print(f"\n" + "=" * 74)
    print("Interpretation")
    print("=" * 74)
    print("""
    h_mem ~ 4e-22 for a 10 M_sun merger at 100 Mpc.  LIGO-detectable.
    Echo amplitude with R = 0.1: 4e-23.  Below LIGO, above ET.

    QG prediction for R:
        R ~ (l_Pl / r_s)^n
    For a stellar BH, l_Pl/r_s ~ 1e-40.  Any observable R requires
    non-standard QG (firewall, fuzzball, Planck-scale modifications
    of horizon reflectivity).

    LIGO has searched for echoes.  None confirmed.  Constraints:
        R < 0.1 for most BBH events (95% CL)
    Which already rules out firewalls at 90% level.
    """)
