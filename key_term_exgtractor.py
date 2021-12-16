import spacy
import pandas as pd
import re


nlp = spacy.load("en_core_web_md")


def clean(text):

    text = re.sub(r"\n", "", text)

    return " ".join(text.split())


def get_key_terms(text):

    """
    Selects a list of key terms or noun phrases based on dependency parsing rules.
    """
    text = clean(text)

    doc = nlp(text)

    result = []

    df = []

    for i, token in enumerate(doc):

        df.append([token.text, token.dep_, token.head.text])

        if token.dep_ in ["dobj", "nsubj", "pobj"]:
            if doc[i - 1].dep_ in ["amod"]:
                result.append(doc[i - 1].text + " " + token.text)
            result.append(token.text)

        if token.dep_ in ["compound"]:
            if doc[i - 1].dep_ in ["amod"]:
                result.append(doc[i - 1].text + " " + token.text)
            result.append(token.text + " " + token.head.text)

        if token.dep_ == "ROOT":
            result.append(token.text)

    df = pd.DataFrame(df, columns=["text", "dep", "head"])

    return result, df

    result, df = get_key_terms(text)
