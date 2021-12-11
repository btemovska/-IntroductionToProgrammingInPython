gas_const = 8.3144621

def compute_gas_volume(pressure, temperature, moles):
    gas_volume = (moles * gas_const * temperature) / pressure
    return gas_volume


gas_pressure = float(input())
gas_moles = float(input())
gas_temperature = float(input())
gas_volume = 0.0

gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
print('Gas volume:', gas_volume, 'm^3')

