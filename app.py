import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 设置页面配置
st.set_page_config(
    page_title="网易云音乐榜单数据分析大屏",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: bold;
        color: #e84393;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .sub-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #6c5ce7;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        padding: 20px;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# 标题
st.markdown('<div class="main-header">🎵 网易云音乐榜单数据分析大屏</div>', unsafe_allow_html=True)

# 创建标签页
tab1, tab2, tab3, tab4 = st.tabs(["📊 榜单概览", "🎤 歌手分析", "📈 趋势洞察", "🔍 数据详情"])

with tab1:
    # 第一行：关键指标
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>总播放量</h3>
            <h1>245亿+</h1>
            <p>所有榜单累计播放</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>总歌曲数</h3>
            <h1>850+</h1>
            <p>所有榜单歌曲总和</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>总收藏量</h3>
            <h1>2250万+</h1>
            <p>所有榜单收藏总量</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>MV歌曲占比</h3>
            <h1>15.3%</h1>
            <p>有MV的歌曲比例</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 第二行：图表
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="sub-header">各榜单播放量对比</div>', unsafe_allow_html=True)
        chart_data = pd.DataFrame({
            '榜单': ['热歌榜', '飙升榜', '新歌榜', '原创榜', '中文说唱榜', '电音榜', '古典榜', '全球说唱榜', '潮流风向榜'],
            '播放量(亿)': [135.01, 63.48, 31.59, 6.11, 5.17, 4.05, 0.75, 0.02, 0.05]
        })
        
        fig = px.bar(chart_data, x='榜单', y='播放量(亿)',
                    color='播放量(亿)',
                    color_continuous_scale='viridis',
                    height=400)
        fig.update_layout(title_text="各榜单播放量分布", title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('<div class="sub-header">各榜单歌曲数量</div>', unsafe_allow_html=True)
        songs_data = pd.DataFrame({
            '榜单': ['热歌榜', '飙升榜', '新歌榜', '原创榜', '中文说唱榜', '古典榜', '电音榜', '全球说唱榜', '潮流风向榜'],
            '歌曲数量': [200, 100, 100, 100, 50, 100, 50, 10, 10]
        })
        
        fig = px.pie(songs_data, values='歌曲数量', names='榜单',
                    hole=0.3,
                    color_discrete_sequence=px.colors.sequential.RdBu)
        fig.update_layout(title_text="各榜单歌曲数量占比", title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
    
    # 第三行：MV分析
    st.markdown('<div class="sub-header">MV分布情况</div>', unsafe_allow_html=True)
    
    mv_data = pd.DataFrame({
        '榜单': ['热歌榜', '飙升榜', '新歌榜', '原创榜', '中文说唱榜', '古典榜', '电音榜'],
        '有MV': [45, 12, 8, 6, 3, 2, 0],
        '无MV': [155, 88, 92, 94, 47, 98, 50]
    })
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=mv_data['榜单'],
        y=mv_data['有MV'],
        name='有MV',
        marker_color='#e84393'
    ))
    fig.add_trace(go.Bar(
        x=mv_data['榜单'],
        y=mv_data['无MV'],
        name='无MV',
        marker_color='#6c5ce7'
    ))
    
    fig.update_layout(
        barmode='stack',
        title="各榜单MV分布情况",
        xaxis_title="榜单名称",
        yaxis_title="歌曲数量",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    # 歌手分析
    st.markdown('<div class="sub-header">热门歌手排行榜</div>', unsafe_allow_html=True)
    
    hot_artists = pd.DataFrame({
        '歌手': ['周深', '薛之谦', '郑润泽', '陈奕迅', '林俊杰', '王齐铭WatchMe', '艾志恒Asen', 'GALI', '马思唯', '陈粒'],
        '上榜次数': [28, 15, 14, 12, 10, 9, 8, 7, 7, 6],
        '主要榜单': ['新歌榜/热歌榜/原创榜', '热歌榜/新歌榜', '热歌榜/新歌榜/飙升榜', '热歌榜/飙升榜', '热歌榜/飙升榜', '中文说唱榜/新歌榜', '中文说唱榜', '中文说唱榜/新歌榜', '中文说唱榜/新歌榜', '热歌榜/飙升榜']
    })
    
    # 显示热门歌手表格
    st.dataframe(hot_artists, use_container_width=True, height=400)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="sub-header">歌手上榜次数TOP10</div>', unsafe_allow_html=True)
        fig = px.bar(hot_artists.head(10), x='歌手', y='上榜次数',
                    color='上榜次数',
                    color_continuous_scale='plasma',
                    height=400)
        fig.update_layout(title_text="歌手上榜次数排名", title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('<div class="sub-header">多榜单歌手分布</div>', unsafe_allow_html=True)
        
        multi_chart_data = pd.DataFrame({
            '上榜榜单数量': [1, 2, 3, 4],
            '歌手数量': [320, 85, 25, 8]
        })
        
        fig = px.pie(multi_chart_data, values='歌手数量', names='上榜榜单数量',
                    title="歌手跨榜单分布",
                    color_discrete_sequence=px.colors.sequential.Rainbow)
        fig.update_layout(title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    # 趋势洞察
    st.markdown('<div class="sub-header">音乐类型热度分析</div>', unsafe_allow_html=True)
    
    genre_data = pd.DataFrame({
        '音乐类型': ['流行音乐', '说唱音乐', '电音', '古典音乐', '民谣', '摇滚', 'R&B', '其他'],
        '歌曲数量': [420, 180, 50, 100, 65, 30, 25, 15],
        '平均播放量(万)': [850, 620, 480, 120, 350, 280, 410, 200]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(genre_data, x='音乐类型', y='歌曲数量',
                    color='歌曲数量',
                    color_continuous_scale='sunset',
                    title="各音乐类型歌曲数量",
                    height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.line(genre_data, x='音乐类型', y='平均播放量(万)',
                    markers=True,
                    title="各音乐类型平均播放量",
                    height=400,
                    line_shape='spline')
        fig.update_traces(line=dict(color='#e84393', width=4))
        st.plotly_chart(fig, use_container_width=True)
    
    # 时间趋势分析
    st.markdown('<div class="sub-header">发布时间分析</div>', unsafe_allow_html=True)
    
    time_data = pd.DataFrame({
        '发布类型': ['新歌首发', 'Live版本', '重新编曲', '经典重录', '合作版本', 'Remix版本'],
        '数量': [180, 120, 85, 60, 95, 45],
        '增长率%': [25.3, 18.7, 12.5, 8.9, 22.1, 15.6]
    })
    
    fig = go.Figure(data=[
        go.Bar(name='数量', x=time_data['发布类型'], y=time_data['数量'], marker_color='#6c5ce7'),
        go.Scatter(name='增长率%', x=time_data['发布类型'], y=time_data['增长率%'], 
                  yaxis='y2', mode='lines+markers', line=dict(color='#e84393', width=3))
    ])
    
    fig.update_layout(
        title="不同发布类型的歌曲数量及增长率",
        yaxis=dict(title="歌曲数量"),
        yaxis2=dict(title="增长率%", overlaying='y', side='right'),
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    # 数据详情
    st.markdown('<div class="sub-header">榜单数据详情表</div>', unsafe_allow_html=True)
    
    # 创建示例数据表
    sample_data = pd.DataFrame({
        '榜单名称': ['热歌榜', '飙升榜', '新歌榜', '原创榜', '网易云中文说唱榜', '网易云古典榜', '网易云电音榜', '网易云全球说唱榜', '潮流风向榜'],
        '收藏量': ['12,691,782', '4,172,750', '2,790,101', '728,562', '812,732', '440,795', '1,311,832', '4,157', '4,785'],
        '转发量': ['64,897', '16,818', '13,877', '12,917', '6,613', '3,906', '13,396', '44', '47'],
        '评论量': ['311,600', '225,998', '157,187', '14,338', '20,411', '5,065', '43,566', '114', '75'],
        '歌曲数量': [200, 100, 100, 100, 50, 100, 50, 10, 10],
        '播放次数': ['135亿', '63.5亿', '31.6亿', '6.11亿', '5.17亿', '0.75亿', '4.05亿', '0.02亿', '0.05亿']
    })
    
    st.dataframe(sample_data, use_container_width=True, height=400)
    
    # 播放量排行榜图表
    st.markdown('<div class="sub-header">播放量排行榜</div>', unsafe_allow_html=True)
    
    chart_df = sample_data.copy()
    chart_df['播放次数_数值'] = chart_df['播放次数'].str.replace('亿', '').astype(float)
    chart_df = chart_df.sort_values('播放次数_数值', ascending=False)
    
    fig = px.bar(chart_df, x='榜单名称', y='播放次数_数值',
                title="播放次数排行榜",
                color='播放次数_数值',
                color_continuous_scale='thermal')
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

# 页脚
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>网易云音乐榜单数据分析大屏 | 数据来源：网易云音乐官方榜单</p>
    <p>数据时间：2025年11月 | 技术支持：Streamlit + Plotly</p>
</div>
""", unsafe_allow_html=True)