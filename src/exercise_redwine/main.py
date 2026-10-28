from pathlib import Path
from utils.main import add_new_line
import pandas as pd

def challenge_input_shape():
    ROOT = Path(__file__).resolve().parent.parent.parent
    redwine = pd.read_csv(ROOT / "dataset" / "redwine.csv");
    redwine.head();

    print("# ------------------------- #");
    print("# (1) Input Shape Challenge #");
    print("# ------------------------- #")
    input_shape = [redwine.shape[1] - 1];
    print(input_shape);


def run_exercise_redwine():
    add_new_line(1);
    challenge_input_shape();
    add_new_line(1);
