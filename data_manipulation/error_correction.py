import pandas as pd
import nltk
df = pd.read_csv("df_diseases.csv")
X = df.values
def func(word):
    min=999999999
    output=""
    for i in range(X.shape[0]):
        if(nltk.edit_distance(X[i][0], word)<min):
            min=nltk.edit_distance(X[i][0], word)
            output=X[i][0]

    return output

word="lung cncer"
ans = func(word)
print(ans)
