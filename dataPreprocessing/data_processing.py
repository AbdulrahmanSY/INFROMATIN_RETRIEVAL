import string
import re
# from  abbreviations import abbreviations
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


def data_prossing(collection_dataFrame):
    print("1")
    collection_dataFrame['clean_doc'] = collection_dataFrame['doc'].apply(lambda x: tokenize_text(str(x)))
    print("2")
    collection_dataFrame['clean_doc'] = collection_dataFrame['clean_doc'].apply(lambda x: stemming(x))
    print("3")
    collection_dataFrame['clean_doc'] = collection_dataFrame['clean_doc'].apply(lambda x: remove_stopwords(x))
    print("4")
    collection_dataFrame['clean_doc'] = collection_dataFrame['clean_doc'].apply(lambda x: cleaning(str(x)))
    print("5")
    collection_dataFrame['clean_doc'] = collection_dataFrame['clean_doc'].apply(lambda x: remove_punctuation(str(x)))
    collection_dataFrame['clean_doc'] = collection_dataFrame['clean_doc'].apply(lambda x: tokenize_text(str(x)))
    print("6")
    collection_dataFrame['clean_doc'] = collection_dataFrame['clean_doc'].apply(lambda x: remove_numbers_with_text(x))
    print("7")
    collection_dataFrame['clean_doc'] = collection_dataFrame['clean_doc'].apply(lambda x: lemmatization(x))
    print(collection_dataFrame.shape)
    print(len(collection_dataFrame['clean_doc']))
    print("8")
    return collection_dataFrame


def remove_punctuation(txt):
    txt_nopunct = ''.join([c for c in txt if c not in string.punctuation])
    return txt_nopunct


def cleaning(text):
    # Remove not useful numbers
    text = re.sub(r'\b\d+\b', '', text)

    # Remove words that are two characters or shorter
    text = re.sub(r'\b\w{1,2}\b', '', text)

    # Remove words that are longer than twenty characters
    text = re.sub(r'\b\w{21,}\b', '', text)
    return text


def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens


def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    additional_stopwords = ['those', 'himself', 'more', 'not', 'ain', 'your', 'no', 'theirs', 'aren', 'he', 'should',
                            'under', 'doing', 'such', 've', 'if', 'was', "couldn't", 'are', "don't", 'hasn', 'then',
                            'haven', "should've", 'here', 'wouldn', "needn't", 'weren', "shan't", 'their', 'most',
                            'her', 'the', 'who', 'these', 's', 'our', 'any', 'after', 'won', 'themselves', 'in',
                            'needn', 'mightn', 'there', 'but', 'yourself', 'how', "shouldn't", 'as', 'herself', 'o',
                            'its', 'my', "weren't", 'had', "didn't", "isn't", 'when', 'it', 'which', 'did', 'me',
                            'once', 'hadn', 'his', 'itself', 'now', 'during', 'm', 'him', "you're", 'own', 't', "it's",
                            'with', 'y', 'nor', 'from', 'few', 'to', 'doesn', "doesn't", 'you', 'a', 'has', 'into',
                            'below', 'shan', 'i', 'an', "aren't", 'll', "you've", 'don', 'at', 'why', 'because', 'out',
                            'by', 'before', 'whom', 'other', 'yourselves', 'off', 'or', "that'll", 'does', 'didn',
                            'yours', 'above', "mightn't", 'so', 'too', "wasn't", "haven't", 'she', 'only', 'up', 'over',
                            'wasn', 'is', 'ours', 're', 'ma', 'against', 'both', 'couldn', 'than', 'through', 'mustn',
                            'will', "won't", 'hers', 'that', 'been', 'ourselves', 'while', 'shouldn', 'being', 'some',
                            'where', 'were', 'have', 'until', 'down', 'same', 'and', 'of', 'myself', "she's", 'isn',
                            'between', "mustn't", 'they', 'about', "you'd", 'all', 'for', 'just', 'on', 'am', 'each',
                            'very', 'we', 'having', 'further', 'what', 'be', 'them', 'can', 'again', "hasn't", 'do',
                            "wouldn't", "you'll", 'd', 'this', "hadn't"]

    tokens_without_stopwords = ' '.join(
        [token for token in tokens if token.lower() not in stop_words and token.lower() not in additional_stopwords])
    return tokens_without_stopwords


def stemming(text):
    ps = PorterStemmer()
    text = [ps.stem(word) for word in text]
    return text


def lemmatization(token_txt):
    wn = nltk.WordNetLemmatizer()
    text = ' '.join([wn.lemmatize(word) for word in token_txt])
    return text


def remove_numbers_with_text(words):
    return [word for word in words if not any(char.isdigit() for char in word)]
