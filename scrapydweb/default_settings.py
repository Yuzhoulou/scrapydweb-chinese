# coding: utf-8
"""
ScrapydWeb 的工作原理：
浏览器 <<<>>> SCRAPYDWEB_BIND:SCRAPYDWEB_PORT <<<>>> 你的 SCRAPYD_SERVERS

GitHub: https://github.com/my8100/scrapydweb
文档: https://github.com/my8100/files/blob/master/scrapydweb/README.md
文档（中文）: https://github.com/my8100/files/blob/master/scrapydweb/README_CN.md
"""
import os


############################## QUICK SETUP start ##############################
############################## 快速设置 开始 ###################################
# 将 SCRAPYDWEB_BIND 设置为 '0.0.0.0' 或当前主机的 IP
# 将使 ScrapydWeb 服务器对外部可见；否则，将其设置为 '127.0.0.1'。
# 默认为 '0.0.0.0'。
SCRAPYDWEB_BIND = '0.0.0.0'
# 接受指定端口上的连接，默认为 5000。
SCRAPYDWEB_PORT = 5000

# 默认为 False，将其设置为 True 以启用 Web UI 的基本身份验证。
ENABLE_AUTH = False
# 为了启用基本身份验证，USERNAME 和 PASSWORD 都应该是非空字符串。
USERNAME = ''
PASSWORD = ''


# 确保已经在所有主机上安装并启动了 [Scrapyd](https://github.com/scrapy/scrapyd)。
# 请注意，对于远程访问，您必须在 Scrapyd 的配置文件中手动设置 'bind_address = 0.0.0.0'
# 并重新启动 Scrapyd，使其对外部可见。
# 有关更多信息，请查看 'https://scrapyd.readthedocs.io/en/latest/config.html#example-configuration-file'。
# ------------------------------ Chinese --------------------------------------
# 请先确保所有主机都已经安装和启动 [Scrapyd](https://github.com/scrapy/scrapyd)。
# 如需远程访问 Scrapyd，则需在 Scrapyd 配置文件中设置 'bind_address = 0.0.0.0'，然后重启 Scrapyd。
# 详见 https://scrapyd.readthedocs.io/en/latest/config.html#example-configuration-file

# - 字符串格式：username:password@ip:port#group
#   - 如果未提供，则默认端口为 6800，
#   - 基本身份验证和组都是可选的。
#   - 例如 '127.0.0.1:6800' 或 'username:password@localhost:6801#group'
# - 元组格式：(username, password, ip, port, group)
#   - 当用户名、密码或组太复杂（例如，包含 ':@#'）时，
#   - 或者如果 ScrapydWeb 无法解析传入的字符串格式，
#   - 建议传入一个包含 5 个元素的元组。
#   - 例如 ('', '', '127.0.0.1', '6800', '') 或 ('username', 'password', 'localhost', '6801', 'group')
SCRAPYD_SERVERS = [
    '127.0.0.1:6800',
    # 'username:password@localhost:6801#group',
    ('username', 'password', 'localhost', '6801', 'group'),
]

# 默认为 True，将其设置为 False 以在启动时跳过检查 scrapyd 的连接性。
CHECK_SCRAPYD_SERVERS = True

# 如果 ScrapydWeb 和您的某个 Scrapyd 服务器运行在同一台机器上，
# 建议您更新以下三个选项。
# ------------------------------ Chinese --------------------------------------
# 假如 ScrapydWeb 和某个 Scrapyd 运行于同一台主机，建议更新如下三个设置项。

# 如果 ScrapydWeb 和您的某个 Scrapyd 服务器运行在同一台机器上，
# ScrapydWeb 将尝试直接从磁盘读取 Scrapy 日志文件，而不是向 Scrapyd 服务器发出请求。
# 例如 '127.0.0.1:6800' 或 'localhost:6801'，不要忘记端口号。
LOCAL_SCRAPYD_SERVER = ''

# 输入您运行 Scrapyd 的目录，运行以下命令
# 以找出 Scrapy 日志的存储位置：
# python -c "from os.path import abspath, isdir; from scrapyd.config import Config; path = abspath(Config().get('logs_dir')); print(path); print(isdir(path))"
# 有关更多信息，请查看 https://scrapyd.readthedocs.io/en/stable/config.html#logs-dir。
# 例如 'C:/Users/username/logs' 或 '/home/username/logs'
LOCAL_SCRAPYD_LOGS_DIR = ''

# 默认为 False，将其设置为 True 以在启动时自动将 LogParser 作为子进程运行。
# 请注意，您可以根据需要通过命令 'logparser' 单独运行 LogParser 服务。
# 运行 'logparser -h' 以查找 LogParser 的配置文件以进行更高级的设置。
# 访问 https://github.com/my8100/logparser 获取更多信息。
ENABLE_LOGPARSER = False
############################## QUICK SETUP end ################################
############################## 快速设置 结束 ###################################


############################## ScrapydWeb #####################################
# 默认为 False，将其设置为 True 并添加 CERTIFICATE_FILEPATH 和 PRIVATEKEY_FILEPATH
# 以在 HTTPS 模式下运行 ScrapydWeb。
# 请注意，此功能尚未经过全面测试，如果 ScrapydWeb
# 在启动时引发任何异常，请在此处留下您的评论：https://github.com/my8100/scrapydweb/issues/18
ENABLE_HTTPS = False
# 例如 '/home/username/cert.pem'
CERTIFICATE_FILEPATH = ''
# 例如 '/home/username/cert.key'
PRIVATEKEY_FILEPATH = ''


############################## Scrapy #########################################
# ScrapydWeb 能够定位 SCRAPY_PROJECTS_DIR 中的项目，
# 这样您只需选择一个项目进行部署，而无需提前打包。
# 例如 'C:/Users/username/myprojects' 或 '/home/username/myprojects'
SCRAPY_PROJECTS_DIR = ''


############################## Scrapyd ########################################
# ScrapydWeb 将按顺序尝试每个扩展名以定位 Scrapy 日志文件。
# 默认为 ['.log', '.log.gz', '.txt']。
SCRAPYD_LOG_EXTENSIONS = ['.log', '.log.gz', '.txt']

# 默认为 None，仅当您需要通过反向代理访问 Scrapyd 服务器时才进行设置。
# 确保 SCRAPYD_SERVERS_PUBLIC_URLS 的长度与上面的 SCRAPYD_SERVERS 相同。
# 例如
# SCRAPYD_SERVERS_PUBLIC_URLS = [
#     'https://a.b.com',  # 通过反向代理访问第一个 Scrapyd 服务器。
#     '',  # 不通过反向代理访问第二个 Scrapyd 服务器。
# ]
# 有关更多信息，请参见 https://github.com/my8100/scrapydweb/issues/94。
SCRAPYD_SERVERS_PUBLIC_URLS = None


############################## LogParser ######################################
# 在您访问作业的“统计信息”页面后，是否要在本地备份统计信息 json 文件，
# 这样即使原始日志文件已被删除，它仍然可以访问。
# 默认为 True，将其设置为 False 以禁用此行为。
BACKUP_STATS_JSON_FILE = True


############################## Timer Tasks ####################################
# 使用参数 '-sw' 或 '--switch_scheduler_state' 运行 ScrapydWeb，或单击
# “定时任务”页面上的“启用|禁用”按钮以打开/关闭以下定时任务和快照机制的调度器。

# 默认为 300，这意味着 ScrapydWeb 将自动创建“作业”页面的快照
# 并在后台每 300 秒将作业信息保存在数据库中。
# 请注意，如果禁用定时任务的调度器，则此行为将暂停。
# 将其设置为 0 以禁用此行为。
JOBS_SNAPSHOT_INTERVAL = 300


# 默认为 300，这意味着 ScrapydWeb 将自动检查所有定时任务的任务结果数量
# 在后台每 300 秒删除数据库中一些过期的记录。
# 仅当 KEEP_TASK_RESULT_LIMIT 或 KEEP_TASK_RESULT_WITHIN_DAYS 不为 0 时，此选项才有效。
# 请注意，如果禁用定时任务的调度器，则此行为将暂停。
# 将其设置为 0 以禁用此行为。
CHECK_TASK_RESULT_INTERVAL = 300

# 默认为 1000，这意味着只有最新的 1000 个定时任务结果不会从数据库中删除。
# 另请参见 CHECK_TASK_RESULT_INTERVAL。将其设置为 0 以禁用此行为。
KEEP_TASK_RESULT_LIMIT = 1000

# 默认为 31，这意味着只有最近 31 天内执行的定时任务结果
# 不会从数据库中删除。
# 另请参见 CHECK_TASK_RESULT_INTERVAL。将其设置为 0 以禁用此行为。
KEEP_TASK_RESULT_WITHIN_DAYS = 31


############################## Run Spider #####################################
# 默认为 False，将其设置为 True 以自动
# 展开“运行爬虫”页面中的“设置和参数”部分。
SCHEDULE_EXPAND_SETTINGS_ARGUMENTS = False

# 默认为 'Mozilla/5.0'，将其设置为非空字符串以自定义 `USER_AGENT`
# 下拉列表中 `custom` 的默认值。
SCHEDULE_CUSTOM_USER_AGENT = 'Mozilla/5.0'

# 默认为 None，将其设置为 ['custom', 'Chrome', 'iPhone', 'iPad', 'Android'] 中的任何值
# 以自定义 `USER_AGENT` 的默认值。
SCHEDULE_USER_AGENT = None

# 默认为 None，将其设置为 True 或 False 以自定义 `ROBOTSTXT_OBEY` 的默认值。
SCHEDULE_ROBOTSTXT_OBEY = None

# 默认为 None，将其设置为 True 或 False 以自定义 `COOKIES_ENABLED` 的默认值。
SCHEDULE_COOKIES_ENABLED = None

# 默认为 None，将其设置为非负整数以自定义 `CONCURRENT_REQUESTS` 的默认值。
SCHEDULE_CONCURRENT_REQUESTS = None

# 默认为 None，将其设置为非负数以自定义 `DOWNLOAD_DELAY` 的默认值。
SCHEDULE_DOWNLOAD_DELAY = None

# 默认为 "-d setting=CLOSESPIDER_TIMEOUT=60\r\n-d setting=CLOSESPIDER_PAGECOUNT=10\r\n-d arg1=val1"，
# 将其设置为 '' 或任何非空字符串以自定义 `additional` 的默认值。
# 使用 '\r\n' 作为行分隔符。
SCHEDULE_ADDITIONAL = "-d setting=CLOSESPIDER_TIMEOUT=60\r\n-d setting=CLOSESPIDER_PAGECOUNT=10\r\n-d arg1=val1"


############################## Page Display ###################################
# 默认为 True，将其设置为 False 以隐藏“项目”页面，以及
# “作业”页面中的“项目”列。
SHOW_SCRAPYD_ITEMS = True

# 默认为 True，将其设置为 False 以在使用非数据库视图的“作业”页面中隐藏“作业”列。
SHOW_JOBS_JOB_COLUMN = True

# 默认为 0，表示无限制，将其设置为正整数，以便
# 只有最新的 N 个已完成作业会显示在使用非数据库视图的“作业”页面中。
JOBS_FINISHED_JOBS_LIMIT = 0

# 如果您的浏览器停留在“作业”页面上，它将每 N 秒自动重新加载。
# 默认为 300，将其设置为 0 以禁用自动重新加载。
JOBS_RELOAD_INTERVAL = 300

# 每隔 N 秒检查一次当前 Scrapyd 服务器的负载状态，
# 该状态显示在页面右上角。
# 默认为 10，将其设置为 0 以禁用自动刷新。
DAEMONSTATUS_REFRESH_INTERVAL = 10


############################## Send Text ######################################
########## scrapy 项目中的用法 ##########
# 请参阅“发送文本”页面

########## slack ##########
# 如何创建 slack 应用程序：
# 1. 访问 https://api.slack.com/apps 并按“Create New App”按钮。
# 2. 输入您的应用程序名称（例如 myapp）并选择您的一个 Slack 工作区，然后按“Create App”。
# 3. 单击页面左侧边栏中的“OAuth & Permissions”菜单。
# 4. 向下滚动页面并在“Scopes”部分中找到“Select Permission Scopes”
# 5. 输入“send”并选择“Send messages as <your-app-name>”，然后按“Save Changes”
# 6. 向上滚动页面并按“Install App to Workspace”，然后按“Install”
# 7. 复制“OAuth Access Token”，例如 xoxp-123-456-789-abcde
# 有关更多信息，请参见 https://api.slack.com/apps

# 请参见上面的步骤 1~7，例如 'xoxp-123-456-789-abcde'
SLACK_TOKEN = os.environ.get('SLACK_TOKEN', '')
# 使用 slack 发送文本时的默认频道，例如 'general'
SLACK_CHANNEL = 'general'

########## telegram ##########
# 如何创建 telegram 机器人：
# 1. 访问 https://telegram.me/botfather 以开始与创建其他机器人的 Telegram 机器人进行对话。
# 2. 向 BotFather 发送 /newbot 命令以在与 BotFather 的聊天中创建一个新机器人。
# 3. 按照说明为您的机器人设置名称和用户名（例如 my_bot）。
# 4. 在步骤 3 之后，您将获得一个令牌（例如 123:abcde）。
# 5. 访问 telegram.me/<bot_username>（例如 telegram.me/my_bot）并向您的机器人打招呼以发起对话。
# 6. 访问 https://api.telegram.org/bot<token-in-setp-4>/getUpdates 以获取 chat_id。
#   （例如，访问 https://api.telegram.org/bot123:abcde/getUpdates
#    您可以在 "chat":{"id":123456789,... 中找到 chat_id）
# 有关更多信息，请参见 https://core.telegram.org/bots#6-botfather

# 请参见上面的步骤 1~4，例如 '123:abcde'
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '')
# 请参见上面的步骤 5~6，例如 123456789
TELEGRAM_CHAT_ID = int(os.environ.get('TELEGRAM_CHAT_ID', 0))

########## email ##########
# 使用电子邮件发送文本时的默认主题。
EMAIL_SUBJECT = '来自 #scrapydweb 的电子邮件'

########## 电子邮件发件人和收件人 ##########
# 将此选项保留为 '' 以默认为下面的 EMAIL_SENDER 选项；否则，如果您的电子邮件服务提供商
# 需要与下面的 EMAIL_SENDER 选项不同的用户名才能登录，请进行设置。
# 例如 'username'
EMAIL_USERNAME = ''
# 至于不同的电子邮件服务提供商，您可能需要获取一个 APP 密码（如 Gmail）
# 或一个授权码（如 QQ 邮箱）并将其设置为 EMAIL_PASSWORD。
# 请查看以下链接以获取更多帮助：
# https://stackoverflow.com/a/27515833/10517783 如何使用 Python 将电子邮件作为提供商发送？
# https://stackoverflow.com/a/26053352/10517783 Python smtplib 代理支持
# 例如 'password4gmail'
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')

# 例如 'username@gmail.com'
EMAIL_SENDER = ''
# 例如 ['username@gmail.com', ]
EMAIL_RECIPIENTS = [EMAIL_SENDER]

########## 电子邮件 smtp 设置 ##########
# 如果您使用的是阿里云的 ECS 并且您的 SMTP 服务器仅提供 TCP 端口 25，请查看此链接：
# https://www.alibabacloud.com/help/doc-detail/56130.htm
# 使用 SSL 的 https://mail.google.com 的配置：('smtp.gmail.com', 465, True)
# https://mail.google.com 的配置：           ('smtp.gmail.com', 587, False)
# 使用 SSL 的 https://mail.qq.com 的配置：     ('smtp.qq.com', 465, True)
# http://mail.10086.cn 的配置：              ('smtp.139.com', 25, False)
SMTP_SERVER = ''
SMTP_PORT = 0
SMTP_OVER_SSL = False
# 连接尝试的超时时间（以秒为单位），默认为 30。
SMTP_CONNECTION_TIMEOUT = 30


############################## Monitor & Alert ################################
# 默认为 False，将其设置为 True 以启动 poll 子进程来监视您的爬网作业。
ENABLE_MONITOR = False


########## poll 间隔 ##########
# 提示：为了及时收到通知（并在触发时停止或强制停止作业），
# 你可以减少 POLL_ROUND_INTERVAL 和 POLL_REQUEST_INTERVAL 的值，
# 但代价是增加服务器的 CPU 和带宽负担

# Sleep N 秒后开始下一轮轮询，默认值为 300。
POLL_ROUND_INTERVAL = 300
# 在轮询时，每次向 Scrapyd 服务器发出请求之间休眠 N 秒，默认值为 10。
POLL_REQUEST_INTERVAL = 10

########## 告警开关 ##########
# 提示：将“快速设置”部分中的 SCRAPYDWEB_BIND 选项设置为你的主机实际 IP，
# 这样你就可以通过告警中附加的链接访问 ScrapydWeb。

# 默认值为 False，将其设置为 True 以启用通过 Slack、Telegram 或电子邮件发送告警。
# 你必须先在上面的“发送文本”部分设置你的帐户。
ENABLE_SLACK_ALERT = False
ENABLE_TELEGRAM_ALERT = False
ENABLE_EMAIL_ALERT = False

########## 告警工作时间 ##########
# 星期一是 1，星期日是 7。
# 例如：[1, 2, 3, 4, 5, 6, 7]
ALERT_WORKING_DAYS = []

# 从 0 到 23。
# 例如：[9] + list(range(15, 18)) >>> [9, 15, 16, 17]，或 range(24) 表示 24 小时
ALERT_WORKING_HOURS = []

########## 基本触发器 ##########
# 每隔 N 秒为每个正在运行的作业触发告警。
# 默认值为 0，将其设置为正整数以启用此触发器。
ON_JOB_RUNNING_INTERVAL = 0

# 作业完成时触发告警。
# 默认值为 False，将其设置为 True 以启用此触发器。
ON_JOB_FINISHED = False

########## 高级触发器 ##########
# - LOG_XXX_THRESHOLD:
#   - 首次达到特定日志类型的阈值时触发告警。
#   - 默认值为 0，将其设置为正整数以启用此触发器。
# - LOG_XXX_TRIGGER_STOP (可选):
#   - 默认值为 False，将其设置为 True 以在达到 LOG_XXX_THRESHOLD 时自动停止当前作业。
#   - SIGTERM 信号只会发送一次，以优雅地关闭爬虫。
#   - 为了避免 UNCLEAN 关闭，如果未启用任何 'FORCESTOP' 触发器，无论启用了多少 'STOP' 触发器，
#   - 'STOP' 操作最多只会执行一次。
# - LOG_XXX_TRIGGER_FORCESTOP (可选):
#   - 默认值为 False，将其设置为 True 以在达到 LOG_XXX_THRESHOLD 时自动强制停止当前作业。
#   - SIGTERM 信号将发送两次，导致 UNCLEAN 关闭，Scrapy 统计信息不会被转储！
#   - 如果同时启用了 'STOP' 和 'FORCESTOP' 触发器，将执行 'FORCESTOP' 操作。

# 请注意，即使当前时间不在 ALERT_WORKING_DAYS 和 ALERT_WORKING_HOURS 内，
# 'STOP' 操作和 'FORCESTOP' 操作仍然会执行，但不会发送告警。

LOG_CRITICAL_THRESHOLD = 0
LOG_CRITICAL_TRIGGER_STOP = False
LOG_CRITICAL_TRIGGER_FORCESTOP = False

LOG_ERROR_THRESHOLD = 0
LOG_ERROR_TRIGGER_STOP = False
LOG_ERROR_TRIGGER_FORCESTOP = False

LOG_WARNING_THRESHOLD = 0
LOG_WARNING_TRIGGER_STOP = False
LOG_WARNING_TRIGGER_FORCESTOP = False

LOG_REDIRECT_THRESHOLD = 0
LOG_REDIRECT_TRIGGER_STOP = False
LOG_REDIRECT_TRIGGER_FORCESTOP = False

LOG_RETRY_THRESHOLD = 0
LOG_RETRY_TRIGGER_STOP = False
LOG_RETRY_TRIGGER_FORCESTOP = False

LOG_IGNORE_THRESHOLD = 0
LOG_IGNORE_TRIGGER_STOP = False
LOG_IGNORE_TRIGGER_FORCESTOP = False


############################## System #########################################
# 默认值为 False，将其设置为 True 以启用调试模式，交互式调试器将
# 显示在浏览器中，而不是“500 Internal Server Error”页面。
# 请注意，run.py 中 use_reloader 设置为 False。
DEBUG = False

# 默认值为 False，将其设置为 True 以将日志级别从 INFO 更改为 DEBUG，
# 以获取有关 ScrapydWeb 工作方式的更多信息，尤其是在调试时。
VERBOSE = False

# 默认值为 ''，表示将所有程序数据保存在 Python 目录中。
# 例如：'C:/Users/username/scrapydweb_data' 或 '/home/username/scrapydweb_data'
DATA_PATH = os.environ.get('DATA_PATH', '')

# 默认值为 ''，表示使用 SQLite 将作业和定时任务的数据保存在 DATA_PATH 中。
# 为了提高并发性，数据也可以保存在 MySQL 或 PostgreSQL 后端。
# 要使用 MySQL 后端，请运行命令：pip install --upgrade pymysql
# 要使用 PostgreSQL 后端，请运行命令：pip install --upgrade psycopg2
# 例如：
# 'mysql://username:password@127.0.0.1:3306'
# 'postgresql://username:password@127.0.0.1:5432'
# 'sqlite:///C:/Users/username'
# 'sqlite:////home/username'
DATABASE_URL = os.environ.get('DATABASE_URL', '')