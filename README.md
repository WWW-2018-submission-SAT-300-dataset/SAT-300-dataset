# SAT-300 dataset

The SAT-300 dataset aims to provide ground truth for the task of Named Entity Recognition and Disambiguation.
Its main focus is on short texts that have a high density of ambiguous named entities.
Each one of the dataset's 300 texts is accompanied with its named entities' start and end character offsets, as well as their best matches in Wikipedia and Google Knowledge Graph. Both the entities' limits in text and their corresponding canonical entities were extracted and verified by humans.

*SAT-300.json* is the dataset in JSON format. 
*SAT-300_JSON_to_HTML.py* is a simple Python script that parses the JSON file and produces an HTML file containing the dataset, named *SAT-300.html*.
Finally, the dataset is also distributed in NIF format (*SAT-300.nif*), which is appropriate for evaluation of annotators using the GERBIL framework.

