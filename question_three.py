from collections import defaultdict

def question_three(words):
    return {i:words.count(i) for i in set(words)}
    
print(question_three('hello how are you'))

