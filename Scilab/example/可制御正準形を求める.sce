//可制御正準形を求める
L=[-3 1; 1 0];
Mc=cont_mat(A,b);
Tc=inv(Mc*L);
Ac=Tc*A*inv(Tc); bc=Tc*b; cc=c*inv(Tc);

