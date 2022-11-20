import json

INPUT_FILE = "output.csv"


def csv_to_list_dict(FILENAME) -> list[dict]:
    x = []
    with open(FILENAME, "r", encoding="utf-8") as f:
        for line in f:
            x.append(line.rstrip())
    row = []
    for i in range(0, len(x)):
        row.append(x[i].split(","))
    dict_ = [{row[0][i]: row[j][i] for i in range(0, len(row[j]))} for j in range(1, len(x))]
    return dict_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
