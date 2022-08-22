import collections


def GetMinimumEnergySpent(n, shortcuts):
    """Allows to get the list of minimum energy spent.
    Input:
        n: int. Number of intersections.
        shortcuts: List[int]. List of all the shortcuts from idx to shortcuts[idx].
    Returns:
        List of the minimum energy spent to go from 1 to idx + 1.
    """
    energy_spent = [i for i in range(n)]
    queue = collections.deque(energy_spent)

    while len(queue) > 0:
        idx = queue.popleft()
        # Check next intersection
        if idx < n - 1 and energy_spent[idx + 1] > energy_spent[idx] + 1:
            energy_spent[idx + 1] = energy_spent[idx] + 1
            queue.append(idx + 1)
        # Check previous intersection
        if idx > 0 and energy_spent[idx - 1] > energy_spent[idx] + 1:
            energy_spent[idx - 1] = energy_spent[idx] + 1
            queue.append(idx - 1)
        # Check shortcut
        if energy_spent[idx] + 1 < energy_spent[shortcuts[idx]]:
            energy_spent[shortcuts[idx]] = energy_spent[idx] + 1
            queue.append(shortcuts[idx])

    return energy_spent


if __name__ == "__main__":
    n = int(input())
    shortcuts = [int(k) - 1 for k in input().split()]
    energy_spent_str = [str(k) for k in GetMinimumEnergySpent(n, shortcuts)]
    print(' '.join(energy_spent_str))
