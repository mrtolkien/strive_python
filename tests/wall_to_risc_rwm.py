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
windll.kernel32.ReadProcessMemory(process, base_address + 0x4C6E4F8)


##
risc_pointer = process.get_pointer(
    base_address + 0x4C6E4F8, offsets=[0x110, 0x0, 0xC424]
)

print(process.read(risc_pointer))

##
wallOnP1 = (0x4C6E4F8, [0x110, 0x0, 0xCFA0])
wallOnP2 = (0x4C6E4F8, [0x110, 0x8, 0xCFA0])
riscOnP1 = (0x4C6E4F8, [0x110, 0x0, 0xC424])
riscOnP2 = (0x4C6E4F8, [0x110, 0x8, 0xC424])
