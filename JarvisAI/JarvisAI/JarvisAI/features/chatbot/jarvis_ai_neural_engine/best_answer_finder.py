def find_best(text, answers_dict, question_answering):
    def calculate_weight(d):
        weights = {}
        for k, v in d.items():
            max_ = 0
            answer = None
            if k == 'conversation':
                if len(v) == 0:
                    continue
                d[k] = [question_answering(question=text, context=f'{v[0]}')]
                v = d[k]
            for i in v:
                if i['score'] > max_:
                    max_ = i['score']
                    answer = i['answer']
            # print(f"{k}: {answer}: {max_}")
            weights[k] = (answer, max_)
        return weights

    weights = calculate_weight(answers_dict)
    weights_of_all_models = {k: v for k, v in sorted(weights.items(), key=lambda item: item[1][1], reverse=True)}

    suggested_answer = question_answering(question=text, context=f'{weights["conversation"]}'
                                                                 f'{weights["general_knowledge"]} '
                                                                 f'{weights["neural_search_engine"]} '
                                                                 f'{weights["wikipedia_result"]}')
    # print("weights_of_all_models-\n", weights_of_all_models)
    # print("suggested_answer-\n", suggested_answer)
    return weights_of_all_models, suggested_answer
