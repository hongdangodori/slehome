from collections import OrderedDict

def markdown(page_name, text) :
    edit_url = '/sle/wiki/edit/' + page_name + '/'

    # 제목 태그
    token1 = {
        '==' : ['<span id="','">&nbsp;</span><br /><br /><h1><b>', '</b></h1><a href="'+edit_url, '/">[edit]</a>'],
        '===' : ['<span id="','">&nbsp;</span><br /><br /><h3>', '</h3><a href="'+edit_url, '/">[edit]</a>'],
        '====' : ['<span id="','">&nbsp;</span><br /><br /><h4>', '</h4><a href="'+edit_url, '/">[edit]</a>']
        }
    token1 = OrderedDict(sorted(token1.items(), key = lambda t : t[0], reverse = True))
    # 태그
    token2 = {
        '----' : '<hr />',
        '\r\n\r\n' : '<p /><br />',
        '\n\n' : '<p /><br />'
        }
    # 링크 태그
    token3 = {
        '[[' : [']]', '<a href="/sle/wiki/page/', '/">', '</a>'],
        '[[[' : [']]]', '<a href="', '" target=new>', '</a>'],
        '[youtube]((' : ['))', '<br /><iframe width="420" height="315" src="//www.youtube.com/embed/', '" frameborder="0" allowfullscreen>', '</iframe><br />'],
        '[image]((' : ['))', '<br /><img src="', '', '" class="img-rounded"></image><br />']
    }
    token3 = OrderedDict(sorted(token3.items(), key = lambda t : t[0], reverse = True))

    token_enum = {
        '==' : 0,
        '===' : 1,
        '====' : 2
        }
    
    # 줄 단위로 나누기
    words = text.split('\r\n')

    dic = {}
    context = []
    section = 0

    lines = 0
    new_text = ''
    name = ''

    # 이 부분에 관해서 예외 처리 해야됨....
    first = 0
    second = 0
    third = 0

    for w in words :
        lines += 1
        for tok in token1.keys() :
            # 토큰으로 파티션 나누기
            par = w.partition(tok)
            rpar = w.rpartition(tok)

            # 양 끝에 토큰이 있는지 없는지 확인
            if (par[0] == '') and (par[1] == tok) and (rpar[1] == tok) and (rpar[2] == '') :
                section += 1
                title = par[2].rpartition(tok)[0]

                # 목차에 나올 숫자 계산
                if token_enum[tok] <= 2 :
                    third += 1
                    if token_enum[tok] <= 1 :
                        second, third = second + 1, 0
                        if token_enum[tok] == 0 :
                            first, second, third = first + 1, 0, 0
                
                context += [{
                    'tok' : token_enum[tok], 
                    'section' : section, 
                    'line' : lines,
                    'next_line' : -1, 
                    'title' : title,
                    'number' : [first, second, third]
                    }]

                # 토큰을 태그로 교체
                words[lines - 1] = words[lines - 1].replace(tok, token1[tok][0] + str(section) + token1[tok][1], 1)
                words[lines - 1] = (token1[tok][2] + str(section) + token1[tok][3]).join(words[lines - 1].rsplit(tok, 1))

                break

        # 링크 토큰을 태그로 교체
        for tok in token3 :
            # 토큰이 있는지 없는지 확인
            while words[lines - 1].partition(tok)[1] != '' :
                link = words[lines - 1].partition(tok)[2].partition(token3[tok][0])[0]
                # 유튜브 링크인 경우
                if 'watch?v=' in link :
                    link = link.partition('watch?v=')[2]
                # 이미지 태그인 경우
                elif tok == '[image]((' :
                    link = ''
                # 토큰을 태그로 교체
                words[lines - 1] = words[lines - 1].replace(tok, token3[tok][1] + link + token3[tok][2], 1)
                words[lines - 1] = words[lines - 1].replace(token3[tok][0], token3[tok][3], 1)

        new_text += words[lines - 1] + '\r\n'
    new_text = ''.join(new_text.rsplit('\r\n', 1))

    for tok in token2 :
        new_text = new_text.replace(tok, token2[tok])

    context = make_context(context, lines)
    dic['context'] = context['context']
    dic['edit'] = context['edit']
    dic['content'] = new_text

    return dic

def make_context(context, total_line) :
    new_context = ''
    pre = -1
    for c in context :
        if pre > c['tok'] :
            if pre - c['tok'] >= 2 :
                new_context += '</ul>\r\n'
            new_context += '</ul>\r\n'
        elif pre < c['tok'] :
            new_context += '<ul style="list-style-type:none">\r\n'

        new_context += '<li><a href="#' + str(c['section']) + '">'
        if c['tok'] >= 0 :
            new_context += str(c['number'][0])
            if c['tok'] >= 1 :
                new_context += '.' + str(c['number'][1])
                if c['tok'] >= 2 :
                    new_context += '.' + str(c['number'][2])
        new_context += ' &nbsp;' + c['title'] + '</a></li>\r\n'
        pre = c['tok']
    if pre > 0 :
        if pre > 1 :
            new_context += '</ul>\r\n'
        new_context += '</ul>\r\n'
    new_context += '</ul><p />'
    return {'context' : new_context, 'edit' : EditLine(context, total_line) }

def EditLine(context, total_line) :
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

def ContentEdit(content, start, end) :
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