"""Re-run the exact-fit search on the open lines with an 1850s Oxford vocabulary added (Oct 2026, 4th session):
Hertford scholars 1852-56 from the Historical Register 1888, Balliol tutors, the university's terms,
exams and set texts. Output: search_oxnames.txt."""
import sys, search
search.EXTRA = search.EXTRA + ('montgomerie newman bowen broughton winstanley scott lake woollcombe riddell temple '
    'wall palmer jenkyns gaisford ireland chancellor latin verse prize essay greats moderations mods smalls '
    'responsions vacation michaelmas hilary trinity lent easter viva schools logic aristotle ethics plato '
    'republic thucydides herodotus vergil virgil juvenal persius lucretius cicero tacitus pupil private coach '
    'master scholar exhibition bursar gown quad chapel battels rusticated gated proctors sconce class first '
    'second third honours ode odes epistle epistles ars poetica translation composition paper papers viva '
    'examiner examiners elected election candidate candidates').split()
search.main([int(x) for x in sys.argv[1:]] or [5, 6, 9, 12, 14, 19, 21, 23, 26, 29])
