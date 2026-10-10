# Freedomlink1 Unified Layer - CIM Introspection Module
# Replaces WMIC-based system identity calls.

function Get-FL1SystemProfile {
    $os = Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version
    $cpu = Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors
    $bios = Get-CimInstance Win32_BIOS | Select-Object SerialNumber, Manufacturer, SMBIOSBIOSVersion
    $mb = Get-CimInstance Win32_BaseBoard | Select-Object Product, Manufacturer, SerialNumber
    $disk = Get-CimInstance Win32_DiskDrive | Select-Object Model, SerialNumber, Size
    $mem = Get-CimInstance Win32_PhysicalMemory | Select-Object Capacity, Manufacturer
    $nic = Get-CimInstance Win32_NetworkAdapter | Select-Object Name, MACAddress

    return [PSCustomObject]@{
        OS = $os
        CPU = $cpu
        BIOS = $bios
        Board = $mb
        Disk = $disk
        Memory = $mem
        NIC = $nic
    }
}