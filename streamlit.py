# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:34:36 2021

@author: inher
"""

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


left_comuln, right_column = st.beta_columns(2)
button = left_comuln.button('show button')
if button:
    right_column.write('Here is the right column')


st.title('Streamlit 超入門')
st.write('DataFrame')
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c'])

expander = st.beta_expander('Inquiry')
expander.write('write inquiry')

st.write('Display Image')
if st.checkbox('Show image'):
    img = Image.open('5. MAY.jpg')
    st.image(img, caption = 'sample picture', use_column_width=True)

st.write('Interactive widgets')
option = st.selectbox('Choose your favorite number', list(range(1,11)))
'Your favorite number is ', option, '!'

text = st.text_input('Your hobby is?')
'Your hobby is :', text

condition = st.slider('your condition is?',0,100,50)
'Your condition is :', condition
#st.dataframe(df, width = 100, height = 100)
#st.table(df)
#st.line_chart(df)


#df1 = pd.DataFrame(
#    np.random.rand(100,2)/[50,50]+[35.69,139.70],
#    columns=['lat','lon'])

#st.map(df1)


"""

# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

