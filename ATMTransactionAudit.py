'''Algorithm
Start.

Initialize the account balance and define a sequence of transactions.

Read each transaction, including its type, amount, and details.

Validate the transaction amount; reject zero or negative amounts.

Process the transaction:

Deposit: Add the amount to the balance.

Withdrawal: Subtract the amount if sufficient funds are available.
Transfer: Subtract the amount if sufficient funds are available and record the transfer.

Detect invalid transactions, such as insufficient funds or unsupported transaction types.

Track repeated transactions and flag suspicious patterns, such as three or more consecutive withdrawals of the same amount.

Record each transaction's status and resulting balance.

Display the transaction audit report, suspicious patterns, and final balance.

Stop.
Flowchart

flowchart TD
    A([Start]) --> B[Initialize accounts and transactions]
    B --> C[Read next transaction]
    C --> D{More transactions?}
    D -- No --> K[Analyze repeated transaction patterns]
    D -- Yes --> E{Valid account and positive amount?}
    E -- No --> F[Record invalid transaction]
    E -- Yes --> G{Deposit, withdrawal, or transfer?}
    G -- Deposit --> H[Add amount to balance]
    G -- Withdrawal --> I{Sufficient balance?}
    I -- No --> F
    I -- Yes --> J[Deduct amount]
    G -- Transfer --> L{Valid destination and sufficient funds?}
    L -- No --> F
    L -- Yes --> M[Update both account balances]
    H --> N[Record successful transaction]
    J --> N
    M --> N
    F --> C
    N --> C
    K --> O[Print audit report and final balances]
    O --> P([Stop])
code 

from collections import Counter

# Initial account balances
accounts = {
    "A101": 1000.00,
    "A102": 500.00,
    "A103": 800.00
}

# Transaction format:
# (type, source_account, amount, destination_account)
transactions = [
    ("DEPOSIT", "A101", 200, None),
    ("WITHDRAW", "A101", 100, None),
    ("TRANSFER", "A101", 300, "A102"),
    ("WITHDRAW", "A101", 900, None),  # Insufficient funds
    ("DEPOSIT", "A102", 100, None),
    ("WITHDRAW", "A102", 50, None),
    ("WITHDRAW", "A102", 50, None),
    ("WITHDRAW", "A102", 50, None),
    ("TRANSFER", "A103", 100, "A999"),  # Invalid destination
    ("DEPOSIT", "A101", -20, None)       # Invalid amount
]

successful = []
invalid = []
pattern_counts = Counter()

print("===== ATM TRANSACTION AUDIT =====")

for i, (kind, source, amount, destination) in enumerate(
    transactions, start=1
):
    reason = None

    if source not in accounts:
        reason = "Invalid source account"
    elif amount <= 0:
        reason = "Amount must be positive"
    elif kind not in ("DEPOSIT", "WITHDRAW", "TRANSFER"):
        reason = "Unknown transaction type"
    elif kind == "WITHDRAW" and accounts[source] < amount:
        reason = "Insufficient balance"
    elif kind == "TRANSFER":
        if destination not in accounts:
            reason = "Invalid destination account"
        elif source == destination:
            reason = "Source and destination must differ"
        elif accounts[source] < amount:
            reason = "Insufficient balance for transfer"

    if reason:
        invalid.append((i, kind, source, amount, reason))
        print(f"TXN {i}: REJECTED - {reason}")
        continue

    # Process valid transactions
    if kind == "DEPOSIT":
        accounts[source] += amount

    elif kind == "WITHDRAW":
        accounts[source] -= amount

    elif kind == "TRANSFER":
        accounts[source] -= amount
        accounts[destination] += amount

    successful.append((i, kind, source, amount, destination))
    pattern_counts[(kind, source)] += 1

    print(f"TXN {i}: SUCCESS - {kind} {amount:.2f}")

print("\n===== INVALID TRANSACTIONS =====")
if invalid:
    for i, kind, source, amount, reason in invalid:
        print(
            f"TXN {i}: {kind}, Account={source}, "
            f"Amount={amount:.2f} - {reason}"
        )
else:
    print("None")

print("\n===== SUSPICIOUS PATTERNS =====")
found = False

for (kind, source), count in pattern_counts.items():
    if count >= 3:
        print(
            f"ALERT: {count} successful {kind} transactions "
            f"from {source}"
        )
        found = True

if not found:
    print("No suspicious repeated patterns detected.")

print("\n===== FINAL ACCOUNT BALANCES =====")
for account, balance in accounts.items():
    print(f"{account}: {balance:.2f}")

print("\n===== AUDIT SUMMARY =====")
print(f"Total transactions: {len(transactions)}")
print(f"Successful: {len(successful)}")
print(f"Rejected: {len(invalid)}")
output
===== ATM TRANSACTION AUDIT =====
TXN 1: SUCCESS - DEPOSIT 200.00
TXN 2: SUCCESS - WITHDRAW 100.00
TXN 3: SUCCESS - TRANSFER 300.00
TXN 4: REJECTED - Insufficient balance
TXN 5: SUCCESS - DEPOSIT 100.00
TXN 6: SUCCESS - WITHDRAW 50.00
TXN 7: SUCCESS - WITHDRAW 50.00
TXN 8: SUCCESS - WITHDRAW 50.00
TXN 9: REJECTED - Invalid destination account
TXN 10: REJECTED - Amount must be positive

===== INVALID TRANSACTIONS =====
TXN 4: WITHDRAW, Account=A101, Amount=900.00 - Insufficient balance
TXN 9: TRANSFER, Account=A103, Amount=100.00 - Invalid destination account
TXN 10: DEPOSIT, Account=A101, Amount=-20.00 - Amount must be positive

===== SUSPICIOUS PATTERNS =====
ALERT: 3 successful WITHDRAW transactions from A102

===== FINAL ACCOUNT BALANCES =====
A101: 800.00
A102: 750.00
A103: 800.00

===== AUDIT SUMMARY =====
Total transactions: 10
Successful: 7
Rejected: 3'''