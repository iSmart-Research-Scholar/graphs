import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.metrics.distance import jaccard_distance

def similarity(para1, para2):
    stop_words = set(stopwords.words("english"))
    para1_words = [w.lower() for w in word_tokenize(para1) if w.lower() not in stop_words]
    para2_words = [w.lower() for w in word_tokenize(para2) if w.lower() not in stop_words]
    similarity = 1 - jaccard_distance(set(para1_words), set(para2_words))
    return similarity

para1 = '''Three bears had prepared breakfast and
while waiting for it to be ready, decided to go on a
walk. There was a father, mother, and baby bear.
While they were gone a little girl broke into their
home. Her name was Goldilocks. She went
through each room, trying out furniture and trying
on clothes. There was always one thing too big or
too hard and another that was too little or too
soft, but the third was always perfect. Then she
noticed the breakfast. The first was too hot, then
too cold, then perfect and she ate it all up.
Goldilocks went to the beds and found the perfect
one and fell asleep, which is where the three
bears found her.'''
para2 = '''The three little pigs were all brothers.
Each brother was different, but they were still
family. Each brother decided to build his own
home. The first pig built a house of straw, the
second of sticks, and the third of bricks. One day a
big bad wolf came along and threatened to eat
the pigs. Each ran to his house. The wolf followed
the first pig and blew the straw house down. The
first pig ran to the second pigs house. Again, the
wolf blew down the stick house. Both brothers ran
to the third pigs house. The wolf tried and tried,
but the third house was perfect and could not be
blown down. The pigs had to figure out how to get
rid of the wolf.'''

sim = similarity(para1, para2)
print("Similarity:", sim)


