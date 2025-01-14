import random

elements = [
    "0-92837-9ashdbadf7t",
    "-087asdflkadf-9723sd",
    "sdfv986dfgadfg2q34dfb",
    "9-sdnfaidf-0a8ga345gag",
    "dfget3q4623645shwyFEQT3",
    "4356FB*&3456dagfw--wdf"
]


asset_code = random.choice(elements)


for element in elements:
    while asset_code != element:
        break
    else:
        print(f'found match {element} and {asset_code}')


