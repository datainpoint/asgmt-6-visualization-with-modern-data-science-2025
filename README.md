# asgmt-6-visualization-with-modern-data-science-2025
Assignment 6: Visualization with Modern Data Science 2025.

## 01. Define a function `import_presidents_taipei_xlsx()` which imports `presidents_taipei.xlsx` in working directory.

```python
def import_presidents_taipei_xlsx() -> pd.core.frame.DataFrame:
    """
    >>> presidents_taipei_xlsx = import_presidents_taipei_xlsx()
    >>> type(presidents_taipei_xlsx)
    pandas.core.frame.DataFrame
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a function `retrieve_candidates_from_presidents_taipei_xlsx()` which returns candidate names given `presidents_taipei.xlsx` in working directory.

```
   number president_candidate vice_president_candidate
0       1                 柯文哲                      吳欣盈
1       2                 賴清德                      蕭美琴
2       3                 侯友宜                      趙少康
```

```python
def retrieve_candidates_from_presidents_taipei_xlsx() -> pd.core.frame.DataFrame:
    """
    >>> candidates = retrieve_candidates_from_presidents_taipei_xlsx()
    >>> candidates.shape
    (3, 3)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a function `retrieve_towns_from_presidents_taipei_xlsx()` which returns town names given `presidents_taipei.xlsx` in working directory.

```
0     中山區
1     中正區
2     信義區
3     內湖區
4     北投區
5     南港區
6     士林區
7     大同區
8     大安區
9     文山區
10    松山區
11    萬華區
dtype: object
```

```python
def retrieve_towns_from_presidents_taipei_xlsx() -> pd.core.series.Series:
    """
    >>> towns = retrieve_towns_from_presidents_taipei_xlsx()
    >>> towns.shape
    (12,)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a function `summarize_votes_by_candidates_from_presidents_taipei_xlsx()` which returns votes received by each candidate given `presidents_taipei.xlsx` in working directory.

```
   number president_candidate vice_president_candidate   votes
0       1                 柯文哲                      吳欣盈  366854
1       2                 賴清德                      蕭美琴  587899
2       3                 侯友宜                      趙少康  587258
```

```python
def summarize_votes_by_candidates_from_presidents_taipei_xlsx() -> pd.core.frame.DataFrame:
    """
    >>> votes_by_candidates = summarize_votes_by_candidates_from_presidents_taipei_xlsx()
    >>> votes_by_candidates.shape
    (3, 4)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a function `summarize_votes_by_towns_from_presidents_taipei_xlsx()` which returns votes received by each candidate given `presidents_taipei.xlsx` in working directory.

```
    town  number president_candidate vice_president_candidate  votes
0   　中山區       1                 柯文哲                      吳欣盈  30227
3   　中正區       1                 柯文哲                      吳欣盈  21278
6   　信義區       1                 柯文哲                      吳欣盈  30132
9   　內湖區       1                 柯文哲                      吳欣盈  44597
12  　北投區       1                 柯文哲                      吳欣盈  35975
15  　南港區       1                 柯文哲                      吳欣盈  19007
18  　士林區       1                 柯文哲                      吳欣盈  37782
21  　大同區       1                 柯文哲                      吳欣盈  18485
24  　大安區       1                 柯文哲                      吳欣盈  35909
27  　文山區       1                 柯文哲                      吳欣盈  39875
30  　松山區       1                 柯文哲                      吳欣盈  26090
33  　萬華區       1                 柯文哲                      吳欣盈  27497
```

```
    town  number president_candidate vice_president_candidate  votes
1   　中山區       2                 賴清德                      蕭美琴  54448
4   　中正區       2                 賴清德                      蕭美琴  32196
7   　信義區       2                 賴清德                      蕭美琴  46634
10  　內湖區       2                 賴清德                      蕭美琴  61339
13  　北投區       2                 賴清德                      蕭美琴  61151
16  　南港區       2                 賴清德                      蕭美琴  26117
19  　士林區       2                 賴清德                      蕭美琴  71869
22  　大同區       2                 賴清德                      蕭美琴  34270
25  　大安區       2                 賴清德                      蕭美琴  62381
28  　文山區       2                 賴清德                      蕭美琴  50345
31  　松山區       2                 賴清德                      蕭美琴  43780
34  　萬華區       2                 賴清德                      蕭美琴  43369
```

```
    town  number president_candidate vice_president_candidate  votes
2   　中山區       3                 侯友宜                      趙少康  48579
5   　中正區       3                 侯友宜                      趙少康  34733
8   　信義區       3                 侯友宜                      趙少康  53076
11  　內湖區       3                 侯友宜                      趙少康  64781
14  　北投區       3                 侯友宜                      趙少康  51657
17  　南港區       3                 侯友宜                      趙少康  26529
20  　士林區       3                 侯友宜                      趙少康  56397
23  　大同區       3                 侯友宜                      趙少康  21351
26  　大安區       3                 侯友宜                      趙少康  72954
29  　文山區       3                 侯友宜                      趙少康  70844
32  　松山區       3                 侯友宜                      趙少康  47452
35  　萬華區       3                 侯友宜                      趙少康  38905
```

```python
def summarize_votes_by_towns_from_presidents_taipei_xlsx(number: int) -> pd.core.frame.DataFrame:
    """
    >>> votes_by_towns = summarize_votes_by_towns_from_presidents_taipei_xlsx(1)
    >>> votes_by_towns.shape
    (12, 5)
    >>> votes_by_towns = summarize_votes_by_towns_from_presidents_taipei_xlsx(2)
    >>> votes_by_towns.shape
    (12, 5)
    >>> votes_by_towns = summarize_votes_by_towns_from_presidents_taipei_xlsx(3)
    >>> votes_by_towns.shape
    (12, 5)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `retrieve_electoral_districts_from_regional_legislators_taipei_xlsx()` which retrieves the electoral districts given `regional_legislators_taipei.xlsx` in working directory.

```python
def retrieve_electoral_districts_from_regional_legislators_taipei_xlsx() -> list:
    """
    >>> electoral_districts = retrieve_electoral_districts_from_regional_legislators_taipei_xlsx()
    >>> type(electoral_districts)
    list
    >>> len(electoral_districts)
    8
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `retrieve_candidates_from_regional_legislators_taipei_xlsx()` which retrieves candidates given `regional_legislators_taipei.xlsx` in working directory.

```python
def retrieve_candidates_from_regional_legislators_taipei_xlsx() -> list:
    """
    >>> candidates = retrieve_candidates_from_regional_legislators_taipei_xlsx()
    >>> type(candidates)
    list
    >>> len(candidates)
    53
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `retrieve_candidates_and_parties_from_regional_legislators_taipei_xlsx()` which retrieves candidates and their parties given `regional_legislators_taipei.xlsx` in working directory.

```
   electoral_district      party candidate
0            臺北市第1選舉區      民主進步黨       吳思瑤
1            臺北市第1選舉區      中國國民黨       張斯綱
2            臺北市第1選舉區      人民民主黨       賴宗育
3            臺北市第1選舉區          無       侯漢廷
4            臺北市第1選舉區      人民最大黨       張臺勝
5            臺北市第1選舉區      人民最大黨       胡金城
6            臺北市第1選舉區          無       許盛鋒
7            臺北市第1選舉區    臺灣雙語無法黨       陳執中
8            臺北市第2選舉區      制度救世島       熊嘉玲
9            臺北市第2選舉區      人民最大黨       何梅娟
10           臺北市第2選舉區      民主進步黨       王世堅
11           臺北市第2選舉區    中華統一促進黨       郭啟源
12           臺北市第2選舉區      中國國民黨       游淑慧
13           臺北市第3選舉區      人民最大黨       余新造
14           臺北市第3選舉區          無       陳源發
15           臺北市第3選舉區      民主進步黨       謝佩芬
16           臺北市第3選舉區      制度救世島       高士恩
17           臺北市第3選舉區      中國國民黨       王鴻薇
18           臺北市第3選舉區       台灣維新       楊時睿
19           臺北市第3選舉區    臺灣雙語無法黨       陳一郎
20           臺北市第4選舉區      中國國民黨       李彥秀
21           臺北市第4選舉區       台灣基進       吳欣岱
22           臺北市第4選舉區      民主進步黨       高嘉瑜
23           臺北市第4選舉區      制度救世島       黃啟彬
24           臺北市第4選舉區  台灣整復師聯盟工黨       林秋彤
25           臺北市第5選舉區      中國國民黨       鍾小平
26           臺北市第5選舉區          無       陳燕玉
27           臺北市第5選舉區     合一行動聯盟       許敬民
28           臺北市第5選舉區          無       林志成
29           臺北市第5選舉區          無       于美人
30           臺北市第5選舉區        經濟黨        蘇諍
31           臺北市第5選舉區      民主進步黨       吳沛憶
32           臺北市第5選舉區          無       孫智麗
33           臺北市第5選舉區    台灣麻將最大黨       張華特
34           臺北市第5選舉區      司法改革黨       李慧曦
35           臺北市第6選舉區      制度救世島       張雪卿
36           臺北市第6選舉區      社會民主黨       苗博雅
37           臺北市第6選舉區    臺灣雙語無法黨       崔建章
38           臺北市第6選舉區      中國國民黨       羅智強
39           臺北市第6選舉區       台灣維新       朱翊銘
40           臺北市第7選舉區    中華愛國同心黨       李承龍
41           臺北市第7選舉區      中國國民黨       徐巧芯
42           臺北市第7選舉區       台灣維新        羅丹
43           臺北市第7選舉區          無       陳韋安
44           臺北市第7選舉區      民主進步黨       許淑華
45           臺北市第8選舉區       台灣維新       劉佩玲
46           臺北市第8選舉區      中國國民黨       賴士葆
47           臺北市第8選舉區      民主進步黨       王閔生
48           臺北市第8選舉區  小民參政歐巴桑聯盟       賴宣任
49           臺北市第8選舉區          無       夏萬浪
50           臺北市第8選舉區      台灣民眾黨       張其祿
51           臺北市第8選舉區          無       張維學
52           臺北市第8選舉區      興中同盟會       胡之壯
```

```python
def retrieve_candidates_and_parties_from_regional_legislators_taipei_xlsx() -> pd.core.frame.DataFrame:
    """
    >>> candidates_and_parties = retrieve_candidates_and_parties_from_regional_legislators_taipei_xlsx()
    >>> candidates_and_parties.shape
    (53, 3)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `retrieve_votes_received_from_regional_legislators_taipei_xlsx()` which retrieves votes received by each candidate given `regional_legislators_taipei.xlsx` in working directory.

```
   electoral_district      party candidate   votes
0            臺北市第1選舉區      民主進步黨       吳思瑤   91958
1            臺北市第1選舉區      中國國民黨       張斯綱   71837
2            臺北市第1選舉區      人民民主黨       賴宗育     836
3            臺北市第1選舉區          無       侯漢廷   28510
4            臺北市第1選舉區      人民最大黨       張臺勝     161
5            臺北市第1選舉區      人民最大黨       胡金城     255
6            臺北市第1選舉區          無       許盛鋒     231
7            臺北市第1選舉區    臺灣雙語無法黨       陳執中     950
8            臺北市第2選舉區      制度救世島       熊嘉玲     968
9            臺北市第2選舉區      人民最大黨       何梅娟    1741
10           臺北市第2選舉區      民主進步黨       王世堅  111605
11           臺北市第2選舉區    中華統一促進黨       郭啟源     305
12           臺北市第2選舉區      中國國民黨       游淑慧   69754
13           臺北市第3選舉區      人民最大黨       余新造     596
14           臺北市第3選舉區          無       陳源發    1851
15           臺北市第3選舉區      民主進步黨       謝佩芬   89850
16           臺北市第3選舉區      制度救世島       高士恩     195
17           臺北市第3選舉區      中國國民黨       王鴻薇  105050
18           臺北市第3選舉區       台灣維新       楊時睿    1378
19           臺北市第3選舉區    臺灣雙語無法黨       陳一郎    1107
20           臺北市第4選舉區      中國國民黨       李彥秀  112743
21           臺北市第4選舉區       台灣基進       吳欣岱   26382
22           臺北市第4選舉區      民主進步黨       高嘉瑜   95241
23           臺北市第4選舉區      制度救世島       黃啟彬     422
24           臺北市第4選舉區  台灣整復師聯盟工黨       林秋彤    1881
25           臺北市第5選舉區      中國國民黨       鍾小平   57634
26           臺北市第5選舉區      司法改革黨       李慧曦    1502
27           臺北市第5選舉區          無       陳燕玉     194
28           臺北市第5選舉區     合一行動聯盟       許敬民     174
29           臺北市第5選舉區          無       林志成     138
30           臺北市第5選舉區          無       于美人   38913
31           臺北市第5選舉區        經濟黨        蘇諍     472
32           臺北市第5選舉區      民主進步黨       吳沛憶   66932
33           臺北市第5選舉區          無       孫智麗    1489
34           臺北市第5選舉區    台灣麻將最大黨       張華特     692
35           臺北市第6選舉區      制度救世島       張雪卿     896
36           臺北市第6選舉區      社會民主黨       苗博雅   74375
37           臺北市第6選舉區    臺灣雙語無法黨       崔建章    2202
38           臺北市第6選舉區      中國國民黨       羅智強   87973
39           臺北市第6選舉區       台灣維新       朱翊銘     660
40           臺北市第7選舉區    中華愛國同心黨       李承龍     310
41           臺北市第7選舉區      中國國民黨       徐巧芯   89727
42           臺北市第7選舉區       台灣維新        羅丹    1073
43           臺北市第7選舉區          無       陳韋安    3286
44           臺北市第7選舉區      民主進步黨       許淑華   76113
45           臺北市第8選舉區       台灣維新       劉佩玲    1122
46           臺北市第8選舉區      中國國民黨       賴士葆   87099
47           臺北市第8選舉區      民主進步黨       王閔生   59490
48           臺北市第8選舉區  小民參政歐巴桑聯盟       賴宣任    6374
49           臺北市第8選舉區          無       夏萬浪     761
50           臺北市第8選舉區      台灣民眾黨       張其祿   28335
51           臺北市第8選舉區          無       張維學     201
52           臺北市第8選舉區      興中同盟會       胡之壯     136
```

```python
def retrieve_votes_received_from_regional_legislators_taipei_xlsx() -> pd.core.frame.DataFrame:
    """
    >>> votes_received = retrieve_votes_received_from_regional_legislators_taipei_xlsx()
    >>> votes_received.shape
    (53, 4)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `retrieve_elected_from_regional_legislators_taipei_xlsx()` which retrieves elected regional legislators by each electoral district given `regional_legislators_taipei.xlsx` in working directory.

```
  electoral_district  party candidate   votes
0           臺北市第1選舉區  民主進步黨       吳思瑤   91958
1           臺北市第2選舉區  民主進步黨       王世堅  111605
2           臺北市第3選舉區  中國國民黨       王鴻薇  105050
3           臺北市第4選舉區  中國國民黨       李彥秀  112743
4           臺北市第5選舉區  民主進步黨       吳沛憶   66932
5           臺北市第6選舉區  中國國民黨       羅智強   87973
6           臺北市第7選舉區  中國國民黨       徐巧芯   89727
7           臺北市第8選舉區  中國國民黨       賴士葆   87099
```

```python
def retrieve_elected_from_regional_legislators_taipei_xlsx() -> pd.core.frame.DataFrame:
    """
    >>> elected = retrieve_elected_from_regional_legislators_taipei_xlsx()
    >>> elected.shape
    (8, 4)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```