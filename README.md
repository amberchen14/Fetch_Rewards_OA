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
1. Transform the paragraph to a list of words. Steps:
  - Remove punctuations
  - Lower capital.
  - Split the words with space. 
![example1](/pic/example1.png | width=100)
2. Find unique words between two lists. For example, the result shows that red words (+) are unique in list 1, and blue words (-) are unique in list 2. 
![example2](/pic/example2.png)
3. Concat the unique words with same sign and calculate string similarity using SequenceMatcher in Difflib package.
![example3](/pic/example3.png)

### Score calculation
- total_score: 2 cases, with/out sign
  - No sign before the word: +1. (ex. "i", "like", "dog" = 3)
  - Sign before the word: 
    1. Sum the signs until no sign before the word. 
    2. If only facing one sign: + number of sign
    3. Two signs (+ and -): + min(number of -, number of +)
![example4](/pic/example4.png)    
- string_similarity: 2 cases, with/out sign
  - No sign before the word: +1. (ex. "i", "like", "dog" = 3)
  - Sign before the word: 
    1. Concat the words with the same sign until no sign before the word.  
    2. If only facing one sign: + 0
    3. Two signs (+ and -): + SequenceMatcher(words with +, words with -).ratio()
![example5](/pic/example5.png)    
- Ratio= string_similarity/total_score. (ex. 3.8/4=0.95)

## Steps to launch the app
1. Git clone this repository. (git clone https://github.com/amberchen14/Fetch_Rewards_OA.git) 
2. Open terminal and navigate to this folder
3. Run the query line by line below:
```bash
docker image build -t test .  
docker run -p 5000:5000 -d test      
```
4. Turn on browser and copy compared texts on http://0.0.0.0:5000/
5. Click submit.
```

