import argparse
import keras
from keras import layers
from exercise_redwine.main import run_exercise_redwine

parser = argparse.ArgumentParser();
parser.add_argument("--dataset", required=True, help="Dataset name");
args = parser.parse_args();

if args.dataset == "redwine":
    run_exercise_redwine();

model = keras.Sequential([
    keras.Input(shape=[3]),
    layers.Dense(units=1)
]);

print(model.summary());
