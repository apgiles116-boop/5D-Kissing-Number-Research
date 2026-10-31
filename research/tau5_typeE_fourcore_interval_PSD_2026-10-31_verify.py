#!/usr/bin/env python3
"""Exact rational Type-E four-core Q6 < 1979/1000 certificate.

See tau5_typeE_fourcore_interval_PSD_2026-10-31.md for proof.
Uses fractions.Fraction only, no floating-point optimization or SDP.
"""
from fractions import Fraction as F

T = F(383, 504)
D = F(1780062775, 4032758016)
TARGET = F(1979, 1000)


def interval_certificate(N):
    """Cover 0<=q<=p<=1/4, p+q<=D with rational boxes of side 1/N."""
    assert N % 4 == 0
    h = F(1, N)
    worst, where, count, b2_used = F(-1), None, 0, 0
    for ip in range(N // 4):
        pl, pu = ip*h, (ip+1)*h
        for iq in range(ip+1):
            ql, qu = iq*h, (iq+1)*h
            if pl + ql > D:
                continue
            ru = D-pl-ql
            # Remaining four defects: sum r<=ru, each r_k<=q<=qu.
            # Hence sum r_k^2 <= min(ru^2, qu*ru).
            eupper = pu*pu + qu*qu + min(ru*ru, qu*ru)
            b1 = F(3,2) + D/4 + 3*T/8 + eupper
            upper = b1
            if pl + ql > T/2:
                # Top two defect edges share a vertex.
                # 3x3 midpoint Gram PSD plus a rational AM-GM bound.
                denom = F(1,8) - pl*pl - ql*ql
                assert denom > 0
                g0 = 2*(pl+ql)**2 - F(1,4) + (
                    (pl*pl-ql*ql)**2 / denom
                )
                g0 = max(F(0), g0)
                if g0 <= F(1,4):
                    b2 = F(3,2) + D + eupper - g0*(1-g0)
                    upper = min(upper, b2)
                    b2_used += 1
                # g0>1/4 implies infeasibility of this PSD branch;
                # retaining b1 is harmless and still valid.
            if upper > worst:
                worst, where = upper, (ip, iq)
            assert upper < (TARGET if N == 1000 else F(99,50)), (
                N, ip, iq, upper
            )
            count += 1
    return count, b2_used, worst, where


def global_frame_floor():
    umax = F(3,16) + (T-F(3,4))**2
    qfloor = 30 - 3*T + T*T/10 - umax/2
    safe = qfloor - TARGET
    assert umax == F(47653,254016)
    assert qfloor == F(8790283,317520)
    assert safe == F(204047773,7938000)
    return umax, qfloor, safe


def main():
    print('EXACT TYPE-E FOUR-CORE INTERVAL/PSD CERTIFICATE')
    print('T =', T, 'D =', D)
    for n in (500,1000):
        count, used, worst, where = interval_certificate(n)
        print(f'N={n}: {count} boxes; PSD bound used in {used}; '
              f'worst={worst} ~ {float(worst):.12f}; box={where}')
    umax, qfloor, safe = global_frame_floor()
    print('Umax(T) =', umax)
    print('Q_all >=', qfloor, '~', float(qfloor))
    print('Q6 <', TARGET)
    print('Q_safe >', safe, '~', float(safe))
    center_q = F(5876056025347,211680000000)
    print('With separately retained center variance: Q_safe >',
          center_q-TARGET, '~', float(center_q-TARGET))
    for r in (F(0), F(1,8), F(1,5), F(1,4), F(1,3)):
        t = (safe-184*r*r)/(F(1,4)-r*r)
        print(f'Safe pairs with |z_i.z_j|>{r}: at least '
              f'{t.numerator//t.denominator+1}')
    print('ALL EXACT CERTIFICATES PASS')


if __name__ == '__main__':
    main()
