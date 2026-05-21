from __future__ import annotations

import json
import random
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score


def set_seed(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def save_json(obj, path: str | Path) -> None:
    Path(path).write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")


def compute_metrics(y_true: list[int], y_pred: list[int]) -> dict[str, float]:
    return {
        "acc": float(accuracy_score(y_true, y_pred)),
        "macro_f1": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
    }


def plot_curves(history: list[dict], output_path: str | Path) -> None:
    df = pd.DataFrame(history)
    plt.figure(figsize=(9, 5))
    if "train_loss" in df:
        plt.plot(df["epoch"], df["train_loss"], label="train_loss")
    if "val_loss" in df:
        plt.plot(df["epoch"], df["val_loss"], label="val_loss")
    if "val_acc" in df:
        plt.plot(df["epoch"], df["val_acc"], label="val_acc")
    if "val_macro_f1" in df:
        plt.plot(df["epoch"], df["val_macro_f1"], label="val_macro_f1")
    plt.xlabel("epoch")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def plot_confusion_matrix(
    y_true: list[int],
    y_pred: list[int],
    class_names: list[str],
    output_path: str | Path,
) -> None:
    cm = confusion_matrix(y_true, y_pred, labels=list(range(len(class_names))))
    plt.figure(figsize=(8, 7))
    plt.imshow(cm)
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.xticks(range(len(class_names)), class_names, rotation=45, ha="right")
    plt.yticks(range(len(class_names)), class_names)
    for i in range(len(class_names)):
        for j in range(len(class_names)):
            plt.text(j, i, str(cm[i, j]), ha="center", va="center")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
