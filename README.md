# ssd.pytorchでオリジナルデータセットを使えるようにする

## データセットの階層構造

```sh:
tree ~/ssd-pytorch/data/coco_helmet -L 2
data/coco_helmet
├── READ_ME.txt
├── annotations
│   ├── all.json
│   ├── train.json
│   └── val.json
├── coco_labels_helmet.txt
└── images
    ├── all
    ├── train
    └── val
```


## 実行例

```sh:
python train.py --cuda False --num_workers 0 --dataset COCO --dataset_root ~/ssd-pytorch/data/coco_helmet --org_ds True
```
