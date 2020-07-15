# Copy JAR To Lib

## 前言

本萌新java代码审计初入门，看到大型项目下的jar，真的是遍地都是，一个一个导入又比较麻烦，索性写个脚本，把文件夹下所有jar文件拷贝到一个文件夹里，届时再直接引入这个文件夹即可。缺点就是比较耗费空间，毕竟是拷贝出来的，目前暂未了解到导入一系列jar文件比较方便的方法。如果大家有好方法，欢迎在issue给我指出，我会根据情况改写工具~

突然发现windows直接用快速搜索就行了，自己好蠢qwq，就当练习吧

## 用法

```shell
usage: CopyJarToLib.py [-h] [-t TARGET] [-c COPY]

Copy Jar To Library

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        目标路径（需完整路径）
  -c COPY, --copy COPY  复制路径（需完整路径）
  
$ python CopyJarToLib.py -t F:\WebLogic\WebLogic_Home\12.2.1.4.0 -c 
or
$ python CopyJarToLib.py -t F:\WebLogic\WebLogic_Home\12.2.1.4.0 -c F:\lib
```

