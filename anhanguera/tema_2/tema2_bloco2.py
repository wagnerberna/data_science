# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

file = "C:/0-BK/0-Vscode/data_science/tema2_bloco2/chamados.csv"

data = np.genfromtxt(file, delimiter=";", names=True, deletechars=" !#$%&'()*+, -./:;<=>?@[\\]^{|}~ï»¿")

data

time = data["tempo"]

hours = data["tempo"] / 60

data["atendente"]

plt.scatter(data["atendente"], data["chamados"])

plt.bar(data["atendente"], data["chamados"])
