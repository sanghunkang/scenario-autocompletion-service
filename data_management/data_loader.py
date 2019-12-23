import json



FILEPATH_NLU_BENCHMARK = "/Users/sanghunkang/dev/NLU-Evaluation-Corpora/WebApplicationsCorpus.json"

def load_data(dataset_name):
    if dataset_name == "nlu_benchmark":
        return load_data_nlu_benchmark()    
    elif dataset_name == "<OTHER DATASET>":
        return None
    else:
        raise Exception("Unprepared dataset")

def load_data_nlu_benchmark():
    # Read file
    with open(FILEPATH_NLU_BENCHMARK) as f:
        records = json.loads(f.read())["sentences"]
        for record in records:
            # print(json.dumps(record, indent=2))
            print(record["training"], ":", record["intent"],  "<<<", record["text"])

    # Remove unneccessary parts


    # Normalise


    # Split into train/validation/test

load_data("nlu_benchmark")