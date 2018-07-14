# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from predictor import Predictor

predict=Predictor()
#target for below:{"death_penalty": false, "imprisonment": 8, "life_imprisonment": false}, "punish_of_money": 0, "accusation": ["盗窃"], "relevant_articles": [264]},
content1=u"经审理查明：一、2016年9月20日，被告人胡某某伙同罗某某（13岁）将被害人龙某甲停放在桂阳县欧阳海乡周塘村7组龙某某家门前水泥坪的一辆雅奇牌男式两轮摩托车盗走，并将该摩托车以300元的价格卖掉，被告人胡某某分得100元。案发后，公安机关已将追回的被盗摩托车发还给被害人龙某甲。经鉴定，被盗摩托车的价值为1330元。二、2016年9月21日，被告人胡某某伙同罗某某将被害人刘某甲停放在桂阳县仁义镇烟草站仓库门口空坪处的一辆豪江牌男式两轮摩托车盗走，并将该摩托车以300元的价格卖掉，被告人胡某某分得100元。案发后，公安机关已将追回的被盗摩托车发还给被害人刘某甲。经鉴定，被盗摩托车的价值为1580元。三、2016年9月23日，被告人胡某某伙同罗某某将被害人李某甲停放在桂阳县敖泉卫生院内空坪处的一辆豪爵牌男式两轮摩托车盗走，后两人与张某甲一起将该摩托车拖走后以800元的价格卖掉，被告人胡某某分得300元。案发后，公安机关已将追回的被盗摩托车发还给被害人李某甲。经鉴定，被盗摩托车的价值为2800元。上述事实，被告人胡某某在庭审时也无异议，且有受案登记表、立案决定书，抓获经过，健康检查登记表，被盗摩托车的相关材料，扣押物品决定书，扣押物品清单，发还物品清单，价格鉴定意见，行政处罚决定书，责令监管通知书，证人史某某、王某某、罗某某、张某甲的证言，被害人刘某甲、李某甲、龙某甲的陈述，被告人胡某某的供述与辩解，现场勘查笔录及照片，现场指认笔录及照片，辨认笔录，监控视频及视频截图，户籍资料等证据证实，足以认定。"
#targe for below:{"death_penalty": false, "imprisonment": 8, "life_imprisonment": false}, "punish_of_money": 4000, "accusation": ["盗窃"], "relevant_articles": [264]},
content2=u"上海市静安区人民检察院指控被告人童某与“昆昆”(另案处理)共同于2016年3月1日16时许，在本市静安区江宁路XXX号XXX楼走道内，趁人不备，窃得被害人薛某停放在此的一辆价值人民币7,298元的白色标志牌QP100T-12C型摩托车，后逃逸销赃。被告人童某于2016年4月7日主动至上海市公安局静安分局投案自首。"
#target for below:{"death_penalty": false, "imprisonment": 10, "life_imprisonment": false}, "punish_of_money": 2000, "accusation": ["盗窃"], "relevant_articles": [264]}
content3=u"公诉机关指控：2013年11月7日11时许，被告人钟某某在佛山市高明区明城镇某某金属有限公司工作时，趁其他员工去吃午饭时将公司的19条黄铜锭从公司厂房墙角的洞口丢到外面，并于2013年11月8日2时许独自驾驶一辆女装摩托车到公司厂房墙外将其中的15条黄铜锭盗走并销赃给他人。2013年11月8日11时许，被告人钟某某以同样的方式将11条黄铜锭丢到公司厂房外面，并于2013年11月10日2时许独自驾驶一辆女装摩托车准备把剩余的15条黄铜锭盗走，行至公司厂房墙外时被伏击的公安人员抓获。公安人员扣押了上述15条黄铜锭，并已发还给被害人。经价格鉴定，被盗的30条黄铜锭共价值人民币13884元。公诉机关认为被告人钟某某无视国家法律，以非法占有为目的，盗窃他人财物，价值人民币13884元，数额较大，其行为已触犯了《中华人民共和国刑法》××之规定，应以××追究其刑事责任。在法庭上，公诉机关还详细阐述了关于指控被告人盗窃数额为13884元的相关依据和计算方法。公诉机关建议对被告人钟某某判处六个月至一年六个月××，并处罚金。提请本院依法判处。"
#{"death_penalty": false, "imprisonment": 3, "life_imprisonment": false}, "punish_of_money": 1000, "accusation": ["盗窃"], "relevant_articles": [264]}
content4=u"昆山市人民检察院指控并经本院审理查明，2014年4月17日凌晨，被告人熊某伙同冯某、张某、杨某（另案处理）至昆山市锦溪镇阮家浜村X组X号XX超市，由张某用手拉弯防盗窗栏杆，被告人熊某、张某、冯某在外望风，杨某从窗户爬进店内，窃得人民币1300余元；三星牌GT-I8552型手机1部（价值人民币904元）；南京（特醇）香烟5包（价值人民币55元）；南京（佳品）香烟5包（价值人民币75元）；黄鹤楼（硬雅香金）香烟2包（价值人民币40元）；利某（新版）香烟1包（价值人民币13元）；苏某（五星红杉树）香烟1包（价值人民币20元）。被告人熊某归案后如实供述了犯罪事实。另查明，案发后公安机关已将扣押的涉案香烟十四包、手机一部、现金人民币860元已发还被害人阮某。在本院审理期间，被告人熊某退缴人民币440元及预缴罚金保证金人民币1000元，暂扣于本院。上述事实，有公诉机关提交，并经庭审质证、认证的证人张某、冯某、杨某等人的证言，被害人阮某的陈述，昆山市价格认证中心出具的价格鉴证结论书，搜查笔录，现场勘验笔录，监控录像，扣押、发还物品清单，抓获经过，身份信息等证据予以证实，被告人熊某亦供认不讳，且与上述证据证实的事实相吻合，证据均具有证明效力，本院予以确认。"
#{"death_penalty": false, "imprisonment": 11, "life_imprisonment": false}, "punish_of_money": 0, "accusation": ["故意伤害"], "relevant_articles": [234]}
content5=u"北京市密云县人民检察院指控，被告人邓×5于2013年11月17日15时50分许，在自己家中，因琐事与尹×2发生口角，后被告人邓×5持菜刀将尹×2头部和脖子砍伤。经鉴定，尹×2身体所受损伤程度属轻伤。公诉机关向本院提供了相关证据，认为被告人邓×5有自首情节，提请依照《中华人民共和国刑法》××的规定，对被告人邓×5处罚。"
#"imprisonment": 80, "life_imprisonment": false}, "punish_of_money": 4000, "accusation": ["强奸", "盗窃"], "relevant_articles": [264]}
content6=u"河北省武安市人民检察院指控，2008年8月9日凌晨，被告人王丁某伙同张2某（在逃）合谋后，窜至武安市冶陶镇马村，趁无人之机，将张某停放在家门前的一辆邯郸牌150型拖拉机盗走，后二人将拖拉机卖到阳邑镇刘某（已判）的废品收购站，得款几千元，所得赃款平分后挥霍，经武安市价格认证中心鉴定，被盗拖拉机价值6440元。破案后，赃物被追回，退还失主。"
#{'accusation': [], 'articles': [], 'imprisonment': })
content7=u"定襄县人民检察院指控：2013年10月11日6时许，被告人李XX在自家院中用木屑、合肥料、柴油按比例炒制炸药12公斤。次日在西霍村南小沟山小沟采石点准备爆破时被公安局民警当场抓获。当场查获自制炸药14.2公斤、雷管2枚、导火索1.5米，后从其小舅子刘2某家中查获雷管58枚，导火索124米。据被告人供述，其将六、七年前开石料厂时用剩的62枚雷管、126米导火索，未上交有关部门，私自藏匿于自己家中。2012年冬（具体时间不清），其将藏匿的雷管和导火索非法储存在其位于定襄县南王乡西霍村院中的南房内。炸药是其于2013年8月份下旬、2013年9月初自己炒制的，并均于次日爆破。公诉机关为证明上述事实，提供了相应的证据材料。公诉机关认为，被告人李XX的行为构成了非法制造、储存爆炸物罪，依法提起公诉，请予以判处。"
#{"meta": {"criminals": ["李某"], "term_of_imprisonment": {"death_penalty": false, "imprisonment": 12, "life_imprisonment": false}, "punish_of_money": 0, "accusation": ["盗窃", "非法持有毒品"], "relevant_articles": [264]}, "fact":
content8=u"公诉机关指控，2015年10月15日，被告人李某因吸毒成瘾无钱购买毒品，便产生盗窃电动车变卖要钱的歹念。当晚10时许，李某窜至隆安县县城蝶城路电力人厦一楼南方电网营业厅大门前，发现被害人覃某停放在该处的一辆黑色绿源牌电动车（车型为G-M12-CS6020-Z2，车架号069321312660757)，见四周无人，便用螺丝刀撬开电动车的电门锁，将该电动车盗走藏放起来。10月17日下午，李某骑该电动车到隆安县××街购买毒品时，被公安民警抓获，当场查获被盗电动车。经隆安县价格认证中心鉴定，被害人覃某被盗电动车价值2343元。公诉机关认为，被告人李某秘密窃取他人财物，其行为触犯了《中华人民共和国刑法》××的规定，犯罪事实清楚，证据确实充分，应当以××追究其刑事责任。"
#高利转贷
cotent9=u'青岛市市南区人民检察院指控：2010年10月28日，被告人施某为获取高额利息与李某（在逃）签订借款1500万元的抵押借款合同和委托贷款协议书，' \
        u'并委托李某在银行进行贷款。同年11月16日，李某通过价值确认书，并提供了施某的结婚证、身份证、房地产权证的原件及复印件与孙某办理了燕儿岛路XX号X户的房地产他项权利证。' \
        u'同年10月至11月期间，施某欲再以燕儿岛路XX号X户房产作抵押，以青岛君平中联盟××管理有限丰农村合作银行中韩银行申请抵押贷款。' \
        u'在申请过程中，施某虚构贷款用途，在无实际业务情况下，伙同李某编造了虚假的青岛君平中联盟××管理有限公司与青岛爱购惠商贸有限公司之间的医疗设备购销合同。' \
        u'同年11月26日市房地产登记中心办理抵押手续和房地产他项权利证书，后青岛华丰农村合作银行中韩银行将1300万元抵押贷款发放至青岛君平中联盟××管理有限公司账户，' \
        u'该款项后于同日由青岛君平中联盟××管理有限公司账户汇入青岛爱失，其行为触犯了《中华人民共和国刑法》××××，应当以骗取贷款罪追究刑事责任。'
#
content10=u'经审理查明，2009年11月19日，丰某、陈某甲等人通过投标获得乐清市柳市镇翔金垟村综合大楼的租赁权，为尽快腾空被该村村民占用的大楼及在办理相关验收手续中得到便利，' \
          u'分别于2010年1月月24日主动到乐清市公安局经济犯罪侦查大队投案，并如实供述了自己的犯罪事实。同年7月27日，被告人李某甲向乐清市公安局退赃人民币80万元，该款现已上缴至本院。' \
          u'同年10月19日，被告人李某甲协助公安机关抓获犯人罪被本院判处××。上述事实，被告人李某甲在开庭审理过程中亦无异议，并有证人陈某甲、丰某、吴某、李某乙、谌某、胡某甲、李某丙、陈某乙、' \
          u'李某丁、胡某乙的证言、到案经过、银行交易明细、会议记录、招标文件。'
content_list=[content1,content2,content3,content4,content5,content6,content7,content8,cotent9,content10]
result=predict.predict(content_list)
print("length of result:",str(len(result)));
for i,e in enumerate(result):
    print(i,e)