from __future__ import annotations

from pathlib import Path

file_dir_path = Path(__file__).parent
example_dir_name = "scripts"
gallery_dir = file_dir_path / "generated" / example_dir_name
examples_dir = file_dir_path / example_dir_name
examples_subdirs = [
    subdir.name
    for subdir in examples_dir.iterdir()
    if (examples_dir / subdir).is_dir()
    and (examples_dir / subdir / "README.md").is_file()
]

conf = {
    "examples_dirs": [examples_dir / subdir for subdir in examples_subdirs],
    "gallery_dirs": [gallery_dir / subdir for subdir in examples_subdirs],
}
