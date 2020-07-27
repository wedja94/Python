#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[2]:


arq = pd.DataFrame({'Classe': ['Nesossilicatos', 'Sorossilicatos', 'Ciclossilicatos'],
                   'Átomos de O compartilhados': [0,1,2],
                   'Arranjo das tetraedros': ['Independenes, isolados', 'Duplos, isolados', 'Anéis'],
                   'Realação Si:O': ['1:4','2:7', '1:3'],
                   'Exemplos': ['Olivina,(Mg,Fr)2SiO4', 'Hemimorfita, Zn4(Si2O7)(OH)2,H20',
                                'Turmalina, NaMg3Al6(OH)4(BO)3Si6O18']})
arq


# In[3]:


estilo =  sns.light_palette("yellow", as_cmap=True)


# In[4]:


estilo1 = arq.style.background_gradient(cmap=estilo)
estilo1


# In[ ]:




