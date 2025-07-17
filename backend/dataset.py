import random
import json

# Sample templates for positive and negative sentiments
positive_phrases = [
    "I love this!", "Amazing experience.", "Fantastic job!", "Absolutely wonderful.",
    "Great service and support.", "Really satisfied.", "So happy with the result.",
    "Couldn't be better!", "Superb quality!", "Highly recommend this product.",
    "Best decision ever.", "I'm impressed!", "Works perfectly.", "Everything was perfect.",
    "Top-notch experience.", "Extremely pleased.", "Awesome support team.",
    "Enjoyed it thoroughly.", "Brilliant!", "Five stars!"
]

negative_phrases = [
    "I hate this.", "Terrible experience.", "Very disappointed.", "Worst product ever.",
    "Absolutely awful.", "Would not recommend.", "Poor support and quality.",
    "Extremely dissatisfied.", "It's broken.", "Completely useless.",
    "Waste of time.", "Didn't like it at all.", "Really bad.", "Unacceptable service.",
    "Horrible quality.", "Frustrating experience.", "Never again.",
    "This was a mistake.", "Regret buying it.", "So bad!"
]

# Generate entries
data = []
for _ in range(2500):  # 2500 positive
    entry = {
        "text": random.choice(positive_phrases),
        "label": "positive"
    }
    data.append(entry)

for _ in range(2500):  # 2500 negative
    entry = {
        "text": random.choice(negative_phrases),
        "label": "negative"
    }
    data.append(entry)

# Shuffle the data
random.shuffle(data)

# Write to JSONL file
with open("synthetic_sentiment_5000.jsonl", "w", encoding="utf-8") as f:
    for entry in data:
        json.dump(entry, f)
        f.write('\n')

print("✅ Dataset with 5000 entries saved as 'synthetic_sentiment_5000.jsonl'")
