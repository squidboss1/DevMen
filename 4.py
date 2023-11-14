import json

def show_interface_status(lines):
    print("Interface Status")
    print("=" * 81)
    print("DN" + " " * 43 + \
          "Description" + " " * 6 + \
          "Speed" + " " * 8 + \
          "MTU")
    print("-" * 44 + " " + "-" * 15 + " " + "-" * 12 + " " + "-" * 7)

    # for line in lines:
    #     print(line)
    return [print(line) for line in lines]


with open('data.json', 'r', encoding="utf-8") as file:
    data = json.load(file)
    lines = []

    # Iteracja w key imdata
    for item in data['imdata']:
        dn_value = item['l1PhysIf']['attributes']['dn']
        descr_value = item['l1PhysIf']['attributes']['descr']
        speed_value = item['l1PhysIf']['attributes']['speed']
        mtu_value = item['l1PhysIf']['attributes']['mtu']

        # Budowanie linii
        line = (dn_value + " " * 10 + \
              descr_value + " " * 10 + \
              speed_value + " " * 6 + \
              mtu_value + "\n")

        lines.append(line)
    show_interface_status(lines)

