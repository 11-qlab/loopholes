# Loopholes: attempts to bypass the (H/M_Pl)^2 wall

## Surviving channels

1. **Neutrino decoherence n=-4** (src/neutrino_decoherence.py)
   IceCube rules out n = 0..3.  Open-system QG predicts n = -4.
   Reactor and solar neutrinos probe the right regime.
   NOT YET CONSTRAINED — the strongest surviving channel.

2. **GW memory echoes** (src/gw_memory.py)
   h_echo ~ 1e-22 for 30 Msun BBH at 100 Mpc, if horizon
   reflectivity R = 0.1.  LIGO marginal, ET/CE detectable.
   Requires non-standard QG (firewall, fuzzball).

3. **Tabletop gravitational AB** (src/tabletop_gravity.py)
   Observable phase ~ 1e-11 rad.  Current atom interferometry
   ~1e-10 rad.  Space-based can reach.  Tests whether gravity
   mediates quantum coherence — a genuinely open question.

## Live but not QG-specific

4. **Cosmological collider** (src/collider.py)
   Resonance helps only m/H < 2.  Heavy-moduli probe requires
   a periodic coupling, not single resonance.
   String-compactification signature.

## Null

5. **PBH GW background** (src/pbh_gw.py)
   f_peak ~ 1e21 Hz for observable PBHs.  19 orders above
   every detector band.

6. **Birefringence QG** (src/birefringence_qg.py)
   Formula matches observation but gives no independent test.

7. **LQC IR cutoff** (src/lqc_anomaly.py)
   Pipeline verified on fake data.  Real-data test
   cosmic-variance limited; LiteBIRD B-modes needed.

## Summary

The wall stands for QG amplitudes.  Two channels genuinely
escape it — neutrino decoherence at low energy and GW memory
echoes — but both require either a specific non-standard QG
model, or a neutrino experiment that doesn't yet exist at the
right energy.  No loophole gives a same-session detection.
