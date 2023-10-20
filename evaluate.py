"""
Evaluate Test Set Predictions
=============================

This script reads images from the `test_set` folder and generates a CSV file named `test_preds.csv`,
which contains the predictions for these images.

Participants should implement their prediction logic in the function `user_defined_predict_function`.

Dependencies:
    - PIL (Pillow) for image reading.
    - csv module for generating CSV output.
"""

import csv
import random
import tensorflow as tf
from pathlib import Path
from PIL import Image
from typing import Any
import glob
import numpy as np
import os
import Unzip

Unzip.unzip_model()
model = Path("Model/MyModel")  # pretrained model path
loaded_model = tf.keras.models.load_model(model)                                        # load pretrained model

def user_defined_predict_function(image: Image.Image) -> Any:
    """
    Implement your model's prediction logic here.

    Args:
        image: PIL Image object.

    Returns:
        prediction: Replace `Any` with the type of prediction your model will return. E.g., int or float.
    """
    # TODO: Add your model's prediction logic here

    image_list = []                                                                     # put file into list, if not RGB, then change, translate to .jpg format
    if image.mode != 'RGB':
        image = image.convert('RGB')
    imjpg = image.save('File.jpg')
    imjpg = Image.open('File.jpg')
    image_list.append(imjpg)

    validation_batch = np.stack([np.array(img.resize((400, 400)))                       # prepare validation_batch with files
                                 for img in image_list])

    pred_probs = loaded_model.predict(validation_batch)                                 # predict the probabilities of validation_batch
    result = 0
    if pred_probs[0][0] < pred_probs[0][1]:                                             # results is set as non solar, if probability is higher, then change to solar
        result = 1
    if os.path.isfile('File.jpg'):                                                      # remove temporary .jpg file
        os.remove('File.jpg')
    return result  # This line is only a placeholder                                    # return result , 0=non_solar, 1=solar


def make_predictions(test_folder: Path, output_file: Path) -> None:
    """
    Generate a CSV file with predictions for images in the test set.

    Args:
        test_folder: The directory containing the test images.
        output_file: The path for the CSV file to write the predictions.
    """

    with open(output_file, "w", newline='') as csvfile:
        fieldnames = ["id", "pred"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for image_path in test_folder.glob("*.png"):
            image_id = image_path.stem
            image = Image.open(image_path)

            # Do NOT modify this line. Replace the logic inside `user_defined_predict_function` instead.
            prediction = user_defined_predict_function(image)

            writer.writerow({"id": image_id, "pred": prediction})


# DO NOT MODIFY THIS SECTION
# Run the function to generate test_preds.csv
if __name__ == "__main__":
    test_folder_path = Path("test_set")
    output_file_path = Path("test_preds.csv")
    make_predictions(test_folder_path, output_file_path)
