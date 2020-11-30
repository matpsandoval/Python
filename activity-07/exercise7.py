import os

file_dir = os.path.dirname(__file__)
file_signal = open(os.path.join(file_dir, "signal.txt"))
file_network = open(os.path.join(file_dir, "networks.txt"))

signal = file_signal.readlines()
network = file_network.readlines()

