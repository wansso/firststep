import streamlit as st

st.title('MBTI 특성 및 궁합 알아보기')

# 사용자 입력 받기
name = st.text_input('이름을 입력해주세요!')
mbti = st.selectbox('당신의 MBTI를 선택해주세요!', 
                    ['INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP', 
                     'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP'])

if st.button('특성 및 궁합 분석하기'):
    # MBTI 유형에 따른 특성 및 궁합 설명
    if mbti == 'INTJ':
        description = 'INTJ는 독립적이고 전략적인 사고를 가진 유형으로, 미래를 계획하고 목표를 향해 나아갑니다.'
        best_match = 'ENFP'
        worst_match = 'ESFP'
    elif mbti == 'INTP':
        description = 'INTP는 분석적이고 논리적인 사고를 중요시하며, 지적 호기심이 많은 유형입니다.'
        best_match = 'ENTJ'
        worst_match = 'ESFJ'
    # 다른 MBTI 유형에 대한 설명 추가
    # ...
    # 아래에 각 유형에 따른 특성, 잘 맞는 유형, 맞지 않는 유형을 추가
    # ...

    # 사용자에게 결과 보여주기
    st.write(f'{name}님! 당신의 MBTI 유형은 {mbti}입니다.')
    st.write(description)
    st.write(f'가장 잘 맞는 MBTI 유형: {best_match}')
    st.write(f'가장 맞지 않는 MBTI 유형: {worst_match}')

