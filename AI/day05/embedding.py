import torch as t
from matplotlib import pyplot as plt

#embedding

class Embedding:

    # this model is based on skip-gram #

    def __init__(self, dict_size, dim = 2) -> None:
        self.__vectors = t.empty(dim, dict_size, requires_grad=True)
        t.nn.init.xavier_uniform(self.__vectors)
        self.__dict_size = dict_size

        self.__model_weights = t.empty(dim, dict_size, requires_grad=False)
        t.nn.init.xavier_normal(self.__model_weights)

    def from_one_hot(self, vector : t.Tensor):

        assert (vector.size() > self.__dict_size), "Invalid Vector"

        return self.__vectors * vector
    
    def train(self, data : t.Tensor, epochs : int, dictionnary : dict):

        a = t.optim.Adam([self.__model_weights, self.__vectors], lr=0.01)

        loss = t.nn.CrossEntropyLoss()

        figure, axis = plt.subplots(2, 5) 

        for i in range(epochs):
            print(i / epochs,"epochs")
            for x, y in data:
                y_pred = t.softmax(t.matmul(t.matmul(self.__vectors, x), self.__model_weights), 0)
                a.zero_grad()
                res = loss(y_pred, y)
                res.backward()
                a.step()

            if (not(i % 10)):
                axis[(i // 10) // 5, (i // 10) % 5].scatter(self.__vectors.detach().numpy()[0], self.__vectors.detach().numpy()[1])
                for key, value in dictionnary.items():
                    axis[(i // 10) // 5, (i // 10) % 5].annotate(key, (self.__vectors.detach().numpy()[0][value], self.__vectors.detach().numpy()[1][value]))
                # plt.show()
                axis[(i // 10) // 5, (i // 10) % 5].set_title("Epochs:" + str(i))

        # plt.scatter(self.__vectors.detach().numpy()[0], self.__vectors.detach().numpy()[1])
        # for key, value in dictionnary.items():
        #     plt.annotate(key, (self.__vectors.detach().numpy()[0][value], self.__vectors.detach().numpy()[1][value]))
        plt.show()

        print(self.__vectors)
        print(dictionnary)
            

def flatten(x : list[list]):
    return [ e for row in x for e in row ]

def prepare_data(filename : str):

    propositions = open(filename, "r").read().split("\n")
    dictionnary = {}
    size = 0
    i = 0

    for sentence in propositions:
        x, y = tuple(sentence.split("."))
        if not(y.strip() in dictionnary):
            dictionnary[y.strip()] = i
            i += 1
        size += 1

        for token in x.split(" "):
            if not(token in dictionnary):
                dictionnary[token] = i
                i += 1
            size += 1

    encoded = []

    for sentence in propositions:
        for token in flatten([ token.strip().split(" ") for token in sentence.split(".")]):
            res = t.zeros(len(dictionnary))
            res[dictionnary[token]] = 1
            encoded.append(res)

    return t.stack(encoded).as_strided((size - 1, 2, len(dictionnary)), (len(dictionnary), len(dictionnary), 1)), dictionnary

# data, dictionnary = prepare_data("data")

# embeddings = Embedding(len(dictionnary), 2)

# embeddings.train(data, 100, dictionnary)


