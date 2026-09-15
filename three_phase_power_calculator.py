import math

print("===== THREE-PHASE POWER CALCULATOR =====")

# Get input values
voltage = float(input("Enter line voltage (V): "))
current = float(input("Enter line current (A): "))
power_factor = float(input("Enter power factor (0 to 1): "))

# Check valid power factor
if power_factor < 0 or power_factor > 1:
    print("Invalid power factor. Enter a value between 0 and 1.")
else:
    # Calculate apparent power
    apparent_power = math.sqrt(3) * voltage * current

    # Calculate real power
    real_power = apparent_power * power_factor

    # Calculate reactive power
    reactive_power = math.sqrt(
        apparent_power ** 2 - real_power ** 2
    )

    # Convert to kVA, kW and kVAR
    apparent_kva = apparent_power / 1000
    real_kw = real_power / 1000
    reactive_kvar = reactive_power / 1000

    # Display results
    print("\n===== CALCULATION RESULTS =====")
    print(f"Real Power       : {real_kw:.2f} kW")
    print(f"Apparent Power   : {apparent_kva:.2f} kVA")
    print(f"Reactive Power   : {reactive_kvar:.2f} kVAR")
import math

print("===== THREE-PHASE POWER CALCULATOR =====")

# Get input values
voltage = float(input("Enter line voltage (V): "))
current = float(input("Enter line current (A): "))
power_factor = float(input("Enter power factor (0 to 1): "))

# Check valid power factor
if power_factor < 0 or power_factor > 1:
    print("Invalid power factor. Enter a value between 0 and 1.")
else:
    # Calculate apparent power
    apparent_power = math.sqrt(3) * voltage * current

    # Calculate real power
    real_power = apparent_power * power_factor

    # Calculate reactive power
    reactive_power = math.sqrt(
        apparent_power ** 2 - real_power ** 2
    )

    # Convert to kVA, kW and kVAR
    apparent_kva = apparent_power / 1000
    real_kw = real_power / 1000
    reactive_kvar = reactive_power / 1000

    # Display results
    print("\n===== CALCULATION RESULTS =====")
    print(f"Real Power       : {real_kw:.2f} kW")
    print(f"Apparent Power   : {apparent_kva:.2f} kVA")
    print(f"Reactive Power   : {reactive_kvar:.2f} kVAR")
