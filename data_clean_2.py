from datasets import load_dataset, concatenate_datasets, load_from_disk
from collections import Counter
import random
import difflib
import numpy as np



if __name__ == "__main__":

    # load the saved dataset
    ds_cleaned_1 = load_from_disk("/workspace/datasets/cleaned_diff_1.hf")


    def subject_filtering(dict_entry):
        if len(dict_entry['subject']) >= 3 and len(dict_entry['subject']) <= 75:
            return True


    ds_subject_clean = ds_cleaned_1.filter(subject_filtering)


    def diff_filtering(dict_entry):
        if len(dict_entry["diff"]) > 0:
            for line in dict_entry["diff"].splitlines():
                if line.startswith(("+", "-")) and not line.startswith(("+++", "---")):
                    if line[1:].strip() != "":
                        return True
        return False

    ds_diff_clean = ds_subject_clean.filter(diff_filtering)

    print(ds_diff_clean[0])

    #ds_diff_clean.save_to_disk("datasets/cleaned_diff_2.hf") 



    # longest = max(ds_diff_clean, key=lambda x: len(x['subject']) + len(x['diff']))
    # print(len(longest['subject']) + len(longest['diff']))


    #diff_list = [ds_diff_clean[i]["diff"] for i in range(len(ds_diff_clean))]

    # from our diff cleaned list - we just take the shortest entries and display them later 
    # overall looks good, the entries we found are meaningful
    # def diff_len_filtering(dict_entry):
    #     if len(dict_entry["diff"]) < 100:
    #             return True

    # mini_diffs_ds = ds_diff_clean.filter(diff_len_filtering)

    # mini_diffs_list = [mini_diffs_ds[i]["diff"] for i in range(100)]


    # print(mini_diffs_list)

    # whitespaces_gone = [i for i in mini_diffs_list if i.strip()]

    # print("\n\n---\n\n".join(whitespaces_gone))

















    # commit_list = [ds_subject_clean[i]['subject'] for i in range(500)]
    
    # maxl = len(max(commit_list, key=len))
    # minl = len(min(commit_list, key=len))

    # print(f"max l is: {maxl} und minl is {minl}")