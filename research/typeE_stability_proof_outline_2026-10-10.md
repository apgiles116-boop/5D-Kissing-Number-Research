# Proof sketch for strengthened F3 matching stability

Let D=C-N and Eij=||mi||²+||mj||²-2|mi·mj|. The exact identity is 4D=||sum mi||²+sum Eij.

For a doubled-contact F3 matching, relabel the doubled quotient edge 03 and missing edge 12. Set H=||m0+m3+(m1+m2)/2||²+||m1-m2||²/4. Six strict deep contacts and cancellation of the two doubled-edge mixed terms yield H<4 sqrt((4-C)D).

Choose a maximal-norm midpoint mj, with ||mj||≥sqrt(C)/2. Align signs of the other three midpoints with mj, obtaining a signed rank-one comparison Y. Then ||m-Y||≤2sqrt(D). If the signs split 2+2, H(Y)=||mj||², and the operator norm sqrt(5/2) yields sqrt(H)≥sqrt(C)/2-sqrt(10D). Otherwise sqrt(C)≤6sqrt(D), so the same inequality is automatic.

Hence C/4<[4sqrt(4-C)+sqrt(10C)]sqrt(D). Therefore D>C²/K(C), K(C)=1024-96C+128sqrt(10C(4-C)). K increases on 0<C≤1 and K(1)<1630. The singleton matching has D>1/96, which also implies D>C²/1630.

The rational checker verifies K(383/504)<1587 and K(0.603545)<1546. These last constants depend on retained Type E energy bounds. No Type E elimination is claimed.