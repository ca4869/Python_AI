slang_dict = {"aigc":"每个毛都看得清清楚楚","html":"I kown how to meet ladies"}
slang_dict["降低门槛"] = "我将提供购买以外的所有支持"
slang_dict["乳法"] = "even the french"

query = input("请输入您要查询的关键词 :")
if query in slang_dict:
    print("您查询的" + query + "含义如下")
    print(slang_dict[query])
else:
    print("您查询的关键词暂未收录.")
    print("当前本词典收录词条数为:" + str(len(slang_dict)) + "条.")
