% Este trabalho refere-se a nanocompósitos de matriz polimérica.
% Estes trabalhos referem-se a nanocompósitos de matriz polimérica.

s --> noun_phrase(NUM), verb_phrase(NUM).

noun_phrase(NUM) --> det(NUM), suj(NUM).
verb_phrase(NUM) --> verb(NUM), clitic, v_prep, ind_obj, prep_phrase.

det(sing) --> [este].
det(plur) --> [estes].
suj(sing) --> [trabalho].
suj(plur) --> [trabalhos].

verb(sing) --> [refere].
verb(plur) --> [referem].
clitic --> [-se].
v_prep --> [a].
ind_obj --> [nanocompositos].

prep_phrase --> prep_prep, prep_obj, prep_adj.
prep_prep --> [de].
prep_obj --> [matriz].
prep_adj --> [polimerica].