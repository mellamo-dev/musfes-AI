import streamlit as st
import pandas as pd

mat = pd.read_csv('mat.csv',index_col=0)
time_table = pd.read_csv('time_table.csv',index_col=0)
time_table.fillna('_',inplace=True)
time_table2 = pd.read_csv('time_table2.csv',index_col=0)
time_table2.fillna('_',inplace=True)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
options = []

def change_color_background(val):
    if val in options:
        color = (0,0,255,0.5)
    elif val == '_' or val not in options_dic.keys():
        color = (255,0,0,0)
    else:
        color = (255,0,0,options_dic[val]/normal_num)
        print(options_dic[val])
        print(options_dic[val]/normal_num)
    return 'background-color: rgba{}'.format(color)

st.title('夏フェスAI予測')
st.write('もうすぐ待ちに待った音楽フェス！ウキウキで回る順番を考えていますね！')
st.write('しかし、音楽好きのあなたでも「この時間は知らないアーティストばかりだ、、」と落ち込んでしまうかもしれません。')
st.write('でもそれは、新しい音楽と出会えるチャンスかも！')
st.write('あなたがきっと気に入るだろうアーティストをAIが予測します！')

st.subheader('サマソニ2022')

options = st.multiselect(
    '既に見に行く予定のアーティストを教えてください',
    ['Novelbright', 'Mrs. GREEN APPLE', 'Måneskin', 'King Gnu', 'The 1975',
       'Chilli Beans.', 'chilldspot', 'Sambomaster', 'HENTAI SHINSHI CLUB',
       'never young beach', 'Tahiti 80', 'KIRINJI', 'CVLTE',
       'The Linda Lindas', '渋谷すばる', 'BLUE ENCOUNT', 'All Time Low', 'Fishbone',
       'The Offspring', 'MAN WITH A MISSION', 'Doul',
       'CHAMELEON LIME WHOOPIEPIE', 'CHAI', 'Squid', 'Awesome City Club',
       'Vaundy', 'Aimer', 'Kacey Musgraves', 'St. Vincent', 'Who-ya Extended',
       'Regal Lily', 'WONFU', 'Billkin', 'RAISE A SUILEN', 'BAND-MAID',
       'Fear, and Loathing in Las Vegas', 'HYDE', 'PIGGS', 'beabadoobee',
       'Rina Sawayama', 'WENDY', '神使轟く、激情の如く。', 'BRIDEAR', 'ザ・リーサルウェポンズ',
       'ASH DA HERO', 'バックドロップシンデレラ', 'yonawo', 'OCTPATH', 'BE:FIRST',
       'THE ORAL CIGARETTES', 'The Struts', 'YUNGBLUD', 'WANIMA',
       'Megan Thee Stallion', 'ONE OK ROCK', 'Post Malone', 'Black Leech',
       'NOA', 'MONONKVL', 'Omoinotake', 'chelmico', 'iri', 'Def Tech', 'STUTS',
       'Motohiro Hata', 'Mississippi Khaki Hair', 'Yuuri', 'easy life',
       '3OH!3', 'TOMORROW X TOGETHER', 'milet', 'Kula Shaker',
       'ASIAN KUNG-FU GENERATION', 'Primal Scream', '新東京', 'Hitsujibungaku',
       'salem ilese', 'CHANMINA', 'Griff', 'QUEEN BEE', 'ENDRECHERI', 'CL',
       'Carly Rae Jepsen', 'SARM', 'Tani Yuuki', 'Liella!', 'KANGDANIEL',
       'KANDYTOWN', 'Novel Core', 'Kyary Pamyu Pamyu', 'ZICO',
       'Okazaki Taiiku', 'Lyrical Lily', 'Kolokol', 'DAISY', 'FRUITS ZIPPER',
       'BATTEN GIRLS', '22/7'])

col = mat.columns
options_dic = dict(mat[options].sum(axis=1))
normal_num = max(options_dic.values())

st.info('選択したアーティストは青で表示されます。赤が濃くなるほど、あなたが気に入る可能性が高いです。')

st.subheader('1日目')
st.table(time_table.style.applymap(change_color_background))

st.subheader('2日目')
st.table(time_table2.style.applymap(change_color_background))
