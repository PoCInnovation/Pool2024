from typing import Any

import torch as t

# Embedding taken from the previous exercise

dictionnary = {'good': 0, 'je': 1, 'suis': 2, 'bien': 3, 'bad': 4, 'fatigué': 5, 'nice': 6, '<eos>' : 7, '<sos>' : 8}

embbedding = t.tensor([
    [-2.7545,  3.5838, -1.8906, -0.8958, -2.6207,  0.7260, -0.8996, 0, 0],
    [-2.6029, -3.0760,  1.6500, -0.5518, -2.1129,  3.0733, -0.5555, 0, 0]
])

def one_hot_to_vec(hot_vector: t.Tensor):
    return t.sum(embbedding * hot_vector, dim=1)

def one_hot_to_word(hot_vector: t.Tensor):
    return list(dictionnary.keys())[t.argmax(hot_vector)]

def word_to_one_hot(word : t.Tensor):
    res = t.zeros(len(dictionnary))
    res[dictionnary[word]] = 1
    return res

def word_to_vec(word : t.Tensor):
    return one_hot_to_vec(word_to_one_hot(word))


class RNN_CELL:

    def __init__(self, hidden_size : int, entry_size : int) -> None:
        
        self.__entry_size  : int    = entry_size
        self.__hidden_size : int    = hidden_size
        
        # weights
        self.__w_hh : t.Tensor = t.empty(self.__hidden_size, self.__hidden_size, requires_grad=True)
        t.nn.init.xavier_uniform_(self.__w_hh)
        self.__w_hx : t.Tensor = t.empty(self.__hidden_size, self.__entry_size, requires_grad=True)
        t.nn.init.xavier_uniform_(self.__w_hx)

        self.__b_hh : t.Tensor = t.zeros(self.__hidden_size, 1, requires_grad=True)
        self.__b_hx : t.Tensor = t.zeros(self.__hidden_size, 1, requires_grad=True)

    @property
    def weights(self):
        return [ self.__w_hx, self.__w_hh, self.__b_hx, self.__b_hh ]
        
    def forward(self, context : t.Tensor, x : t.Tensor) -> t.Tensor:

        hidden = t.matmul(self.__w_hh, context) + self.__b_hh
        value = t.matmul(self.__w_hx, x) + self.__b_hx
        return t.tanh(hidden + value)
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.forward(*args, **kwds)


def flatten(x : list[list]):
    return [ e for row in x for e in row ]

def prepare_data2(filename : str):

    propositions = open(filename, "r").read().split("\n")

    encoded_sequences = []

    for sentence in propositions:
        tok_seq = sentence.split(".")
        result = tok_seq[1].strip()
        seq = tok_seq[0].strip().split(" ")
        x = []
        for token in seq:
            res = t.zeros(len(dictionnary))
            res[dictionnary[token]] = 1
            x.append(res)
        res = t.zeros(len(dictionnary))
        res[dictionnary[result]] = 1

        encoded_sequences.append((t.stack(x), res))

    return encoded_sequences, dictionnary

# dataset, dictionnary = prepare_data2("data")
# t.autograd.set_detect_anomaly(True)

# # Sizes
# entry_size = 2
# hidden_size = 4
# output_size = len(dictionnary)

# # Traning paramter
# epochs  = 10
# lr      = 0.01

# # Model & training tools
# model = RNN_CELL(hidden_size, entry_size)
# w_yh = t.empty(output_size, hidden_size, requires_grad=True)
# t.nn.init.xavier_uniform_(w_yh)
# optimizer = t.optim.Adam(model.weights + [w_yh], lr)
# loss_fct = t.nn.MSELoss()

# for i in range(epochs):

#     #  The context is reinitialised each time
#     avg_loss = 0
#     for seq, y in dataset:

#         optimizer.zero_grad()
#         context = t.zeros(hidden_size, 1)

#         # encode the entry
#         for token in seq:
#             context = model(context, one_hot_to_vec(token).unsqueeze(1))

#         # decode
#         context = model(context, word_to_vec("<sos>").unsqueeze(1))
#         res = t.matmul(w_yh, context)

#         loss = loss_fct(res, y.unsqueeze(1))
#         avg_loss += loss.item()
#         loss.backward(retain_graph=True)

#         optimizer.step()

#     print("Avg_loss:", avg_loss / len(dataset))


# # test
# for seq, y in dataset:

#     context = t.zeros(hidden_size, 1)

#     # encode the entry
#     for token in seq:
#         print(one_hot_to_word(token), end=" ")
#         context = model(context, one_hot_to_vec(token).unsqueeze(1))

#     context = model(context, word_to_vec("<sos>").unsqueeze(1))
#     print(one_hot_to_word(t.matmul(w_yh, context)))

