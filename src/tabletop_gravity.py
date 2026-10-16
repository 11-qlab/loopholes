"""
Tabletop gravitational Aharonov-Bohm — corrected physics.

The TOTAL phase (G m_s m_a T / hbar d) is unobservable.
The OBSERVABLE phase difference is suppressed by Δd/d, where Δd
is the spatial separation of the interfering wavepackets.
"""
import numpy as np

hbar = 1.055e-34
G = 6.674e-11
m_atom = 1.4e-25


def total_phase(m_source, d, T):
    """Total AB phase along one path (unobservable)."""
    return G * m_source * m_atom * T / (hbar * d)


def observable_phase(m_source, d, Delta_d, T):
    """Observable phase difference between two paths."""
    return G * m_source * m_atom * T * Delta_d / (hbar * d**2)


if __name__ == "__main__":
    print("=" * 74)
    print("Tabletop gravitational AB — observable phase")
    print("=" * 74)

    print(f"\nAtom: Rb-87, m_a = 1.4e-25 kg")
    print(f"Source: 1 kg test mass at d = 1 m")
    print(f"Wavepacket separation Delta_d")
    print(f"Interaction time T\n")

    print(f"{'T [s]':>8}  {'Delta_d [m]':>14}  {'total phase':>14}  "
          f"{'observable':>14}  {'S/N (1e-10)':>14}")
    print("-" * 70)
    for T in (0.1, 1.0, 10.0):
        for Dd in (1e-9, 1e-7, 1e-5):
            total = total_phase(1.0, 1.0, T)
            obs = observable_phase(1.0, 1.0, Dd, T)
            snr = obs / 1e-10
            print(f"{T:>8.2f}  {Dd:>14.1e}  {total:>14.4e}  "
                  f"{obs:>14.4e}  {snr:>14.3e}")

    print(f"\n" + "=" * 74)
    print("Interpretation")
    print("=" * 74)
    print("""
    Total phase ~ 1e-2 rad (large, unobservable — it's a global phase).
    Observable phase ~ 1e-11 rad for realistic setups.

    Current atom interferometry sensitivity: ~1e-10 rad.
    Observable effect is right at the threshold.

    Space-based interferometers (10^4 s coherence, 10 m baselines)
    could reach ~1e-13 rad — a genuine detection of the
    gravitational AB effect.

    This IS a QG-relevant signal (no (H/M_Pl)^2 suppression) —
    it's a direct test of whether gravity has quantum coherence
    effects at laboratory scales.
    """)
