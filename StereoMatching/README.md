# 立体匹配

立体匹配（Stereo matching）的目的就是通过对stereo相机拍摄的左右两张图进行匹配找出视差图，可以还原物体的3D信息。

## 步骤

1. 预处理
2. 匹配计算cost，每个像素点都会计算cost了——绝对值计算或者平方值计算

$$
AD: |I_L(x, y) - I_R(x, y)| \\
SD: (I_L(x, y) - I_R(x, y))^2
$$

3. 全局最优化
4. 后续处理

## 算法

常用的立体匹配算法可以分为基于局部的和基于全局的：

1. 基于局部的有：BM（SSD，SAD，NCC等）
2. 基于全局的有：DP，graph cuts，Belief Propagation等



## Demo实现

在进行立体矫正之前，先进行极线矫正，目的是使两帧图像极线处于水平方向。效果如下：

![img](https://github.com/LucienXian/Slam_training/blob/master/StereoMatching/MiddEval3/trainingQ/MotorcycleE/RectifiedL.png)

![img](https://github.com/LucienXian/Slam_training/blob/master/StereoMatching/MiddEval3/trainingQ/MotorcycleE/RectifiedR.png)

然后使用自己实现的ssd算法来重建深度图（效果一般and慢）

```python
def stereo_match(imgL, imgR, kernel=6, search_range=30, name="default.png"):
    w, h = imgL.size
    left, right = np.asarray(imgL), np.asarray(imgR)
    depth = np.zeros((h, w), np.uint8) # PIL and numpy have different indexing systems.
    
    #depth.shape = h, w
    half_kernel = kernel//2
    depth_offset = 255//search_range
    for y in range(half_kernel, h-half_kernel):
        print(".", end="", flush=True)
        for x in range(half_kernel, w-half_kernel):
            optimal_offset = 0
            ssd_min = 256*256
            for search_idx in range(search_range):
                ssd = 0
                for u in range(-half_kernel, half_kernel):
                    for v in range(-half_kernel, half_kernel):
                        ssd += (int(left[y+u, x+v]) - int(right[y+u, x+v-search_idx]))**2
                if ssd < ssd_min:
                    ssd_min = ssd
                    optimal_offset = search_idx
            depth[y, x] = optimal_offset * depth_offset
    print(depth)
    Image.fromarray(depth).save(name)
```

出来的效果图如下：

![img](https://github.com/LucienXian/Slam_training/blob/master/StereoMatching/MiddEval3/trainingQ/MotorcycleE/output_v2.png)

