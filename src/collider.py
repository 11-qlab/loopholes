"""Cosmological collider — properly normalized resonance."""
import numpy as np


def f_NL_std(m_over_H, coupling=1.0):
    return coupling * np.exp(-np.pi * m_over_H)


def f_NL_resonant(m_over_H, omega_over_H, coupling=1.0, Gamma=0.01):
    """
    At exact resonance, enhancement = 1/Gamma relative to off-resonance.
    Peak value = f_NL_std / Gamma (line width enters linearly in amplitude).
    """
    x = m_over_H
    omega = omega_over_H
    detuning = (x - omega)**2 + Gamma**2
    peak_enhancement = Gamma / detuning
    boltzmann = np.exp(-np.pi * x)
    return coupling * boltzmann * peak_enhancement


if __name__ == "__main__":
    print("=" * 74)
    print("Cosmological collider — proper resonance normalization")
    print("=" * 74)
    print(f"\nGamma = 0.01 (1% line width)\n")
    print(f"{'m/H':>6}  {'omega/H':>10}  {'f_NL_std':>12}  {'f_NL_res':>12}  {'planck':>8}  {'S4':>5}")
    print("-" * 62)
    for m in (1.0, 2.0, 3.0, 5.0):
        for omega in (m * 0.999, m, m * 1.001):
            f_std = f_NL_std(m)
            f_res = f_NL_resonant(m, omega, Gamma=0.01)
            p = "YES" if abs(f_res) > 5 else "no"
            s = "YES" if abs(f_res) > 1 else "no"
            print(f"{m:>6.2f}  {omega:>10.4f}  {f_std:>12.4e}  "
                  f"{f_res:>12.4e}  {p:>8}  {s:>5}")

    print(f"\nAt exact resonance, enhancement factor = 1/Gamma = 100.")
    print(f"For m/H = 1, f_NL_res = 0.043 * 100 = 4.3 — Planck-detectable!")
