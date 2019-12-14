
lati = {'셔틀콕': 37.298748, '제1공학관': 37.297579,
        '제3공학관': 37.297442, '제4공학관': 37.296845,
        '제1학술관': 37.298245, '컨퍼런스홀': 37.299030,
        '제2과학기술관': 37.298603, '학생복지관': 37.298023,
        '학생회관': 37.297468, '학술정보관': 37.296775,
        '제5공학관': 37.296884, '창업보육센터': 37.295587,
        '학연산 클러스터': 37.296398, '기숙사 셔틀콕': 37.293088,
        '한대앞역': 37.309642}

longti = {'셔틀콕': 126.838021, '제1공학관': 126.837431,
          '제3공학관': 126.836229, '제4공학관': 126.836250,
          '제1학술관': 126.835864, '컨퍼런스홀': 126.836830,
          '제2과학기술관': 126.837216, '학생복지관': 126.834437,
          '학생회관': 126.834737, '학술정보관': 126.835214,
          '제5공학관': 126.837381, '창업보육센터': 126.837231,
          '학연산 클러스터': 126.838883, '기숙사 셔틀콕': 126.835827,
          '한대앞역': 126.853635}


def loca(spot):
    return [lati[spot], longti[spot]]


spot_num_latlng = [[], [37.298139, 126.834400], [37.297482, 126.834743],
                   [37.297721, 126.835326], [37.297454, 126.835495],
                   [37.297146, 126.835715], [37.297659, 126.835950],
                   [37.297840, 126.836450], [37.297962, 126.836677],
                   [37.298130, 126.837063], [37.298515, 126.837927], #10
                   [37.298703, 126.837812], [37.298748, 126.838065],
                   [37.298607, 126.837222], [37.299033, 126.836843],
                   [37.298243, 126.835846], [37.298444, 126.836361],
                   [37.297471, 126.836248], [37.297632, 126.836602],
                   [37.297518, 126.837401], [37.297378, 126.836741], #20
                   [37.296986, 126.835834], [37.296752, 126.835989],
                   [37.296802, 126.835287], [37.296808, 126.836303],
                   [37.296035, 126.836405], [37.296131, 126.836628],
                   [37.296315, 126.837138], [37.296482, 126.837503],
                   [37.296824, 126.837250], [37.297229, 126.838313], #30
                   [37.297359, 126.838662], [37.296593, 126.838451],
                   [37.296347, 126.838897], [37.295069, 126.837950],
                   [37.295565, 126.837277], [37.295373, 126.836837],
                   [37.294734, 126.837140], [37.293027, 126.835540],
                   [37.298265, 126.837337], [37.298876, 126.836550], #40
                   [37.298342, 126.836109], [37.296281, 126.838664],
                   [37.309642, 126.853635], [37.298335, 126.834942],
                   [37.297476, 126.836041], [37.297604, 126.836508],
                   [37.297263, 126.835965], [37.297668, 126.836677],
                   [37.297793, 126.836792], [37.297902, 126.837219], #50
                   [37.298105, 126.837605], [37.299244, 126.837453],
                   [37.299088, 126.836963], [37.299050, 126.836652],
                   [37.298986, 126.836491], [37.298628, 126.835906],
                   [37.298699, 126.837541], [37.298490, 126.837190],
                   [37.297236, 126.836418], [37.297181, 126.835877], #60
                   [37.297048, 126.836174], [37.296831, 126.836163],
                   [37.296571, 126.836419], [37.296257, 126.836945],
                   [37.296698, 126.836988], [37.296598, 126.836773],
                   [37.296854, 126.836885], [37.296668, 126.837406],
                   [37.297026, 126.837862], [37.296821, 126.838307], #70
                   [37.296904, 126.838489], [37.296676, 126.838636],
                   [37.296323, 126.838795], [37.296477, 126.839243],
                   [37.295562, 126.839122], [37.293662, 126.837094],
                   [37.293220, 126.836028]]
