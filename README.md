# Lemon-Crawler

爬鍵盤大檸檬中的所有熱門主題

['驚悚','開酸','宅玩','萌獸','奇聞','潮流','感情','打卡','運勢','長腦']

https://www.ettoday.net/dalemon/latest-news

比較特別的是這次爬蟲找出日期的方式是

datelist = re.findall('(\d+)',ele.find(itemprop='datePublished').get('content'))

用到re正規式的get方法

好...好神奇阿阿阿吼喔喔喔喔
