# comicCollection
网络上搜索了不少时间, 没有找到合适的管理电子版漫画的软件. 想通过学习自己写一个合适自己用来整理电脑上的电子版漫画压缩包(zip,rar,7z), 通过固定的文件名格式将电脑上的漫画目录或文件收录到数据库中, 方便查询管理所收藏的漫画.

## 准备条件
电脑上保存的漫画压缩包目录或文件名用统一的取名规则保存, 方便获取漫画的信息.
> 完结与否是指扫本而非出版状态, 推荐使用繁体名，即跟出版封面文体一致。
### 目录统一取名规则:
  * 完结的：[超異能少年][青樹佑夜×奈央晃德][東立][zsliming][7完]
  * 未完结：[超異能少年][青樹佑夜×奈央晃德][東立][zsliming][7未]

### 文件名统一取名规则:
  * 卷数序号: [SLAM.DUNK 灌篮高手完全版][井上雄彥][天下][C.C].Vol.01.zip
  * 完结序号: [SLAM.DUNK 灌篮高手完全版][井上雄彥][天下][C.C].Vol.25end.zip

## 数据库结构
|ID|Bookname|Author|Publisher|Scaner|Number|end|read|edition|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|1|SLAM.DUNK 灌篮高手完全版|井上雄彥|天下|C.C|25|完结|已读|完全版|

## 功能列表
* [ ] 自动扫描收藏漫画数目变化
* [ ] 分析目录及文件名添加到数据库
* [ ] 存入数据自动转换简体中文
* [ ] 扫描指定目录漫画
* [ ] 添加命令行参数
