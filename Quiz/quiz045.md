# This is quiz 045
<img width="900" alt="Screenshot 2025-02-24 at 23 48 14" src="https://github.com/user-attachments/assets/ecbe57fb-4fca-401a-aa32-011fc8a39fd1" />

## Paper Work
![IMG_1678](https://github.com/user-attachments/assets/445dda41-3f70-40df-ad20-080600a0a9a9)

## UML Diagram
![IMG_1680](https://github.com/user-attachments/assets/e9cbdaaf-315d-4cd7-bb45-5b79ebc56d0b)

## Code
```py
class WordCounter:
    def __init__(self, text):
        self.text = text

    def wordCount(self):
        words = self.text.split()
        result = {}
        for w in words:
            w = w.strip(".!?").lower()
            if w not in result:
                result[w] = 1
            else:
                result[w] += 1
        self.result = result
        return self.result

print(WordCounter("This is a sample text. It contains some words that will be counted.").wordCount())
```

## Proof of Work

<img width="1000" alt="Screenshot 2025-02-25 at 8 30 51" src="https://github.com/user-attachments/assets/e5eda942-c742-472f-8d1b-9a56c3eb0a27" />
