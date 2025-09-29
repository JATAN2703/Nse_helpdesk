import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

def extract_text(file):
    pdf_file = open(file, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ""

    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()

    pdf_file.close()
    return text

def summarize(text):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]

    frequency = nltk.FreqDist(words)
    sentences = nltk.sent_tokenize(text)
    sentence_scores = {}

    for sentence in sentences:
        for word, freq in frequency.items():
            if word in sentence.lower():
                if sentence in sentence_scores:
                    sentence_scores[sentence] += freq
                else:
                    sentence_scores[sentence] = freq

    sum_values = 0
    for sentence in sentence_scores:
        sum_values += sentence_scores[sentence]

    average = int(sum_values / len(sentence_scores))

    summary = ''
    for sentence in sentences:
        if sentence in sentence_scores and sentence_scores[sentence] > (1.2 * average):
            summary += " " + sentence
    return summary

pdf_file = "trial.pdf"
text = extract_text(pdf_file)
summary = summarize(text)
print(summary)