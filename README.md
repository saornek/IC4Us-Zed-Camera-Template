# IC4U's ZED Camera Template

This repository contains IC4U's object detection related projects code template. This code template can be used for building a custom object detector using the ZED 2i stereo camera, the ZED SDK, and a custom Pytorch weight.

[![Link to my YouTube video!](https://github.com/saornek/IC4Us-Zed-Camera-Template/blob/main/example.png?raw=true)](https://www.youtube.com/watch?v=0KgxXRvYVTQ)

To see more of IC4U, visit my [YouTube channel](https://www.youtube.com/@Selinoid).

## Getting Started
 - Get the latest [ZED SDK](https://www.stereolabs.com/developers/release/) and [pyZED Package](https://www.stereolabs.com/docs/app-development/python/install/)
 - Check the [Documentation](https://www.stereolabs.com/docs/object-detection/custom-od/)

 ## Setting Up 

 - Clone this repository into your ZED folder
```bash
git clone https://github.com/saornek/IC4Us-Zed-Camera-Template.git
```

 - Then clone Yolov5 into the current folder
```bash
git clone https://github.com/ultralytics/yolov5

# Install the dependencies if needed
cd yolov5
pip install -r requirements.txt
```

- Download a model file (or prepare your own) https://github.com/ultralytics/yolov5/releases

```bash
# Downloading by commmand line
wget https://github.com/ultralytics/yolov5/releases/download/v6.0/yolov5m.pt
```
- Prepare your Labels CSV file.

I chose to use a CSV file so, I could match the label ID of each detected object with its corresponding label name.
In this code, I researched what dataset yolov5 model uses. I saw that it used the MSCOCO dataset, so I created a CSV file with the object's IC4U required for its intelligent disobedience feature. 

You can adjust or create a CSV file according to your projects requirements.

A CSV file example format:
```csv
label_id, label
0, person
1, bicycle
2, car
```


## Run the code

*NOTE: The ZED 1 is not compatible with this module*

```
python detector.py --weights yolov5m.pt # [--img_size 512 --conf_thres 0.1 --svo path/to/file.svo]
```

## Training your own model

This sample can use any model trained with YOLOv5, including custom trained one. For a getting started on how to trained a model on a custom dataset with YOLOv5, see here https://docs.ultralytics.com/tutorials/train-custom-datasets/

I have prepared my datasets for IC4U's weights using [Roboflow](https://roboflow.com/). I highly recommend Roboflow for its simplicity and speed in managing and annotating datasets.

## Contributing
Contributions to this repository are welcome.  If you find any bugs or have suggestions for improvements, please feel-free to submit a pull request.

## Acknowledgments
Thank you to Stereolabs for providing the ZED SDK, the custom object detector tutorial and their endless support.

## Support
For any questions or support related to this library, you can contact me via the repository issues page.