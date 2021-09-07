from pymem import Pymem


def read_ints(process, base, offsets):
    value = process.read_int(base)

    for offset in offsets:
        value = process.read_int(value + offset)

    return value


pm = Pymem("GGST-Win64-Shipping.exe")
read_ints(pm, pm.base_address + 0x4C6E4F8, offsets=[0x110, 0x0, 0xC424])

##
