
#load dict
import os, sys, codecs, re
import logging
from abc import ABCMeta, abstractmethod
from typing import List

dirname = os.path.dirname(__file__)


mapf = f'{dirname}/map_data/ARPA2IPA.map'
syllable_to_phone_file = f'{dirname}/map_data/pinyin_to_phone.txt'

class Mapper:
    @abstractmethod
    def convert(self, phn_arr:List) -> List:
        pass

class PinyinMapper(Mapper):
    mapper = None
    def __init__(self):
        #load dict
        if PinyinMapper.mapper is None:
            PinyinMapper.mapper = {}
            logging.info(f"loading mapper file {syllable_to_phone_file}")

            with open(syllable_to_phone_file) as f:  
                for l in f:  
                    cols = l.strip().split('\t')
                    assert(len(cols) == 2)
                    syllable = cols[0]
                    phones   = cols[1].split()
                    PinyinMapper.mapper[syllable] = phones

    def convert(self, phn_arr: List) -> List:
        arr = []
        for phn in phn_arr:
            tr_phn = phn[:-1]
            if not PinyinMapper.mapper.__contains__(tr_phn):
                arr.append(phn)
            else:
                phones = PinyinMapper.mapper[tr_phn].copy()
                phones[-1] = phones[-1]+phn[-1:]
                arr = arr + phones
        return arr

class EnMapper(Mapper):
    mapper = None
    def __init__(self):
        #load dict
        if EnMapper.mapper is None:
            logging.info(f"loading mapper file {mapf}")
            EnMapper.mapper = {}
            with codecs.open(mapf, 'r', 'utf8') as f:
                for l in f:
                    cols = l.strip().split()
                    EnMapper.mapper[cols[0]] = u' '.join(cols[1:])


    def convert(self, phn_arr:List) -> List:
        arr = []
        for phn in phn_arr:
            if not EnMapper.mapper.__contains__(phn):
                arr.append(phn)
            else:
                arr.append(EnMapper.mapper[phn])
        return arr        

