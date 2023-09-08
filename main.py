
def count_batteries_by_health(present_capacities):
  return {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
rated_capacity = 120
SoH% = 100 * present_capacity / rated_capacity

    for i in present_capacities:
        SoH% = 100 * i / rated_capacity
        if SoH% > 80:
            counts["healthy"] += 1
        elif 65 <= SoH% <= 80:
            counts["exchange"] += 1
        elif SoH% < 65:
            counts["failed"] += 1

    return counts

def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 77]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
