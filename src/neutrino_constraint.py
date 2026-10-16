"""
n = -4 QG neutrino decoherence: honest interpretation.

We compare sensitivity across experiments for n = -4.

Key: for n = -4, the rate Γ = ξ (E/E_0)^-4 ENHANCES at low E.
This makes low-energy experiments MUCH more sensitive to ξ.

Result: Borexino already excludes natural (ξ ~ O(1))
n = -4 decoherence by ~48 orders of magnitude.
"""
import numpy as np

km_to_inv_GeV = 5.07e15
AU_to_km = 1.496e8
MeV = 1e-3
TeV = 1e3


def xi_bound(E_GeV, L_km, n, E_0_GeV=TeV):
    """
    Constraint on ξ from requiring Γ(E) < 1/L.
        Γ(E) = ξ (E/E_0)^n
        ξ < (1/L) / (E/E_0)^n
    """
    L_inv_GeV = 1.0 / (L_km * km_to_inv_GeV)
    return L_inv_GeV / (E_GeV / E_0_GeV)**n


if __name__ == "__main__":
    print("=" * 74)
    print("n = -4 decoherence: which experiment wins?")
    print("=" * 74)

    exps = {
        "IceCube (atm ν)":   (1e3, 1e4),
        "KamLAND (reactor)": (3e-3, 180),
        "Borexino (7Be)":    (0.86e-3, AU_to_km),
        "Super-K (8B)":      (10e-3, AU_to_km),
    }

    print(f"\n{'experiment':>20}  {'E [GeV]':>10}  {'L [km]':>12}  "
          f"{'ξ_max (n=-4)':>16}")
    print("-" * 62)

    bounds = {}
    for name, (E, L) in exps.items():
        xi = xi_bound(E, L, n=-4)
        bounds[name] = xi
        print(f"{name:>20}  {E:>10.2e}  {L:>12.2e}  {xi:>16.3e}")

    print(f"\n" + "=" * 74)
    print("Interpretation")
    print("=" * 74)

    xi_IC = bounds["IceCube (atm ν)"]
    xi_Bor = bounds["Borexino (7Be)"]

    print(f"""
    Natural QG expectation: ξ ~ O(1).

    IceCube bound:    ξ < {xi_IC:.2e}
        -> 1 > {xi_IC:.2e}, so IceCube CANNOT exclude ξ=1.
        -> n=-4 looks "open" from IceCube alone.

    Borexino bound:   ξ < {xi_Bor:.2e}
        -> 1 >> {xi_Bor:.2e}, so Borexino EXCLUDES ξ=1
           by {np.log10(1/xi_Bor):.0f} orders of magnitude.

    CONCLUSION:
    The n=-4 escape is CLOSED.  Solar neutrino experiments
    already rule out natural n=-4 QG decoherence.

    The only surviving version has ξ < 1e-48, which requires
    fine-tuning beyond any naturalness argument.

    This is itself a real, publishable statement:
    "Solar neutrino experiments exclude the natural
     realization of E^-4 quantum-gravity decoherence."
    """)

    print(f"\n" + "=" * 74)
    print("What this means for the search for QG signatures")
    print("=" * 74)
    print(f"""
    The n=-4 channel was the strongest surviving escape from
    the (H/M_Pl)^2 wall.  Now it's closed.

    Remaining channels:
    - GW memory echoes: requires horizon reflectivity R > 0.1
    - Tabletop gravitational AB: requires next-gen atom interferometry
    - Birefringence ALP: live signal, but not QG-specific

    None of these gives a same-session detection.
    None of these is Nobel-scale.

    The honest summary: the wall stands everywhere it can be
    tested, and every route around it either requires
    fine-tuning, next-generation experiments, or is not
    QG-specific.
    """)
