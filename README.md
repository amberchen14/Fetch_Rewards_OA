# Fetch_Rewards_OA
This project calculates the string similarity ratio between two paragraphs. The ratio is 1 when the contents are identical; otherwise, the ratio is 0 when the contents are totally different. 

## Results Output
Sample1 and Sample2 ![s1_vs_s2](/pic/s1_vs_s2.png)
Sample2 and Sample3 ![s2_vs_s3](/pic/s2_vs_s3.png)
## Satisfied requirements
1. At least the code can run.
2. Use only standard library.
3. Package this application as a web service.
4. Package the web service in a Docker container.


## Algorithm
### Presumption
- This project ignore all punctuations. For example, "don't" becomes "dont" and "we'll" becomes "well".
- This project imports [difflib](https://docs.python.org/3/library/difflib.html), which can compare string similarity.
- To compare two paragraphs, this project calculate two scores, total_score and similarity_score. Total score is the sum of the words, and similarity_score is the score of string similarity. If two lists are identical, similarity_score = total_score. 

### Process
1. Transform the paragraph to a list of words and ignore punctuations. For example, "I don't like dog." becomes ["I", "dont", "like", "dog"].
2. Use difflib to get different words. For example, ["I", "dont", "like", "dog"] and ["I", "do", not", "like", "dog"] becomes [" I", "+ dont", "- do", "- not", " like", " dog"]. Sign "+" means the unique word at list1 and sign "-" means the unique word at list2.
3. Score calculations: 
  - If the word is identical (no sign before the word, ex. " I"), total_score and similarity_score both plus 1.
  - Otherwise, concat the words with the same sign to compare similarity. For example, the comparison between ["+ dont", "- do", "- not"] is "dont" and "donot" and the score is 0.8. Total_score will plus the minimum number of concated words ("dont"=1) and similarity_score will plus the output of string similarty(0.8).
  - Concat the words until no sign the before words.  
4. After comparing all words in the list, the ratio = similarity_score/total_score. For example, 0.95=similarity_score (3+0.8)/total_score(4).

## Steps to launch the app
1. Git clone this repository. (git clone ) 
2. Open terminal and navigate to this folder
3. run the query line by line below:
```bash
docker image build -t test .  
docker run -p 5000:5000 -d test      
```
4. Turn on browser and copy compared texts on http://0.0.0.0:5000/
5. Click submit.
```

