import argparse
import keras
from keras import layers

parser = argparse.ArgumentParser();
parser.add_argument("--dataset", required=True, help="Dataset name");
args = parser.parse_args();
print(args.dataset)

model = keras.Sequential([
    keras.Input(shape=[3]),
    layers.Dense(units=1)
]);

print(model.summary());
