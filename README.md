Objective:
- This is the automation code that automatically do `git commit` with timestamps in the past. A person looks at the Github repo heatmap will think that we coded a lot.
- Just for fun, the code here shows the small heart shape in Github heatmap.

Algorithm
- Done with help from ChatGPT.
- The file `auto_commit.py` looks at provided timestamps in the file `working_day.yml`. For each day, it will just add a random text to the file `commit.txt` a random number of times, and `git commit`.