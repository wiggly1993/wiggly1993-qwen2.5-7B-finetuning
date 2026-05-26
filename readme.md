











Step 7 — GitHub Upload

Pushed all preprocessing scripts to GitHub. 
Key lessons: never hardcode HF tokens in scripts (use os.environ), 
always set up .gitignore before first commit to exclude datasets and cache folders.

GitHub defaults new repos to main but git CLI defaults to master. Fixed with git branch -m master main to rename locally, then force pushed to main. sd