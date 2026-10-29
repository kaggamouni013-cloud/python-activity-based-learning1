'''Algorithm
Objective: Analyze daily electricity and water consumption across campus buildings, calculate costs and percentage changes, identify excessive consumption, and rank buildings using a defined scoring method.

Start the program.

Input building-wise daily electricity consumption (kWh) and water consumption (litres).

Define electricity and water rates, along with daily consumption limits.

Calculate the total electricity and water consumption for each building.

Calculate the total cost of electricity and water using the specified rates.
Compare daily consumption with the defined limits and flag excessive consumption.

Calculate a performance score for each building using the following scoring method:

Electricity score = electricity consumption divided by its limit, multiplied by 100.

Water score = water consumption divided by its limit, multiplied by 100.

Combined score = average of electricity and water scores.

Rank buildings in ascending order of the combined score. A lower score indicates better resource efficiency.

Display consumption totals, costs, percentage changes, excessive consumption alerts, and building rankings.

Stop.
Flowchart

flowchart TD
    A([Start]) --> B[Input building-wise daily energy and water data]
    B --> C[Set rates and daily consumption limits]
    C --> D[Calculate total consumption and costs]
    D --> E[Calculate first-to-last day percentage changes]
    E --> F{Any daily limit exceeded?}
    F -- Yes --> G[Flag excessive consumption]
    F -- No --> H[Calculate combined efficiency score]
    G --> H
    H --> I[Rank buildings by score]
    I --> J[Display audit report and alerts]
    J --> K([Stop])
code 

# Integrated Campus Energy and Water Audit

# Sample consumption data for three days
# Energy is measured in kWh; water is measured in litres.
buildings = {
    "Academic Block": {
        "energy": [80, 95, 110],
        "water": [800, 900, 1200]
    },
    "Library": {
        "energy": [60, 65, 70],
        "water": [500, 550, 600]
    },
    "Hostel": {
        "energy": [90, 105, 120],
        "water": [900, 1100, 1300]
    }
}

# Rates and daily limits
ENERGY_RATE = 8.0       # currency units per kWh
WATER_RATE = 0.05       # currency units per litre
ENERGY_LIMIT = 100      # kWh per building per day
WATER_LIMIT = 1000      # litres per building per day

report = []

print("===== CAMPUS ENERGY AND WATER AUDIT =====")

for name, data in buildings.items():
    energy = data["energy"]
    water = data["water"]
    days = len(energy)

    total_energy = sum(energy)
    total_water = sum(water)

    energy_cost = total_energy * ENERGY_RATE
    water_cost = total_water * WATER_RATE
    total_cost = energy_cost + water_cost

    # Percentage change from first day to last day
    energy_change = (
        (energy[-1] - energy[0]) / energy[0] * 100
        if energy[0] != 0 else 0
    )
    water_change = (
        (water[-1] - water[0]) / water[0] * 100
        if water[0] != 0 else 0
    )

    # Flag any daily consumption above the limits
    alerts = []
    if any(value > ENERGY_LIMIT for value in energy):
        alerts.append("Excessive energy")
    if any(value > WATER_LIMIT for value in water):
        alerts.append("Excessive water")

    # Score based on average daily consumption relative to limits
    energy_score = total_energy / (ENERGY_LIMIT * days) * 100
    water_score = total_water / (WATER_LIMIT * days) * 100
    combined_score = (energy_score + water_score) / 2

    report.append({
        "name": name,
        "energy": total_energy,
        "water": total_water,
        "energy_cost": energy_cost,
        "water_cost": water_cost,
        "total_cost": total_cost,
        "energy_change": energy_change,
        "water_change": water_change,
        "alerts": alerts,
        "score": combined_score
    })

    print(f"\nBuilding: {name}")
    print(f"Total energy: {total_energy} kWh")
    print(f"Total water: {total_water} litres")
    print(f"Energy cost: {energy_cost:.2f}")
    print(f"Water cost: {water_cost:.2f}")
    print(f"Total cost: {total_cost:.2f}")
    print(f"Energy change: {energy_change:+.2f}%")
    print(f"Water change: {water_change:+.2f}%")
    print("Alerts:", ", ".join(alerts) if alerts else "None")
    print(f"Combined score: {combined_score:.2f}")

# Lower combined score means better resource efficiency
ranked = sorted(report, key=lambda item: item["score"])

print("\n===== BUILDING RANKING =====")
for rank, item in enumerate(ranked, start=1):
    print(
        f"{rank}. {item['name']} - "
        f"Score: {item['score']:.2f}"
    )

print("\n===== CAMPUS TOTALS =====")
print(f"Energy: {sum(x['energy'] for x in report)} kWh")
print(f"Water: {sum(x['water'] for x in report)} litres")
print(f"Total cost: {sum(x['total_cost'] for x in report):.2f}")
output
===== CAMPUS ENERGY AND WATER AUDIT =====

Building: Academic Block
Total energy: 285 kWh
Total water: 2900 litres
Energy cost: 2280.00
Water cost: 145.00
Total cost: 2425.00
Energy change: +37.50%
Water change: +50.00%
Alerts: Excessive energy, Excessive water
Combined score: 95.83

Building: Library
Total energy: 195 kWh
Total water: 1650 litres
Energy cost: 1560.00
Water cost: 82.50
Total cost: 1642.50
Energy change: +16.67%
Water change: +20.00%
Alerts: None
Combined score: 60.00

Building: Hostel
Total energy: 315 kWh
Total water: 3300 litres
Energy cost: 2520.00
Water cost: 165.00
Total cost: 2685.00
Energy change: +33.33%
Water change: +44.44%
Alerts: Excessive energy, Excessive water
Combined score: 107.50

===== BUILDING RANKING =====
1. Library - Score: 60.00
2. Academic Block - Score: 95.83
3. Hostel - Score: 107.50

===== CAMPUS TOTALS =====
Energy: 795 kWh
Water: 7850 litres
Total cost: 6752.50'''