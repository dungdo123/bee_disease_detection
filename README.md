
## <div align="center">Description</div>
YOLOv8 is a cutting-edge, state-of-the-art (SOTA) model that builds upon the success of previous YOLO versions and introduces new features and improvements to further boost performance and flexibility. YOLOv8 is designed to be fast, accurate, and easy to use, making it an excellent choice for a wide range of object detection and tracking, instance segmentation, image classification and pose estimation tasks.

<img width="100%" src="https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/yolo-comparison-plots.png"></a>
Source: [YOLOv8](https://github.com/ultralytics/ultralytics)

## <div align="center">Model Architecture</div>

<img width="100%" src="https://github.com/dungdo123/bee_disease_detection/raw/57389d049c12c963b219f55d54625b4687d08abd/resource/yolov8_architecture.png"></a>

## <div align="center">Usage</div>
<details open>
<summary>Input</summary>

```bash
Input: image_shape = (3,640,640)
```

</details>

<details open>
<summary>Output</summary>

```bash
Output: output_tensor = float32[1,11,8400]
        batch=1
        number_of_classes=7
        maximum_number_of_detected_object=8400
        class_names=["Larva_Normal", "Larva_mite", "Larva_Gypsum", "Larva_Butterfly", "Insect_normal", "Insect_mite", "insect_wing_crippled_virus_infection"]
```

</details>

<details open>
<summary>Task</summary>

```bash
Model Task: Object Detection
```

</details>

## <div align="center">Training</div>
<details open>
<summary>Training Dataset</summary>
The main issue of training on the "Bee_Disease_Detection" dataset is imbalanced in the classes. To Overcome this problem, we need to do balancing the distributions of the dataset which can be done by Oversampling the minority classes.

```bash
Number_of_Original_Image = 32628
Number_of_Augmented_Image = 7267
Total_Training_Image = Number_of_Original_Image + Number_of_Augmented_Image
Number_of_Eval_Image = 16000
```

</details>

<details open>
<summary>Training Parameters</summary>

```bash
epochs=20
batch_size=32
learning_rate=0.01
input_size=640
model_type='yolov8m'
```

</details>

## <div align="center">Evaluation</div>

<details open>
<summary>Training Graph</summary>

```bash
Number_of_Eval_Image = 16000
Total_Training_Image = 39895
```
Training Graph
<img width="100%" src="https://github.com/dungdo123/bee_disease_detection/raw/2dff1f4e61e8e6bd1776f197da6b091f2b9bf61f/resource/training_graph.png"></a>

</details>

<details open>
<summary>Performance on Test Set</summary>

```bash
Number_of_Test_Image = 32000
```

PR curve on Test Set
<img width="100%" src="https://github.com/dungdo123/bee_disease_detection/raw/8bd9d12e8afd16d2ce9b1f236615cc8fc289fdae/resource/pr_curve_test_set.png"></a>

Confusion Matrix on Test Set
<img width="100%" src="https://github.com/dungdo123/bee_disease_detection/raw/8bd9d12e8afd16d2ce9b1f236615cc8fc289fdae/resource/confusion_matrix_on_testset.png"></a>

</details>