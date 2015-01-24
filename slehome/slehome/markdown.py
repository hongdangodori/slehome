from collections import OrderedDict

def markdown(page_name, text) :
    edit_url = '54.169.79.59/sle/wiki/' + page_name + '/edit/'

    token1 = {
        '==' : ['<a name="', '"><h3>', '</h3></a><a href="'+edit_url, '">[edit]</a>'],
        '===' : ['<a name="', '"><h3>', '</h2></a><a href="'+edit_url, '">[edit]</a>'],
        '====' : ['<a name="', '"><h3>', '</h1></a><a href="'+edit_url, '">[edit]</a>']
        }
    token1 = OrderedDict(sorted(token1.items(), key = lambda t : t[0], reverse = True))
    token2 = {
        '----' : '<hr />',
        '\n\n' : '<p />'
        }
    token_enum = {
        '==' : 0,
        '===' : 1,
        '====' : 2
        }
    
    words = text.split('\n')

    dic = {}
    context = []
    section = 0

    lines = 0
    new_text = ''

    for w in words :
        lines += 1
        for tok in token1.keys() :
            par = w.partition(tok)
            rpar = w.rpartition(tok)
            if par[0] == '' and par[1] == tok and rpar[1] == tok and rpar[2] == '' :
                section += 1
                title = par[2].rpartition(tok)[0]
                
                context += [{
                    'tok' : token_enum[tok], 
                    'section' : section, 
                    'line' : lines,
                    'next_line' : -1, 
                    'title' : title
                    }]

                words[lines - 1] = words[lines - 1].replace(tok, token1[tok][0] + str(section) + token1[tok][1], 1)
                # <exception>
                words[lines - 1] = words[lines - 1].replace(tok, token1[tok][2] + str(section) + token1[tok][3], 1)

                break
        new_text += words[lines - 1] + '\n'

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
                new_context += '</ul>\n'
            new_context += '</ul>\n'
        elif pre < c['tok'] :
            new_context += '<ul>\n'
        new_context += '<li><a href="#' + str(c['section']) + '">' + c['title'] + '</a></li>\n'
        pre = c['tok']
    if pre > 0 :
        if pre > 1 :
            new_context += '</ul>\n'
        new_context += '</ul>\n'
    new_context += '</ul>'
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