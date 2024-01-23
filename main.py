import json
from collections import defaultdict

OVERCOLLECT_VALUES = [
    1,
    1.1,
    1.2,
    1.3,
    1.4,
    1.5,
    2,
]


def calculate_submittable():
    with open('region_data.json') as f:
        data = json.load(f)

    TOTALS = defaultdict(lambda: 0)

    for region in data:
        progress = region['progress']

        for overcollect in OVERCOLLECT_VALUES:
            submittable = int(progress / overcollect)
            TOTALS[overcollect] += min(submittable, 2500)

        print(region['region_name'], region['progress'])

    print("Рассмотрены разные пропрорции отбора лучших подписей.")
    print("Учтён лимит в 2500.")

    for overcollect, total in TOTALS.items():
        if overcollect == 1:
            print(f"Если сдавать все подписи без отбрасывания, то всего {total}")
        else:
            print(f"Собрать {overcollect * 100:.0f}%, отбросить {overcollect * 100 - 100:.0f}% и остаётся {total}")

if __name__ == '__main__':
    calculate_submittable()

