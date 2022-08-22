import collections


def CheckNetwork(network):
    checked = set()
    queue = collections.deque()
    queue.append(0)

    while len(queue) > 0:
        idx = queue.popleft()
        for next_idx, value in network[idx]:
            if next_idx not in checked:
                queue.append(next_idx)
        checked.add(idx)
        if len(checked) == len(network):
            return True
    return False


def ComputeWeight(network):
    tot = 0
    done = set()
    for line, node in enumerate(network):
        for col, value in node:
            if (line, col) not in done and (col, line) not in done:
                tot += value
                done.add((line, col))
    return tot


def ComputeSaving(network, ordonned_link):
    for value, idx_line, idx_el in ordonned_link:
        network[idx_line].remove((idx_el, value))
        if not CheckNetwork(network):
            network[idx_line].append((idx_el, value))

    return ComputeWeight(network)


if __name__ == "__main__":
    network = []
    ordonned_link = []
    with open('p107_network.txt', 'r') as file:
        # with open('test.txt', 'r') as file:
        lines = file.read().split('\n')
        for idx_line, line in enumerate(lines):
            network.append([])
            for idx_el, el in enumerate(line.split(',')):
                if el.isnumeric():
                    network[-1].append((idx_el, int(el)))
                    ordonned_link.append(
                        (int(el), idx_line, idx_el))
    ordonned_link.sort(reverse=True)
    weight = ComputeWeight(network)
    print(weight)
    new_weight = ComputeSaving(network[:-1], ordonned_link)
    saving = weight - new_weight
    print(f"new_weight: {new_weight}. saving: {saving}")
