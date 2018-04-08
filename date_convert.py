# -*- coding: utf-8 -*-
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine


def myreplace(x):
    one = x.replace('月', '')
    one = one.replace('上午', 'am')
    one = one.replace('下午', 'pm')
    return one


df = pd.read_csv('/mnt/hgfs/share/all.csv')
df['时间X'] = df['时间X'].apply(lambda x: datetime.strptime(myreplace(x), '%d-%m-%y %I.%M.%S.%f %p'))
df['消失时间X'] = df['消失时间X'].apply(lambda x: datetime.strptime(myreplace(x), '%d-%m-%y %I.%M.%S.%f %p'))
df = df.sort_values('时间X')

df.rename(columns={'站点编号': 'station', '频率': 'fre', '时间X': 'app_time', '消失时间X': 'disapp_time', '背景电平': 'back_level', '电平': 'level', '出现标志': 'flag'}, inplace=True)
print (df)
# 将数据写入到csv文件中
# df[df['站点编号'] == 3].to_csv('/home/sjl/data/20171130/3.1.csv')
# df[df['站点编号'] == 4].to_csv('/home/sjl/data/20171130/4.1.csv')
# df[df['站点编号'] == 5].to_csv('/home/sjl/data/20171130/5.1.csv')
# df[df['站点编号'] == 6].to_csv('/home/sjl/data/20171130/6.1.csv')
# df[df['站点编号'] == 7].to_csv('/home/sjl/data/20171130/7.1.csv')

# 创建数据库连接,并将数据写入mysql数据库中
con = create_engine('mysql+mysqldb://root:1995sjl1005@localhost:3306/test330?charset=utf8')
# pd.io.sql.to_sql(df, 'test', con, schema='test330', if_exists='append')
df.to_sql('test', con, if_exists='append')
