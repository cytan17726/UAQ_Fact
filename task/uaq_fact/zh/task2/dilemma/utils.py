import collections
import re
import sys
import unicodedata

def arr_doc_to_target(doc):
    choice_letters = ["(A)", "(B)", "(C)", "(D)"]
    target_options = doc["target_options"]
    choices = doc["options"]
    idx = choices.index(target_options)
    target = choice_letters[idx]
    return target

def arr_doc_to_choice(doc):
    choice_letters = ["(A)", "(B)", "(C)", "(D)"]
    return choice_letters

def arr_doc_to_text(doc):
    '''Answer the given question in no more than one sentence.\nPlease keep your answer short and concise. Return ##None## if there is no suitable answer.\nQuestion: {{question}}\nAnswer:'''
    import pdb;pdb.set_trace()
