from model import EncoderRNN, AttnDecoderRNN
from evaluation import evaluateRandomly
import training
# import argparse

import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

n_iters = int(input('num_iters:'))
print_every = int(input('print_every:'))
learning_rate = float(input('learning_rate:'))

hidden_size = 256
encoder1 = EncoderRNN(training.input_lang.n_words, hidden_size).to(device)
attn_decoder1 = AttnDecoderRNN(hidden_size, training.output_lang.n_words,
                               dropout_p=0.1).to(device)

# ap = argparse.ArgumentParser()
# ap.add_argument("-n", "--num_iters", required=True,
#                 help="Number of iterations")
# ap.add_argument("-p", "--print_every", required=True, help="Print every")
# ap.add_argument("-l", "--learning_rate", required=True, help="Learning rate")
# args = vars(ap.parse_args())

# training.trainIters(encoder1, attn_decoder1,
#                     n_iters=args['num_iters'],
#                     print_every=args['print_every'],
#                     learning_rate=args['learning_rate'])

training.trainIters(encoder1, attn_decoder1, n_iters, print_every,
                    learning_rate)
evaluateRandomly(encoder1, attn_decoder1)
