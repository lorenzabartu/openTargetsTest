import os
import sys
import json
import argparse
import itertools
import pandas as pd
import heapq

def main(filepath):

	datasets = ["sourceId=eva", "diseases", "targets"]
	file_paths = []

	for dataset in datasets: 
		os.system("cat %s/*.json > %s/merged.json" % (filepath+dataset, filepath+dataset))
		file_paths.append("%s/merged.json" % (filepath+dataset))

	df = pd.read_json(file_paths[0], lines = True)
	df.drop(df.columns.difference(["targetId","diseaseId", "score"]), axis=1, inplace=True)

	grouped = df.groupby(["targetId","diseaseId"])
	gb = grouped.groups

	values_of_interest = pd.DataFrame(columns = ["targetId","diseaseId", "median", "top3"])

	for key, item in grouped:

		scores = grouped.get_group(key).score
		values = [key[0], key[1], scores.median()]

		if len(scores) >= 3:
			maxes = (heapq.nlargest(3, scores))
			values.append(maxes)

		values_of_interest = values_of_interest.append(pd.Series(values, index=values_of_interest.columns[:len(values)]), ignore_index=True)

	diseaseID_all_df = pd.read_json(file_paths[1], lines = True)
	diseaseID_all_df.drop(diseaseID_all_df.columns.difference(["id","name"]), axis=1, inplace=True)

	targetID_all_df = pd.read_json(file_paths[2], lines = True)
	targetID_all_df.drop(targetID_all_df.columns.difference(["id", "approvedSymbol"]), axis=1, inplace = True )

	joined_df = pd.merge(values_of_interest, diseaseID_all_df[["id", "name"]], left_on = "diseaseId", right_on = "id", how = "left")
	values_of_interest["name"] = joined_df["name"]

	joined_df = pd.merge(values_of_interest, targetID_all_df[["id", "approvedSymbol"]], left_on = "targetId", right_on = "id", how = "left")
	values_of_interest["approvedSymbol"] = joined_df["approvedSymbol"]

	values_of_interest = values_of_interest.sort_values(by = ["median"])
	output_file = filepath + "output.json"

	values_of_interest.to_json(output_file, orient='records', lines=True)

	## Count the number target-target pairs share connections with at least two diseases

	values_of_interest.drop(values_of_interest.columns.difference(["targetId","diseaseId"]), axis=1, inplace=True)
	grouped = values_of_interest.groupby('targetId')
	filtered_groups = grouped.filter(lambda x: x['diseaseId'].nunique() >= 2)
	pair_counts = filtered_groups.groupby('targetId').apply(
	    lambda x: len(list(itertools.combinations(x['targetId'], 2)))
	)
	total_pairs = pair_counts.sum()

	print("The number of pairs of targets that repeat together among at least two diseases: ", total_pairs)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('filepath', type = str)
	path = (parser.parse_args()).filepath
	main(path)
