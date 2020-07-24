from model import EncoderRNN, AttnDecoderRNN
from evaluation import evaluateRandomly
import training

import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

hidden_size = 256
encoder1 = EncoderRNN(training.input_lang.n_words, hidden_size).to(device)
attn_decoder1 = AttnDecoderRNN(hidden_size, training.output_lang.n_words,
                               dropout_p=0.1).to(device)

training.trainIters(encoder1, attn_decoder1, 35000, print_every=5000)
evaluateRandomly(encoder1, attn_decoder1)
