import eng_to_ipa as ipa

def convert_to_ipa(phrase, specialized=True):
    """Takes a piece of text and transibes it to the 
    International Phonetic Alphabet (IPA).

    Note: some changes to transcription were made depending on the 
    system, to not have these changed, set <specialized> to false.
    """
    conversions = {
        "oʊ": "ow",
        "eɪ": "ej",
        "ɔɪ": "oj",
        "aɪ": "aj",
        "aʊ": "aw"
    }
    phrase = ipa.convert(phrase)
    for key in conversions:
        if key in phrase:
            phrase = phrase.replace(key, conversions[key])
    return phrase