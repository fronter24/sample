//伝達関数から状態空間表現を得る
s=%s
num=2*s+1; den=s^2+3*s+2;
tf_sys=syslin('c',num,den);
ss_sys=tf2ss(tf_sys)

