import state
import sbox

# https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf

def sub_bytes(st: state.State):
    res = []
    for c in range(4):
        for r in range(4):
            res.append(sbox.s_box(st.get(r, c)))
    return state.State(res)

def shift_rows(st: state.State):
    res = state.State([])

    for r in range(4):
        for c in range(4):
            res.set(r,c,st.get(r,(c + r)%4))

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
