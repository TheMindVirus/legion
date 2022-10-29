import json, copy

INPUT_FILE = "TS_Save_Template_Arcanists.json"
OUTPUT_FILE = "TS_Save_Generated_Arcanists.json"

ASSET_BUNDLES = \
{
    "Obsidian": "http://cloud-3.steamusercontent.com/ugc/1901108810536706523/63A566DA4EB448AA68203CA6860D9B6FA7357A97/",
}

GRID_WIDTH = 69
GRID_HEIGHT = 3
GRID_LENGTH = 47

input_data = ""
with open(INPUT_FILE, "r") as file:
    input_data = file.read()

process_data = json.loads(input_data)
template_item = process_data["ObjectStates"][-1]
process_data["ObjectStates"].pop()
print(template_item)
x = 0
y = 0
z = 0
ox = template_item["Transform"]["posX"]
oy = template_item["Transform"]["posY"]
oz = template_item["Transform"]["posZ"]
sx = template_item["Transform"]["scaleX"]
sy = template_item["Transform"]["scaleY"]
sz = template_item["Transform"]["scaleZ"]
for i in range(0, (GRID_WIDTH * GRID_HEIGHT * GRID_LENGTH)):
    new_item = copy.deepcopy(template_item)
    new_item["Transform"]["posX"] = (x * sx) + ox
    new_item["Transform"]["posY"] = (y * sy) + oy
    new_item["Transform"]["posZ"] = (z * sz) + oz
    new_item["CustomAssetbundle"]["AssetbundleURL"] = ASSET_BUNDLES["Obsidian"]
    process_data["ObjectStates"].append(new_item)
    #print(i, x, y, z)
    x += 1
    if x >= GRID_WIDTH:
        x = 0
        y += 1
        if y >= GRID_HEIGHT:
            y = 0
            z += 1
            if z >= GRID_LENGTH:
                z = 0

output_data = json.dumps(process_data, indent = 4)

with open(OUTPUT_FILE, "w") as file:
    file.write(output_data)

print("Done!")
