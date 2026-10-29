'''Algorithm
Start.

Store the stock details for each location, including opening stock, quantity received, quantity distributed, damaged quantity, and physically counted stock.

Calculate expected remaining stock using:

Expected Stock
=
Opening Stock
+
Received
−
Distributed
−
Damaged
Expected Stock=Opening Stock+Received−Distributed−Damaged
Compare expected stock with physically counted stock.

Calculate the discrepancy:
Discrepancy=Physical Stock−Expected Stock
If the discrepancy is zero, mark the stock as reconciled. Otherwise, report a surplus or shortage.

Define the minimum desired stock level for each location.

Calculate replenishment quantity:

Replenishment
=
max(0,
Target Stock
−
Physical Stock)
Replenishment=max(0,Target Stock−Physical Stock)
Display the reconciliation report, discrepancies, and replenishment requirements for every location.
Stop.
Flowchart
Start
Input stock data for each location
Calculate expected remaining stock
Compare expected stock with physical stock
    Is discrepancy equal to zero?
Yes

Mark as reconciled
No

Report surplus or shortage
Calculate replenishment quantity
Display location-wise stock report
Stop 
code 

# File name: food_stock_reconciliation.py
# Food Supply Chain Stock Reconciliation

# Stock quantities are measured in kilograms (kg).
locations = [
    {
        "name": "Warehouse A",
        "opening": 500,
        "received": 200,
        "distributed": 400,
        "damaged": 20,
        "physical": 270,
        "target": 400
    },
    {
        "name": "Distribution Center B",
        "opening": 300,
        "received": 150,
        "distributed": 250,
        "damaged": 10,
        "physical": 180,
        "target": 300
    },
    {
        "name": "Relief Camp C",
        "opening": 200,
        "received": 100,
        "distributed": 220,
        "damaged": 5,
        "physical": 80,
        "target": 150
    },
    {
        "name": "Storage Unit D",
        "opening": 400,
        "received": 100,
        "distributed": 200,
        "damaged": 10,
        "physical": 300,
        "target": 250
    }
]

total_replenishment = 0
total_discrepancy = 0

print("FOOD SUPPLY CHAIN STOCK RECONCILIATION")
print("=" * 100)

print(
    f"{'Location':<24}{'Expected':>10}"
    f"{'Physical':>10}{'Difference':>12}"
    f"{'Status':>15}{'Replenish':>12}"
)

for item in locations:
    # Calculate expected stock
    expected = (
        item["opening"]
        + item["received"]
        - item["distributed"]
        - item["damaged"]
    )

    # Positive difference = surplus
    # Negative difference = shortage
    discrepancy = item["physical"] - expected

    # Calculate replenishment based on physical stock
    replenishment = max(
        0, item["target"] - item["physical"]
    )

    if discrepancy == 0:
        status = "Reconciled"
    elif discrepancy > 0:
        status = "Surplus"
    else:
        status = "Shortage"

    print(
        f"{item['name']:<24}{expected:>10.1f}"
        f"{item['physical']:>10.1f}"
        f"{discrepancy:>+12.1f}"
        f"{status:>15}"
        f"{replenishment:>12.1f}"
    )

    total_discrepancy += discrepancy
    total_replenishment += replenishment

print("-" * 100)
print(f"Net discrepancy: {total_discrepancy:+.1f} kg")
print(f"Total replenishment required: "
      f"{total_replenishment:.1f} kg")
print("Reconciliation completed.")
output
FOOD SUPPLY CHAIN STOCK RECONCILIATION
====================================================================================================
Location                  Expected  Physical  Difference         Status   Replenish
Warehouse A                   280.0     270.0       -10.0       Shortage       130.0
Distribution Center B         190.0     180.0       -10.0       Shortage       120.0
Relief Camp C                  75.0      80.0        +5.0        Surplus        70.0
Storage Unit D                290.0     300.0       +10.0        Surplus         0.0
----------------------------------------------------------------------------------------------------
Net discrepancy: -5.0 kg
Total replenishment required: 320.0 kg
Reconciliation completed.'''