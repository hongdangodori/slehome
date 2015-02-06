from collections import OrderedDict

class Markdown() :
    edit_url = '/sle/wiki/edit/'

    # 제목 태그
    token1 = {
        '==' : ['<span id="','">&nbsp;</span><br /><br /><b style="font-size:2.5em;">', '</b>&nbsp;&nbsp;&nbsp;<a href="'+edit_url, '/">[Edit]</a><hr />', '2단계 제목', '== 제목 =='],     # 타이틀1
        '===' : ['<span id="','">&nbsp;</span><br /><br /><b style="font-size:1.5em;">', '</b>&nbsp;&nbsp;&nbsp;<a href="'+edit_url, '/">[Edit]</a><br />', '3단계 제목', '=== 제목 ==='],         # 타이틀2
        '====' : ['<span id="','">&nbsp;</span><br /><br /><b style="font-size:1.0em;">', '</b>&nbsp;&nbsp;&nbsp;<a href="'+edit_url, '/">[Edit]</a><br />', '4단계 제목', '==== 제목 ====']       # 타이틀 3
        }

    # 단일 태그
    token2 = {
        '----' : '<hr />',              # 수평선 태그
        '\r\n\r\n' : '<p /><br />',     # 개행하기
        '\n\n' : '<p /><br />'          # 개행하기
        }
    # 링크 태그
    token3 = {
        '[[' : [']]', '<a href="/sle/wiki/page/', '/">', '</a>', '안쪽 링크', '[[문서 이름]]'],        # 내부 링크 걸기
        '[[[' : [']]]', '<a href="', '" target=new>', '</a>', '바깥 링크', '[[[http://hisnet.handong.edu]]]'],      # 외부 링크 걸기
        '[youtube]((' : ['))', '<br /><iframe width="420" height="315" src="//www.youtube.com/embed/', '" frameborder="0" allowfullscreen>', '</iframe><br />', '유튜브 링크', '[youtube]((https://www.youtube.com/watch?v=qR90tdW0Hbo))'],        # 유튜브 영상 링크
        '[image]((' : ['))', '<br /><img src="', '', '" class="img-rounded" style="width:20%;height:20%"></img><br />', '이미지 링크', '[image]((http://hisnet.handong.edu/2012_images/tmenu_center.jpg))']     # 이미지 링크
        }

    def markdown(page_name, text) :
        token_1 = OrderedDict(sorted(Markdown.token1.items(), key = lambda t : t[0], reverse = True))         # key 순으로 정렬 (원래 dictionary는 key 순으로 정렬되지 않음)
        token_2 = Markdown.token2
        token_3 = OrderedDict(sorted(Markdown.token3.items(), key = lambda t : t[0], reverse = True))         # key 순으로 정렬 (원래 dictionary는 key 순으로 정렬되지 않음)

        edit_url2 = Markdown.edit_url + page_name

        for tok in token_1.keys() :      # edit url 변경
            token_1[tok][2] = token_1[tok][2] + page_name + '/'

        # 타이틀 별로 우선 순위 정하기 위해
        token_enum = {
            '==' : 2,
            '===' : 3,
            '====' : 4
            }

        # 줄 단위로 나누기
        words = text.split('\r\n')

        dic = {}        # 바뀐 content 리턴하기 위해
        context = []    # 차례 지정
        section = 0     # 타이틀 별로 섹션 나누기

        lines = 0       # 현재 줄의 수
        new_text = ''   # 바뀐 content 저장하기 위해
        name = ''

        ########## 이 부분에 관해서 예외 처리 해야됨....
        # 차례 표시할 때 숫자 매기기
        first = 0
        second = 0
        third = 0

        for w in words :
            lines += 1      # 한 줄 증가
            for tok in token_1.keys() :
                # 토큰으로 파티션 나누기
                par = w.partition(tok)      # 왼쪽에서 tok 기준으로 두개의 문자열로 나눔
                rpar = w.rpartition(tok)    # 오른쪽에서 tok 기준으로 두개의 문자열로 나눔

                # 양 끝에 토큰이 있는지 없는지 확인
                if (par[0] == '') and (par[1] == tok) and (rpar[1] == tok) and (rpar[2] == '') :
                    section += 1                            # 타이틀이 존재하므로 섹션 증가
                    title = par[2].rpartition(tok)[0]       # 타이틀 저장

                    # 목차에 나올 숫자 계산
                    if token_enum[tok] <= 4 :
                        third += 1
                        if token_enum[tok] <= 3 :
                            second, third = second + 1, 0
                            if token_enum[tok] == 2 :
                                first, second, third = first + 1, 0, 0

                    context += [{
                        'tok' : token_enum[tok],    # 타이틀 우선순위
                        'section' : section,        # 섹션
                        'line' : lines,             # 줄 수
                        'next_line' : -1,           # 다음 줄 수(default 값)
                        'title' : title,            # 타이틀
                        'number' : [first, second, third]   # 차례 앞에 숫자
                        }]

                    # 토큰을 태그로 교체
                    words[lines - 1] = words[lines - 1].replace(tok, token_1[tok][0] + str(section) + token_1[tok][1], 1)
                    words[lines - 1] = (token_1[tok][2] + str(section) + token_1[tok][3]).join(words[lines - 1].rsplit(tok, 1))

                    break

            # 링크 토큰을 태그로 교체
            for tok in token_3 :
                # 토큰이 있는지 없는지 확인
                while words[lines - 1].partition(tok)[1] != '' :
                    link = words[lines - 1].partition(tok)[2].partition(token_3[tok][0])[0]
                    # 유튜브 링크인 경우
                    if 'watch?v=' in link :
                        link = link.partition('watch?v=')[2]
                    # 이미지 태그인 경우
                    elif tok == '[image]((' :
                        link = ''
                    # 토큰을 태그로 교체
                    words[lines - 1] = words[lines - 1].replace(tok, token_3[tok][1] + link + token_3[tok][2], 1)
                    words[lines - 1] = words[lines - 1].replace(token_3[tok][0], token_3[tok][3], 1)

            new_text += words[lines - 1] + '\r\n'
        new_text = ''.join(new_text.rsplit('\r\n', 1))      # 맨 뒤에 개행 삭제

        # 태그 교체
        for tok in token_2 :
            new_text = new_text.replace(tok, token_2[tok])

        context = Markdown.make_context(context, lines)      # 차례 생성
        dic['context'] = context['context']         # 차례
        dic['edit'] = context['edit']               # 부분편집 범위
        dic['content'] = new_text                   # 마크다운 적용 된 내용

        return dic

    def EditManual() :      # 마크다운 설명서
        manual = ['', '']
        token = {'title' : OrderedDict(sorted(Markdown.token1.items(), key = lambda t : t[0])), 'link' : OrderedDict(sorted(Markdown.token3.items(), key = lambda t : t[0]))}

        # 타이틀
        manual[0] += '<b>설명</b><hr><b>문단 제목</b><br /><br />'
        manual[1] += '<b>입력하는 내용</b><hr><br /><br />'
        for tok in token['title'].keys() :
            manual[0] += (token['title'][tok][-2] + '<br />')
            manual[1] += (token['title'][tok][-1] + '<br />')

        # 링크
        manual[0] += '<br /><b>링크</b><br /><br />'
        manual[1] += '<br /><br /><br />'
        for tok in token['link'] :
            manual[0] += (token['link'][tok][-2] + '<br />')
            manual[1] += (token['link'][tok][-1] + '<br />')

        manual[0] = ''.join(manual[0].rsplit('<br />', 1))
        manual[1] = ''.join(manual[1].rsplit('<br />', 1))

        return manual

    def make_context(context, total_line) :     # 차례
        new_context = ''
        pre = -1                # 앞에 나온 타이틀의 우선순위를 저장
        for c in context :      # 우선순위에 따라 <ul> 추가/제거
            if pre > c['tok'] :
                if pre - c['tok'] >= 2 :
                    new_context += '</ul>\r\n'
                new_context += '</ul>\r\n'
            elif pre < c['tok'] :
                new_context += '<ul style="list-style-type:none">\r\n'

            # 섹션별로 링크
            new_context += '<li><a href="#' + str(c['section']) + '">'
            if c['tok'] >= 2 :
                new_context += str(c['number'][0])
                if c['tok'] >= 3 :
                    new_context += '.' + str(c['number'][1])
                    if c['tok'] >= 4 :
                        new_context += '.' + str(c['number'][2])
            new_context += ' &nbsp;' + c['title'] + '</a></li>\r\n'
            pre = c['tok']
        if pre > 2 :
            if pre > 3 :
                new_context += '</ul>\r\n'
            new_context += '</ul>\r\n'
        new_context += '</ul><p />'
        return {'context' : new_context, 'edit' : Markdown.EditLine(context, total_line) }

    def EditLine(context, total_line) :     # 부분편집 범위 구하기
        index = 0
        edit = {}
        for c in context :
            for cont in context[index+1:] :
                if c['tok'] >= cont['tok'] :
                    c['next_line'] = cont['line'] - 1
                    edit[c['section']] = { 'line' : c['line'], 'next_line' : c['next_line'] }
                    break
            if c['next_line'] == -1 :
                c['next_line'] = total_line
                edit[c['section']] = { 'line' : c['line'], 'next_line' : c['next_line'] }
            index += 1
        return edit

    def ContentEdit(content, start, end) :      # 부분편집 범위 불러오기
        words = content.split('\r\n')

        new_content = ''
        lines = 0

        for w in words :
            lines += 1
            if start <= lines :
                new_content += w + '\r\n'
            if lines == end :
                break
        new_content = ''.join(new_content.rsplit('\r\n', 1))
        return new_content