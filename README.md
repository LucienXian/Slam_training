# Stereo matching



计算深度的公式：Z = baseline * f / (d + doffs)

## Code

代码来源[StereoMathingV2](https://github.com/LucienXian/Slam_training/blob/master/StereoMatching_v2/StereoMatchin.py)

## 图像集

来源：http://vision.middlebury.edu/stereo/data/scenes2014/

## ssd效果

* Piano

<p float="left">
  <img src="https://github.com/LucienXian/Slam_training/blob/master/MiddEval3/trainingQ/Piano/im0.png" width="260" />
  <img src="https://github.com/LucienXian/Slam_training/blob/master/MiddEval3/trainingQ/Piano/im1.png" width="260" /> 
  <img src="https://github.com/LucienXian/Slam_training/blob/master/res_ssd/Piano.png" width="260" />
</p>

* Playtable

<p float="left">
  <img src="https://github.com/LucienXian/Slam_training/blob/master/MiddEval3/trainingQ/PlaytableP/im0.png" width="260" />
  <img src="https://github.com/LucienXian/Slam_training/blob/master/MiddEval3/trainingQ/PlaytableP/im1.png" width="260" /> 
  <img src="https://github.com/LucienXian/Slam_training/blob/master/res_ssd/PlaytableP.png" width="260" />
</p>



## ncc效果

>  相比ssd，ncc运行效率较慢

* Piano

<p float="left">
  <img src="https://github.com/LucienXian/Slam_training/blob/master/MiddEval3/trainingQ/Piano/im0.png" width="260" />
  <img src="https://github.com/LucienXian/Slam_training/blob/master/MiddEval3/trainingQ/Piano/im1.png" width="260" /> 
  <img src="https://github.com/LucienXian/Slam_training/blob/master/res_ncc/Piano.png" width="260" />
</p>

* Playtable

<p float="left">
  <img src="https://github.com/LucienXian/Slam_training/blob/master/MiddEval3/trainingQ/PlaytableP/im0.png" width="260" />
  <img src="https://github.com/LucienXian/Slam_training/blob/master/MiddEval3/trainingQ/PlaytableP/im1.png" width="260" /> 
  <img src="https://github.com/LucienXian/Slam_training/blob/master/res_ncc/PlaytableP.png" width="260" />
</p>

* Motorcyble

<p float="left">
  <img src="https://github.com/LucienXian/Slam_training/blob/master/MiddEval3/trainingQ/Motorcyble/im0.png" width="260" />
  <img src="https://github.com/LucienXian/Slam_training/blob/master/MiddEval3/trainingQ/Motorcyble/im1.png" width="260" /> 
  <img src="https://github.com/LucienXian/Slam_training/blob/master/res_ncc/Motorcyble.png" width="260" />
</p>

* Adirondack

<p float="left">
  <img src="https://github.com/LucienXian/Slam_training/blob/master/MiddEval3/trainingQ/Adirondack/im0.png" width="260" />
  <img src="https://github.com/LucienXian/Slam_training/blob/master/MiddEval3/trainingQ/Adirondack/im1.png" width="260" /> 
  <img src="https://github.com/LucienXian/Slam_training/blob/master/res_ncc/Adirondack.png" width="260" />
</p>

* Jadeplant

<p float="left">
  <img src="https://github.com/LucienXian/Slam_training/blob/master/MiddEval3/trainingQ/Jadeplant/im0.png" width="260" />
  <img src="https://github.com/LucienXian/Slam_training/blob/master/MiddEval3/trainingQ/Jadeplant/im1.png" width="260" /> 
  <img src="https://github.com/LucienXian/Slam_training/blob/master/res_ncc/Jadeplant.png" width="260" />
</p>