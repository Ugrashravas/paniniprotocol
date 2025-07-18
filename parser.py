
jefferson_revelation = {
    'A': 'त',
    'B': 'ग',
    'C': 'प',
    'D': 'द',
    'E': 'अ',
    'F': 'ब',
    'G': 'च',
    'H': 'म',
    'I': 'न',
    'J': 'न',
    'K': 'ल',
    'L': 'ए',
    'M': 'क',
    'N': 'र',
    'O': 'इ',
    'P': 'अन्',
    'Q': 'च',
    'R': 'य',
    'S': 'व',
    'T': 'स',
    'U': 'उ',
    'V': 'ज',
    'W': 'ओ',
    'X': 'म',
    'Y': 'अस्',
    'Z': 'व'
}

def decipher(text, phoneme_map):
    result = []
    char_count = 0
    # Uppercase the text
    text = text.upper()
    for char in text:
        if char in phoneme_map:
            result.append(phoneme_map[char])
            char_count+=1

    return '-'.join(filter(None, result)), char_count

import re

def split_into_chunks_by_letters(text, target_letter_count=10):
    words = re.findall(r'\w+', text)  # removes punctuation, keeps words
    chunks = []
    current_chunk = []
    current_count = 0

    for word in words:
        word_len = len(word)
        if current_count + word_len > target_letter_count and current_chunk:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_count = 0
        current_chunk.append(word)
        current_count += word_len

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

import sources
text = ""
# Get segments
SEG = False
# Display each segment and its phoneme mapping
if SEG:
    segments = split_into_chunks_by_letters(text, target_letter_count=16)
    for i, segment in enumerate(segments, 1):
        phonemes, count = decipher(segment, jefferson_revelation)
        print(f"{i:02d},{segment.upper()},{count},{phonemes},,")
else:
    phonemes, count = decipher(text, jefferson_revelation)
    print(f"-,{text.upper()},{count},{phonemes},,")

phonemes, count = decipher(text, jefferson_revelation)
print(f"Total count: {count}")
