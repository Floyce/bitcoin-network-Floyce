from pybloom_live import BloomFilter

# Create Bloom filter
bf = BloomFilter(capacity=1000, error_rate=0.001)

# Example: Add a transaction ID
my_txid = "bb9709703b1e93298d5e5657a19ef5209408bf84554360b0e747207ad9d2df1d"
bf.add(my_txid)

# Print Bloom filter's bit array
print("Bloom Filter Bit Array:")
print(bf.bitarray)

# Demonstrate probabilistic matching
print("Checking if TXID is in filter:", my_txid in bf)
print("Checking a fake TXID:", "1234abcd" in bf)
