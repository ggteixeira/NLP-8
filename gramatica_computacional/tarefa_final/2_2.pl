% O nanocompósito possui uma área de superfície elevada.
% Os nanocompósitos possuem uma área de superfície elevada.

s --> noun_phrase(NUM), verb_phrase(NUM).
noun_phrase(NUM) --> art(NUM), noun(NUM).
verb_phrase(NUM) --> verb(NUM), art, prep_phrase.
prep_phrase --> psubj, prep, pobj, adj.

art(sing) --> [o].
art(plur) --> [os].
art --> [uma].
noun(sing) --> [nanocomposito].
noun(plur) --> [nanocompositos].
psubj --> [area].
pobj --> [superficie].
verb(sing) --> [possui].
verb(plur) --> [possuem].

prep --> [de].
adj --> [elevada].