from __future__ import annotations

import random
import zipfile
from pathlib import Path
from typing import Iterable

from PIL import Image
from torch.utils.data import Dataset, Subset
from torchvision import transforms


IMG_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def _extract_zip_if_needed(data_dir: str | Path, cache_dir: str | Path = ".cache_data") -> Path:
    data_path = Path(data_dir)
    if data_path.is_file() and data_path.suffix.lower() == ".zip":
        cache_path = Path(cache_dir) / data_path.stem
        marker = cache_path / ".extracted"
        if not marker.exists():
            cache_path.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(data_path, "r") as zf:
                zf.extractall(cache_path)
            marker.write_text("ok", encoding="utf-8")
        return cache_path
    return data_path


def _find_class_dirs(root: Path) -> dict[str, Path]:
    class_dirs: dict[str, Path] = {}
    for path in root.rglob("*"):
        if not path.is_dir():
            continue
        has_image = any(child.is_file() and child.suffix.lower() in IMG_EXTENSIONS for child in path.iterdir())
        if has_image:
            class_dirs[path.name.lower()] = path
    return class_dirs


def build_transforms(img_size: int, augment: bool = False):
    if augment:
        return transforms.Compose(
            [
                transforms.Resize((img_size, img_size)),
                transforms.RandomHorizontalFlip(p=0.5),
                transforms.RandomRotation(degrees=8),
                transforms.ColorJitter(brightness=0.15, contrast=0.15, saturation=0.10),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ]
        )

    return transforms.Compose(
        [
            transforms.Resize((img_size, img_size)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )


class SmartCampusIndoorDataset(Dataset):
    def __init__(
        self,
        data_dir: str | Path,
        classes: Iterable[str] | None = None,
        img_size: int = 224,
        augment: bool = False,
        max_per_class: int | None = None,
    ):
        self.root = _extract_zip_if_needed(data_dir)
        if not self.root.exists():
            raise FileNotFoundError(f"Data directory not found: {self.root}")

        class_dirs = _find_class_dirs(self.root)
        selected = [c.lower() for c in classes] if classes else sorted(class_dirs.keys())

        missing = [c for c in selected if c not in class_dirs]
        if missing:
            available = ", ".join(sorted(class_dirs.keys())[:50])
            raise ValueError(
                f"Missing class directories: {missing}. "
                f"Available examples: {available}"
            )

        self.classes = selected
        self.class_to_idx = {name: idx for idx, name in enumerate(self.classes)}
        self.samples: list[tuple[Path, int]] = []

        rng = random.Random(42)
        for class_name in self.classes:
            image_paths = [
                p
                for p in class_dirs[class_name].iterdir()
                if p.is_file() and p.suffix.lower() in IMG_EXTENSIONS
            ]
            image_paths = sorted(image_paths)
            if max_per_class is not None:
                rng.shuffle(image_paths)
                image_paths = image_paths[:max_per_class]
            for p in image_paths:
                self.samples.append((p, self.class_to_idx[class_name]))

        if not self.samples:
            raise RuntimeError(f"No images found under {self.root}")

        self.transform = build_transforms(img_size=img_size, augment=augment)

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, index: int):
        path, label = self.samples[index]
        image = Image.open(path).convert("RGB")
        return self.transform(image), label


def stratified_split_indices(
    dataset: SmartCampusIndoorDataset,
    val_ratio: float = 0.15,
    test_ratio: float = 0.15,
    seed: int = 42,
) -> tuple[list[int], list[int], list[int]]:
    rng = random.Random(seed)
    by_class: dict[int, list[int]] = {}
    for idx, (_, label) in enumerate(dataset.samples):
        by_class.setdefault(label, []).append(idx)

    train_idx, val_idx, test_idx = [], [], []
    for _, indices in by_class.items():
        rng.shuffle(indices)
        n = len(indices)
        n_test = max(1, int(n * test_ratio))
        n_val = max(1, int(n * val_ratio))
        test_idx.extend(indices[:n_test])
        val_idx.extend(indices[n_test : n_test + n_val])
        train_idx.extend(indices[n_test + n_val :])

    rng.shuffle(train_idx)
    rng.shuffle(val_idx)
    rng.shuffle(test_idx)
    return train_idx, val_idx, test_idx


def make_splits(
    dataset: SmartCampusIndoorDataset,
    val_ratio: float = 0.15,
    test_ratio: float = 0.15,
    seed: int = 42,
):
    train_idx, val_idx, test_idx = stratified_split_indices(dataset, val_ratio, test_ratio, seed)
    return Subset(dataset, train_idx), Subset(dataset, val_idx), Subset(dataset, test_idx)
