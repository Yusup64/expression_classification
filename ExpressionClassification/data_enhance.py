import csv
import os
import Augmentor  # 导入包
root_path = os.path.join(
    os.getcwd(), 'ExpressionClassification', 'data_enhance')
p = Augmentor.Pipeline(os.path.join(root_path, 'expr_photo', '1'))  # 导入图像
# p.ground_truth(os.path.join(root_path, 'expr_photo', '1'))  # 两张图像进行相同的变换，名称要相同

p.shear(probability=0.1, max_shear_left=15, max_shear_right=15)  # 图片剪切
p.rotate(probability=0.4, max_left_rotation=20, max_right_rotation=20)  # 图片旋转
p.random_erasing(probability=0.6, rectangle_area=0.8)  # 图片遮挡
p.random_distortion(probability=0.6, grid_height=6,
                    grid_width=6, magnitude=5)  # 图片扭曲
p.sample(5000)  # 生产5000张图像
