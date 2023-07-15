from g2p_zh_en.mapper import EnMapper,PinyinMapper
from pypinyin import pinyin, lazy_pinyin, Style
from typing import List
import cn2an
import re
from .g2p_en import G2p
g2p = G2p()


"""Main module."""
class G2P:
    def __init__(self):
        self.pinyin_mapper = PinyinMapper()
        self.en_mapper = EnMapper()

    #pinyin cannot handle, forward to g2p_en
    def __no_pinyin(self,ch):
        ch = ch.lower()
        ch = re.sub("[^ a-z'.,?!\-。，！]", "", ch)
        pout = g2p(ch)
        out = self.en_mapper.convert(pout)
        if re.match("[a-z]",ch):
            out.extend(['_'])
        return out
    
    #english cannot handle, forward to pinyin
    def __no_eng(self,ch):
        text = cn2an.transform(ch, "an2cn")
        pout = lazy_pinyin(text, style=Style.TONE3, neutral_tone_with_five=True)
        out = self.pinyin_mapper.convert(pout)
        return out

    def g2p(self,language='zh-cn',text:str=None) -> List:
        if language == 'zh-cn':
            #try transform
            text = cn2an.transform(text, "an2cn")
            pout = lazy_pinyin(text, style=Style.TONE3, neutral_tone_with_five=True, errors=self.__no_pinyin)
            out = self.pinyin_mapper.convert(pout)
            return out
        elif language == 'en-us':
            #try transform chinese letter to pinyin
            # carr = lazy_pinyin(text, style=Style.TONE3, neutral_tone_with_five=True)
            # text = " ".join([s.strip() for s in carr])
            pout = g2p(text,no_handler=self.__no_eng)
            out = self.en_mapper.convert(pout)
            return out
        else:
            raise Exception(f"language={language} not supported")



