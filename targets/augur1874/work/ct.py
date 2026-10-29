T={
'29':"Dresden I persons to it fussy unauthorized forward have may self as request anticipate to just attempt that he I. I. request received to secure has buildings as with this table Houston no novel faint Davis following possession Nueces Cypher state Grant nun dispatch of Cheyenne to the scatter from",
'30':"In any sent no have if has am change the instructions I that president informed occurs governors to notice but the though I dispatch give immediate subject that general will Brownsville on have the Sheridan",
'45':"It recognize in of interfere specially Expected seems Either any him to not be to governor way under not need can me you without the Sellers you that if can orders circumstances instruct trouble all governor return from it desireable desire is Davis to me is is party it yields morrow Waco Evident there the collision to unless Denison neither stay nor armed force your Houston the further President without",
}
W={k:v.replace('I. I.','I.I.').split() for k,v in T.items()}
T['1869']="Pleasure I acknowledge instructions famines fuel the job Gumption lag to Easter day the receipt Key Headquarters Empty glass mutton with and thee have this Junks Algeria impulse of honor him"
W={k:v.replace('I. I.','I.I.').split() for k,v in T.items()}
T['22']="Baltic Troops the by under J.Davis me will force are supreme law which decline anticipates to meet to to court is the ta however prevent in get interfere of made last act that this Austin possession in the judge Election without the by on of the State as was orders legislature use tuesday the troubles has to held from and of next state of decided when here the governor united with government a the united unconstitutional precedent then states attempt the state law states governor who elected troops by asks"
W={k:v.replace('I. I.','I.I.').split() for k,v in T.items()}
W['22b']=W['22'][1:5]+['J.','Davis']+W['22'][6:]
W['29b']=[x for t in W['29'][1:] for x in (['I.','I.'] if t=='I.I.' else [t])]
