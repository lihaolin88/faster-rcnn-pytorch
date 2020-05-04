# A PyTorch implementation of Faster R-CNN
This implementation of Faster R-CNN network based on PyTorch 1.0 branch of [jwyang/faster-rcnn.pytorch](https://github.com/jwyang/faster-rcnn.pytorch/tree/pytorch-1.0). However, there are some differences in this version:
* Full performance on CPU (ROI Pooling, ROI Align, NMS implemented on C++ [*thanks, PyTorch team*])
* Multi image batch training based on `collate_fn` function of PyTorch
* Using models from model zoo of torchvision as backbones (VGG16, ResNet[all versions] available)
* More friendly CLI for training, test or detect
* Add simple visualization of training process
* Add abstractions for easy add new datasets, backbones, visualize tools
### TODOs:
- [x] Add support for multi GPU training
- [x] Add another pooling layers (ROI Align)
- [x] Add paramater for color mode of pretrained weights
- [ ] Add config load file parameter (with refresh already defined parameters)
- [ ] Add webcam mode of detection
- [ ] Add approximation line in standart plotter
- [ ] Add PyTorch 1.5.0 support
### Tutorial:
[Blog](http://www.telesens.co/2018/03/11/object-detection-and-classification-using-r-cnns) by [ankur6ue](https://github.com/ankur6ue)
### Benchmarking
|**Learning rate**: 0.001 (1e-3)|**LR Decay**: 5|**Optimizer**: SGD|
|-----------|------------|------------|

All results were obtained on *Pascal VOC 2007* (min scale = 600, **ROI Pool**) with *NVIDIA GeForce GTX1060 (6GB)*:
|Backbone|Batch size|Max epoch|mAP|
|-------|-------|-------|-------|
|VGG16|1|6|70.9%|
|ResNet50|2|7|73.1%|
|ResNet101|1|6|74.5%|

---
## Preparation
Clone this repo and create `data` folder in it:
```
git clone https://github.com/loolzaaa/faster-rcnn-pytorch.git
cd faster-rcnn-pytorch && mkdir data
```

### Prerequisites
- Python 3.5+
- PyTorch 1.3+
- CUDA 8+
- Other libraries in [this gist (Conda environment)](https://gist.github.com/loolzaaa/fdbc406d281db9dc0a723536a41679d6)

### Compilation
Compile all python extensions (NMS, ROI layers) for CPU and CUDA with next commands:
```
cd lib
python setup.py develop
```

### Pretrained model
1. [Download](https://drive.google.com/open?id=1n2hWpTEWe3LwfOYq0VUslok-EmdqrMQP) caffe BGR pretrained models
2. Put them into `data/pretrained_model/`

**NOTE:** Please, remember that this network use caffe (*BGR color mode*) pretrained model **by default**. If you want to use PyTorch pretrained models, you must specify *RGB* color mode, image range = [0, 1], *mean = [0.485, 0.456, 0.406]* and *std = [0.229, 0.224, 0.225]* in additional parameters for run script. For example:
```
python run.py train ............. -ap color_mode=RGB image_range=1 mean="[0.485, 0.456, 0.406]" std="[0.229, 0.224, 0.225]"
```

### Data preparation
Prepare dataset as described [here](https://github.com/rbgirshick/py-faster-rcnn#beyond-the-demo-installation-for-training-and-testing-models) for Pascal VOC.
*Actually, you can use any dataset. Just download it and create softlinks in `library_root/data` folder.*

You can, *but not necessary*, specify directory name for dataset relative `./data` folder in addtional parameters for run script. For example:
- `python run.py train ............. --add_params devkit_path=VOC_DEVKIT_PATH` => ./data/VOC_DEVKIT_PATH
- `python run.py train ............. -ap data_path=COCO2014` => ./data/COCO2014

**NOTE:** Name of the parameter is different for datasets (`devkit_path` for Pascal VOC, `data_path` for COCO, etc.)

**WARNING! If you change any parameter of some dataset, you must remove cache files for this dataset in `./data/cache` folder!**

---
## Usage:
All interaction with the library is done through a `run.py` script. Just run:
```
python run.py -h
```
and follow help message.

### Train
To train Faster R-CNN network with ResNet50 backbone on Pascal VOC 2012 trainval dataset in 10 epochs, run next:
```
python run.py train --net resnet 50 --dataset voc_2012_trainval --total-epoch 10 --cuda
```
Some parameters saved in [default config file](https://github.com/loolzaaa/faster-rcnn-pytorch/blob/master/lib/config.py), another parameters has default values.

For more information about train script, you need to run `python run.py train -h` and follow help message.

### Test
If you want to evlauate the detection performance of above trained model, run next:
```
python run.py test --net resnet 50 --dataset voc_2012_test --epoch $EPOCH --cuda
```
where *$EPOCH* is early saved checkpoint epoch (maximum =10 for training example above).

For more information about test script, you need to run `python run.py test -h` and follow help message.

### Detect
If you want to run detection on your own images with above trained model:
* Put your images in `data/images` folder
* Run script:
```
python run.py detect --net resnet 50 --dataset voc_2012_test --epoch $EPOCH --cuda --vis
```
where *$EPOCH* is early saved checkpoint epoch (maximum =10 for training example above).

After detect, you will find the detection results in folder `dataT/images/result` folder.

For more information about detect script, you need to run `python run.py detect -h` and follow help message.
