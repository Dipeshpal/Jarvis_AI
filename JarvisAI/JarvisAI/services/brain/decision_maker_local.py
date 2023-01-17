import shutup

shutup.please()
from transformers import logging

logging.set_verbosity_error()

from transformers import AutoTokenizer, AutoModel
from torch.nn import functional as F

tokenizer = AutoTokenizer.from_pretrained('deepset/sentence_bert')
model = AutoModel.from_pretrained('deepset/sentence_bert')


def make_decision(classes_list, input_string):
    # classes = "'" + "', '".join(classes_list) + "'"
    sentence = '"' + input_string + '" in which class this belongs to out of following'
    labels = classes_list

    # run inputs through model and mean-pool over the sequence
    # dimension to get sequence-level representations
    inputs = tokenizer.batch_encode_plus([sentence] + labels,
                                         return_tensors='pt',
                                         pad_to_max_length=True)
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']
    output = model(input_ids, attention_mask=attention_mask)[0]
    sentence_rep = output[:1].mean(dim=1)
    label_reps = output[1:].mean(dim=1)

    # now find the labels with the highest cosine similarities to
    # the sentence
    similarities = F.cosine_similarity(sentence_rep, label_reps)
    closest = similarities.argsort(descending=True)
    for ind in closest:
        # print(f'label: {labels[ind]} \t similarity: {similarities[ind]}')
        break
    return labels[ind]


if __name__ == "__main__":
    ans = make_decision(
        ['asking date', 'asking time', 'tell me joke', 'tell me news', 'asking weather', 'tell me about',
         'open website', 'play on youtube', 'send whatsapp message', 'send email',
         'greet and hello hi kind of things, general check in', 'goodbye', 'take screenshot', 'click photo',
         'download youtube video', 'covid cases', 'play games', 'places near me', 'i am bored', 'volume control'],
        "'how are you' in which class this belongs to out of following")

    print(ans)
