a,s=''.join,'񰋦򓶐񲚶󧑌𧌲񰪐𨚲򐪆񯝂彀񩜂犁񮚖񒡑𹊳򠩀񣋤󂲓𽌢󃁌𧊐򢂆񯝂湀񩜂楋𧞢񳨪𠈧𲲃𬓣󒢓𫚂𧮃񽟔󇵂𬌲󆹉񩚂湁𽓢𓵐𠙶󇎅𨝒򲝇𬙒򳅌񮊰򢂐𨚳򣶓𩃂𲍃'
i=a([hex(ord(u)-32)[2:].zfill(5)for u in s])
exec(a([chr(int(i[j:j+2],16))for j in range(0,len(i),2)]))
