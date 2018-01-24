## 导入数据内容 

### 下载 文件并解压
```
wget http://labfile.oss.aliyuncs.com/courses/981/files/week7/loudatabase.zip
unzip loudatabase.zip 
```

### Mysql添加用户和数据库
```
mysql> create user shiyanlou@localhost identified by "Xd4a8lKjeL9Z"；
mysql> create database `shiyanlou-staging`;
mysql> grant all on `shiyanlou-staging`.*  to "shiyanlou"@localhost ;
```
### 创建表
```
mysql> use `shiyanlou-staging`;

//创建表 shiyanlou_user

mysql> create table shiyanlou_user(
    -> id int not null,
    -> name varchar(15) not null,
    -> primary key (id)
    -> ) default charset=utf8;

//创建表 shiyanlou_course

mysql> create table shiyanlou_course(
    -> id int not null,
    -> name varchar(60)  not null,
    -> primary key (id)
    -> ) default charset=utf8;

//创建表 shiyanlou_usercourse

mysql> create table shiyanlou_usercourse(
    -> id int unsigned not null auto_increment, 
    -> user_id int not null,
    -> course_id int not null,
    -> study_time int not null,
    -> primary key (id),
    -> foreign key (user_id) references shiyanlou_user(id),
    -> foreign key (course_id) references shiyanlou_course(id)
    -> ) default charset=utf8;

```
### 导入数据

```
//导入 shiyanlou_user.csv

mysql> load data infile "/home/shiyanlou/loudatabase/shiyanlou_user.csv" into table shiyanlou_user
    -> fileds terminated by ','
    -> optionally enclosed by ''
    -> (id,name);

//导入 shiyanlou_course.csv

mysql> load data infile "/home/shiyanlou/loudatabase/shiyanlou_course.csv" into table shiyanlou_course
    -> character set utf8
    -> fields terminated by ','
    -> optionally enclosed by ''
    -> (id,name);

//导入 shiyanlou_usercourse.csv

mysql> load data infile "/home/shiyanlou/loudatabase/shiyanlou_usercourse.csv" into table shiyanlou_usercourse 
    -> fields terminated by ','
    -> (user_id,course_id,study_time);
```
### `Tips`

* 列自增 添加属性`auto_increment`
* 导入csv文件时出现乱码添加`character set utf8`