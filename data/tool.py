import re


def remove_url(sentence):
    """Remove URLs from a sample string"""
    text = re.sub(r"/\s\s+/g", " ", sentence)
    text = re.sub(r"http:\/\/t.cn\S+", "", text)
    text = re.sub(r"[\u200b\xa0\u202c\u202e\u3000\U0001f90d]", "", text)
    text = text.strip()
    return text