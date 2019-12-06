s --> np(NUM), vp(NUM, _TRANSIT).

np(NUM) --> art(NUM), noun(NUM).
vp(NUM, TRANSIT) --> verb(NUM), art_indef(NUM), noun(NUM, TRANSIT), adj(NUM).

art(singular) --> [o].
art(plural) --> [os].
art_indef(singular) --> [um].
art_indef(plural) --> [].

noun(singular) --> [nanocomposito].
noun(plural) --> [nanocompositos].

noun(singular, obj) --> [material].
noun(plural, obj) --> [materiais].

adj(singular) --> [hibrido].
adj(plural) --> [hibridos].

verb(singular) --> [eh].
verb(plural) --> [sao].