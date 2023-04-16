

app_dict = {
'Anna':{'Experiance' : 2,
'languages':['Python','Ruby','Java','Rust'],'proj_supervision':False},
'Ben':{'Experiance' : 5,
'languages':['Java','Haskell','C++','Perl'],'proj_supervision':False},
'Calvin':{'Experiance' : 3,
'languages':['C','Python','Java','Scala'],'proj_supervision':True},
'Dorothy':{'Experiance' : 6,
'languages':['Java','Python','Elm','Clojure'],'proj_supervision':False},
'Esther':{'Experiance' : 7,
'languages':['Java','Go','Ruby','C#'],'proj_supervision':True}
}

min_ex = 4
req_lan = ['Python','Java']
for name,cv_dict in app_dict.items():
    if cv_dict['Experiance'] >= min_ex and \
        (set(req_lan).issubset(set(cv_dict['languages'])) or \
            cv_dict['proj_supervision']):
            print(name + ' passes the screening.')

