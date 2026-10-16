"""
PBH evaporation GW background — corrected frequency scaling.

A PBH of mass M evaporates at t_evap ∝ M^3 with temperature
T_evap ∝ 1/M.  Emitted gravitons redshift to today:
    f_0 = T_evap / (1+z_evap)
with (1+z) ∝ t^(-1/2) in radiation era.  Net: f_0 ∝ M^(-3/2).
"""
import numpy as np

hbar = 1.055e-34
c = 3.0e8
G = 6.674e-11
k_B = 1.381e-23
M_Pl_kg = 2.18e-8
t_H_s = 4.35e17  # Hubble time
T_0_K = 2.725


def T_Hawking(M_kg):
    return hbar * c**3 / (8 * np.pi * G * M_kg * k_B)


def t_evap(M_kg):
    """Hawking evaporation time."""
    return 5120 * np.pi * G**2 * M_kg**3 / (hbar * c**4)


def T_GUP(M_kg, alpha=1.0):
    T0 = T_Hawking(M_kg)
    return T0 / (1.0 + alpha * (M_Pl_kg / M_kg)**2)


def f_peak_today(M_kg, T_func=T_Hawking):
    """
    Peak GW frequency today from a PBH of mass M_kg.
    Requires: PBH evaporates at t_evap(M).
    """
    T = T_func(M_kg)
    # Emitted photon frequency ∝ T (thermal)
    E_emit_J = k_B * T
    f_emit_Hz = E_emit_J / (2 * np.pi * hbar)
    # Redshift from evaporation to today
    t_e = t_evap(M_kg)
    if t_e > t_H_s:
        return 0.0  # hasn't evaporated yet
    # Radiation era: a ∝ t^(1/2), so 1+z = (t_H/t_e)^(1/2)
    z_plus_1 = (t_H_s / t_e)**0.5
    return f_emit_Hz / z_plus_1


if __name__ == "__main__":
    print("=" * 74)
    print("PBH evaporation GW — corrected frequency scaling")
    print("=" * 74)

    masses = np.logspace(8, 12, 8)  # kg

    print(f"\n{'M [kg]':>10}  {'T_H [K]':>12}  {'t_evap [s]':>12}  "
          f"{'f_0 [Hz]':>12}  {'band':>12}")
    print("-" * 66)
    for M in masses:
        T = T_Hawking(M)
        t_e = t_evap(M)
        f = f_peak_today(M)
        if f == 0:
            band = "—"
        elif 1e-4 < f < 0.1:
            band = "LISA"
        elif 0.01 < f < 10:
            band = "DECIGO"
        elif 1 < f < 1e4:
            band = "ET/LIGO"
        elif 1e-9 < f < 1e-6:
            band = "PTA"
        else:
            band = "—"
        print(f"{M:>10.2e}  {T:>12.3e}  {t_e:>12.3e}  {f:>12.3e}  {band:>12}")

    print(f"\n" + "=" * 74)
    print("Interpretation")
    print("=" * 74)
    print("""
    f_peak ∝ M^(-3/2): lower mass -> higher frequency.
    Only PBHs evaporating TODAY (t_evap ~ t_H) produce observable GW today.
    That mass is M ~ 1e11-1e12 kg.

    QG modification to T(M):
        T_GUP/T_H = 1/(1 + alpha (M_Pl/M)^2)
    For M = 1e12 kg, (M_Pl/M)^2 ~ 1e-40 -> correction negligible.
    For M ~ 1e9 kg, correction is still tiny.

    HONEST: The "10 decades shift" claim in the search results applies
    to Planck-mass PBHs (M ~ M_Pl), not stellar-mass or asteroid-mass.
    For observable PBHs evaporating today, QG corrections are
    (M_Pl/M)^2 ~ 1e-40 — unobservable.
    """)
