import os,ntpath
def ishidden(filepath):import stat;return not not(os.stat(filepath).st_file_attributes&stat.FILE_ATTRIBUTE_HIDDEN)
def tree_scanner(path=None,files=False,hiddens=False):
    path=os.getcwd()if path is None else path;yesfiles=files;hidehid=not hiddens;processnet=[{},[]];d={'.':processnet};todo=[('.',path,d,processnet)];getnxt=todo.pop;_nx=next;_ln=len;addsrh=todo.append;pathjoin=ntpath.join;oslook=os.walk
    while todo:
        I,pa,r,(l1,l2)=getnxt();fl=0
        try:
            a,names,files=_nx(oslook(pa))
            if hidehid:files=[i for i in files if not ishidden(pathjoin(a,i))]
        except StopIteration:fl=1
        if fl or _ln(names)==_ln(files)==0:r[I]=None;continue
        for i in names:
            pn=pathjoin(a,i)
            if hidehid and ishidden(pn):continue
            l1[i]=_=[{},[]];addsrh((i,pn,l1,_))
        if yesfiles:l2.extend(files)
    return d['.']
from functools import wraps;from copy import deepcopy
def nomutate(reps):
    if not isinstance(reps,list):reps=[reps]
    ints={*()};strs={*()};slcs={*()}
    for i in reps:
        if isinstance(i,int):ints.add(i)
        elif isinstance(i,str):strs.add(i)
        elif isinstance(i,range):ints.update(i)
        elif isinstance(i,slice):slcs.update(i)
    def _1(f):
        @wraps(f)
        def _2(*aa,**a):
            l=len(aa);aa=[*aa]
            for i in ints:
                if i<l:aa[i]=deepcopy(aa[i])
            for i in strs:
                if i in a:a[i]=deepcopy(a[i])
            for i in slcs:aa[i]=[deepcopy(j)for j in aa[i]]
            return f(*aa,**a)
        return _2
    return _1
@nomutate([1])
def tree_formatter(a,unicodestyle=True):
    if a is None:return None
    _a={'.':a}
    if unicodestyle:uni='─│└├';_lsf1=_lsf3=_lsf4='  {}';_lsf2='    {}'
    else:uni=('---',*'|\\+');_lsf1=_lsf3='   {}';_lsf2='    {}';_lsf4=' {}'
    _lsf1=_lsf1.format;_lsf3=_lsf3.format;_lsf2=_lsf2.format;_lsf4=_lsf4.format
    u1=uni[1];u0=uni[0]
    while not isinstance(_a['.'],tuple):
        s=[(_a,'.',a)];spop=s.pop;sglue=s.extend
        while s:
            r,na,b=c=spop()
            if isinstance(b,tuple):continue
            b,d=b;_=[(b,n,i)for n,i in b.items()if isinstance(i,list)]
            if _:sglue(_)
            else:
                re=[_lsf1(i)for i in d];r0=re.append;r1=re.extend
                if b:
                    _sf=not not d;ff=len(b)-1
                    for fi,(sn,sv)in enumerate(b.items()):
                        _l=fi==ff
                        if _sf:r0(u1)
                        r0(f'{uni[2 if _l else 3]}{u0}{sn}')
                        if sv:_=_lsf2 if _l else _lsf3;_sv=[_(i)for i in sv];r1(_sv);_sf=_sv[-1].strip()[0]not in uni
                        else:_sf=0
                    _f=0;re1=[*re]
                    for i,v in enumerate(re):
                        ss=v[0]
                        if ss==uni[2]:break
                        if v and ss not in uni:re1[i]=f'{u1}{v[0:]}'
                    re=re1
                else:re=[_lsf4(i)for i in re]
                r[na]=(*re,)
    return'\n'.join(_a['.'])

if'__main__'==__name__:
    from sys import argv;argv=[i.lower()for i in argv][1:]
    if'/?'in argv:print('Python Implementation of the tree command.');raise SystemExit()
    f=0
    if'/f'in argv:f=1;argv.remove('/f')
    U=1
    if'/a'in argv:U=0;argv.remove('/a')
    if argv:path=argv[0]
    else:path=os.getcwd()#os.path.expandvars('C:/Users/%username%/Desktop')#'/storage/emulated/0/'
    print(tree_formatter(tree_scanner(path,files=f),U))
