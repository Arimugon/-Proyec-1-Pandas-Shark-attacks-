#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import csv
pd.set_option('display.max_rows', None) 
pd.set_option('display.max_columns', None) 
import re
import sharkattacks2 as sa


# In[12]:


#funcion para limpiar los date

patron='\d+.\d+.\d+'
def timebad(x):
    cont=0
    num=re.findall(patron,x)
    num=''.join(num)
    if num=='':
        cont=0
        
    elif num in x:
        cont+=1
        
    if cont==0:
        return 'unknown'
    elif cont==1:
        return str(num)


# In[13]:


#función para limpiar years

def years(x):
    if x==0:
        return 'unkwnon'
    else:
        return x
        


# In[14]:


#función para limpiar activity


def cleanact(x):
    dicc_actividades = {"Fishing":re.search(".*[Ff](ishing|ISHING).*",str(x)),
                    "Swimming":re.search(".*[Ss](wimming|WIMMing).*",str(x)),
                    "Kite":re.search(".*[Kk](ite|ITE).*",str(x)),
                    "Walking":re.search(".*[Ww](alking|ALKING).*",str(x)),
                    "Boogie Board":re.search(".*[Bb](oogie|OOGIE).*",str(x)),
                    "Body Boarding":re.search(".*[Bb](ody|ODY).*",str(x)),
                    "Wind Surfing":re.search(".*[wW](ind|IND).*",str(x)),
                    "Boat":re.search(".*[Bb](oat|OAT).*",str(x)),
                    "Interact with sharks":re.search(".*[Ss](hark|HARK).*",str(x)),
                    "Diving":re.search(".*[Dd](iving|IVING).*",str(x)),
                    "Standing in water":re.search(".*[Ss](tand|TAND).*",str(x)),
                    "Paddling":re.search(".*[Pp](addl|ADDL).*",str(x)),
                    "Bathing":re.search(".*[Bb](athing|ATHING).*",str(x)),
                    "OverBoard":re.search(".*[Oo](verb|VERB).*",str(x)),
                    "Bathing":re.search(".*[Bb](athing|ATHING).*",str(x)),
                    "Floating":re.search(".*[Ff](loat|LOAT).*",str(x)),
                    "Jumping":re.search(".*[Jj](ump|UMP).*",str(x))}

    
    for key,values in dicc_actividades.items():
        if values:
            return key
    return "other"


# In[15]:


#funciones para limpiar name:

def nombres(x):
    
        if x=='male':
            return 'Unkwnon'
        elif x=='female':
            return 'Unkwnon'   
        else:
            return x


# In[16]:


def nombrecitos(name):
        if re.search("^[A-Z].+",str(name)):
            return name
        else:
            return 'unknown'


# In[17]:


#función limpieza href:

def htpp(x):
    if re.search("^https?://",str(x)):
        return x
    else:
        return 'Unknown'


# In[18]:


#función limpieza injury:

def limpiar_injury(x):
    dicc_injurys = {"No Injury":re.search(".*[Nn](o|O)\s*[Ii](njury|NJURY).*",str(x)),
                    "Minor Injury":re.search(".*[Mm](inor|INOR).*",str(x)),
                    "Fatal":re.search(".*[Ff](atal|ATAL).*",str(x)),
                    "Cuts":re.search(".*[Cc](uts|UTS).*",str(x)),
                    "Laceration":re.search(".*[Ll](aceration|ACERACION).*" or ".*[Aa](brasion|BRASION).*",str(x)),
                    "Bitten":re.search(".*[Bb](itten|ITTEN).*" or ".*[Bb](ite|ITE).*"or".*[Nn](ipped|IPPED).*",str(x)),
                    "Puncture wounds":re.search(".*[Pp](uncture|UNCTURE).*",str(x)),
                    "Injury in  leg":re.search(".*[Ii](njury|NJURY).*"and".*[Ll](eg|EG).*",str(x)),
                    "Injury in hand":re.search(".*[Ii](njury|NJURY).*"and".*[Hh](and|AND).*",str(x)),
                    "Injury in arm":re.search(".*[Ii](njury|NJURY).*" and ".*[Aa](rm|RM).*",str(x)),
                    "Injury in ankle":re.search(".*[Ii](njury|NJURY).*" and ".*[Aa](nkle|nkle).*",str(x)),
                    "Injury in foot":re.search(".*[Ii](njury|NJURY).*" and ".*[Ff](oot|OOT).*",str(x)),
                    "Injury in calf":re.search(".*[Ii](njury|NJURY).*" and ".*[Cc](alf|ALF).*",str(x)),
                    "Broken bones ":re.search(".*[Bb](roken|ROKEN).*" or ".*[Bb](ones|ONES).*",str(x)),
                    "Injury":re.search(".*[Ii](njury|NJURY).*",str(x)),
                    "Collision":re.search(".*[Cc](ollision|OLLISION).*" or ".*[Cc](ollided|OLLIDED).*",str(x)),
                    "Severe Injury":re.search(".*[Ss](evere|EVERE).*" or ".*[Ss](erius|ERIUS).*" and ".*[Ii](njury|NJURY).*",str(x))}

    
    for key,values in dicc_injurys.items():
        if values:
            return key
        
    return "Unknown"


# In[19]:


#función limpieza time:

def times(x):
    if re.search("\d+h\d+",str(x)):
        return x
    else:
        return 'Unknown'
        
        


# In[20]:


#función limpieza species:

def limpiar_species(x):
    dicc_especies = {
            "White shark":re.search(".*[Ww](hite|HITE).*",str(x)),
            "Tiger shark":re.search(".*[Tt](iger|IGER).*",str(x)),
            "Lemon shark":re.search(".*[Ll](emon|EMON).*",str(x)),
            "Hammerhead shark":re.search(".*[Hh](ammerhead|AMMERHEAD).*",str(x)),
            "Bull shark":re.search(".*[Bb](ull|ULL).*",str(x)),
            "Blue shark":re.search(".*[Bb](lue|LUE).*",str(x)),
            "Silvertip shark":re.search(".*[Ss](ilvertip|ILVERTIP).*",str(x)),
            "Nurse shark":re.search(".*[Nn](urse|URSE).*",str(x)),
            "Whaler shark":re.search(".*[Ww](haler|HALER).*",str(x)),
            "Blacktip shark":re.search(".*[Bb](lacktip|LACKTIP).*",str(x)),
            "Mako shark":re.search(".*[MM](ako|AKO).*",str(x)),
            "Sand shark":re.search(".*[Ss](and|AMD).*",str(x)),
            "Wobbegong shark":re.search(".*[Ww](obbegong|OBBEGONG).*",str(x)),
            "Galapagos shark":re.search(".*[Gg](alapagos|ALAPAGOS).*",str(x)),
            "Grey shark":re.search(".*[Gg](rey|REY).*",str(x)),
            "Leopard shark":re.search(".*[Ll](eopard|EOPARD).*",str(x)),
            "Zambesi shark":re.search(".*[Zz](ambesi|AMBESI).*",str(x)),
            "Blacktail shark":re.search(".*[Bb](lacktail|LACKTAIL).*",str(x)),
            "Red shark":re.search(".*[Rr](ed|ED).*",str(x)),
            "Dusky shark":re.search(".*[Dd](usky|USKY).*",str(x)),
            "Raggedtooth shark":re.search(".*[Rr](aggedtooth|AGGEDTOOTH).*",str(x)),
            "Spinner shark":re.search(".*[Ss](pinner|PINNER).*",str(x)),
            "Cow shark":re.search(".*[Cc](ow|OW).*",str(x)),
            "Porbeagle shark":re.search(".*[Pp](orbeagle|ORBEAGLE).*",str(x)),
            "Caribbean reef shark":re.search(".*[Cc](aribbean|ARIBBEAN).*",str(x)),
            "Sandbar shark":re.search(".*[Ss](and|AND).*",str(x)),
            "Silky shark":re.search(".*[Ss](ilky|ILKY).*",str(x)),
            "Zambezi shark":re.search(".*[Zz](ambezi|AMBEZI).*",str(x)),
            "Sevengill shark":re.search(".*[Ss](evengill|EVENGILL).*",str(x)),
            "Copper shark":re.search(".*[Cc](opper|OPPER).*",str(x)),
            "Angel shark":re.search(".*[Aa](ngel|NGEL)\s",str(x)),
            "Salmon shark":re.search(".*[Ss](almon|ALMON).*",str(x)),
            "Goblin shark":re.search(".*[Gg](oblin|OBLIN).*",str(x)),
            "Thresher shark":re.search(".*[Tt](hresher|HRESHER).*",str(x)),
            "Dogfish shark":re.search(".*[Dd](ogfish|OGFISH).*",str(x)),
            "Involvement not confirmed":re.search("[^.?!]*involvement[^.?!]*",str(x))}
    for key,values in dicc_especies.items():
        if values:
            return key

    return "other_specie"

