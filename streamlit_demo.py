import streamlit as st
import pandas as pd
import numpy as np

example_df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

example_array = np.random.randn(50, 20)

st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.write("This is a pandas DataFrame as st.dataframe:")
st.dataframe(example_df)
st.write("This is a pandas DataFrame as a table:")
st.table(example_df)
st.write("This is a Numpy array:")
st.write(example_array)
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
