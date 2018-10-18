# break_captcha

### 1.项目简介 ###
    针对主流网站验证码所做出的验证码自动识别程序，文件夹名为验证码来源网站

### 2.相关依赖 ###
    opencv2
    PIL
    
### 3.CSND1 ###

 ![image](https://github.com/luoyanhan/break_captcha/blob/master/0cccc87c-a03c-44b8-b113-4a11adf11b99.png)   
   难度很小，二值化（只保留白色部分），投影法切割，再用KNN分类（captchas文件里的cuts文件夹是训练集）
   
### 4.CSDN2 ###

 ![image](https://github.com/luoyanhan/break_captcha/blob/master/1dc2c2da-1e61-4349-90e7-c08c31c70497.png)</br>
   总体过程和CSDN1类型一致，只是制作训练集以及最终识别时的投影法切割添加对Y轴的投影切割,去除字符上下空白来提高分类正确率,
   原因是CSDN2类型验证码各字符不在同一水平面上
   
    
   

