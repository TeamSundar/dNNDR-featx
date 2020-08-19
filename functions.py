#!E:\Projects\DrugTargetNN python
# -*- coding: utf-8 -*-

# Import essential libraries
import pandas as pd
from bioservices.kegg import KEGG
from rdkit import Chem
from rdkit.ML.Descriptors.MoleculeDescriptors import MolecularDescriptorCalculator as md
from rdkit import DataStructs
import rdkit
import wget
import re
import os

class process:
    def __init__(self):
        pass

    #function to import and process data
    def import_data(self, file):
        data = pd.read_csv(file, sep='\t', header = None)
        data.columns=['geneID', 'drugID']
        return data

    # Function to extract mol file from drug ID
    def id2mol(self,id,path):
        u='https://www.genome.jp/dbget-bin/www_bget?-f+m+drug+'+ id
        wget.download(u, path+'/'+str(id)+'.mol')
        return None

    # Function to extract amino acid sequence from ID
    def id2seq(self, hsa):
        s = KEGG()
        d = s.get(hsa)
        dict_d = s.parse(d)
        pattern = re.compile(r'\s+')
        try:
            seq = re.sub(pattern, '', dict_d['AASEQ'])
        except:
            seq=''
        #print('SEQ:', seq)
        text_file = open("dummy.txt", "w")
        text_file.write('>'+str(hsa)+'\n'+seq)
        text_file.close()
        return None
    
    #Extract descriptors from amino acid sequences
    def seq2des(self, seq, type):
        push ='python iFeature/iFeature.py --file %s --type %s'%(seq, type)
        os.system(push) 
        return None
    
    #Extract descriptors from mol file
    def mol2des(self, mol):
        attribs=['MolLogP','NOCount','NHOHCount','MolWt','NumRotatableBonds','TPSA']
        calc = md(attribs)
        m = Chem.MolFromMolFile(mol)
        des=pd.DataFrame(calc.CalcDescriptors(m)).T
        des.columns=attribs
        des['Drug'] = str(mol)
        return des