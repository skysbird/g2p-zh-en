# g2p_zh_en

## Introduction

g2p_zh_en is an open-source project that provides a mixed Grapheme-to-Phoneme (G2P) conversion between Chinese and English based on Bigcidian's translation table. It aims to convert text between Chinese and English phonemes, allowing for pronunciation and speech-related applications.

## Features

- G2P conversion from Chinese to English
- G2P conversion from English to Chinese
- Handling of special characters, such as numbers and currencies

## Installation

1. Make sure your environment meets the following requirements:
   - Python 3.x
   - Other dependencies (listed in requirements.txt)

2. Install the required dependencies by running the following command:

pip install -r requirements.txt


3. Install g2p_zh_en using pip:

pip install g2p_zh_en


## Usage

Import the G2P class from g2p_zh_en and create an instance:

```python
from g2p_zh_en.g2p_zh_en import G2P

g2p = G2P()
text = "我有100美元,i'm so rich."
output = g2p.g2p(text)
print(output)
['w', 'uɔ3', 'y', 'əu3', 'y', 'ii4', 'b', 'ai3', 'm', 'ei3', 'yu', 'an2', ',', ' ', 'ai', 'm', ' ', 's', 'əu', ' ', 'r', 'i', 'ch', ' ', '.']
text = "i have 100 dollar,我是不是很富有？"
output = g2p.g2p(text, language='en-us')
print(output)
['ai', ' ', 'h', 'æ', 'v', ' ', 'w', 'ʌ', 'n', ' ', 'h', 'ʌ', 'n', 'd', 'r', 'ə', 'd', ' ', 'd', 'a', 'l', 'ər', ' ', ',', ' ', 'w', 'uɔ3', 'sh', 'iii4', 'b', 'uu2', 'sh', 'iii4', 'h', 'ən3', 'f', 'uu4', 'y', 'əu3', ' ', '？']
```

Please note that the output represents the phonetic representation of the input text.

## In Progress
The following features are currently being developed:

- [x] G2P conversion with Chinese as the primary language.
- [x] G2P conversion with English as the primary language.
- [ ]Handling various special characters, such as numbers and currencies.
Contribution

If you would like to contribute to this project, you can:

Submit bug reports or feature requests on the project's issue page.
Fork the project, create your own branch, and submit a pull request.
Improve documentation and code comments.
Thank you for your support and contributions!


## License
This project is licensed under the GNU General Public License.