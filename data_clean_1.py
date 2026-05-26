from datasets import load_dataset, concatenate_datasets, load_from_disk
from collections import Counter
import random
import difflib




if __name__ == "__main__":
    print("start")

    # hf_set = load_dataset("bigcode/commitpackft", revision="refs/convert/parquet", 
    #                       languages=["Python", "Java","C++", "Rust", "Go", "JavaScript"],  trust_remote_code=True)

    # hf_set.save_to_disk("datasets/dataset1.hf")  

    # load the saved dataset
    ds = load_from_disk("/workspace/datasets/dataset1.hf")

    # filter out only the languages we are interested in
    langs = ["Python", "Java", "C++", "Rust", "Go", "JavaScript"]
    ds_filtered = ds["train"].filter(lambda x: x["lang"] in langs)

    # drop useless stuff within each entry
    columns_to_drop = ['commit', 'old_file', 'new_file', 'message', 'license', 'repos']
    ds_filtered = ds_filtered.remove_columns(columns_to_drop)

    # define mapping function to create the diff we are interested in
    def replace_with_diff(example):
        diff = difflib.unified_diff(
                            example["old_contents"].splitlines(), 
                            example["new_contents"].splitlines(),
                            lineterm="")
        
        example["diff"] = "\n".join(diff)

        return example

    # apply the mapping
    ds_filtered = ds_filtered.map(replace_with_diff)
    # remove the old columns
    ds_filtered = ds_filtered.remove_columns(['new_contents', 'old_contents'])

    print(ds_filtered[0])

    # save to local disk
    ds_filtered.save_to_disk("datasets/cleaned_diff_1.hf") 