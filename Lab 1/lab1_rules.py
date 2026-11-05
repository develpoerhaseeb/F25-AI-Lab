# Lab 1 :-- Task 02

MIN_SCORE = 70          # from manual (synthetic)
MIN_ATTENDANCE = 75     # new condition 1 (synthetic), percent
MIN_RECOMMENDATIONS = 1 # new condition 2 (synthetic), letters

def score_ok(score):
    return score >= MIN_SCORE

def documents_ok(documents_complete):
    return documents_complete

def attendance_ok(attendance_pct):
    return attendance_pct >= MIN_ATTENDANCE

def recommendation_ok(num_letters):
    return num_letters >= MIN_RECOMMENDATIONS

def screen(score, documents_complete, attendance_pct, num_letters):
    """Return (decision, reason). Every failed condition is named."""
    failed = []
    if not  score_ok (score) :
        failed.append ( "score  < %d "  %  MIN_SCORE ) 
    if not     documents_ok  ( documents_complete) :
        failed.append("documents incomplete")
    if  not      attendance_ok ( attendance_pct )  :
        failed.append ("attendance   <   %d%%" %   MIN_ATTENDANCE)
    if not recommendation_ok(num_letters):
        failed.append("no recommendation letter")
    if failed:
        return "Hold", "; ".join(failed)
    return "Review", "all conditions met"


tests = [
    ("T1_pass",             85, True, 90, 2, "Review"),
    ("T2_fail_attendance",  85, True, 60, 2, "Hold"),
    ("T3_fail_recommend",   85, True, 90, 0, "Hold"),
    ("T4_boundary",         70, True, 75, 1, "Review"),
]

print("Thresholds are synthetic lab assumptions.")
passed = 0
for name, s, d, a, l, expected in tests:
    actual, reason = screen(s, d, a, l)
    ok = actual == expected
    passed += ok
    print("_"    * 60)
    print("Case     :", name)
    print("Input    : score=%d, docs_complete=%s, attendance=%d, letters=%d" % (s, d, a, l))
    print("Expected :", expected)
    print("Actual   :", actual)
    print("Reason   :", reason)
    print("Match    :", "PASS" if ok else "FAIL")
print("_"     * 60)
print(" %d /%d test cases match expect" % (passed, len(tests)))