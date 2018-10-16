# break_captcha

### 1.项目简介 ###
    针对主流网站验证码所做出的验证码自动识别程序，文件夹名为验证码来源网站

### 2.相关依赖 ###
    opencv2
    PIL
    
### 3.CSND1 ###

 ![image](https://github.com/luoyanhan/break_captcha/blob/master/0cccc87c-a03c-44b8-b113-4a11adf11b99.png)   
   难度很小，二值化（只保留白色部分），投影法切割，再用KNN分类（captchas文件里的cuts文件夹是训练集）
    
   

