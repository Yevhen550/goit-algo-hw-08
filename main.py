import heapq


def min_cost_to_connect_cables(cables):
    # Створюємо мін-купу з початковими довжинами кабелів
    heapq.heapify(cables)

    total_cost = 0

    # Продовжуємо з'єднувати, поки в купі більше одного елемента
    while len(cables) > 1:
        # Витягуємо два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Об'єднуємо їх
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost


# Приклад
cables = [4, 3, 2, 6]
result = min_cost_to_connect_cables(cables)
print(f"Мінімальні загальні витрати: {result}")
