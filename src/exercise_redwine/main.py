import argparse
import keras
from keras import layers
from pathlib import Path
from utils.main import add_new_line
import pandas as pd

def challenge_input_shape():
    print("# ------------------------- #");
    print("# (1) Input Shape Challenge #");
    print("# ------------------------- #")

    ROOT = Path(__file__).resolve().parent.parent.parent
    redwine = pd.read_csv(ROOT / "dataset" / "redwine.csv");
    redwine.head();

    input_shape = [redwine.shape[1] - 1];
    print(input_shape);

def challenge_define_linear_model():
    print("# ------------------------- #")
    print("# (2) Define a Linear Model #")
    print("# ------------------------- #")

    model = keras.Sequential([
        keras.Input(shape=[3]),
        layers.Dense(units=1)
    ]);

    print(model.summary());


def run_exercise_redwine():
    add_new_line(1);
    challenge_input_shape();
    add_new_line(1);
    challenge_define_linear_model();
    add_new_line(2);
