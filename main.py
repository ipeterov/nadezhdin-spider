import json

def calculate_submittable():
    with open('region_data.json') as f:
        data = json.load(f)

    total = 0
    for region in data:
        total += min(region['progress'], 2500)
        print(region['region_name'], region['progress'])

    print("Всего подписей с учётом лимита 2500:", total)


if __name__ == '__main__':
    calculate_submittable()

