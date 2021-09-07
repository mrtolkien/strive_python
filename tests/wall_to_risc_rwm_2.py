import ctypes
from ctypes import windll

from ReadWriteMemory import ReadWriteMemory
import win32process
import win32api

rwm = ReadWriteMemory()

process = rwm.get_process_by_name("GGST-Win64-Shipping.exe")
process.open()

# first get pid, see the 32-bit solution

PROCESS_ALL_ACCESS = 0x1F0FFF
processHandle = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, process.pid)
modules = win32process.EnumProcessModules(processHandle)
processHandle.close()
base_address = modules[0]  # for me it worked to select the first item in list...


##
def read_64(process_, address):
    read_buffer = ctypes.c_uint64()
    lp_buffer = ctypes.byref(read_buffer)
    n_size = ctypes.sizeof(read_buffer)
    lp_number_of_bytes_read = ctypes.c_ulong(0)
    ctypes.windll.kernel32.ReadProcessMemory(
        process_.handle,
        ctypes.c_void_p(address),
        lp_buffer,
        n_size,
        lp_number_of_bytes_read,
    )
    return read_buffer.value


##
temp_address = read_64(process, base_address + 0x4C6E4F8)
pointer = 0x0

for offset in [0x110, 0x0, 0xC424]:
    pointer = int(str(temp_address), 0) + int(str(offset), 0)
    temp_address = read_64(process, pointer)


##
print(read_64(process, pointer))

##
wallOnP1 = (0x4C6E4F8, [0x110, 0x0, 0xCFA0])
wallOnP2 = (0x4C6E4F8, [0x110, 0x8, 0xCFA0])
riscOnP1 = (0x4C6E4F8, [0x110, 0x0, 0xC424])
riscOnP2 = (0x4C6E4F8, [0x110, 0x8, 0xC424])
