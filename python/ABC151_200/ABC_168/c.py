import numpy as np

def main():
    A, B, H, M = map(float, input().split())
    # 偏角をどう計算するか,0を基準にどれくらい動いてるか
    omega_short = 6*M # 短針を動かす角度(not radian)
    omega_long = 0.5*M+30*H
    diff_rad = np.abs(omega_long - omega_short)
    cos_theta = np.cos(np.deg2rad(diff_rad))
    res = (A**2 + B**2 - 2*A*B*cos_theta)**(1/2)# 余弦定理
    print(res)
if __name__ == "__main__":
    main()