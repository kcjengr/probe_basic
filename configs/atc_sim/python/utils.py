import json


def _read_store_file():

    with open("atc_store.json", 'r') as storage_file:
        storage = json.load(storage_file)

    return storage


def _store_pocket(pocket, tool):
    storage = _read_store_file()
    storage["pockets"][int(pocket)] = int(tool)
    with open("atc_store.json", 'w') as storage_file:
        json.dump(storage, storage_file)

    return 0


def _store_spindle(tool):
    storage = _read_store_file()
    storage["spindle"] = int(tool)
    with open("atc_store.json", 'w') as storage_file:
        json.dump(storage, storage_file)

    return 0

