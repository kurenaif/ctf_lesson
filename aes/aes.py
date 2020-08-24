import state
import sbox
import gfcpoly

# https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf

def sub_bytes(st: state.State) -> state.State:
    res = []
    for c in range(4):
        for r in range(4):
            res.append(sbox.s_box(st.get(r, c)))
    return state.State(res)

def shift_rows(st: state.State) -> state.State:
    res = state.State([])

    for r in range(4):
        for c in range(4):
            res.set(r,c,st.get(r,(c + r)%4))

    return res

def MixColumns(st: state.State) -> state.State:
    res = state.State([])

    # a(x) = {03}x^3 + {01}x^2 + {01}x + {02}
    a_poly = gfcpoly.GFCPolynomial([0x02, 0x01, 0x01, 0x03])

    for c in range(4):
        s_poly = gfcpoly.GFCPolynomial([st.get(0,c), st.get(1,c), st.get(2,c), st.get(3,c)])
        sdash = (a_poly * s_poly).get_cs()

        for r in range(4):
            res.set(r,c, sdash[r].get_coeffs())

    return res

# p.33 Appendix B Round Number 1
st = state.State([0x19, 0x3d, 0xe3, 0xbe, 
0xa0, 0xf4, 0xe2, 0x2b, 
0x9a, 0xc6, 0x8d, 0x2a, 
0xe9, 0xf8, 0x48, 0x08])
print("-------------------- original --------------------")
print(st.pprint())
print("-------------------- subbytes --------------------")
st = sub_bytes(st)
print(st.pprint())
print("-------------------- shiftRows --------------------")
st = shift_rows(st)
print(st.pprint())
print("-------------------- MixColumns --------------------")
st = MixColumns(st)
print(st.pprint())

