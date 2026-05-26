from huggingface_hub import login, upload_folder
from datasets import Dataset, load_from_disk


if __name__ == "__main__":
    login(token='.....')
    #Push your dataset files
    #upload_folder(folder_path="datasets/cleaned_diff_2.hf", repo_id="wiggly1993/qwen2.5-7B-finetuning", repo_type="dataset")


    ds = load_from_disk("datasets/cleaned_diff_2.hf")
    ds.push_to_hub("wiggly1993/qwen2.5-7B-finetuning")
    
    # print(ds)
    # print(ds[0])
