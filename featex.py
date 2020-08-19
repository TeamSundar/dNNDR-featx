#!E:\Projects\DrugTargetNN python
# -*- coding: utf-8 -*-

# Import essential libraries
import pandas as pd
from bioservices.kegg import KEGG
from functions import process
from tqdm import tqdm
import wget
import os
import os.path
import re

# Data sources from url: 'http://web.kuicr.kyoto-u.ac.jp/supp/yoshi/drugtarget/
url={'url_enzyme':'http://web.kuicr.kyoto-u.ac.jp/supp/yoshi/drugtarget/bind_orfhsa_drug_e.txt'\
    ,'url_ionchannel':'http://web.kuicr.kyoto-u.ac.jp/supp/yoshi/drugtarget/bind_orfhsa_drug_ic.txt'\
    ,'url_gpcr':'http://web.kuicr.kyoto-u.ac.jp/supp/yoshi/drugtarget/bind_orfhsa_drug_gpcr.txt'\
    ,'url_NR':'http://web.kuicr.kyoto-u.ac.jp/supp/yoshi/drugtarget/bind_orfhsa_drug_nr.txt'}

if os.path.isfile('data/url_enzyme.txt')\
    and os.path.isfile('data/url_gpcr.txt')\
    and os.path.isfile('data/url_ionchannel.txt')\
    and os.path.isfile('data/url_NR.txt'):
    print ("Files found")
else:
    print ("Downloading files!!")
    for key,value in url.items():
        wget.download(value,'data/'+key+'.txt')
    print('Files Downloaded!!')

#Initialize object
print('******************Initalizing Object*******************')
obj=process()

#Import data
enzyme = obj.import_data('data/url_enzyme.txt')
gpcr = obj.import_data('data/url_gpcr.txt')
ionchannel = obj.import_data('data/url_ionchannel.txt')
NR = obj.import_data('data/url_NR.txt')

#****************Extract features from protein sequence*************

print('Extracting features from protein sequences!')
fset=pd.DataFrame()
protein_list=enzyme.geneID.unique()
# desc=['AAC', 'CKSAAP', 'CTDC', 'CTDD', 'CTDT', 'DDE', 'DPC', 'GAAC', 'GDPC', 'GTPC', 'TPC', 'QSOrder', 'KSCTriad', 'CTriad']
type='CTriad'
#for type in tqdm(desc):
for id in tqdm(protein_list):
    obj.id2seq(id)
    obj.seq2des('dummy.txt', type)
    enc=pd.read_csv('encoding.tsv', delimiter='\t', encoding='utf-8')
    enc['#']=id
    fset=fset.append(enc)

fset.to_csv('extracted_feats_enzyme/fset_enzyme_'+ type + '.csv')

#****************Extract features from mol file********************

drug_list=ionchannel.drugID.unique()
print('Found '+str(len(drug_list))+' unique drugs in file.')
print('Converting drugID to mol file!!')
for drug in tqdm(drug_list):
    obj.id2mol(drug)

print('Extracting descriptors!!')
files=os.listdir('drugs_ionchannel')
fset_mol=pd.DataFrame()
for mol in tqdm(files):
    descriptors=obj.mol2des('drugs_ionchannel/'+mol)
    #print(descriptors)
    fset_mol=fset_mol.append(descriptors)
fset_mol.to_csv('extracted_feats_ionchannel/fset_mol_gpcr.csv')

print('Data processed!!')
