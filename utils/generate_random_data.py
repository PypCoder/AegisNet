import numpy as np

def generate_random_data(n_samples):
    data = []

    for _ in range(n_samples):

        # Force 50% clear attack traffic
        traffic_type = np.random.choice(["safe", "attack"])

        if traffic_type == "safe":
            sample = [
                np.random.randint(100000, 300000),     # Moderate duration
                np.random.randint(20, 60),             # Normal packets
                np.random.randint(20, 60),
                np.random.randint(5000, 20000),        # Normal size
                np.random.randint(5000, 20000),
                np.random.uniform(300, 2000),          # Normal rate
                np.random.uniform(10, 60),
                np.random.uniform(300, 1200),
                np.random.uniform(100, 500),
                np.random.randint(4000, 16000),
                np.random.randint(4000, 16000),
            ]

        else:
            sample = [
                np.random.randint(500000, 50000000),            # Very huge duration burst
                np.random.randint(0, 3),          # small forward packets
                np.random.randint(0, 3),               # Almost no backward packets
                np.random.randint(0, 3),     # small forward bytes
                np.random.randint(0, 3),
                np.random.uniform(0, 3),      # small bytes/sec
                np.random.uniform(0, 3),         # small packets/sec
                np.random.uniform(0, 3),
                np.random.uniform(0, 3),
                np.random.randint(300000, 650000),
                np.random.randint(10000, 100000),
            ]

        data.append(sample)

    return np.array(data)
