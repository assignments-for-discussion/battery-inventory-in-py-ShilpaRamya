
def count_batteries_by_health(present_capacities):
  return {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
def calculate_soh(present_capacity, rated_capacity):
  try:
    soh_percentage = (present_capacity / rated_capacity) * 100
        return soh_percentage
  except ZeroDivisionError:
    print("Error: Rated capacity cannot be zero.")
    return None
def classify_batteries(present_capacities):
  healthy_count = 0
  exchange_count = 0
  failed_count = 0

  for present_capacity in present_capacities:
    rated_capacity = 120  # Rated capacity of all batteries is 120 Ah

        # Calculate State of Health (SoH) for the current battery
        soh_percentage = (present_capacity / rated_capacity) * 100

        # Classify the battery based on SoH
        if soh_percentage > 80:
            healthy_count += 1
        elif 65 <= soh_percentage <= 80:
            exchange_count += 1
        else:
            failed_count += 1

return healthy_count, exchange_count, failed_count

def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 77]
  counts = classify_batteries(present_capacities)
  
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()




