import kivy
from kivy.app import App
from kivy.uix.widget import Widget
import random
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout



class MyLayout(Widget):
    pass

            
        
        


class RootLayout(FloatLayout):
    global important
    important = StringProperty()
    
    def correct1(self):
       
        prior = self.ids.user_input.text
        prior = prior.lower()
        global correct_answer
        if correct_answer == prior or correct_answer == prior:
            self.ids.chill.color = (0,1,0,1)
            self.ids.chill.font_size = 50
            self.ids.chill.text = "Correct"
            flagfile_list_2 = ["ad.png",'ae.png',"al.png","am.png","ao.png","ar.png","au.png","aw.png","az.png",'ba.png',"bb.png","bd.png","be.png","bf.png","bg.png","bh.png","bi.png","bj.png","bn.png","bo.png","br.png","bs.png","bt.png","bw.png","bz.png","ca.png","cd.png","ch.png","cl.png","cm.png","cn.png","co.png","cr.png","cu.png","cy.png","cz.png","de.png","dj.png","dk.png","dm.png","do.png","dz.png","ec.png","ee.png","eg.png","er.png","es.png","et.png","fi.png","fj.png","fm.png","fr.png","gb.png","ge.png","gh.png","gn.png","gq.png","gr.png","gt.png","gy.png","hr.png","ht.png","hu.png","id.png","ie.png","il.png","in.png","iq.png","ir.png","is.png","it.png","jm.png","jo.png","jp.png","ke.png","kg.png","kh.png","ki.png","km.png","kp.png","kr.png","kw.png","kz.png","la.png","lb.png","lc.png","li.png","lk.png","lr.png","ls.png","lu.png","ly.png","ma.png","md.png","me.png","mg.png","mh.png","mk.png","ml.png","mm.png","mn.png","mr.png","mt.png","mv.png","mw.png","mx.png","my.png","mz.png","na.png","ne.png","ng.png","nl.png","no.png","np.png","nr.png","nz.png","om.png","pa.png","pe.png","pg.png","ph.png","pk.png","pt.png","py.png","qa.png","ro.png","rs.png","ru.png","rw.png","sa.png","sb.png","sc.png","sd.png","se.png","sg.png","si.png","sk.png","sl.png","sm.png","sn.png","sr.png","ss.png","sv.png","sy.png","sz.png","tg.png","th.png","tj.png","tm.png","tn.png","to.png","tr.png","tz.png","ua.png","ug.png","us.png","uy.png","uz.png","va.png","ve.png","vn.png","vu.png","ws.png","ye.png","za.png","zm.png","zw.png"]
            important = random.choice(flagfile_list_2)
            flagfile= important
            self.ids.user_input.text = "Enter Guess Here"
            try:
                self.ids.cardimage.source = flagfile
            except:
                important =random.choice(flagfile_list_2)
                flagfile = important
                self.ids.cardimage.source = flagfile
            

            
            other_answer = 'sdkjfhsadjkhfasfasd'

            if important == "gb-wls.png":
                correct_answer = "wales"
            elif important == "bt.png":
                correct_answer = "bhutan"
            elif important == "sm.png":
                correct_answer = "san marino"
            elif important == "tm.png":
                correct_answer = "turkmenistan"
            elif important == "va.png":
                correct_answer = "vatican city"
            elif important == "rs.png":
                correct_answer = "serbia"
            elif important == "ec.png":
                correct_answer = "ecuador"
            elif important == "pt.png":
                correct_answer = "portugal"
            elif important == "ad.png":
                correct_answer = "andorra"
            elif important == "ki.png":
                correct_answer = "kiribati"
            elif important == "kg.png":
                correct_answer = "kyrgyzstan"
            elif important == "mx.png":
                correct_answer = "mexico"
            elif important == "es.png":
                correct_answer = "spain"
            elif important == "np.png":
                correct_answer = "nepal"
            elif important == "me.png":
                correct_answer = "montenegro"
            elif important == "lk.png":
                correct_answer = "sri lanka"
            elif important == "bn.png":
                correct_answer = "brunei"
            elif important == "fj.png":
                correct_answer = "fiji"
            elif important == "sa.png":
                correct_answer = "saudi arabia"
            elif important == "kz.png":
                correct_answer = "kazakhstan"
            elif important == "br.png":
                correct_answer = "brazil"
            elif important == "al.png":
                correct_answer = "albania"
            elif important == "pg.png":
                correct_answer = "papua new guinea"
            elif important == "mh.png":
                correct_answer = "marshall islands"
            elif important == "kr.png":
                correct_answer = "south korea"
            elif important == "kh.png":
                correct_answer = "cambodia"
            elif important == "md.png":
                correct_answer = "moldova"
            elif important == "sz.png":
                correct_answer = "eswatini"
            elif important == "gt.png":
                correct_answer = "guatemala"
            elif important == "er.png":
                correct_answer = "eritrea"
            elif important == "uy.png":
                correct_answer = "uruguay"
            elif important == "sv.png":
                correct_answer = "el salvador"
            elif important == "mz.png":
                correct_answer = "mozambique"
            elif important == "cy.png":
                correct_answer = "cyprus"
            elif important == "ir.png":
                correct_answer = "iran"
            elif important == "ht.png":
                correct_answer = "haiti"
            elif important == "ke.png":
                correct_answer = "kenya"
            elif important == "gq.png":
                correct_answer = "equatorial guinea"
            elif important == "na.png":
                correct_answer = "namibia"
            elif important == "et.png":
                correct_answer = "ethiopia"
            elif important == "bi.png":
                correct_answer = "burundi"
            elif important == "hr.png":
                correct_answer = "croatia"
            elif important == "dm.png":
                correct_answer = "dominica"
            elif important == "vu.png":
                correct_answer = "vanuatu"
            elif important == "cr.png":
                correct_answer = "costa rica"
            elif important == "ph.png":
                correct_answer = "philippines"
            elif important == "do.png":
                correct_answer = "dominican republic"
            elif important == "au.png":
                correct_answer = "australia"
            elif important == "mk.png":
                correct_answer = "north macedonia"
            elif important == "km.png":
                correct_answer = "comoros"
            elif important == "ao.png":
                correct_answer = "angola"
            elif important == "ar.png":
                correct_answer = "argentina"
            elif important == "nz.png":
                correct_answer = "new zealand"
            elif important == "lc.png":
                correct_answer = "saint lucia"
            elif important == "zw.png":
                correct_answer = "zimbabwe"
            elif important == "cd.png":
                correct_answer = "democratic republic of congo"
            elif important == "cd.png":
                other_answer = "drc"
                
            elif important == "dj.png":
                correct_answer = "dijibouti"
            elif important == "mw.png":
                correct_answer = "malawi"
            elif important == "ug.png":
                correct_answer = "uganda"
            elif important == "sb.png":
                correct_answer = "solomon islands"
            elif important == "gy.png":
                correct_answer = "guyana"
            elif important == "sc.png":
                correct_answer = "seychelles"
            elif important == "sk.png":
                correct_answer = "slovakia"
            elif important == "li.png":
                correct_answer = "liechtenstein"
            elif important == "ca.png":
                correct_answer = "canada"
            elif important == "mm.png":
                correct_answer = "myanmar"
            elif important == "us.png":
                correct_answer = "united states of america"
            elif important == "us.png":
                other_answer = "usa"
            elif important == "pk.png":
                correct_answer = "pakistan"
            elif important == "in.png":
                correct_answer = "india"
            elif important == "lb.png":
                correct_answer = "lebanon"
            elif important == "eg.png":
                correct_answer = "egypt"
            elif important == "ba.png":
                correct_answer = "bosnia and herzegovina"
            elif important == "tz.png":
                correct_answer = "tanzania"
            elif important == "py.png":
                correct_answer = "paraguay"
            elif important == "rw.png":
                correct_answer = "rwanda"
            elif important == "my.png":
                correct_answer = "malaysia"
            elif important == "kp.png":
                correct_answer = "north korea"
            elif important == "tn.png":
                correct_answer = "tunisia"
            elif important == "pa.png":
                correct_answer = "panama"
            elif important == "mt.png":
                correct_answer = "malta"
            elif important == "ls.png":
                correct_answer = "lesotho"
            elif important == "zm.png":
                correct_answer = "zambia"
            elif important == "cu.png":
                correct_answer = "cuba"
            elif important == "ge.png":
                correct_answer = "georgia"
            elif important == "mr.png":
                correct_answer = "mauritania"
            elif important == "bb.png":
                correct_answer = "barbados"
            elif important == "dz.png":
                correct_answer = "algeria"
            elif important == "za.png":
                correct_answer = "south africa"
            elif important == "gb.png":
                correct_answer = "united kingdom"
            elif important == "gb.png":
                other_answer = "great britain"
            elif important == "sg.png":
                correct_answer = "singapore"
            elif important == "jm.png":
                correct_answer = "jamaica"
            elif important == "cn.png":
                correct_answer = "china"
            elif important == "tr.png":
                correct_answer = "turkey"
            elif important == "cz.png":
                correct_answer = "czechia"
            elif important == "ss.png":
                correct_answer = "south sudan"
            elif important == "jp.png":
                correct_answer = "japan"
            elif important == "si.png":
                correct_answer = "slovenia"
            elif important == "ma.png":
                correct_answer = "morocco"
            elif important == "vn.png":
                correct_answer = "vietnam"
            elif important == "ve.png":
                correct_answer = "venezuela"
            elif important == "il.png":
                correct_answer = "israel"
            elif important == "tj.png":
                correct_answer = "tajikistan"
            elif important == "bh.png":
                correct_answer = "bahrain"
            elif important == "sy.png":
                correct_answer = "syria"
            elif important == "bd.png":
                correct_answer = "bangladesh"
            elif important == "mn.png":
                correct_answer = "mongolia"
            elif important == "iq.png":
                correct_answer = "iraq"
            elif important == "om.png":
                correct_answer = "oman"
            elif important == "uz.png":
                correct_answer = "uzbekistan"
            elif important == "tg.png":
                correct_answer = "togo"
            elif important == "sd.png":
                correct_answer = "sudan"
            elif important == "aw.png":
                correct_answer = "aruba"
            elif important == "bs.png":
                correct_answer = "bahamas"
            elif important == "az.png":
                correct_answer = "azerbaijan"
            elif important == "mv.png":
                correct_answer = "maldives"
            elif important == "ws.png":
                correct_answer = "somoa"
            elif important == "sr.png":
                correct_answer = "suriname"
            elif important == "sn.png":
                correct_answer = "senegal"
            elif important == "fm.png":
                correct_answer = "micronesia"
            elif important == "la.png":
                correct_answer = "laos"
            elif important == "jo.png":
                correct_answer = "jordan"
            elif important == "nr.png":
                correct_answer = "nauru"
            elif important == "ne.png":
                correct_answer = "niger"
            elif important == "gh.png":
                correct_answer = "ghana"
            elif important == "cm.png":
                correct_answer = "cameroon"
            elif important == "lr.png":
                correct_answer = "liberia"
            elif important == "ly.png":
                correct_answer = "libya"
            elif important == "cl.png":
                correct_answer = "chile"
            elif important == "kw.png":
                correct_answer = "kuwait"
            elif important == "is.png":
                correct_answer = "iceland"
            elif important == "qa.png":
                correct_answer = "qatar"
            elif important == "no.png":
                correct_answer = "norway"
            elif important == "gr.png":
                correct_answer = "greece"
            elif important == "be.png":
                correct_answer = "belgium"
            elif important == "dk.png":
                correct_answer = "denmark"
            elif important == "mg.png":
                correct_answer = "madagascar"
            elif important == "fr.png":
                correct_answer = "france"
            elif important == "gn.png":
                correct_answer = "guinea"
            elif important == "it.png":
                correct_answer = "italy"
            elif important == "ml.png":
                correct_answer = "mali"
            elif important == "ro.png":
                correct_answer = "romania"
            elif important == "fi.png":
                correct_answer = "finland"
            elif important == "ae.png":
                correct_answer = "united arab emirates"
            elif important == "co.png":
                correct_answer = "colombia"
            elif important == "bo.png":
                correct_answer = "bolivia"
            elif important == "ie.png":
                correct_answer = "ireland"
            elif important == "bw.png":
                correct_answer = "botswana"
            elif important == "hu.png":
                correct_answer = "hungary"
            elif important == "am.png":
                correct_answer = "armenia"
            elif important == "bj.png":
                correct_answer = "benin"
            elif important == "pe.png":
                correct_answer = "peru"
            elif important == "th.png":
                correct_answer = "thailand"
            elif important == "to.png":
                correct_answer = "tonga"
            elif important == "ng.png":
                correct_answer = "nigera.png"
            elif important == "ch.png":
                correct_answer = "switzerland"
            elif important == "ee.png":
                correct_answer = "estonia"
            elif important == "nl":
                correct_answer = "netherlands"
            elif important == "ru.png":
                correct_answer = "russia"
            elif important == "sl.png":
                correct_answer = "sierra leone"
            elif important == "ye.png":
                correct_answer = "yemen"
            elif important == "bg.png":
                correct_answer = "bulgaria"
            elif important == "de.png":
                correct_answer = "germany"
            elif important == "lu.png":
                correct_answer = "luxembourg"
            elif important == "se.png":
                correct_answer = "sweden"
            elif important == "id.png":
                correct_answer = "indonesia"
            elif important == "ua.png":
                correct_answer = "ukraine"
            else: 
                correct_answer = "undefined"


           
        else: 
            correct_answer = correct_answer.capitalize()
            self.ids.chill.color = (1,0,0,1)
            self.ids.chill.font_size = 30
            self.ids.chill.text = f'Incorrect the correct answer was {correct_answer}'           
            flagfile_list_2 = ["ad.png",'ae.png',"al.png","am.png","ao.png","ar.png","au.png","aw.png","az.png",'ba.png',"bb.png","bd.png","be.png","bf.png","bg.png","bh.png","bi.png","bj.png","bn.png","bo.png","br.png","bs.png","bt.png","bw.png","bz.png","ca.png","cd.png","ch.png","cl.png","cm.png","cn.png","co.png","cr.png","cu.png","cy.png","cz.png","de.png","dj.png","dk.png","dm.png","do.png","dz.png","ec.png","ee.png","eg.png","er.png","es.png","et.png","fi.png","fj.png","fm.png","fr.png","gb.png","ge.png","gh.png","gn.png","gq.png","gr.png","gt.png","gy.png","hr.png","ht.png","hu.png","id.png","ie.png","il.png","in.png","iq.png","ir.png","is.png","it.png","jm.png","jo.png","jp.png","ke.png","kg.png","kh.png","ki.png","km.png","kp.png","kr.png","kw.png","kz.png","la.png","lb.png","lc.png","li.png","lk.png","lr.png","ls.png","lu.png","ly.png","ma.png","md.png","me.png","mg.png","mh.png","mk.png","ml.png","mm.png","mn.png","mr.png","mt.png","mv.png","mw.png","mx.png","my.png","mz.png","na.png","ne.png","ng.png","nl.png","no.png","np.png","nr.png","nz.png","om.png","pa.png","pe.png","pg.png","ph.png","pk.png","pt.png","py.png","qa.png","ro.png","rs.png","ru.png","rw.png","sa.png","sb.png","sc.png","sd.png","se.png","sg.png","si.png","sk.png","sl.png","sm.png","sn.png","sr.png","ss.png","sv.png","sy.png","sz.png","tg.png","th.png","tj.png","tm.png","tn.png","to.png","tr.png","tz.png","ua.png","ug.png","us.png","uy.png","uz.png","va.png","ve.png","vn.png","vu.png","ws.png","ye.png","za.png","zm.png","zw.png"]
            important = random.choice(flagfile_list_2)
            flagfile= important
            try:
                self.ids.cardimage.source = flagfile
            except:
                important =random.choice(flagfile_list_2)
                flagfile = important
                self.ids.cardimage.source = flagfile
        
            other_answer = 'sdkjfhsadjkhfasfasd'


            if important == "gb-wls.png":
                correct_answer = "wales"
            elif important == "bt.png":
                correct_answer = "bhutan"
            elif important == "sm.png":
                correct_answer = "san marino"
            elif important == "tm.png":
                correct_answer = "turkmenistan"
            elif important == "va.png":
                correct_answer = "vatican city"
            elif important == "rs.png":
                correct_answer = "serbia"
            elif important == "ec.png":
                correct_answer = "ecuador"
            elif important == "pt.png":
                correct_answer = "portugal"
            elif important == "ad.png":
                correct_answer = "andorra"
            elif important == "ki.png":
                correct_answer = "kiribati"
            elif important == "kg.png":
                correct_answer = "kyrgyzstan"
            elif important == "mx.png":
                correct_answer = "mexico"
            elif important == "es.png":
                correct_answer = "spain"
            elif important == "np.png":
                correct_answer = "nepal"
            elif important == "me.png":
                correct_answer = "montenegro"
            elif important == "lk.png":
                correct_answer = "sri lanka"
            elif important == "bn.png":
                correct_answer = "brunei"
            elif important == "fj.png":
                correct_answer = "fiji"
            elif important == "sa.png":
                correct_answer = "saudi arabia"
            elif important == "kz.png":
                correct_answer = "kazakhstan"
            elif important == "br.png":
                correct_answer = "brazil"
            elif important == "al.png":
                correct_answer = "albania"
            elif important == "pg.png":
                correct_answer = "papua new guinea"
            elif important == "mh.png":
                correct_answer = "marshall islands"
            elif important == "kr.png":
                correct_answer = "south korea"
            elif important == "kh.png":
                correct_answer = "cambodia"
            elif important == "md.png":
                correct_answer = "moldova"
            elif important == "sz.png":
                correct_answer = "eswatini"
            elif important == "gt.png":
                correct_answer = "guatemala"
            elif important == "er.png":
                correct_answer = "eritrea"
            elif important == "uy.png":
                correct_answer = "uruguay"
            elif important == "sv.png":
                correct_answer = "el salvador"
            elif important == "mz.png":
                correct_answer = "mozambique"
            elif important == "cy.png":
                correct_answer = "cyprus"
            elif important == "ir.png":
                correct_answer = "iran"
            elif important == "ht.png":
                correct_answer = "haiti"
            elif important == "ke.png":
                correct_answer = "kenya"
            elif important == "gq.png":
                correct_answer = "equatorial guinea"
            elif important == "na.png":
                correct_answer = "namibia"
            elif important == "et.png":
                correct_answer = "ethiopia"
            elif important == "bi.png":
                correct_answer = "burundi"
            elif important == "hr.png":
                correct_answer = "croatia"
            elif important == "dm.png":
                correct_answer = "dominica"
            elif important == "vu.png":
                correct_answer = "vanuatu"
            elif important == "cr.png":
                correct_answer = "costa rica"
            elif important == "ph.png":
                correct_answer = "philippines"
            elif important == "do.png":
                correct_answer = "dominican republic"
            elif important == "au.png":
                correct_answer = "australia"
            elif important == "mk.png":
                correct_answer = "north macedonia"
            elif important == "km.png":
                correct_answer = "comoros"
            elif important == "ao.png":
                correct_answer = "angola"
            elif important == "ar.png":
                correct_answer = "argentina"
            elif important == "nz.png":
                correct_answer = "new zealand"
            elif important == "lc.png":
                correct_answer = "saint lucia"
            elif important == "zw.png":
                correct_answer = "zimbabwe"
            elif important == "cd.png":
                correct_answer = "democratic republic of congo"
            elif important == "cd.png":
                other_answer = "drc"
            elif important == "dj.png":
                correct_answer = "dijibouti"
            elif important == "mw.png":
                correct_answer = "malawi"
            elif important == "ug.png":
                correct_answer = "uganda"
            elif important == "sb.png":
                correct_answer = "solomon islands"
            elif important == "gy.png":
                correct_answer = "guyana"
            elif important == "sc.png":
                correct_answer = "seychelles"
            elif important == "sk.png":
                correct_answer = "slovakia"
            elif important == "li.png":
                correct_answer = "liechtenstein"
            elif important == "ca.png":
                correct_answer = "canada"
            elif important == "mm.png":
                correct_answer = "myanmar"
            elif important == "us.png":
                correct_answer = "united states of america"
            elif important == "us.png":
                other_answer = "usa"
            elif important == "pk.png":
                correct_answer = "pakistan"
            elif important == "in.png":
                correct_answer = "india"
            elif important == "lb.png":
                correct_answer = "lebanon"
            elif important == "eg.png":
                correct_answer = "egypt"
            elif important == "ba.png":
                correct_answer = "bosnia and herzegovina"
            elif important == "tz.png":
                correct_answer = "tanzania"
            elif important == "py.png":
                correct_answer = "paraguay"
            elif important == "rw.png":
                correct_answer = "rwanda"
            elif important == "my.png":
                correct_answer = "malaysia"
            elif important == "kp.png":
                correct_answer = "north korea"
            elif important == "tn.png":
                correct_answer = "tunisia"
            elif important == "pa.png":
                correct_answer = "panama"
            elif important == "mt.png":
                correct_answer = "malta"
            elif important == "ls.png":
                correct_answer = "lesotho"
            elif important == "zm.png":
                correct_answer = "zambia"
            elif important == "cu.png":
                correct_answer = "cuba"
            elif important == "ge.png":
                correct_answer = "georgia"
            elif important == "mr.png":
                correct_answer = "mauritania"
            elif important == "bb.png":
                correct_answer = "barbados"
            elif important == "dz.png":
                correct_answer = "algeria"
            elif important == "za.png":
                correct_answer = "south africa"
            elif important == "gb.png":
                correct_answer = "united kingdom"
            elif important == "gb.png":
                other_answer = "great britain"
            elif important == "sg.png":
                correct_answer = "singapore"
            elif important == "jm.png":
                correct_answer = "jamaica"
            elif important == "cn.png":
                correct_answer = "china"
            elif important == "tr.png":
                correct_answer = "turkey"
            elif important == "cz.png":
                correct_answer = "czechia"
            elif important == "ss.png":
                correct_answer = "south sudan"
            elif important == "jp.png":
                correct_answer = "japan"
            elif important == "si.png":
                correct_answer = "slovenia"
            elif important == "ma.png":
                correct_answer = "morocco"
            elif important == "vn.png":
                correct_answer = "vietnam"
            elif important == "ve.png":
                correct_answer = "venezuela"
            elif important == "il.png":
                correct_answer = "israel"
            elif important == "tj.png":
                correct_answer = "tajikistan"
            elif important == "bh.png":
                correct_answer = "bahrain"
            elif important == "sy.png":
                correct_answer = "syria"
            elif important == "bd.png":
                correct_answer = "bangladesh"
            elif important == "mn.png":
                correct_answer = "mongolia"
            elif important == "iq.png":
                correct_answer = "iraq"
            elif important == "om.png":
                correct_answer = "oman"
            elif important == "uz.png":
                correct_answer = "uzbekistan"
            elif important == "tg.png":
                correct_answer = "togo"
            elif important == "sd.png":
                correct_answer = "sudan"
            elif important == "aw.png":
                correct_answer = "aruba"
            elif important == "bs.png":
                correct_answer = "bahamas"
            elif important == "az.png":
                correct_answer = "azerbaijan"
            elif important == "mv.png":
                correct_answer = "maldives"
            elif important == "ws.png":
                correct_answer = "somoa"
            elif important == "sr.png":
                correct_answer = "suriname"
            elif important == "sn.png":
                correct_answer = "senegal"
            elif important == "fm.png":
                correct_answer = "micronesia"
            elif important == "la.png":
                correct_answer = "laos"
            elif important == "jo.png":
                correct_answer = "jordan"
            elif important == "nr.png":
                correct_answer = "nauru"
            elif important == "ne.png":
                correct_answer = "niger"
            elif important == "gh.png":
                correct_answer = "ghana"
            elif important == "cm.png":
                correct_answer = "cameroon"
            elif important == "lr.png":
                correct_answer = "liberia"
            elif important == "ly.png":
                correct_answer = "libya"
            elif important == "cl.png":
                correct_answer = "chile"
            elif important == "kw.png":
                correct_answer = "kuwait"
            elif important == "is.png":
                correct_answer = "iceland"
            elif important == "qa.png":
                correct_answer = "qatar"
            elif important == "no.png":
                correct_answer = "norway"
            elif important == "gr.png":
                correct_answer = "greece"
            elif important == "be.png":
                correct_answer = "belgium"
            elif important == "dk.png":
                correct_answer = "denmark"
            elif important == "mg.png":
                correct_answer = "madagascar"
            elif important == "fr.png":
                correct_answer = "france"
            elif important == "gn.png":
                correct_answer = "guinea"
            elif important == "it.png":
                correct_answer = "italy"
            elif important == "ml.png":
                correct_answer = "mali"
            elif important == "ro.png":
                correct_answer = "romania"
            elif important == "fi.png":
                correct_answer = "finland"
            elif important == "ae.png":
                correct_answer = "united arab emirates"
            elif important == "co.png":
                correct_answer = "colombia"
            elif important == "bo.png":
                correct_answer = "bolivia"
            elif important == "ie.png":
                correct_answer = "ireland"
            elif important == "bw.png":
                correct_answer = "botswana"
            elif important == "hu.png":
                correct_answer = "hungary"
            elif important == "am.png":
                correct_answer = "armenia"
            elif important == "bj.png":
                correct_answer = "benin"
            elif important == "pe.png":
                correct_answer = "peru"
            elif important == "th.png":
                correct_answer = "thailand"
            elif important == "to.png":
                correct_answer = "tonga"
            elif important == "ng.png":
                correct_answer = "nigera.png"
            elif important == "ch.png":
                correct_answer = "switzerland"
            elif important == "ee.png":
                correct_answer = "estonia"
            elif important == "nl":
                correct_answer = "netherlands"
            elif important == "ru.png":
                correct_answer = "russia"
            elif important == "sl.png":
                correct_answer = "sierra leone"
            elif important == "ye.png":
                correct_answer = "yemen"
            elif important == "bg.png":
                correct_answer = "bulgaria"
            elif important == "de.png":
                correct_answer = "germany"
            elif important == "lu.png":
                correct_answer = "luxembourg"
            elif important == "se.png":
                correct_answer = "sweden"
            elif important == "id.png":
                correct_answer = "indonesia"
            elif important == "ua.png":
                correct_answer = "ukraine"
            else: 
                correct_answer = "hello"
                RootLayout().correct1()

    

       
prior = StringProperty()




class testApp(App):
    
    

    global correct_answer
    
    global important 

    correct_answer = "x"

    flagfile = StringProperty("0")

    #path = "/Users/samarth/Downloads/App/w320"
    file_name_list = ["ad.png",'ae.png',"al.png","am.png","ao.png","ar.png","au.png","aw.png","az.png",'ba.png',"bb.png","bd.png","be.png","bf.png","bg.png","bh.png","bi.png","bj.png","bn.png","bo.png","br.png","bs.png","bt.png","bw.png","bz.png","ca.png","cd.png","ch.png","cl.png","cm.png","cn.png","co.png","cr.png","cu.png","cy.png","cz.png","de.png","dj.png","dk.png","dm.png","do.png","dz.png","ec.png","ee.png","eg.png","er.png","es.png","et.png","fi.png","fj.png","fm.png","fr.png","gb.png","ge.png","gh.png","gn.png","gq.png","gr.png","gt.png","gy.png","hr.png","ht.png","hu.png","id.png","ie.png","il.png","in.png","iq.png","ir.png","is.png","it.png","jm.png","jo.png","jp.png","ke.png","kg.png","kh.png","ki.png","km.png","kp.png","kr.png","kw.png","kz.png","la.png","lb.png","lc.png","li.png","lk.png","lr.png","ls.png","lu.png","ly.png","ma.png","md.png","me.png","mg.png","mh.png","mk.png","ml.png","mm.png","mn.png","mr.png","mt.png","mv.png","mw.png","mx.png","my.png","mz.png","na.png","ne.png","ng.png","nl.png","no.png","np.png","nr.png","nz.png","om.png","pa.png","pe.png","pg.png","ph.png","pk.png","pt.png","py.png","qa.png","ro.png","rs.png","ru.png","rw.png","sa.png","sb.png","sc.png","sd.png","se.png","sg.png","si.png","sk.png","sl.png","sm.png","sn.png","sr.png","ss.png","sv.png","sy.png","sz.png","tg.png","th.png","tj.png","tm.png","tn.png","to.png","tr.png","tz.png","ua.png","ug.png","us.png","uy.png","uz.png","va.png","ve.png","vn.png","vu.png","ws.png","ye.png","za.png","zm.png","zw.png"]
    #files = os.listdir(path)

    important = random.choice(file_name_list)

    flagfile= important


    other_answer = 'sdkjfhsadjkhfasfasd'


    if important == "gb-wls.png":
        correct_answer = "wales"
    elif important == "bt.png":
        correct_answer = "bhutan"
    elif important == "sm.png":
        correct_answer = "san marino"
    elif important == "tm.png":
        correct_answer = "turkmenistan"
    elif important == "va.png":
        correct_answer = "vatican city"
    elif important == "rs.png":
        correct_answer = "serbia"
    elif important == "ec.png":
        correct_answer = "ecuador"
    elif important == "pt.png":
        correct_answer = "portugal"
    elif important == "ad.png":
        correct_answer = "andorra"
    elif important == "ki.png":
        correct_answer = "kiribati"
    elif important == "kg.png":
        correct_answer = "kyrgyzstan"
    elif important == "mx.png":
        correct_answer = "mexico"
    elif important == "es.png":
        correct_answer = "spain"
    elif important == "np.png":
        correct_answer = "nepal"
    elif important == "me.png":
        correct_answer = "montenegro"
    elif important == "lk.png":
        correct_answer = "sri lanka"
    elif important == "bn.png":
        correct_answer = "brunei"
    elif important == "fj.png":
        correct_answer = "fiji"
    elif important == "sa.png":
        correct_answer = "saudi arabia"
    elif important == "kz.png":
        correct_answer = "kazakhstan"
    elif important == "br.png":
        correct_answer = "brazil"
    elif important == "al.png":
        correct_answer = "albania"
    elif important == "pg.png":
        correct_answer = "papua new guinea"
    elif important == "mh.png":
        correct_answer = "marshall islands"
    elif important == "kr.png":
        correct_answer = "south korea"
    elif important == "kh.png":
        correct_answer = "cambodia"
    elif important == "md.png":
        correct_answer = "moldova"
    elif important == "sz.png":
        correct_answer = "eswatini"
    elif important == "gt.png":
        correct_answer = "guatemala"
    elif important == "er.png":
        correct_answer = "eritrea"
    elif important == "uy.png":
        correct_answer = "uruguay"
    elif important == "sv.png":
        correct_answer = "el salvador"
    elif important == "mz.png":
        correct_answer = "mozambique"
    elif important == "cy.png":
        correct_answer = "cyprus"
    elif important == "ir.png":
        correct_answer = "iran"
    elif important == "ht.png":
        correct_answer = "haiti"
    elif important == "ke.png":
        correct_answer = "kenya"
    elif important == "gq.png":
        correct_answer = "equatorial guinea"
    elif important == "na.png":
        correct_answer = "namibia"
    elif important == "et.png":
        correct_answer = "ethiopia"
    elif important == "bi.png":
        correct_answer = "burundi"
    elif important == "hr.png":
        correct_answer = "croatia"
    elif important == "dm.png":
        correct_answer = "dominica"
    elif important == "vu.png":
        correct_answer = "vanuatu"
    elif important == "cr.png":
        correct_answer = "costa rica"
    elif important == "ph.png":
        correct_answer = "philippines"
    elif important == "do.png":
        correct_answer = "dominican republic"
    elif important == "au.png":
        correct_answer = "australia"
    elif important == "mk.png":
        correct_answer = "north macedonia"
    elif important == "km.png":
        correct_answer = "comoros"
    elif important == "ao.png":
        correct_answer = "angola"
    elif important == "ar.png":
        correct_answer = "argentina"
    elif important == "nz.png":
        correct_answer = "new zealand"
    elif important == "lc.png":
        correct_answer = "saint lucia"
    elif important == "zw.png":
        correct_answer = "zimbabwe"
    elif important == "cd.png":
        correct_answer = "democratic republic of congo"
    elif important == "cd.png":
        other_answer = "drc"
    elif important == "dj.png":
        correct_answer = "dijibouti"
    elif important == "mw.png":
        correct_answer = "malawi"
    elif important == "ug.png":
        correct_answer = "uganda"
    elif important == "sb.png":
        correct_answer = "solomon islands"
    elif important == "gy.png":
        correct_answer = "guyana"
    elif important == "sc.png":
        correct_answer = "seychelles"
    elif important == "sk.png":
        correct_answer = "slovakia"
    elif important == "li.png":
        correct_answer = "liechtenstein"
    elif important == "ca.png":
        correct_answer = "canada"
    elif important == "mm.png":
        correct_answer = "myanmar"
    elif important == "us.png":
        correct_answer = "united states of america"
    elif important == "us.png":
        other_answer = "usa"
    elif important == "pk.png":
        correct_answer = "pakistan"
    elif important == "in.png":
        correct_answer = "india"
    elif important == "lb.png":
        correct_answer = "lebanon"
    elif important == "eg.png":
        correct_answer = "egypt"
    elif important == "ba.png":
        correct_answer = "bosnia and herzegovina"
    elif important == "tz.png":
        correct_answer = "tanzania"
    elif important == "py.png":
        correct_answer = "paraguay"
    elif important == "rw.png":
        correct_answer = "rwanda"
    elif important == "my.png":
        correct_answer = "malaysia"
    elif important == "kp.png":
        correct_answer = "north korea"
    elif important == "tn.png":
        correct_answer = "tunisia"
    elif important == "pa.png":
        correct_answer = "panama"
    elif important == "mt.png":
        correct_answer = "malta"
    elif important == "ls.png":
        correct_answer = "lesotho"
    elif important == "zm.png":
        correct_answer = "zambia"
    elif important == "cu.png":
        correct_answer = "cuba"
    elif important == "ge.png":
        correct_answer = "georgia"
    elif important == "mr.png":
        correct_answer = "mauritania"
    elif important == "bb.png":
        correct_answer = "barbados"
    elif important == "dz.png":
        correct_answer = "algeria"
    elif important == "za.png":
        correct_answer = "south africa"
    elif important == "gb.png":
        correct_answer = "united kingdom"
    elif important == "gb.png":
        other_answer = "great britain"
    elif important == "sg.png":
        correct_answer = "singapore"
    elif important == "jm.png":
        correct_answer = "jamaica"
    elif important == "cn.png":
        correct_answer = "china"
    elif important == "tr.png":
        correct_answer = "turkey"
    elif important == "cz.png":
        correct_answer = "czechia"
    elif important == "ss.png":
        correct_answer = "south sudan"
    elif important == "jp.png":
        correct_answer = "japan"
    elif important == "si.png":
        correct_answer = "slovenia"
    elif important == "ma.png":
        correct_answer = "morocco"
    elif important == "vn.png":
        correct_answer = "vietnam"
    elif important == "ve.png":
        correct_answer = "venezuela"
    elif important == "il.png":
        correct_answer = "israel"
    elif important == "tj.png":
        correct_answer = "tajikistan"
    elif important == "bh.png":
        correct_answer = "bahrain"
    elif important == "sy.png":
        correct_answer = "syria"
    elif important == "bd.png":
        correct_answer = "bangladesh"
    elif important == "mn.png":
        correct_answer = "mongolia"
    elif important == "iq.png":
        correct_answer = "iraq"
    elif important == "om.png":
        correct_answer = "oman"
    elif important == "uz.png":
        correct_answer = "uzbekistan"
    elif important == "tg.png":
        correct_answer = "togo"
    elif important == "sd.png":
        correct_answer = "sudan"
    elif important == "aw.png":
        correct_answer = "aruba"
    elif important == "bs.png":
        correct_answer = "bahamas"
    elif important == "az.png":
        correct_answer = "azerbaijan"
    elif important == "mv.png":
        correct_answer = "maldives"
    elif important == "ws.png":
        correct_answer = "somoa"
    elif important == "sr.png":
        correct_answer = "suriname"
    elif important == "sn.png":
        correct_answer = "senegal"
    elif important == "fm.png":
        correct_answer = "micronesia"
    elif important == "la.png":
        correct_answer = "laos"
    elif important == "jo.png":
        correct_answer = "jordan"
    elif important == "nr.png":
        correct_answer = "nauru"
    elif important == "ne.png":
        correct_answer = "niger"
    elif important == "gh.png":
        correct_answer = "ghana"
    elif important == "cm.png":
        correct_answer = "cameroon"
    elif important == "lr.png":
        correct_answer = "liberia"
    elif important == "ly.png":
        correct_answer = "libya"
    elif important == "cl.png":
        correct_answer = "chile"
    elif important == "kw.png":
        correct_answer = "kuwait"
    elif important == "is.png":
        correct_answer = "iceland"
    elif important == "qa.png":
        correct_answer = "qatar"
    elif important == "no.png":
        correct_answer = "norway"
    elif important == "gr.png":
        correct_answer = "greece"
    elif important == "be.png":
        correct_answer = "belgium"
    elif important == "dk.png":
        correct_answer = "denmark"
    elif important == "mg.png":
        correct_answer = "madagascar"
    elif important == "fr.png":
        correct_answer = "france"
    elif important == "gn.png":
        correct_answer = "guinea"
    elif important == "it.png":
        correct_answer = "italy"
    elif important == "ml.png":
        correct_answer = "mali"
    elif important == "ro.png":
        correct_answer = "romania"
    elif important == "fi.png":
        correct_answer = "finland"
    elif important == "ae.png":
        correct_answer = "united arab emirates"
    elif important == "co.png":
        correct_answer = "colombia"
    elif important == "bo.png":
        correct_answer = "bolivia"
    elif important == "ie.png":
        correct_answer = "ireland"
    elif important == "bw.png":
        correct_answer = "botswana"
    elif important == "hu.png":
        correct_answer = "hungary"
    elif important == "am.png":
        correct_answer = "armenia"
    elif important == "bj.png":
        correct_answer = "benin"
    elif important == "pe.png":
        correct_answer = "peru"
    elif important == "th.png":
        correct_answer = "thailand"
    elif important == "to.png":
        correct_answer = "tonga"
    elif important == "ng.png":
        correct_answer = "nigera.png"
    elif important == "ch.png":
        correct_answer = "switzerland"
    elif important == "ee.png":
        correct_answer = "estonia"
    elif important == "nl":
        correct_answer = "netherlands"
    elif important == "ru.png":
        correct_answer = "russia"
    elif important == "sl.png":
        correct_answer = "sierra leone"
    elif important == "ye.png":
        correct_answer = "yemen"
    elif important == "bg.png":
        correct_answer = "bulgaria"
    elif important == "de.png":
        correct_answer = "germany"
    elif important == "lu.png":
        correct_answer = "luxembourg"
    elif important == "se.png":
        correct_answer = "sweden"
    elif important == "id.png":
        correct_answer = "indonesia"
    elif important == "ua.png":
        correct_answer = "ukraine"
    else: 
        correct_answer = ""




  
   

    def build(self):
 

        return RootLayout()


    
if __name__ == "__main__":
    testApp().run()




   
