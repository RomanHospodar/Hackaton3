"""
Generate Sample Images for Test Set
===================================

This script populates the `test_set` folder with a number of sample images for testing purposes.
The generated images are basic and serve as placeholders.

Dependencies:
    - PIL (Pillow) for image manipulation.

"""

from PIL import Image, ImageDraw
from pathlib import Path


def generate_sample_images(path: Path, num_samples: int = 10):
    """Generate sample images for the test set.

    Args:
        path: The directory where the sample images will be saved.
        num_samples: The number of sample images to generate.
    """
    path.mkdir(parents=True, exist_ok=True)
    for i in range(num_samples):
        image = Image.new("RGB", (100, 100), color=(0, 128, 0))
        draw = ImageDraw.Draw(image)
        draw.text((10, 10), f"Sample {i + 1}", fill=(255, 255, 0))
        image.save(path / f"image_{i + 1}.png")


# Generate 10 sample images in the test_set directory
generate_sample_images(Path("test_set"))
