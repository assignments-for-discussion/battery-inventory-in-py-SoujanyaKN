def count_batteries_by_health(present_capacities):
    rated_capacity = 120
    healthy_count = 0
    exchange_count = 0
    failed_count = 0

    for present_capacity in present_capacities:
        soh = (present_capacity / rated_capacity) * 100
        
        if soh > 83:
            healthy_count += 1
        elif 63 <= soh <= 83:
            exchange_count += 1
        else:
            failed_count += 1

    return {
        "healthy": healthy_count,
        "exchange": exchange_count,
        "failed": failed_count
    }

def test_bucketing_by_health():
    present_capacities = [113, 116, 80, 95, 92, 70]
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 2)
    assert(counts["exchange"] == 3)
    assert(counts["failed"] == 1)

    present_capacities_boundary = [120, 83, 83, 63, 63, 62]
    counts_boundary = count_batteries_by_health(present_capacities_boundary)
    assert(counts_boundary["healthy"] == 1)
    assert(counts_boundary["exchange"] == 2)
    assert(counts_boundary["failed"] == 3)

    present_capacities_healthy = [120, 100, 110, 115]
    counts_healthy = count_batteries_by_health(present_capacities_healthy)
    assert(counts_healthy["healthy"] == 4)
    assert(counts_healthy["exchange"] == 0)
    assert(counts_healthy["failed"] == 0)

    present_capacities_failed = [50, 60, 62]
    counts_failed = count_batteries_by_health(present_capacities_failed)
    assert(counts_failed["healthy"] == 0)
    assert(counts_failed["exchange"] == 0)
    assert(counts_failed["failed"] == 3)

    present_capacities_mixed = [100, 83, 64, 60, 110, 85]
    counts_mixed = count_batteries_by_health(present_capacities_mixed)
    assert(counts_mixed["healthy"] == 3)
    assert(counts_mixed["exchange"] == 2)
    assert(counts_mixed["failed"] == 1)

    print("All test cases passed!")

if __name__ == '__main__':
    test_bucketing_by_health()
