PHONEME_SINGLE_CONSONANT_INITIAL = ["k", "kh", "ng", "c", "ch", 
                                    "s", "j", "d", "t", "th", 
                                    "n", "b", "p", "ph", "f", 
                                    "m", "r", "l", "w", "h", "z"
]

PHONEME_SINGLE_CONSONANT_FINAL = ["k^", "ng^", "t^", "j^", 
                                  "n^", "p^", "m^", "w^"
]

PHONEME_DOUBLE_CONSONANT = ["pr", "pl", "phr", "phl", "tr", 
                            "thr", "kr", "kl", "kw", "khr",
                            "khl", "khw"
]

PHONEME_SINGLE_VOWEL = ["i", "ii", "v", "vv", "u", "uu",
                        "e", "ee", "q", "qq", "o", "oo",
                        "x", "xx", "a", "aa", "@", "@@",
                        "ia", "iia", "va", "vva", "ua", "uua"
]

PHONEME_SILENT = [""]

PHONEMES = []
PHONEMES.extend(PHONEME_SILENT)
PHONEMES.extend(PHONEME_SINGLE_CONSONANT_INITIAL)
PHONEMES.extend(PHONEME_SINGLE_CONSONANT_FINAL)
PHONEMES.extend(PHONEME_DOUBLE_CONSONANT)
PHONEMES.extend(PHONEME_SINGLE_VOWEL)

print(PHONEMES)

PHONEME_MAP = {v: k for k, v in enumerate(PHONEMES)}

LEN_PHONEME_MAP = len(PHONEME_MAP)

print(PHONEME_MAP)

input_phoneme = ["k", "k", "ee", "d"]
feature = list(map(lambda x: PHONEME_MAP[x], input_phoneme))

print(feature)