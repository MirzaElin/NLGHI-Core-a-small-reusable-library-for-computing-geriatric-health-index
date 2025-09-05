from nlghi import core, domains

def test_zero_and_full_scale():
    zeros = [0]*27; dsav, ghi0 = core.compute(zeros, domains.WEIGHTS)
    assert ghi0 == 0.0 and sum(dsav) == 0.0
    fives = [5]*27; dsav2, ghi2 = core.compute(fives, domains.WEIGHTS)
    assert round(ghi2*27, 6) == round(sum(dsav2), 6)

def test_matches_app_formula():
    imps = [0,1,2,3,4]*5 + [1,2]; imps = imps[:27]
    dsav, ghi = core.compute(imps, domains.WEIGHTS)
    assert round(ghi, 4) == round(sum([imps[i]*domains.WEIGHTS[i] for i in range(27)]) / 27.0, 4)
