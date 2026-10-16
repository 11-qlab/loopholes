"""LQC IR cutoff — using self-consistent fake data."""
import numpy as np


def P_LCDM(k, A_s=2.1e-9, n_s=0.965, k_star=0.05):
    return A_s * (k / k_star)**(n_s - 1.0)


def P_LQC(k, k_cut, A_s=2.1e-9, n_s=0.965, k_star=0.05):
    return A_s * (k / k_star)**(n_s - 1.0) * (1.0 - np.exp(-(k / k_cut)**2))


if __name__ == "__main__":
    print("=" * 74)
    print("LQC IR cutoff — corrected test")
    print("=" * 74)

    # ell range
    ell = np.arange(2, 31)
    k = ell / 14000.0

    # Generate fake data FROM LCDM + cosmic variance noise
    rng = np.random.default_rng(0)
    P_true = P_LCDM(k)
    # cosmic variance error: sigma_C_l / C_l = sqrt(2/(2l+1))
    sigma_frac = np.sqrt(2.0 / (2.0 * ell + 1.0))
    P_obs = P_true * (1.0 + sigma_frac * rng.standard_normal(len(ell)))
    P_err = P_true * sigma_frac

    chi2_std = np.sum(((P_obs - P_LCDM(k)) / P_err)**2)
    print(f"\nFake data generated from LCDM + cosmic variance")
    print(f"LCDM chi2 (should be ~n_dof): {chi2_std:.2f}, dof={len(ell)-2}")

    print(f"\n{'k_cut [Mpc^-1]':>16}  {'chi2':>10}  {'delta chi2':>12}")
    print("-" * 42)
    for k_cut in (1e-4, 1e-3, 5e-3, 1e-2, 5e-2, 1e-1):
        c = np.sum(((P_obs - P_LQC(k, k_cut)) / P_err)**2)
        print(f"{k_cut:>16.1e}  {c:>10.3f}  {c - chi2_std:>+12.3f}")

    print(f"\n" + "=" * 74)
    print("Interpretation")
    print("=" * 74)
    print("""
    If LQC cutoff is real, chi2 should drop significantly for
    some k_cut.  But with only 29 ell bins and cosmic variance,
    the statistical power is weak.  Best case: Delta chi2 ~ a few.

    HONEST: this cannot be a detection.  It's a consistency check.
    A real test requires:
      - Broad ell range (LiteBIRD will give ell=2..200)
      - B-mode cutoff signature (not just TT)
      - Cross-check with tensor-to-scalar ratio
    """)
