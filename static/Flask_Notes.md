### 设置flask环境变量：
若想启动前一节编写的hello.py 应用，首先确保之前创建的虚拟环境已经激活，而且里面
安装了Flask。Linux 和macOS 用户执行下述命令启动Web 服务器：
(venv) $ export FLASK_APP=hello.py
(venv) $ flask run
* Serving Flask app "hello"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
微软Windows 用户执行的命令和刚才一样，只不过设定FLASK_APP 环境变量的方式不同：
(venv) $ set FLASK_APP=hello.py
(venv) $ flask run
* Serving Flask app "hello"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
服务器启动后便开始轮询，处理请求。直到按Ctrl+C 键停止服务器，轮询才会停止。


### pip换源
    linux下，修改 ~/.pip/pip.conf (没有就创建一个)
    windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下：
    [global]
    index-url=https://pypi.tuna.tsinghua.edu.cn/simple
    [install]
    trusted-host=pypi.tuna.tsinghua.edu.cn

### pipenv commands
    pipenv --three
    pipenv --python 3.6
    pipenv shell
    pipenv --where
    pipenv --venv
    pipenv install
    pipenv install django==1.11.15
    pipenv graph
    pipenv --py
    pipenv uninstall --all


### Jinja2界定符
    if, for: {% ... %}
    表达式，如字符串、变量、函数调用： {{ ... }}
    注释： {# ... #}
    另外，在模板中，Jinja2支持使用“.”获取变量的属性，比如user字典中的username键值通过“.”获取，即user.username，在效果上等同于user['username']。
    




### 模板中使用变量的示例：
```html
<p>这是列表my_list的第一个元素：{{ my_list[0] }}</p>
<p>这是元组my_tuple的第一个元素：{{ my_tuple[0] }}</p>
<p>这是字典my_dict的键为name的值：{{ my_dict['name'] }}</p>
<p>这是函数my_func的返回值：{{ my_func() }}</p>
<p>这是对象my_object调用某方法的返回值：{{ my_object.name() }}</p>
```

### 变量过滤器：
    Hello, {{ name|capitalize }}     # 将name变量值的首字母大写

    safe        渲染值时不转义
    capitalize  把值的首字母转换成大写，其他字母转换成小写
    lower       把值转换成小写形式
    upper       把值转换成大写形式
    title       把值中每个单词的首字母都转换成大写
    trim        把值的首尾空格删掉
    striptags   渲染之前把值中所有的HTML 标签都删掉

    safe 过滤器值得特别说明一下。默认情况下，出于安全考虑，Jinja2 会转义所有变量。例
    如，如果一个变量的值为'\<h1>Hello</h1>/'，Jinja2 会将其渲染成'&lt;h1&gt;Hello&lt;/h1&gt;'，
    浏览器能显示这个h1 元素，但不会解释它。
    很多情况下需要显示变量中存储的HTML 代码，这时就可使用safe 过滤器。
    千万别在不可信的值上使用safe 过滤器，例如用户在表单中输入的文本。
    完整的过滤器列表:
    http://jinja.pocoo.org/docs/2.10/templates/#builtin-filters

### 上下文：
    current_app 应用上下文当前应用的应用实例
    g           应用上下文处理请求时用作临时存储的对象，每次请求都会重设这个变量
    request     请求上下文请求对象，封装了客户端发出的HTTP 请求中的内容
    session     请求上下文用户会话，值为一个字典，存储请求之间需要“记住”的值

### Flask-Bootstrap基模板中定义的区块
    区块名             说　明
    doc             整个HTML 文档
    html_attribs    <html> 标签的属性
    html            <html> 标签中的内容
    head            <head> 标签中的内容
    title           <title> 标签中的内容
    metas           一组<meta> 标签
    styles CSS      声明
    body_attribs    <body> 标签的属性
    body            <body> 标签中的内容
    navbar          用户定义的导航栏
    content         用户定义的页面内容
    scripts         文档底部的JavaScript 声明
    -如果应用需要向已经有内容的块中添加新内容，必须使用Jinja2 提供的super() 函数。


### WTForms支持的HTML标准字段
    字段类型                    说　明
    BooleanField        复选框，值为True 和False
    DateField           文本字段，值为datetime.date 格式
    DateTimeField       文本字段，值为datetime.datetime 格式
    DecimalField        文本字段，值为decimal.Decimal
    FileField           文件上传字段
    HiddenField         隐藏的文本字段
    MultipleFileField   多文件上传字段
    FieldList           一组指定类型的字段
    FloatField          文本字段，值为浮点数
    FormField           把一个表单作为字段嵌入另一个表单
    IntegerField        文本字段，值为整数
    PasswordField       密码文本字段
    RadioField          一组单选按钮
    SelectField         下拉列表
    SelectMultipleField 下拉列表，可选择多个值
    SubmitField         表单提交按钮
    StringField         文本字段
    TextAreaField       多行文本字段


### WTForms验证函数
    验证函数                说　明
    DataRequired    确保转换类型后字段中有数据
    Email           验证电子邮件地址
    EqualTo         比较两个字段的值；常用于要求输入两次密码进行确认的情况
    InputRequired   确保转换类型前字段中有数据
    IPAddress       验证IPv4 网络地址
    Length          验证输入字符串的长度
    MacAddress      验证MAC 地址
    NumberRange     验证输入的值在数字范围之内
    Optional        允许字段中没有输入，将跳过其他验证函数
    Regexp          使用正则表达式验证输入值
    URL             验证URL
    UUID            验证UUID
    AnyOf           确保输入值在一组可能的值中
    NoneOf          确保输入值不在一组可能的值中

### 最常用的SQLAlchemy列类型
     类型名         Python类型                    说　明
    Integer         int                     普通整数，通常是32 位
    SmallInteger    int                     取值范围小的整数，通常是16 位
    BigInteger      int或long               不限制精度的整数
    Float           float                   浮点数
    Numeric         decimal.Decimal         定点数
    String          str                     变长字符串
    Text            str                     变长字符串，对较长或不限长度的字符串做了优化
    Unicode         unicode                 变长Unicode字符串
    UnicodeText     unicode                 变长Unicode 字符串，对较长或不限长度的字符串做了优化
    Boolean         bool                    布尔值
    Date            datetime.date           日期
    Time            datetime.time           时间
    DateTime        datetime.datetime       日期和时间
    Interval        datetime.timedelta      时间间隔
    Enum            str                     一组字符串
    PickleType      任何Python对象           自动使用Pickle 序列化
    LargeBinary     str                     二进制blob


### 最常用的SQLAlchemy列选项
    选项名                 说　明
    primary_key     如果设为True，列为表的主键
    unique          如果设为True，列不允许出现重复的值
    index           如果设为True，为列创建索引，提升查询效率
    nullable        如果设为True，列允许使用空值；如果设为False，列不允许使用空值
    default         为列定义默认值
    - Flask-SQLAlchemy 要求每个模型都定义主键，这一列经常命名为id。



