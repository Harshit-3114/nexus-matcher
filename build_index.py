#!/usr/bin/env python3
"""Build the FAISS index and metadata cache from the source CSV.

The app loads ``dataset/employee_index.faiss`` and ``dataset/employee_metadata.pkl``
at startup. Those two files are generated artefacts - this script rebuilds them
from ``dataset/cleaned_employee_llm_data.csv`` so the repository only has to
carry the source data.

    python build_index.py

The embeddings use ``all-MiniLM-L6-v2`` (384 dimensions) and the index is a
flat L2 index, which matches the metric the app expects: lower distance means
a closer match.
"""
from __future__ import annotations

import csv
import pickle
from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

DATASET_DIR = Path(__file__).parent / "dataset"
SOURCE_CSV = DATASET_DIR / "cleaned_employee_llm_data.csv"
INDEX_PATH = DATASET_DIR / "employee_index.faiss"
METADATA_PATH = DATASET_DIR / "employee_metadata.pkl"
MODEL_NAME = "all-MiniLM-L6-v2"


def load_profiles() -> list[dict]:
    """Read the synthetic expert profiles from the source CSV."""
    if not SOURCE_CSV.exists():
        raise SystemExit(
            f"Source dataset not found: {SOURCE_CSV}\n"
            "Expected a CSV with columns 'id' and 'text_for_llm'."
        )

    profiles: list[dict] = []
    with SOURCE_CSV.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            text = (row.get("text_for_llm") or "").strip()
            if not text:
                continue
            profiles.append({"id": int(row["id"]), "text_for_llm": text})

    if not profiles:
        raise SystemExit(f"No usable rows found in {SOURCE_CSV}")
    return profiles


def build() -> None:
    profiles = load_profiles()
    print(f"Loaded {len(profiles)} profiles from {SOURCE_CSV.name}")

    model = SentenceTransformer(MODEL_NAME)
    texts = [profile["text_for_llm"] for profile in profiles]
    vectors = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    vectors = np.asarray(vectors, dtype=np.float32)

    dimension = vectors.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)

    faiss.write_index(index, str(INDEX_PATH))
    with METADATA_PATH.open("wb") as handle:
        pickle.dump(profiles, handle)

    print(f"Wrote {INDEX_PATH.name}  ({index.ntotal} vectors, dim {dimension})")
    print(f"Wrote {METADATA_PATH.name} ({len(profiles)} records)")


if __name__ == "__main__":
    build()
