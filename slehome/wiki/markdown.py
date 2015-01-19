from collections import OrderedDict

def markdown(page_name, text) :
    def make_context(context) :
        result = ''
        pre = ''
        for cont in context :
            if pre < cont[0] :
                result += '<ul>\n'
                result += '<li><a href="' + str(cont[1]) + '">' + cont[3] + '</a></li>\n'
            pre = cont[0]
        return result

    dic = {}

    context = []
    section = 0

    token1 = {
        '==' : ['<a name="', '"><h3>', '</h3></a><a href="54.169.79.59/sle/wiki/edit/'+page_name+'/', '>[edit]</a><p />'],
        '===' : ['<a name="', '"><h3>', '</h2></a><a href="54.169.79.59/sle/wiki/edit/'+page_name+'/', '>[edit]</a><p />'],
        '====' : ['<a name="', '"><h3>', '</h1></a><a href="54.169.79.59/sle/wiki/edit/'+page_name+'/', '>[edit]</a><p />']
        }
    token1 = OrderedDict(sorted(token1.items(), key=lambda t : t[0]))
    token2 = {
        '----' : '<hr />',
        '\n\n' : '<p />'
        }
    # token2 = OrderedDict(sorted(token2.items(), key=lambda t : t[0]))
    
    tokenize = text.split(' ')
    
    cur_token = ''
    cur_idx = 0
    idx = 0

    first = 0
    second = 0
    third = 0

    for wd in tokenize :
        for tok in token1 :
            words = wd.split('\n')
            w_idx = 0

            for w in words :
                if w == tok :
                    if cur_token == tok :
                        content = ''
                        for ch in tokenize[cur_idx : idx + 1] :
                            content += ch + ' '
                        content = content.partition(tok)[2].partition(tok)[0]

                        section += 1
                        tokenize[cur_idx] = tokenize[cur_idx].replace(tok, token1[tok][0] + str(section) + token1[tok][1], 1)
                        tokenize[idx] = tokenize[idx].replace(tok, token1[tok][2] + str(section) + token1[tok][3], 1)
                        cur_token = ''

                        if tok == '==' :
                            first += 1
                            second = 0
                            third = 0
                            context += [['==', section, str(first), content]]
                        elif tok == '===' :
                            second += 1
                            third = 0
                            context += [['===', section, str(first) + '.' + str(second), content]]
                        elif tok == '====' :
                            third += 1
                            context += [['====', section, str(first) + '.' + str(second) + '.' + str(third), content]]
                    else :
                        cur_token = tok
                        cur_idx = idx
        for tok in token2 :
            tokenize[idx] = tokenize[idx].replace(tok, token2[tok])
        
        idx += 1

    new_text = ''
    
    for word in tokenize :
        new_text += word + ' '

    dic['context'] = make_context(context)
    dic['content'] = new_text
    return dic