import hashlib
#here's my 2 cent script😭
# Function to double SHA256 hash bytes
def double_sha256(b):
    return hashlib.sha256(hashlib.sha256(b).digest()).digest()

# Replace these with your block's transaction IDs from block_details.txt
txids = [
    "bb9709703b1e93298d5e5657a19ef5209408bf84554360b0e747207ad9d2df1d",
    # add other txids here if more than 1
]

# Convert txid strings to bytes (little-endian)
tx_bytes = [bytes.fromhex(txid)[::-1] for txid in txids]

# Compute Merkle Root
while len(tx_bytes) > 1:
    if len(tx_bytes) % 2 != 0:
        tx_bytes.append(tx_bytes[-1])  # duplicate last if odd number of tx
    new_level = []
    for i in range(0, len(tx_bytes), 2):
        new_level.append(double_sha256(tx_bytes[i] + tx_bytes[i+1]))
    tx_bytes = new_level

# Convert final root to hex (big-endian)
merkle_root = tx_bytes[0][::-1].hex()
print("Merkle Root:", merkle_root)
#thankssss
